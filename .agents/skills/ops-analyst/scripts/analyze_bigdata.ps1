param (
    [string]$FilePattern = "*ERP_OP_BigData_200rows*.csv"
)

$file = Get-ChildItem -Path "sample-data" -Filter $FilePattern | Select-Object -First 1
if ($file -eq $null) {
    Write-Error "No matching file found for pattern: $FilePattern"
    exit 1
}

Write-Host "Processing file: $($file.FullName)"
$data = Import-Csv -LiteralPath $file.FullName -Encoding UTF8
Write-Host "Total records: $($data.Count)"

$months = $data | ForEach-Object { $_.Month } | Select-Object -Unique
Write-Host "Months: $($months -join ', ')"

$depts = $data | ForEach-Object { $_.Department } | Select-Object -Unique
Write-Host "Departments: $($depts -join ', ')"

$managers = $data | ForEach-Object { $_.Manager } | Select-Object -Unique
Write-Host "Managers: $($managers -join ', ')"

# Summary by Department
Write-Host "`n--- SUMMARY BY DEPARTMENT ---"
foreach ($d in $depts) {
    $rows = @($data | Where-Object { $_.Department -eq $d })
    $baseSum = 0; $bonusSum = 0; $penaltySum = 0
    foreach ($r in $rows) {
        $baseSum += [double]$r.Base_Salary
        $bonusSum += [double]$r.Bonus
        $penaltySum += [double]$r.Penalty
    }
    $netPayout = $baseSum + $bonusSum - $penaltySum
    $bonusRate = if ($baseSum -gt 0) { [math]::Round(($bonusSum / $baseSum) * 100, 1) } else { 0 }
    $penaltyRate = if ($baseSum -gt 0) { [math]::Round(($penaltySum / $baseSum) * 100, 1) } else { 0 }
    
    Write-Host "$d : Count=$($rows.Count) | Base=$('{0:N0}' -f $baseSum) | Bonus=$('{0:N0}' -f $bonusSum) ($bonusRate%) | Penalty=$('{0:N0}' -f $penaltySum) ($penaltyRate%) | Net Payout=$('{0:N0}' -f $netPayout)"
}

# Summary by Manager
Write-Host "`n--- SUMMARY BY MANAGER ---"
foreach ($m in $managers) {
    $rows = @($data | Where-Object { $_.Manager -eq $m })
    $baseSum = 0; $bonusSum = 0; $penaltySum = 0
    foreach ($r in $rows) {
        $baseSum += [double]$r.Base_Salary
        $bonusSum += [double]$r.Bonus
        $penaltySum += [double]$r.Penalty
    }
    $netPayout = $baseSum + $bonusSum - $penaltySum
    $bonusRate = if ($baseSum -gt 0) { [math]::Round(($bonusSum / $baseSum) * 100, 1) } else { 0 }
    $penaltyRate = if ($baseSum -gt 0) { [math]::Round(($penaltySum / $baseSum) * 100, 1) } else { 0 }

    Write-Host "$m : Count=$($rows.Count) | Base=$('{0:N0}' -f $baseSum) | Bonus=$('{0:N0}' -f $bonusSum) ($bonusRate%) | Penalty=$('{0:N0}' -f $penaltySum) ($penaltyRate%) | Net Payout=$('{0:N0}' -f $netPayout)"
}

# Overall Company Total
$totalBase = 0; $totalBonus = 0; $totalPenalty = 0
foreach ($r in $data) {
    $totalBase += [double]$r.Base_Salary
    $totalBonus += [double]$r.Bonus
    $totalPenalty += [double]$r.Penalty
}
$totalNet = $totalBase + $totalBonus - $totalPenalty
Write-Host "`n--- COMPANY TOTAL ---"
Write-Host "Total Headcount: $($data.Count)"
Write-Host "Total Base Salary: $('{0:N0}' -f $totalBase) VND"
Write-Host "Total Bonus:       ('{0:N0}' -f $totalBonus) VND"
Write-Host "Total Penalty:     ('{0:N0}' -f $totalPenalty) VND"
Write-Host "Total Net Payout:  ('{0:N0}' -f $totalNet) VND"
