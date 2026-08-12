param(
  [Parameter(Mandatory = $true)]
  [string]$SiteRoot,

  [string]$Config = "",

  [string]$JsonOutput = "",

  [switch]$AllowMissingArtifacts,

  [switch]$Strict
)

$ErrorActionPreference = "Stop"
$scriptPath = Join-Path $PSScriptRoot "validate-content-design.py"

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
  throw "Python 3 is required to run validate-content-design.py."
}

$argsList = @($scriptPath, $SiteRoot)
if (-not [string]::IsNullOrWhiteSpace($Config)) {
  $argsList += @("--config", $Config)
}
if (-not [string]::IsNullOrWhiteSpace($JsonOutput)) {
  $argsList += @("--json-output", $JsonOutput)
}
if ($AllowMissingArtifacts) { $argsList += "--allow-missing-artifacts" }
if ($Strict) { $argsList += "--strict" }

if ($python.Name -eq "py.exe" -or $python.Name -eq "py") {
  & $python.Source -3 @argsList
} else {
  & $python.Source @argsList
}
exit $LASTEXITCODE
