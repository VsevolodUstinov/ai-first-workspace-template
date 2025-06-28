#!/bin/bash

# ⚠️  CONFIGURATION REQUIRED ⚠️
# Before running this script, customize these variables for your organization:

# TODO: Replace with your development repository names (same as in clone-all-repos.sh)
# Examples: ("MyApp" "MyAPI" "MyMobileApp") or ("Frontend" "Backend" "Mobile")
DEV_REPOS=("YOUR-PRODUCT-1" "YOUR-PRODUCT-2" "YOUR-PRODUCT-3")

# ============================================================================
# Configuration check
if [[ " ${DEV_REPOS[*]} " =~ " YOUR-PRODUCT-1 " ]]; then
    echo "⚠️  CONFIGURATION REQUIRED"
    echo ""
    echo "Before running this script, you need to customize it for your organization:"
    echo ""
    echo "1. Open this file: setup/update-all.sh"
    echo "2. Replace the DEV_REPOS array with your actual repository names"
    echo "   (should match what you configured in clone-all-repos.sh)"
    echo ""
    echo "Example configuration:"
    echo '   DEV_REPOS=("MyMainApp" "MyAPI" "MyDashboard")'
    echo ""
    echo "💡 Pro tip: Ask your AI assistant to help customize this script!"
    exit 1
fi

echo "🔄 Updating AI First Workspace Template..."
echo ""

# Update workspace repository itself
echo "📋 Updating workspace template..."
git pull
echo ""

# Array of documentation repositories
doc_repos=("Strategy" "Product" "SalesAndMarketing" "Operations" "Operations/Hiring" "Finance" "Legal-HR")

# Update documentation repositories in Docs/
echo "📚 Updating Documentation repositories..."
for repo in "${doc_repos[@]}"; do
    repo_path="Docs/$repo"
    if [ -d "$repo_path" ]; then
        echo "📱 Updating $repo repository..."
        (cd "$repo_path" && git pull) || echo "   ⚠️  Update failed (possibly empty repository)"
    else
        echo "ℹ️  $repo repository not yet cloned (run ./setup/clone-all-repos.sh)"
    fi
done
echo ""

# Update development repositories in Dev/
echo "💻 Updating Development repositories..."
for repo in "${DEV_REPOS[@]}"; do
    repo_path="Dev/$repo"
    if [ -d "$repo_path" ]; then
        echo "⚙️  Updating $repo repository..."
        (cd "$repo_path" && git pull) || echo "   ⚠️  Update failed (possibly empty repository)"
    else
        echo "ℹ️  $repo repository not yet cloned (run ./setup/clone-all-repos.sh)"
    fi
done
echo ""

# Update Presales repository
echo "💼 Updating Presales repository..."
if [ -d "Presales" ]; then
    echo "🎯 Updating Presales repository..."
    (cd Presales && git pull) || echo "   ⚠️  Update failed (possibly empty repository)"
else
    echo "ℹ️  Presales repository not yet cloned (run ./setup/clone-all-repos.sh)"
fi
echo ""

# Update Projects repository
echo "🚀 Updating Projects repository..."
if [ -d "Projects/.git" ]; then
    echo "📊 Updating Projects repository..."
    (cd Projects && git pull) || echo "   ⚠️  Update failed for Projects repository"
else
    echo "ℹ️  Projects repository not yet cloned (run ./setup/clone-all-repos.sh)"
fi
echo ""

echo "🎉 Workspace update complete!"
echo ""
echo "📊 Summary:"
echo "   📚 Documentation repos in Docs/"
echo "   💻 Development repos in Dev/ (${DEV_REPOS[*]})" 
echo "   🚀 Project repos in Projects/"
echo "   💼 Presales repo in root level"
echo ""
echo "💡 To add a new client project:"
echo "   cd Projects && git clone <project-repo-url>" 