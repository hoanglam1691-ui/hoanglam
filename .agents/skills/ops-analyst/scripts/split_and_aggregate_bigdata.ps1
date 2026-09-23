# ==============================================================================
# Script: Process BigData 200 rows ERP Payroll & Operations
# Outputs:
#   - outputs/departments/[Dept]_2026-03.csv
#   - outputs/managers/[Manager]_2026-03.csv
#   - outputs/reports/bigdata_kpi_summary.json
# ==============================================================================

$file = Get-ChildItem -Path "sample-data" -Filter "*ERP_OP_BigData_200rows*.csv" | Select-Object -First 1
if ($file -eq $null) {
    Write-Error "File not found!"
    exit 1
}

$rawRows = Import-Csv -LiteralPath $file.FullName -Encoding UTF8

# Filter non-empty valid employee rows
$cleanRows = @()
foreach ($r in $rawRows) {
    if (-not [string]::IsNullOrWhiteSpace($r.Employee_ID) -and $r.Employee_ID -ne "") {
        $base = [double]$r.Base_Salary
        $bonus = [double]$r.Bonus
        $penalty = [double]$r.Penalty
        $net = $base + $bonus - $penalty

        $cleanRows += [PSCustomObject]@{
            Employee_ID   = $r.Employee_ID.Trim()
            Employee_Name = $r.Employee_Name.Trim()
            Manager       = $r.Manager.Trim()
            Department    = $r.Department.Trim()
            Base_Salary   = $base
            Bonus         = $bonus
            Penalty       = $penalty
            Net_Payout    = $net
            Month         = $r.Month.Trim()
        }
    }
}

Write-Host "Valid records to process: $($cleanRows.Count)"

$deptDir = "outputs/departments"
$mgrDir = "outputs/managers"
$reportDir = "outputs/reports"

if (-not (Test-Path $deptDir)) { New-Item -ItemType Directory -Path $deptDir -Force | Out-Null }
if (-not (Test-Path $mgrDir)) { New-Item -ItemType Directory -Path $mgrDir -Force | Out-Null }
if (-not (Test-Path $reportDir)) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }

$month = "2026-03"

# 1. Split by Department
$depts = $cleanRows | ForEach-Object { $_.Department } | Select-Object -Unique
$deptSummary = @()

foreach ($d in $depts) {
    $dRows = @($cleanRows | Where-Object { $_.Department -eq $d })
    $dPath = Join-Path $deptDir "$($d)_$($month).csv"
    $dRows | Export-Csv -Path $dPath -NoTypeInformation -Encoding UTF8

    $bSum = ($dRows | Measure-Object -Property Base_Salary -Sum).Sum
    $bnSum = ($dRows | Measure-Object -Property Bonus -Sum).Sum
    $pSum = ($dRows | Measure-Object -Property Penalty -Sum).Sum
    $netSum = ($dRows | Measure-Object -Property Net_Payout -Sum).Sum

    $deptSummary += [PSCustomObject]@{
        Department   = $d
        Headcount    = $dRows.Count
        Base_Salary  = $bSum
        Bonus        = $bnSum
        Penalty      = $pSum
        Net_Payout   = $netSum
        Bonus_Rate   = [math]::Round(($bnSum / $bSum) * 100, 1)
        Penalty_Rate = [math]::Round(($pSum / $bSum) * 100, 1)
        FilePath     = $dPath
    }
}

# 2. Split by Manager
$managers = $cleanRows | ForEach-Object { $_.Manager } | Select-Object -Unique
$mgrSummary = @()

foreach ($m in $managers) {
    $mRows = @($cleanRows | Where-Object { $_.Manager -eq $m })
    $mPath = Join-Path $mgrDir "$($m)_$($month).csv"
    $mRows | Export-Csv -Path $mPath -NoTypeInformation -Encoding UTF8

    $bSum = ($mRows | Measure-Object -Property Base_Salary -Sum).Sum
    $bnSum = ($mRows | Measure-Object -Property Bonus -Sum).Sum
    $pSum = ($mRows | Measure-Object -Property Penalty -Sum).Sum
    $netSum = ($mRows | Measure-Object -Property Net_Payout -Sum).Sum

    # Top penalized and top bonused employees under this manager
    $topBonusEmp = $mRows | Sort-Object -Property Bonus -Descending | Select-Object -First 1
    $topPenaltyEmp = $mRows | Sort-Object -Property Penalty -Descending | Select-Object -First 1

    $mgrSummary += [PSCustomObject]@{
        Manager          = $m
        Headcount        = $mRows.Count
        Base_Salary      = $bSum
        Bonus            = $bnSum
        Penalty          = $pSum
        Net_Payout       = $netSum
        Bonus_Rate       = [math]::Round(($bnSum / $bSum) * 100, 1)
        Penalty_Rate     = [math]::Round(($pSum / $bSum) * 100, 1)
        Top_Bonus_Emp    = "$($topBonusEmp.Employee_Name) ($('{0:N0}' -f $topBonusEmp.Bonus) VND)"
        Top_Penalty_Emp  = "$($topPenaltyEmp.Employee_Name) ($('{0:N0}' -f $topPenaltyEmp.Penalty) VND)"
        FilePath         = $mPath
    }
}

# 3. Overall Totals
$totBase = ($cleanRows | Measure-Object -Property Base_Salary -Sum).Sum
$totBonus = ($cleanRows | Measure-Object -Property Bonus -Sum).Sum
$totPenalty = ($cleanRows | Measure-Object -Property Penalty -Sum).Sum
$totNet = ($cleanRows | Measure-Object -Property Net_Payout -Sum).Sum

$finalSummary = [PSCustomObject]@{
    Month          = $month
    TotalHeadcount = $cleanRows.Count
    TotalBase      = $totBase
    TotalBonus     = $totBonus
    TotalPenalty   = $totPenalty
    TotalNet       = $totNet
    AvgBonusRate   = [math]::Round(($totBonus / $totBase) * 100, 1)
    AvgPenaltyRate = [math]::Round(($totPenalty / $totBase) * 100, 1)
    Departments    = $deptSummary
    Managers       = $mgrSummary
}

$summaryJsonPath = Join-Path $reportDir "bigdata_200rows_kpi_summary.json"
$finalSummary | ConvertTo-Json -Depth 5 | Set-Content -Path $summaryJsonPath -Encoding UTF8

Write-Host "Splitting completed successfully!"
Write-Host "Departments: $($deptSummary.Count) files created in $deptDir"
Write-Host "Managers: $($mgrSummary.Count) files created in $mgrDir"
Write-Host "Summary JSON saved to $summaryJsonPath"
