# Setup Scripts Configuration

This folder contains setup and maintenance scripts for the AI First Workspace Template. **Before using these scripts, you need to customize them for your organization.**

## ⚠️ Configuration Required

The scripts in this folder are templates that need to be configured with your specific organization and repository details.

### 1. Edit Configuration Variables

Open each script file and replace the placeholder values:

**For Bash scripts (`*.sh`):**
```bash
# Replace these values:
ORG="YOUR-GITHUB-ORGANIZATION"
DEV_REPOS=("YOUR-PRODUCT-1" "YOUR-PRODUCT-2" "YOUR-PRODUCT-3")
```

**For PowerShell scripts (`*.ps1`):**
```powershell
# Replace these values:
$ORG = "YOUR-GITHUB-ORGANIZATION"
$DEV_REPOS = @("YOUR-PRODUCT-1", "YOUR-PRODUCT-2", "YOUR-PRODUCT-3")
```

### 2. Example Configuration

If your company is "Acme Corp" with GitHub organization "acme-corp" and you have three products:

**Bash version:**
```bash
ORG="acme-corp"
DEV_REPOS=("AcmeApp" "AcmeAPI" "AcmeDashboard")
```

**PowerShell version:**
```powershell
$ORG = "acme-corp"
$DEV_REPOS = @("AcmeApp", "AcmeAPI", "AcmeDashboard")
```

## 📁 Script Files

### `clone-all-repos.sh` / `clone-all-repos.ps1`
- **Purpose**: Initial setup - clones all department and development repositories
- **Usage**: Run once when setting up a new workspace
- **Configuration needed**: Organization name and development repository names

### `update-all.sh` / `update-all.ps1`
- **Purpose**: Daily maintenance - pulls latest changes from all repositories
- **Usage**: Run daily/weekly to keep all repositories synchronized
- **Configuration needed**: Development repository names (should match clone script)

## 🚀 Quick Setup with AI Assistant

The easiest way to configure these scripts is to ask your AI assistant:

```
"Help me configure the setup scripts in this AI First Workspace Template for my organization:

Organization: [Your Company Name]
GitHub org: [your-github-org]
Development repositories: [list your products/codebases]

Please update all four setup scripts with the correct values."
```

## 💡 Usage Instructions

### First Time Setup:
1. Configure the scripts as described above
2. Set up workspace .gitignore: `cp .gitignore.template .gitignore`
3. Run: `bash setup/clone-all-repos.sh` (or `.\setup\clone-all-repos.ps1` on Windows)

### Daily Workflow:
1. Run: `bash setup/update-all.sh` (or `.\setup\update-all.ps1` on Windows)
2. Start working with AI context: "Use strategy context" (or your preferred department)

## 🔍 What Gets Cloned

**Department Repositories (always):**
- `Strategy` - Company strategy and competitive intelligence
- `Product` - Product roadmap and specifications  
- `SalesAndMarketing` - Marketing campaigns and sales processes

**Department Repositories (optional):**
- `Operations` - Operational processes and metrics
- `Operations-Hiring` - Hiring processes and recruitment
- `Finance` - Financial models and projections
- `Legal-HR` - Legal contracts and HR policies

**Your Development Repositories:**
- Whatever you configure in the `DEV_REPOS` array

**Project Repositories (optional):**
- `Projects` - Client project portfolio management
- `Presales` - Presales materials and proposals

## ⚠️ Important Notes

- **Run configuration check**: Scripts will check for placeholder values and refuse to run until configured
- **Set up .gitignore**: Copy `.gitignore.template` to `.gitignore` before running scripts
- **Repository permissions**: You'll only be able to clone repositories you have access to
- **Missing repositories**: Scripts handle missing repositories gracefully - they'll show info messages for repos that don't exist yet
- **SSH keys required**: Make sure you have SSH keys set up for GitHub access

## 🆘 Troubleshooting

**"Configuration Required" error**: You haven't replaced the placeholder values in the script files.

**"Could not clone [repo]" warnings**: Normal - means the repository doesn't exist yet or you don't have access. Create repositories as needed.

**SSH authentication errors**: Set up SSH keys for GitHub: https://docs.github.com/en/authentication/connecting-to-github-with-ssh 