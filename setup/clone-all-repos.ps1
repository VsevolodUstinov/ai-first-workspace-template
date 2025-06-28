# PowerShell script for cloning AI First Workspace Template repositories

# ⚠️  CONFIGURATION REQUIRED ⚠️
# Before running this script, customize these variables for your organization:

# TODO: Replace with your GitHub organization name
$ORG = "YOUR-GITHUB-ORGANIZATION"

# TODO: Replace with your development repository names
# Examples: @("MyApp", "MyAPI", "MyMobileApp") or @("Frontend", "Backend", "Mobile")
$DEV_REPOS = @("YOUR-PRODUCT-1", "YOUR-PRODUCT-2", "YOUR-PRODUCT-3")

# ============================================================================
# Configuration check
if ($ORG -eq "YOUR-GITHUB-ORGANIZATION") {
    Write-Host "⚠️  CONFIGURATION REQUIRED" -ForegroundColor Red
    Write-Host ""
    Write-Host "Before running this script, you need to customize it for your organization:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Open this file: setup\clone-all-repos.ps1"
    Write-Host "2. Replace 'YOUR-GITHUB-ORGANIZATION' with your GitHub organization name"
    Write-Host "3. Replace the `$DEV_REPOS array with your actual repository names"
    Write-Host ""
    Write-Host "Example configuration:" -ForegroundColor Cyan
    Write-Host '   $ORG = "mycompany"'
    Write-Host '   $DEV_REPOS = @("MyMainApp", "MyAPI", "MyDashboard")'
    Write-Host ""
    Write-Host "💡 Pro tip: Ask your AI assistant to help customize this script!" -ForegroundColor Green
    exit 1
}

Write-Host "🚀 Setting up AI First Workspace Template..." -ForegroundColor Green
Write-Host ""

# Set up workspace .gitignore if it doesn't exist
if (-not (Test-Path ".gitignore") -and (Test-Path ".gitignore.template")) {
    Write-Host "📝 Setting up workspace .gitignore..." -ForegroundColor Cyan
    Copy-Item ".gitignore.template" ".gitignore"
    Write-Host "   ✅ Copied .gitignore.template to .gitignore" -ForegroundColor Green
    Write-Host ""
}

# Create main organizational folders
Write-Host "📁 Creating organizational structure..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path "Docs", "Dev" | Out-Null
Write-Host ""

Write-Host "📋 Cloning repositories for organization: $ORG" -ForegroundColor Yellow
Write-Host "Note: You'll only be able to clone repositories you have access to"
Write-Host ""

# Function to clone repository
function Clone-Repository {
    param (
        [string]$repoName,
        [string]$targetPath,
        [string]$description,
        [bool]$isOptional = $false
    )
    
    if (-not (Test-Path $targetPath)) {
        Write-Host $description -ForegroundColor Cyan
        Write-Host "   Cloning $repoName to $targetPath..."
        try {
            git clone "git@github.com:$ORG/$repoName.git" $targetPath 2>$null
            Write-Host "   ✅ Successfully cloned $repoName to $targetPath" -ForegroundColor Green
        }
        catch {
            if ($isOptional) {
                Write-Host "   ℹ️  $repoName repository not yet created (can be created later)" -ForegroundColor Yellow
            } else {
                Write-Host "   ⚠️  Could not clone $repoName (check access permissions or repository may not exist yet)" -ForegroundColor Yellow
            }
        }
        Write-Host ""
    }
    else {
        Write-Host $description -ForegroundColor Cyan
        Write-Host "   ✅ $targetPath already exists, skipping..." -ForegroundColor Green
        Write-Host ""
    }
}

# Clone documentation repositories
Write-Host "📚 Setting up Documentation repositories..." -ForegroundColor Cyan

$docRepos = @(
    @{Name="Strategy"; Path="Docs/Strategy"; Desc="🎯 Company strategy and competitive intelligence"; Optional=$false},
    @{Name="Product"; Path="Docs/Product"; Desc="📱 Product roadmap and specifications"; Optional=$false},
    @{Name="SalesAndMarketing"; Path="Docs/SalesAndMarketing"; Desc="📈 Campaigns, content, and sales processes"; Optional=$false},
    @{Name="Operations"; Path="Docs/Operations"; Desc="📊 Operational processes and metrics"; Optional=$true},
    @{Name="Operations-Hiring"; Path="Docs/Operations/Hiring"; Desc="👥 Hiring processes and recruitment"; Optional=$true},
    @{Name="Finance"; Path="Docs/Finance"; Desc="💰 Financial models and projections"; Optional=$true},
    @{Name="Legal-HR"; Path="Docs/Legal-HR"; Desc="⚖️  Legal contracts and HR policies"; Optional=$true}
)

foreach ($repo in $docRepos) {
    # Create parent directory if needed (for Operations/Hiring)
    $parentDir = Split-Path $repo.Path -Parent
    if ($parentDir -and -not (Test-Path $parentDir)) {
        New-Item -ItemType Directory -Force -Path $parentDir | Out-Null
    }
    Clone-Repository -repoName $repo.Name -targetPath $repo.Path -description $repo.Desc -isOptional $repo.Optional
}

# Clone development repositories
Write-Host "💻 Setting up Development repositories..." -ForegroundColor Cyan

foreach ($repoName in $DEV_REPOS) {
    Clone-Repository -repoName $repoName -targetPath "Dev/$repoName" -description "⚙️  $repoName codebase" -isOptional $false
}

# Clone Projects repository
Write-Host "📁 Setting up Projects repository..." -ForegroundColor Cyan
Clone-Repository -repoName "Projects" -targetPath "Projects" -description "💼 Client project repositories and management" -isOptional $true

# Clone Presales repository
Write-Host "💼 Setting up Presales repository..." -ForegroundColor Cyan
Clone-Repository -repoName "Presales" -targetPath "Presales" -description "🎯 Presales materials and proposals" -isOptional $true

Write-Host "🎉 Workspace setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Your workspace structure:" -ForegroundColor Cyan
Write-Host "   Docs/        - Department repositories (Strategy, Product, etc.)"
Write-Host "   Dev/         - Technical codebases ($($DEV_REPOS -join ', '))"
Write-Host "   Projects/    - Client project repositories (separate git repository)"
Write-Host "   Presales/    - Presales materials and proposals"
Write-Host ""
Write-Host "💡 Next steps:" -ForegroundColor Yellow
Write-Host "   1. Open this folder in Cursor"
Write-Host "   2. Run '.\setup\update-all.ps1' each morning to get latest changes"
Write-Host "   3. Start working with: 'Use strategy context' (or your department context)"
Write-Host "   4. Manage client projects in the Projects/ repository" 