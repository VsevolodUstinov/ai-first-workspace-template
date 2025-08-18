# Automated Sales Meeting Processing - Demo

🚀 **Demo system for processing Fireflies.ai meeting transcripts and creating structured client profiles.**

This is a demonstration version designed for presentations and workshops. It processes a specific demo meeting to show AI-powered sales automation capabilities.

## 🎯 Demo Meeting

**Meeting:** Elly Analytics XS Discovery Call  
**Meeting ID:** `01K1ZF3FGSY686JHZV0QSFG57K`  
**URL:** https://app.fireflies.ai/view/Elly-Analytics-XS-discovery-call::01K1ZF3FGSY686JHZV0QSFG57K

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment (Optional)
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run Demo
```bash
python demo-meeting-processor.py
```

## 📋 What It Does

1. **Fetches Meeting Transcript** from Fireflies.ai API
2. **Processes with AI** using two different analysis templates:
   - `prompt_internal.txt` - Internal team summary
   - `prompt_notion.txt` - Structured sales analysis
3. **Saves Results** in markdown format with timestamps
4. **Auto-detects Workspace** and saves files appropriately

## 📁 Output Files

The script creates files in the `output/` directory:
- `XS Discovery Call_prompt_internal_[timestamp].md`
- `XS Discovery Call_prompt_notion_[timestamp].md`

## 🔧 Demo Mode

**Without API Keys:** Script runs in demo mode with mock data  
**With API Keys:** Connects to real Fireflies.ai and OpenAI APIs

## 📊 Example Output

### Internal Summary
```markdown
🎯 **Meeting Purpose**
- Discovery call with XS Corp
- Initial exploration of marketing analytics needs

👥 **Client Overview**
- XS Corp - B2C SaaS company
- Subscription-based business model

💻 **Current Tech Stack**
- Google Ads and Facebook campaigns
- $50K monthly ad spend
- Attribution challenges
```

### Notion Summary
```markdown
# 📌 Short Summary

**Lead Information**
- **Lead Source:** Inbound
- **🚀 Next Step:** Meeting scheduled: Yes - Jan 22, 2024
- **👤 Business Type:** B2C SaaS
- **💸 Ad Spend & Channels:** $50K monthly - Google Ads, Facebook
```

## 🎬 Live Demo Instructions

1. **Show Fireflies.ai** with the demo meeting
2. **Run the script** and explain the process
3. **Display results** showing AI-generated analysis
4. **Highlight key features:**
   - Automatic workspace detection
   - Dual analysis templates
   - Structured output format
   - Real-time processing

## 🔗 Integration Possibilities

- **Notion:** Automatic client profile creation
- **CRM Systems:** Lead scoring and data enrichment  
- **Slack/Teams:** Automated meeting summaries
- **Email:** Follow-up action items

## ⚙️ Configuration

The script automatically detects the workspace:
- `Personal-Super-Agent-Ru` → Saves in this workspace
- `Personal-Super-Agent` → Saves in this workspace  
- `ai-first-workspace-template` → Saves in this workspace

## 🎯 Use Cases

- **Sales Teams:** Automated meeting summaries
- **Account Managers:** Client profile building
- **Marketing:** Lead qualification insights
- **Management:** Pipeline analysis and coaching

---

*This is a demonstration tool designed to showcase AI-powered sales automation capabilities. Perfect for presentations, workshops, and proof-of-concept demonstrations.*
