#!/bin/bash

# Ensure we're using bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ This script requires bash. Please run with: bash setup/clone-all-repos.sh"
    exit 1
fi

# ⚠️  CONFIGURATION REQUIRED ⚠️
# Before running this script, customize these variables for your organization:

# TODO: Replace with your GitHub organization name
ORG="YOUR-GITHUB-ORGANIZATION"

# TODO: Replace with your development repository names
# Examples: ("MyApp" "MyAPI" "MyMobileApp") or ("Frontend" "Backend" "Mobile")
DEV_REPOS=("YOUR-PRODUCT-1" "YOUR-PRODUCT-2" "YOUR-PRODUCT-3")

# ============================================================================
# Configuration check
if [ "$ORG" = "YOUR-GITHUB-ORGANIZATION" ]; then
    echo "⚠️  CONFIGURATION REQUIRED"
    echo ""
    echo "Before running this script, you need to customize it for your organization:"
    echo ""
    echo "1. Open this file: setup/clone-all-repos.sh"
    echo "2. Replace 'YOUR-GITHUB-ORGANIZATION' with your GitHub organization name"
    echo "3. Replace the DEV_REPOS array with your actual repository names"
    echo ""
    echo "Example configuration:"
    echo '   ORG="mycompany"'
    echo '   DEV_REPOS=("MyMainApp" "MyAPI" "MyDashboard")'
    echo ""
    echo "💡 Pro tip: Ask your AI assistant to help customize this script!"
    exit 1
fi

echo "🚀 Setting up AI First Workspace Template..."
echo ""

# Set up workspace .gitignore if it doesn't exist
if [ ! -f ".gitignore" ] && [ -f ".gitignore.template" ]; then
    echo "📝 Setting up workspace .gitignore..."
    cp .gitignore.template .gitignore
    echo "   ✅ Copied .gitignore.template to .gitignore"
    echo ""
fi

# Create main organizational folders
echo "📁 Creating organizational structure..."
mkdir -p Docs Dev
echo ""

echo "📋 Cloning repositories for organization: $ORG"
echo "Note: You'll only be able to clone repositories you have access to"
echo ""

# Clone documentation repositories to Docs/
echo "📚 Setting up Documentation repositories..."

# Strategy repository
if [ ! -d "Docs/Strategy" ]; then
    echo "🎯 Company strategy and competitive intelligence"
    echo "   Cloning Strategy to Docs/..."
    if git clone "git@github.com:$ORG/Strategy.git" "Docs/Strategy" 2>/dev/null; then
        echo "   ✅ Successfully cloned Strategy to Docs/"
    else
        echo "   ⚠️  Could not clone Strategy (check access permissions or repository may not exist yet)"
    fi
    echo ""
else
    echo "🎯 Company strategy and competitive intelligence"
    echo "   ✅ Docs/Strategy already exists, skipping..."
    echo ""
fi

# Product repository
if [ ! -d "Docs/Product" ]; then
    echo "📱 Product roadmap and specifications"
    echo "   Cloning Product to Docs/..."
    if git clone "git@github.com:$ORG/Product.git" "Docs/Product" 2>/dev/null; then
        echo "   ✅ Successfully cloned Product to Docs/"
    else
        echo "   ⚠️  Could not clone Product (check access permissions or repository may not exist yet)"
    fi
    echo ""
else
    echo "📱 Product roadmap and specifications"
    echo "   ✅ Docs/Product already exists, skipping..."
    echo ""
fi

# SalesAndMarketing repository
if [ ! -d "Docs/SalesAndMarketing" ]; then
    echo "📈 Campaigns, content, and sales processes"
    echo "   Cloning SalesAndMarketing to Docs/..."
    if git clone "git@github.com:$ORG/SalesAndMarketing.git" "Docs/SalesAndMarketing" 2>/dev/null; then
        echo "   ✅ Successfully cloned SalesAndMarketing to Docs/"
    else
        echo "   ⚠️  Could not clone SalesAndMarketing (check access permissions or repository may not exist yet)"
    fi
    echo ""
else
    echo "📈 Campaigns, content, and sales processes"
    echo "   ✅ Docs/SalesAndMarketing already exists, skipping..."
    echo ""
fi

# Operations repository
if [ ! -d "Docs/Operations" ]; then
    echo "📊 Operational processes and metrics"
    echo "   Cloning Operations to Docs/..."
    if git clone "git@github.com:$ORG/Operations.git" "Docs/Operations" 2>/dev/null; then
        echo "   ✅ Successfully cloned Operations to Docs/"
    else
        echo "   ℹ️  Operations repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "📊 Operational processes and metrics"
    echo "   ✅ Docs/Operations already exists, skipping..."
    echo ""
fi

# Finance repository
if [ ! -d "Docs/Finance" ]; then
    echo "💰 Financial models and projections"
    echo "   Cloning Finance to Docs/..."
    if git clone "git@github.com:$ORG/Finance.git" "Docs/Finance" 2>/dev/null; then
        echo "   ✅ Successfully cloned Finance to Docs/"
    else
        echo "   ℹ️  Finance repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "💰 Financial models and projections"
    echo "   ✅ Docs/Finance already exists, skipping..."
    echo ""
fi

# Legal-HR repository
if [ ! -d "Docs/Legal-HR" ]; then
    echo "⚖️  Legal contracts and HR policies"
    echo "   Cloning Legal-HR to Docs/..."
    if git clone "git@github.com:$ORG/Legal-HR.git" "Docs/Legal-HR" 2>/dev/null; then
        echo "   ✅ Successfully cloned Legal-HR to Docs/"
    else
        echo "   ℹ️  Legal-HR repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "⚖️  Legal contracts and HR policies"
    echo "   ✅ Docs/Legal-HR already exists, skipping..."
    echo ""
fi

# Operations/Hiring repository
if [ ! -d "Docs/Operations/Hiring" ]; then
    echo "👥 Hiring processes and recruitment"
    echo "   Cloning Operations-Hiring to Docs/Operations/Hiring..."
    # Create parent directory if it doesn't exist
    mkdir -p "Docs/Operations"
    if git clone "git@github.com:$ORG/Operations-Hiring.git" "Docs/Operations/Hiring" 2>/dev/null; then
        echo "   ✅ Successfully cloned Operations-Hiring"
    else
        echo "   ℹ️  Operations-Hiring repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "👥 Hiring processes and recruitment"
    echo "   ✅ Docs/Operations/Hiring already exists, skipping..."
    echo ""
fi

# Clone technical repositories to Dev/
echo "💻 Setting up Development repositories..."

for repo in "${DEV_REPOS[@]}"; do
    if [ ! -d "Dev/$repo" ]; then
        echo "⚙️  $repo codebase"
        echo "   Cloning $repo to Dev/..."
        if git clone "git@github.com:$ORG/$repo.git" "Dev/$repo" 2>/dev/null; then
            echo "   ✅ Successfully cloned $repo to Dev/"
        else
            echo "   ⚠️  Could not clone $repo (check access permissions or repository may not exist yet)"
        fi
        echo ""
    else
        echo "⚙️  $repo codebase"
        echo "   ✅ Dev/$repo already exists, skipping..."
        echo ""
    fi
done

# Set up Projects repository  
echo "📁 Setting up Projects repository..."
if [ ! -d "Projects/.git" ]; then
    echo "💼 Client project repositories and management"
    echo "   Cloning Projects..."
    if git clone "git@github.com:$ORG/Projects.git" "Projects" 2>/dev/null; then
        echo "   ✅ Successfully cloned Projects"
    else
        echo "   ℹ️  Projects repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "💼 Client project repositories and management"
    echo "   ✅ Projects already exists, skipping..."
    echo ""
fi

# Set up Presales repository
echo "💼 Setting up Presales repository..."
if [ ! -d "Presales/.git" ]; then
    echo "🎯 Presales materials and proposals"
    echo "   Cloning Presales..."
    if git clone "git@github.com:$ORG/Presales.git" "Presales" 2>/dev/null; then
        echo "   ✅ Successfully cloned Presales"
    else
        echo "   ℹ️  Presales repository not yet created (can be created later)"
    fi
    echo ""
else
    echo "🎯 Presales materials and proposals"
    echo "   ✅ Presales already exists, skipping..."
    echo ""
fi

echo "🎉 Workspace setup complete!"
echo ""
echo "📁 Your workspace structure:"
echo "   Docs/        - Department repositories (Strategy, Product, etc.)"
echo "   Dev/         - Technical codebases (${DEV_REPOS[*]})"
echo "   Projects/    - Client project repositories (separate git repository)"
echo "   Presales/    - Presales materials and proposals"
echo ""
echo "💡 Next steps:"
echo "   1. Open this folder in Cursor"
echo "   2. Run 'bash setup/update-all.sh' each morning to get latest changes"
echo "   3. Start working with: 'Use strategy context' (or your department context)"
echo "   4. Manage client projects in the Projects/ repository" 