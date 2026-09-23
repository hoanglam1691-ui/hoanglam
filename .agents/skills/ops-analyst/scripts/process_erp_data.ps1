# ==============================================================================
# AI4A: Operations Analyst Data Processing Engine
# Skill: ai4a:ops-analyst
# ==============================================================================

param (
    [Parameter(Mandatory = $false)]
    [string]$InputPath = "sample-data/erp_operations_sample.csv",

    [Parameter(Mandatory = $false)]
    [string]$TargetMonth = ""
)

$ErrorActionPreference = "Stop"

function Get-Slug([string]$text) {
    if ([string]::IsNullOrWhiteSpace($text)) { return "Unassigned" }
    $clean = $text.Trim()
    $clean = $clean.Replace([char]0x0111, [char]'d').Replace([char]0x0110, [char]'D')
    $normalized = $clean.Normalize([System.Text.NormalizationForm]::FormD)
    $sb = New-Object System.Text.StringBuilder
    foreach ($ch in $normalized.ToCharArray()) {
        $uc = [System.Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch)
        if ($uc -ne [System.Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$sb.Append($ch)
        }
    }
    $ascii = $sb.ToString()
    $slug = ($ascii -replace "[^a-zA-Z0-9]", "_") -replace "_+", "_"
    return $slug.Trim("_")
}

Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host " AI4A: Operations Analyst Data Processing Engine" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

# 1. Verify input file
if (-not (Test-Path $InputPath)) {
    Write-Error "File not found at: $InputPath"
    exit 1
}

Write-Host "[1/4] Loading ERP data from: $InputPath" -ForegroundColor Yellow
$rows = Import-Csv -Path $InputPath -Encoding UTF8

if ($rows.Count -eq 0) {
    Write-Error "Dataset is empty!"
    exit 1
}

# 2. Prepare output directories according to Workspace Rule 4
$deptDir = "outputs/departments"
$reportDir = "outputs/reports"

if (-not (Test-Path $deptDir)) { New-Item -ItemType Directory -Path $deptDir -Force | Out-Null }
if (-not (Test-Path $reportDir)) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }

# 3. Clean and standardize records
Write-Host "[2/4] Sanitizing data and standardizing status..." -ForegroundColor Yellow
$cleanedRows = @()

foreach ($row in $rows) {
    $empId = if ($row.PSObject.Properties['employee_id']) { $row.employee_id.Trim() } else { "UNKNOWN" }
    $empName = if ($row.PSObject.Properties['employee_name']) { $row.employee_name.Trim() } else { "N/A" }
    $dept = if ($row.PSObject.Properties['department']) { $row.department.Trim() } else { "Unassigned" }
    $date = if ($row.PSObject.Properties['record_date']) { $row.record_date.Trim() } else { "" }
    $rawStatus = if ($row.PSObject.Properties['task_status']) { $row.task_status.Trim() } else { "In Progress" }
    $outputUnits = 0
    if ($row.PSObject.Properties['output_units']) {
        [double]::TryParse($row.output_units, [ref]$outputUnits) | Out-Null
    }

    # Map status into 4 standardized buckets
    $stdStatus = "In Progress"
    if ($rawStatus -match "(Completed|Done|Closed)") {
        $stdStatus = "Completed"
    } elseif ($rawStatus -match "(Delayed|Late|Overdue)") {
        $stdStatus = "Delayed"
    } elseif ($rawStatus -match "(Cancelled|Failed|Rejected)") {
        $stdStatus = "Cancelled"
    } else {
        $stdStatus = "In Progress"
    }

    if ($TargetMonth -ne "" -and $date -notlike "$TargetMonth*") {
        continue
    }

    $cleanedRows += [PSCustomObject]@{
        employee_id   = $empId
        employee_name = $empName
        department    = $dept
        record_date   = $date
        output_units  = $outputUnits
        task_status   = $stdStatus
    }
}

Write-Host "-> Cleaned $($cleanedRows.Count) valid records." -ForegroundColor Green

# Determine reporting month
if ($TargetMonth -eq "") {
    $dates = $cleanedRows | Where-Object { $_.record_date -ne "" } | ForEach-Object { $_.record_date }
    if ($dates.Count -gt 0) {
        $firstDate = ($dates | Sort-Object)[-1]
        $monthStr = $firstDate.Substring(0, 7)
    } else {
        $monthStr = (Get-Date -Format "yyyy-MM")
    }
} else {
    $monthStr = $TargetMonth
}

# 4. Multi-tenant department isolation (Splitting files)
Write-Host "[3/4] Isolating and splitting files by department..." -ForegroundColor Yellow
$departments = $cleanedRows | ForEach-Object { $_.department } | Select-Object -Unique

$deptStats = @()

foreach ($d in $departments) {
    $deptRows = @($cleanedRows | Where-Object { $_.department -eq $d })
    $slugDept = Get-Slug $d
    $deptFilePath = Join-Path $deptDir "$($slugDept)_$($monthStr).csv"

    $deptRows | Export-Csv -Path $deptFilePath -NoTypeInformation -Encoding UTF8
    Write-Host "   + Department file created: $deptFilePath ($($deptRows.Count) records)" -ForegroundColor Gray

    $totalTasks = $deptRows.Count
    $doneTasks = @($deptRows | Where-Object { $_.task_status -eq "Completed" }).Count
    $doingTasks = @($deptRows | Where-Object { $_.task_status -eq "In Progress" }).Count
    $lateTasks = @($deptRows | Where-Object { $_.task_status -eq "Delayed" }).Count
    $empCount = @($deptRows | ForEach-Object { $_.employee_id } | Select-Object -Unique).Count
    $totalOutput = ($deptRows | Measure-Object -Property output_units -Sum).Sum

    $compRate = if ($totalTasks -gt 0) { [math]::Round(($doneTasks / $totalTasks) * 100, 1) } else { 0 }
    $delayRate = if ($totalTasks -gt 0) { [math]::Round(($lateTasks / $totalTasks) * 100, 1) } else { 0 }

    # Rating threshold
    $rating = if ($delayRate -gt 20) { "Red (High Risk)" } elseif ($delayRate -gt 10) { "Yellow (Watchlist)" } else { "Normal (Healthy)" }

    # Employee breakdown
    $empPerformances = @()
    $empGroups = $deptRows | Group-Object -Property employee_id
    foreach ($g in $empGroups) {
        $eName = ($g.Group | Select-Object -First 1).employee_name
        $eTotal = $g.Count
        $eDone = @($g.Group | Where-Object { $_.task_status -eq "Completed" }).Count
        $eDoing = @($g.Group | Where-Object { $_.task_status -eq "In Progress" }).Count
        $eLate = @($g.Group | Where-Object { $_.task_status -eq "Delayed" }).Count
        $eOutput = ($g.Group | Measure-Object -Property output_units -Sum).Sum
        $eRate = if ($eTotal -gt 0) { [math]::Round(($eDone / $eTotal) * 100, 1) } else { 0 }

        $empPerformances += [PSCustomObject]@{
            employee_id   = $g.Name
            employee_name = $eName
            total_tasks   = $eTotal
            completed     = $eDone
            in_progress   = $eDoing
            delayed       = $eLate
            output        = $eOutput
            rate          = $eRate
        }
    }

    $deptStats += [PSCustomObject]@{
        department      = $d
        slug            = $slugDept
        headcount       = $empCount
        total_tasks     = $totalTasks
        completed       = $doneTasks
        in_progress     = $doingTasks
        delayed         = $lateTasks
        completion_rate = $compRate
        delay_rate      = $delayRate
        total_output    = $totalOutput
        status_rating   = $rating
        file_path       = $deptFilePath
        employees       = @($empPerformances | Sort-Object -Property rate, output -Descending)
    }
}

# 5. Company-wide quantitative aggregation
Write-Host "[4/4] Aggregating company-wide quantitative KPIs..." -ForegroundColor Yellow
$compTotalTasks = $cleanedRows.Count
$compDoneTasks = @($cleanedRows | Where-Object { $_.task_status -eq "Completed" }).Count
$compDoingTasks = @($cleanedRows | Where-Object { $_.task_status -eq "In Progress" }).Count
$compLateTasks = @($cleanedRows | Where-Object { $_.task_status -eq "Delayed" }).Count
$compTotalHeadcount = @($cleanedRows | ForEach-Object { $_.employee_id } | Select-Object -Unique).Count
$compTotalOutput = ($cleanedRows | Measure-Object -Property output_units -Sum).Sum

$compOverallRate = if ($compTotalTasks -gt 0) { [math]::Round(($compDoneTasks / $compTotalTasks) * 100, 1) } else { 0 }
$compOverallDelay = if ($compTotalTasks -gt 0) { [math]::Round(($compLateTasks / $compTotalTasks) * 100, 1) } else { 0 }

$bestDept = ($deptStats | Sort-Object -Property completion_rate -Descending | Select-Object -First 1).department

$allEmployees = @()
foreach ($ds in $deptStats) {
    foreach ($emp in $ds.employees) {
        $allEmployees += [PSCustomObject]@{
            employee_id   = $emp.employee_id
            employee_name = $emp.employee_name
            department    = $ds.department
            completed     = $emp.completed
            output        = $emp.output
            rate          = $emp.rate
        }
    }
}
$top3Performers = @($allEmployees | Sort-Object -Property output, rate -Descending | Select-Object -First 3)

$summaryReport = [PSCustomObject]@{
    month                   = $monthStr
    processed_at            = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    total_headcount         = $compTotalHeadcount
    total_tasks             = $compTotalTasks
    total_completed         = $compDoneTasks
    total_in_progress       = $compDoingTasks
    total_delayed           = $compLateTasks
    total_output            = $compTotalOutput
    overall_completion_rate = $compOverallRate
    overall_delay_rate      = $compOverallDelay
    health_score            = [math]::Max(0, [math]::Round(100 - ($compOverallDelay * 2), 0))
    best_department         = $bestDept
    top_performers          = $top3Performers
    departments             = $deptStats
}

$jsonPath = Join-Path $reportDir "operations_kpi_summary.json"
$summaryReport | ConvertTo-Json -Depth 5 | Set-Content -Path $jsonPath -Encoding UTF8

Write-Host "=====================================================" -ForegroundColor Green
Write-Host " SUCCESS: Operations dataset successfully processed!" -ForegroundColor Green
Write-Host "   - Department files saved to: $deptDir" -ForegroundColor White
Write-Host "   - KPI Summary JSON saved to: $jsonPath" -ForegroundColor White
Write-Host "=====================================================" -ForegroundColor Green
