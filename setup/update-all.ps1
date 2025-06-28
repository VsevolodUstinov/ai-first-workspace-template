# PowerShell script for updating AI First Workspace Template repositories

# ⚠️  CONFIGURATION REQUIRED ⚠️
# Before running this script, customize these variables for your organization:

# TODO: Replace with your development repository names (same as in clone-all-repos.ps1)
# Examples: @("MyApp", "MyAPI", "MyMobileApp") or @("Frontend", "Backend", "Mobile")
$DEV_REPOS = @("YOUR-PRODUCT-1", "YOUR-PRODUCT-2", "YOUR-PRODUCT-3")

# ============================================================================
# Configuration check
if ($DEV_REPOS -contains "YOUR-PRODUCT-1") {
    Write-Host "⚠️  CONFIGURATION REQUIRED" -ForegroundColor Red
    Write-Host ""
    Write-Host "Before running this script, you need to customize it for your organization:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Open this file: setup\update-all.ps1"
    Write-Host "2. Replace the `$DEV_REPOS array with your actual repository names"
    Write-Host "   (should match what you configured in clone-all-repos.ps1)"
    Write-Host ""
    Write-Host "Example configuration:" -ForegroundColor Cyan
    Write-Host '   $DEV_REPOS = @("MyMainApp", "MyAPI", "MyDashboard")'
    Write-Host ""
    Write-Host "💡 Pro tip: Ask your AI assistant to help customize this script!" -ForegroundColor Green
    exit 1
}

Write-Host "🔄 Updating AI First Workspace Template..." -ForegroundColor Green
Write-Host ""

# Update workspace repository itself
Write-Host "📋 Updating workspace template..." -ForegroundColor Cyan
git pull
Write-Host ""

# Array of documentation repositories
$docRepos = @("Strategy", "Product", "SalesAndMarketing", "Operations", "Operations/Hiring", "Finance", "Legal-HR")

# Update documentation repositories in Docs/
Write-Host "📚 Updating Documentation repositories..." -ForegroundColor Cyan
foreach ($repo in $docRepos) {
    $repoPath = "Docs/$repo"
    if (Test-Path $repoPath) {
        Write-Host "📱 Updating $repo repository..." -ForegroundColor Yellow
        try {
            Push-Location $repoPath
            git pull
            Pop-Location
        }
        catch {
            Write-Host "   ⚠️  Update failed (possibly empty repository)" -ForegroundColor Red
        }
    }
    else {
        Write-Host "ℹ️  $repo repository not yet cloned (run .\setup\clone-all-repos.ps1)" -ForegroundColor Yellow
    }
}
Write-Host ""

# Update development repositories in Dev/
Write-Host "💻 Updating Development repositories..." -ForegroundColor Cyan
foreach ($repo in $DEV_REPOS) {
    $repoPath = "Dev/$repo"
    if (Test-Path $repoPath) {
        Write-Host "⚙️  Updating $repo repository..." -ForegroundColor Yellow
        try {
            Push-Location $repoPath
            git pull
            Pop-Location
        }
        catch {
            Write-Host "   ⚠️  Update failed (possibly empty repository)" -ForegroundColor Red
        }
    }
    else {
        Write-Host "ℹ️  $repo repository not yet cloned (run .\setup\clone-all-repos.ps1)" -ForegroundColor Yellow
    }
}
Write-Host ""

# Update Presales repository
Write-Host "💼 Updating Presales repository..." -ForegroundColor Cyan
if (Test-Path "Presales") {
    Write-Host "🎯 Updating Presales repository..." -ForegroundColor Yellow
    try {
        Push-Location "Presales"
        git pull
        Pop-Location
    }
    catch {
        Write-Host "   ⚠️  Update failed (possibly empty repository)" -ForegroundColor Red
    }
}
else {
    Write-Host "ℹ️  Presales repository not yet cloned (run .\setup\clone-all-repos.ps1)" -ForegroundColor Yellow
}
Write-Host ""

# Update Projects repository
Write-Host "🚀 Updating Projects repository..." -ForegroundColor Cyan
if (Test-Path "Projects/.git") {
    Write-Host "📊 Updating Projects repository..." -ForegroundColor Yellow
    try {
        Push-Location "Projects"
        git pull
        Pop-Location
    }
    catch {
        Write-Host "   ⚠️  Update failed for Projects repository" -ForegroundColor Red
    }
}
else {
    Write-Host "ℹ️  Projects repository not yet cloned (run .\setup\clone-all-repos.ps1)" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "🎉 Workspace update complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Summary:" -ForegroundColor Cyan
Write-Host "   📚 Documentation repos in Docs/"
Write-Host "   💻 Development repos in Dev/ ($($DEV_REPOS -join ', '))"
Write-Host "   🚀 Project repos in Projects/"
Write-Host "   💼 Presales repo in root level"
Write-Host ""
Write-Host "💡 To add a new client project:" -ForegroundColor Yellow
Write-Host "   cd Projects && git clone <project-repo-url>" 