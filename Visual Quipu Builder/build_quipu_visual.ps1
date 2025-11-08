param(
    [string]$Base = (Split-Path -Parent $PSScriptRoot),
    [string[]]$Formats = @("dot","svg"),
    [switch]$Quiet
)

$validFormats = @("dot","svg","png","pdf")
$chosen = @()
foreach ($fmt in $Formats) {
    if (-not $fmt) { continue }
    $lower = $fmt.ToLowerInvariant()
    if ($validFormats -notcontains $lower) {
        throw "Unsupported format '$fmt'. Choose from: $($validFormats -join ', ')"
    }
    if ($chosen -notcontains $lower) {
        $chosen += $lower
    }
}
if ($chosen -notcontains "dot") {
    $chosen = ,"dot" + $chosen
}

$exporterPath = Join-Path $Base "export_quipu_graph.py"
if (-not (Test-Path $exporterPath)) {
    throw "Cannot find export_quipu_graph.py under $Base"
}

try {
    $pythonCmd = (Get-Command python -ErrorAction Stop).Source
} catch {
    throw "Python is required to run the exporter. Ensure 'python' is on PATH."
}

$visualDir = $PSScriptRoot
if (-not (Test-Path $visualDir)) {
    New-Item -ItemType Directory -Path $visualDir | Out-Null
}

foreach ($fmt in $chosen) {
    $outputPath = Join-Path $visualDir ("quipu.{0}" -f $fmt)
    $args = @($exporterPath, "--base", $Base, "--output", $outputPath, "--format", $fmt)
    & $pythonCmd @args
    $exit = $LASTEXITCODE
    if ($exit -ne 0) {
        if ($fmt -eq "dot") {
            throw "Failed to export Graphviz DOT (exit code $exit)."
        } else {
            Write-Warning "Failed to render format '$fmt'. Ensure Graphviz 'dot' is installed for non-DOT outputs."
            continue
        }
    }
    if (-not $Quiet) {
        Write-Host "wrote quipu.$fmt" -ForegroundColor Green
    }
}