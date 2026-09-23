# ==============================================================================
# Helper: Convert XLSX to CSV using native .NET ZipFile & XML (No Office required)
# ==============================================================================
param (
    [Parameter(Mandatory = $true)]
    [string]$XlsxPath,

    [Parameter(Mandatory = $false)]
    [string]$CsvPath = ""
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.IO.Compression.FileSystem

if (-not (Test-Path $XlsxPath)) {
    Write-Error "File not found: $XlsxPath"
    exit 1
}

$resolvedXlsx = (Resolve-Path $XlsxPath).Path
if ([string]::IsNullOrWhiteSpace($CsvPath)) {
    $CsvPath = [System.IO.Path]::ChangeExtension($resolvedXlsx, ".csv")
}

Write-Host "Converting $resolvedXlsx to $CsvPath..." -ForegroundColor Cyan

$zip = [System.IO.Compression.ZipFile]::OpenRead($resolvedXlsx)

# 1. Read shared strings
$sharedStrings = @()
$ssEntry = $zip.GetEntry("xl/sharedStrings.xml")
if ($ssEntry -ne $null) {
    $stream = $ssEntry.Open()
    $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
    [xml]$ssXml = $reader.ReadToEnd()
    $reader.Close()
    $stream.Close()

    foreach ($si in $ssXml.sst.si) {
        if ($si.t -ne $null) {
            $sharedStrings += $si.t
        } elseif ($si.r -ne $null) {
            $tParts = ($si.r | ForEach-Object { $_.t }) -join ""
            $sharedStrings += $tParts
        } else {
            $sharedStrings += ""
        }
    }
}

Write-Host "Read $($sharedStrings.Count) shared strings." -ForegroundColor Green

# 2. Read first sheet
$sheetEntry = $zip.GetEntry("xl/worksheets/sheet1.xml")
if ($sheetEntry -eq $null) {
    Write-Error "Could not find xl/worksheets/sheet1.xml in zip archive."
    $zip.Dispose()
    exit 1
}

$sheetStream = $sheetEntry.Open()
$sheetReader = New-Object System.IO.StreamReader($sheetStream, [System.Text.Encoding]::UTF8)
[xml]$sheetXml = $sheetReader.ReadToEnd()
$sheetReader.Close()
$sheetStream.Close()
$zip.Dispose()

# 3. Parse rows and cells
function Get-ColIndex([string]$cellRef) {
    $colLetters = $cellRef -replace '[0-9]', ''
    $col = 0
    foreach ($ch in $colLetters.ToCharArray()) {
        $col = $col * 26 + ([int][char]$ch - [int][char]'A' + 1)
    }
    return $col
}

$csvLines = New-Object System.Collections.Generic.List[string]

foreach ($row in $sheetXml.worksheet.sheetData.row) {
    $rowCells = @{}
    $maxCol = 0

    foreach ($c in $row.c) {
        $colIdx = Get-ColIndex $c.r
        if ($colIdx -gt $maxCol) { $maxCol = $colIdx }
        
        $val = ""
        if ($c.v -ne $null) {
            $rawVal = $c.v
            if ($c.t -eq "s") {
                $sIdx = [int]$rawVal
                if ($sIdx -lt $sharedStrings.Count) {
                    $val = $sharedStrings[$sIdx]
                }
            } elseif ($c.t -eq "b") {
                $val = if ($rawVal -eq "1") { "TRUE" } else { "FALSE" }
            } else {
                $val = $rawVal
            }
        } elseif ($c.is -ne $null -and $c.is.t -ne $null) {
            $val = $c.is.t
        }

        $rowCells[$colIdx] = $val
    }

    $lineParts = @()
    for ($i = 1; $i -le $maxCol; $i++) {
        $cellVal = if ($rowCells.ContainsKey($i)) { $rowCells[$i] } else { "" }
        # Escape quotes
        $escaped = $cellVal.Replace('"', '""')
        $lineParts += "`"$escaped`""
    }
    $csvLines.Add(($lineParts -join ","))
}

[System.IO.File]::WriteAllLines($CsvPath, $csvLines, [System.Text.Encoding]::UTF8)
Write-Host "Successfully converted $($csvLines.Count) rows to $CsvPath!" -ForegroundColor Green
