param(
  [Parameter(Mandatory = $true)]
  [string]$Target,

  [Parameter(Mandatory = $true)]
  [string]$Product,

  [Parameter(Mandatory = $true)]
  [ValidateSet("marketing-website", "professional-services-website", "saas-web-app", "internal-tool", "dashboard", "ai-workspace", "ecommerce", "mobile-style-app", "other")]
  [string]$BuildType,

  [Parameter(Mandatory = $true)]
  [string[]]$PrimaryUser,

  [Parameter(Mandatory = $true)]
  [string[]]$TopTask,

  [string]$Domain = "",

  [ValidateSet("sparse", "balanced", "informational", "data-dense")]
  [string]$ContentDensity = "balanced",

  [switch]$Force
)

$ErrorActionPreference = "Stop"
$scriptPath = Join-Path $PSScriptRoot "initialize-vault-project.py"
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command py -ErrorAction SilentlyContinue }
if (-not $python) { throw "Python 3 is required to initialize a vault project." }

$argsList = @($scriptPath, $Target, "--product", $Product, "--build-type", $BuildType, "--content-density", $ContentDensity)
if (-not [string]::IsNullOrWhiteSpace($Domain)) { $argsList += @("--domain", $Domain) }
foreach ($item in $PrimaryUser) { $argsList += @("--primary-user", $item) }
foreach ($item in $TopTask) { $argsList += @("--top-task", $item) }
if ($Force) { $argsList += "--force" }

if ($python.Name -eq "py.exe" -or $python.Name -eq "py") {
  & $python.Source -3 @argsList
} else {
  & $python.Source @argsList
}
exit $LASTEXITCODE
