#!/usr/bin/env python3
"""
Automated Sales Meeting Processing - Demo Version
==============================================

Demo script for processing Fireflies.ai meeting transcripts and creating 
structured client profiles. This version is designed for presentation purposes
and always processes the same demo meeting.

Demo Meeting: Elly Analytics XS discovery call
Meeting ID: 01K1ZF3FGSY686JHZV0QSFG57K
URL: https://app.fireflies.ai/view/Elly-Analytics-XS-discovery-call::01K1ZF3FGSY686JHZV0QSFG57K
"""

import os
import requests
import json
import time
from datetime import datetime
from openai import OpenAI

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using system environment variables.")

# === DEMO CONFIGURATION ===

# Demo meeting details - always the same for consistency
DEMO_MEETING_ID = "01K1ZF3FGSY686JHZV0QSFG57K"
DEMO_MEETING_URL = "https://app.fireflies.ai/view/Elly-Analytics-XS-discovery-call::01K1ZF3FGSY686JHZV0QSFG57K"
DEMO_CLIENT_NAME = "XS Discovery Call"

# Fireflies.ai API Configuration
API_TOKEN = os.getenv("FIREFLIES_API_TOKEN", "your_fireflies_token_here")
API_URL = "https://api.fireflies.ai/graphql"

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_key_here")

# Demo sales team emails (anonymized)
SALES_EMAILS = {
    "sales1@company.com",
    "sales2@company.com", 
    "sales3@company.com"
}

# Automatically detect workspace and set output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def detect_workspace():
    """Detect which workspace we're running from and set appropriate output directory"""
    current_path = SCRIPT_DIR
    
    # Check for workspace identifiers and set output to Marketing-Sales/Sales Calls
    if "Personal-Super-Agent-Ru" in current_path:
        # Navigate to Marketing-Sales/Sales Calls folder
        base_path = current_path.split("Personal-Super-Agent-Ru")[0] + "Personal-Super-Agent-Ru"
        output_path = os.path.join(base_path, "Docs", "My Company Example", "Marketing-Sales", "Sales Calls")
        return "Personal-Super-Agent-Ru", output_path
    elif "Personal-Super-Agent" in current_path:
        # Navigate to Marketing-Sales/Sales Calls folder  
        base_path = current_path.split("Personal-Super-Agent")[0] + "Personal-Super-Agent"
        output_path = os.path.join(base_path, "Docs", "My Company Example", "Marketing-Sales", "Sales Calls")
        return "Personal-Super-Agent", output_path
    elif "ai-first-workspace-template" in current_path:
        # Navigate to appropriate folder in AI-First workspace
        base_path = current_path.split("ai-first-workspace-template")[0] + "ai-first-workspace-template"
        output_path = os.path.join(base_path, "Sales Calls")
        return "AI-First-Workspace", output_path
    else:
        return "Unknown", os.path.join(SCRIPT_DIR, "output")

WORKSPACE_NAME, OUTPUT_DIR = detect_workspace()

def load_prompt_template(template_name):
    """Load prompt template from file"""
    template_path = os.path.join(SCRIPT_DIR, f"{template_name}.txt")
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ Template file {template_name}.txt not found. Using default.")
        return get_default_template(template_name)

def get_default_template(template_name):
    """Get default template if file is missing"""
    if template_name == "prompt_internal":
        return """
# Sales Meeting Analysis Agent for Demo

You are an expert sales analyst specializing in creating detailed meeting summaries 
between our sales team and potential clients.

## Your Task
Analyze the provided meeting transcript and create a structured summary focusing on:
1. Client business overview
2. Current tech stack and challenges  
3. Key pain points discussed
4. Next steps and follow-up actions

## Output Format
🎯 **Meeting Purpose**
- Meeting type (discovery, demo, negotiation)
- Brief overview in 2-3 sentences

👥 **Client Overview** 
- Business name and type
- What they do

💻 **Current Tech Stack** (if discussed)
- Advertising channels and budgets
- CRM/Backend systems
- Marketing tools
- Analytics stack

🔥 **Pain Points** (if discussed)
- Specific problems with examples
- Client's own words and concerns

📝 **Key Discussion Points**
- 3-5 most important topics discussed
- Focus on client-specific information

🎯 **Next Steps**
- Agreed follow-up actions
- Timeline for decisions
- Materials to prepare

**Important:** 
- Focus on client information, not our company details
- Maximum 800 words
- Use bullet points for clarity
- Include only discussed topics
"""
    
    elif template_name == "prompt_notion":
        return """
# VP of Sales Meeting Summary Agent

You're a VP of Sales with extensive SaaS experience. Create a structured meeting 
summary for internal team use.

## Output Format

# 📌 Short Summary

**Lead Information**
- **Lead Source:** [Inbound/Outbound/Other]
- **🚀 Next Step:** [Meeting scheduled: Yes/No - Date/Time or reason for refusal]
- **👤 Contact Role:** [Job Title]
- **👤 Business Type:** [B2B/B2C/eCommerce/etc.]
- **💸 Ad Spend & Channels:** [Mentioned budgets or "Not discussed"]
- **🎯 Decision-Maker Status:** [Yes/No/Unknown and why]
- **🎯 ICP Fit:** [Yes/No/Unknown - B2C lead-gen, eCommerce with repeat purchases, SaaS subscription]

**💬 Client Engagement Level:** [Number of questions asked by client]

**✨ Key Positive Reactions (3 bullet points):**
- [Reaction 1]
- [Reaction 2] 
- [Reaction 3]

**⚡ Main Pain Points (3 bullet points):**
- [Pain Point 1]
- [Pain Point 2]
- [Pain Point 3]

**🚧 Key Objections (3 bullet points):**
- [Objection 1]
- [Objection 2]
- [Objection 3]

# 🔍 Detailed Analysis

## 1. Company & Prospect Overview
- Business type and main product/service
- Prospect's role and primary goals

## 2. Marketing & Tech Stack
- Ad Channels: [List or "Not discussed"]
- CRM/Backend: [Systems mentioned or "Not discussed"]
- Ad Spend: [Budget information or "Not discussed"]
- Current Reporting: [Tools mentioned or "Not discussed"]

## 3. Discovery & Q&A
**Discovery Questions Asked:**
- Q1: [Question] → A1: [Summary response]
- Q2: [Question] → A2: [Summary response]

**Client Questions:**
- Q1: [Client question] → Response: [How answered]
- Q2: [Client question] → Response: [How answered]

## 4. Next Steps
[To be filled manually by AE]
"""

def fetch_meeting_transcript():
    """Fetch the demo meeting transcript from Fireflies.ai"""
    
    if API_TOKEN == "your_fireflies_token_here":
        print("🔧 Demo Mode: Using mock transcript data")
        return get_mock_transcript()
    
    query = """
    query GetTranscript($transcriptId: String!) {
        transcript(id: $transcriptId) {
            id
            title
            date
            duration
            sentences {
                text
                speaker_name
                speaker_id
            }
            summary {
                overview
                bullet_points
                action_items
            }
            participants {
                name
                email
            }
        }
    }
    """
    
    variables = {"transcriptId": DEMO_MEETING_ID}
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(
            API_URL,
            json={"query": query, "variables": variables},
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'errors' in data:
                print(f"❌ API Error: {data['errors']}")
                return get_mock_transcript()
            return data['data']['transcript']
        else:
            print(f"❌ HTTP Error {response.status_code}: {response.text}")
            return get_mock_transcript()
            
    except Exception as e:
        print(f"❌ Error fetching transcript: {e}")
        return get_mock_transcript()

def get_mock_transcript():
    """Mock transcript data for demo purposes"""
    return {
        "id": DEMO_MEETING_ID,
        "title": "Elly Analytics + XS - Discovery Call",
        "date": "2024-01-15T10:00:00Z",
        "duration": 2700,  # 45 minutes
        "sentences": [
            {"text": "Hello everyone, thanks for joining today's discovery call.", "speaker_name": "Sales Rep", "speaker_id": "sales1"},
            {"text": "Hi, excited to learn more about your platform.", "speaker_name": "John Smith", "speaker_id": "client1"},
            {"text": "Could you tell us about your current marketing setup?", "speaker_name": "Sales Rep", "speaker_id": "sales1"},
            {"text": "We're running Google Ads and Facebook campaigns, about $50K monthly budget. Main challenge is attribution - we can't see the full customer journey.", "speaker_name": "John Smith", "speaker_id": "client1"}
        ],
        "participants": [
            {"name": "Sales Rep", "email": "sales@company.com"},
            {"name": "John Smith", "email": "john@xscorp.com"}
        ]
    }

def create_full_transcript_text(transcript_data):
    """Convert transcript data to full text format"""
    if not transcript_data or 'sentences' not in transcript_data:
        return "No transcript data available."
    
    transcript_text = f"# Meeting: {transcript_data.get('title', 'Unknown')}\n"
    transcript_text += f"Date: {transcript_data.get('date', 'Unknown')}\n"
    transcript_text += f"Duration: {transcript_data.get('duration', 0)} seconds\n\n"
    
    for sentence in transcript_data['sentences']:
        speaker = sentence.get('speaker_name', 'Unknown')
        text = sentence.get('text', '')
        transcript_text += f"{speaker}: {text}\n"
    
    return transcript_text

def analyze_with_ai(transcript_text, template_name):
    """Analyze transcript using OpenAI with specified template"""
    
    if OPENAI_API_KEY == "your_openai_key_here":
        print("🔧 Demo Mode: Using mock AI analysis")
        return get_mock_analysis(template_name)
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        prompt_template = load_prompt_template(template_name)
        full_prompt = f"{prompt_template}\n\n## Meeting Transcript:\n{transcript_text}"
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert sales meeting analyst."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=2000,
            temperature=0.3
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"❌ Error with AI analysis: {e}")
        return get_mock_analysis(template_name)

def get_mock_analysis(template_name):
    """Mock AI analysis for demo purposes"""
    if template_name == "prompt_internal":
        return """
🎯 **Meeting Purpose**
- Discovery call with XS Corp
- Initial exploration of marketing analytics needs

👥 **Client Overview**
- XS Corp - B2C SaaS company
- Subscription-based business model

💻 **Current Tech Stack**
- Google Ads and Facebook campaigns
- $50K monthly ad spend
- Attribution challenges with customer journey tracking

🔥 **Pain Points**
- Cannot see full customer journey from click to revenue
- Attribution gaps between ad platforms and actual conversions
- Manual reporting processes taking significant time

📝 **Key Discussion Points**
- Strong product-market fit but scaling challenges
- Need for unified analytics across all touchpoints
- Interest in automated reporting solutions

🎯 **Next Steps**
- Schedule demo call for next week
- Prepare custom ROI calculator
- Send case studies from similar B2C SaaS clients
"""
    
    else:  # prompt_notion
        return """
# 📌 Short Summary

**Lead Information**
- **Lead Source:** Inbound
- **🚀 Next Step:** Meeting scheduled: Yes - Jan 22, 2024 2:00 PM
- **👤 Contact Role:** VP of Marketing
- **👤 Business Type:** B2C SaaS
- **💸 Ad Spend & Channels:** $50K monthly - Google Ads, Facebook
- **🎯 Decision-Maker Status:** Yes - has budget authority
- **🎯 ICP Fit:** Yes - B2C SaaS with subscription model

**💬 Client Engagement Level:** 8 questions asked

**✨ Key Positive Reactions:**
- "This is exactly what we've been looking for"
- "The ROI calculator looks very promising"
- "Your attribution model makes perfect sense"

**⚡ Main Pain Points:**
- Cannot track full customer journey
- Attribution gaps causing budget misallocation
- Manual reporting consuming 10+ hours weekly

**🚧 Key Objections:**
- "How does this compare to Google Analytics?"
- "Implementation timeline concerns"
- "Integration complexity with existing stack"

# 🔍 Detailed Analysis

## 1. Company & Prospect Overview
- B2C SaaS subscription business with strong growth
- VP of Marketing focused on scaling paid acquisition

## 2. Marketing & Tech Stack
- Ad Channels: Google Ads, Facebook Ads
- CRM/Backend: Salesforce + custom backend
- Ad Spend: $50K monthly budget
- Current Reporting: Google Analytics + manual Excel sheets

## 3. Discovery & Q&A
**Discovery Questions Asked:**
- Q1: Current attribution model → A1: Last-click only, major gaps
- Q2: Reporting frequency → A2: Weekly manual reports, very time-consuming

**Client Questions:**
- Q1: Integration complexity → Response: 2-week implementation typical
- Q2: ROI measurement → Response: Showed live calculator demo

## 4. Next Steps
Demo scheduled for Jan 22, prepare custom ROI analysis
"""

# Demo folder configuration - always overwrite for clean demo experience
DEMO_FOLDER_NAME = "XS Discovery Call Demo"

def get_demo_folder():
    """
    Get the fixed demo folder name for consistent demo experience.
    Files are overwritten on each run for clean presentation.
    """
    return DEMO_FOLDER_NAME

def save_analysis_to_file(analysis, template_name):
    """Save analysis to file in demo directory (overwrites for clean demo)"""
    
    # Get demo folder (always the same for consistent demo)
    demo_folder = get_demo_folder()
    demo_output_dir = os.path.join(OUTPUT_DIR, demo_folder)
    os.makedirs(demo_output_dir, exist_ok=True)
    
    # English filenames based on template type
    if template_name == "prompt_internal":
        filename = "Short Version for Slack.md"
    elif template_name == "prompt_notion":
        filename = "Notion Extended Version.md"
    else:
        filename = f"{template_name}.md"
    
    filepath = os.path.join(demo_output_dir, filename)
    
    # Demo version for metadata
    demo_version = "Demo"
    
    # Create content with metadata
    content = f"""# Automated Sales Meeting Analysis
**Client:** {DEMO_CLIENT_NAME}  
**Version:** {demo_version}  
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Workspace:** {WORKSPACE_NAME}  
**Meeting ID:** {DEMO_MEETING_ID}  
**Template:** {template_name}  
**Meeting URL:** {DEMO_MEETING_URL}

---

{analysis}

---

*This analysis was generated automatically using the Sales Meeting Processing system.*
*Session: `{demo_folder}`*
*File: `{filename}`*
"""
    
    # Save to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Return filepath and session info for Notion integration
    return filepath, demo_folder, demo_version

def send_to_notion(notion_analysis_file):
    """Send analysis to Notion using the notion integration script"""
    try:
        # Path to Notion integration script
        script_dir = os.path.dirname(SCRIPT_DIR)
        notion_script = os.path.join(script_dir, "notion-integration", "notion-send-meeting-analysis.py")
        
        if not os.path.exists(notion_script):
            print(f"⚠️ Notion script not found at: {notion_script}")
            return False
        
        # Check if Notion is configured
        if not os.getenv("NOTION_TOKEN") and not os.getenv("NOTION_DATABASE_ID"):
            print("🔧 Demo Mode: Using mock Notion integration")
            
            # Extract session info for mock link
            folder_name = os.path.basename(os.path.dirname(notion_analysis_file))
            session_version = "v01"
            if "-v" in folder_name:
                session_version = folder_name.split("-v")[-1]
            
            # Generate mock Notion page details
            mock_page_id = f"abc123def456{session_version}"
            mock_page_url = f"https://www.notion.so/ellyanalytics/XS-Discovery-Call-Demo-{mock_page_id}"
            page_title = f"XS Discovery Call Demo"
            
            print(f"✅ Mock Notion page created successfully!")
            print(f"📄 Page Title: {page_title}")
            print(f"🔗 Page URL: {mock_page_url}")
            print(f"📄 Page ID: {mock_page_id}")
            print(f"💡 To enable real integration: Set NOTION_TOKEN and NOTION_DATABASE_ID environment variables")
            return True
        
        print("📤 Sending analysis to Notion...")
        
        # Run the Notion integration script
        import subprocess
        result = subprocess.run([
            "python3", notion_script, notion_analysis_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Successfully sent to Notion!")
            print(result.stdout)
            return True
        else:
            print(f"❌ Error sending to Notion: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error with Notion integration: {e}")
        return False

def main():
    """Main execution function"""
    print("🚀 Automated Sales Meeting Processing - Demo Version")
    print(f"📁 Workspace: {WORKSPACE_NAME}")
    print(f"📂 Output Directory: {OUTPUT_DIR}")
    print(f"🎯 Processing Demo Meeting: {DEMO_MEETING_ID}")
    print("-" * 60)
    
    # Step 1: Fetch transcript
    print("📥 Fetching meeting transcript...")
    transcript_data = fetch_meeting_transcript()
    
    if not transcript_data:
        print("❌ Failed to fetch transcript data")
        return
    
    print(f"✅ Transcript fetched: {transcript_data.get('title', 'Unknown')}")
    
    # Step 2: Create full transcript text
    print("📝 Converting transcript to text format...")
    transcript_text = create_full_transcript_text(transcript_data)
    
    # Step 3: Analyze with both templates
    analyses = {}
    notion_file = None
    session_folder = None
    session_version = None
    
    for template_name in ["prompt_internal", "prompt_notion"]:
        print(f"🤖 Analyzing with {template_name} template...")
        analysis = analyze_with_ai(transcript_text, template_name)
        analyses[template_name] = analysis
        
        # Save analysis to file
        filepath, folder, version = save_analysis_to_file(analysis, template_name)
        session_folder = folder
        session_version = version
        print(f"💾 Saved: {folder}/{os.path.basename(filepath)}")
        
        # Track Notion file for upload
        if template_name == "prompt_notion":
            notion_file = filepath
    
    # Step 4: Send to Notion
    if notion_file:
        send_to_notion(notion_file)
    
    print("\n" + "=" * 60)
    print("🎉 Demo Processing Complete!")
    print(f"📊 Generated {len(analyses)} analysis reports")
    print(f"📁 Files saved in: {OUTPUT_DIR}")
    print(f"🌐 Original meeting: {DEMO_MEETING_URL}")
    
    # Display summary
    print("\n📋 Files Created:")
    for filename in os.listdir(OUTPUT_DIR):
        if DEMO_CLIENT_NAME in filename:
            print(f"  • {filename}")

if __name__ == "__main__":
    main()
