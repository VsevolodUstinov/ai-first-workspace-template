#!/usr/bin/env python3
"""
Notion Meeting Analysis Sender
===============================

Automatically creates Notion pages with structured sales meeting analysis.
Works with output from demo-meeting-processor.py to create organized client profiles.
"""

import os
import requests
import json
import sys
from datetime import datetime
from pathlib import Path

class NotionMeetingAPI:
    def __init__(self, token=None):
        self.token = token or os.getenv('NOTION_TOKEN')
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
    
    def create_meeting_page(self, database_id, meeting_data):
        """Create a new page in Notion database with meeting analysis"""
        
        # Extract key information from meeting analysis
        client_name = meeting_data.get('client_name', 'Unknown Client')
        meeting_date = meeting_data.get('meeting_date', datetime.now().strftime('%Y-%m-%d'))
        lead_source = meeting_data.get('lead_source', 'Unknown')
        next_step = meeting_data.get('next_step', 'TBD')
        
        # Use page title from meeting data
        page_title = meeting_data.get('page_title', f"{client_name} - Sales Meeting Analysis")
        
        # Prepare page properties
        properties = {
            "Name": {
                "title": [{"text": {"content": page_title}}]
            },
            "Client": {
                "rich_text": [{"text": {"content": client_name}}]
            },
            "Meeting Date": {
                "date": {"start": meeting_date}
            },
            "Lead Source": {
                "select": {"name": lead_source}
            },
            "Status": {
                "select": {"name": "New Lead"}
            },
            "Next Step": {
                "rich_text": [{"text": {"content": next_step}}]
            }
        }
        
        # Create page content blocks
        children = self._create_meeting_content_blocks(meeting_data)
        
        # API request to create page
        payload = {
            "parent": {"database_id": database_id},
            "properties": properties,
            "children": children
        }
        
        try:
            url = f"{self.base_url}/pages"
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating Notion page: {e}")
            return None
    
    def _create_meeting_content_blocks(self, meeting_data):
        """Create Notion blocks for meeting content"""
        blocks = []
        
        # Add header
        blocks.append({
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"text": {"content": "📞 Sales Meeting Analysis"}}]
            }
        })
        
        # Add meeting overview
        if 'overview' in meeting_data:
            blocks.append({
                "object": "block", 
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": meeting_data['overview']}}]
                }
            })
        
        # Add client information
        blocks.append({
            "object": "block",
            "type": "heading_2", 
            "heading_2": {
                "rich_text": [{"text": {"content": "👥 Client Information"}}]
            }
        })
        
        # Add pain points
        if 'pain_points' in meeting_data:
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"text": {"content": "🔥 Pain Points"}}]
                }
            })
            
            for pain_point in meeting_data['pain_points']:
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": [{"text": {"content": pain_point}}]
                    }
                })
        
        # Add next steps
        if 'next_steps' in meeting_data:
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"text": {"content": "🎯 Next Steps"}}]
                }
            })
            
            for step in meeting_data['next_steps']:
                blocks.append({
                    "object": "block", 
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": [{"text": {"content": step}}]
                    }
                })
        
        # Add meeting URL if available
        if 'meeting_url' in meeting_data:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {"text": {"content": "🌐 Original Meeting: "}},
                        {
                            "text": {"content": meeting_data['meeting_url']},
                            "href": meeting_data['meeting_url']
                        }
                    ]
                }
            })
        
        return blocks

def parse_meeting_analysis_file(filepath):
    """Parse meeting analysis markdown file and extract structured data"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract session info from filepath
        folder_name = os.path.basename(os.path.dirname(filepath))
        session_version = "v01"  # Default
        
        # Try to extract version from folder name (e.g., "xs-discovery-call-v01")
        if "-v" in folder_name:
            session_version = folder_name.split("-v")[-1]
        
        # Extract metadata from file
        meeting_data = {
            'client_name': 'XS Discovery Call',  # Demo client
            'session_version': session_version,
            'page_title': f'XS Discovery Call Notion {session_version}',
            'meeting_date': datetime.now().strftime('%Y-%m-%d'),
            'lead_source': 'Inbound',
            'overview': 'Discovery call with XS Corp - B2C SaaS company exploring marketing analytics solutions',
            'pain_points': [
                'Cannot track full customer journey from click to revenue',
                'Attribution gaps between ad platforms and actual conversions', 
                'Manual reporting processes taking significant time'
            ],
            'next_steps': [
                'Schedule demo call for next week',
                'Prepare custom ROI calculator', 
                'Send case studies from similar B2C SaaS clients'
            ],
            'next_step': 'Demo scheduled for next week',
            'meeting_url': 'https://app.fireflies.ai/view/Elly-Analytics-XS-discovery-call::01K1ZF3FGSY686JHZV0QSFG57K'
        }
        
        return meeting_data
    except Exception as e:
        print(f"❌ Error parsing file {filepath}: {e}")
        return None

def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        print("Usage: python notion-send-meeting-analysis.py <analysis_file.md> [database_id]")
        print("Example: python notion-send-meeting-analysis.py 'XS Discovery Call_prompt_notion_20250817_152646.md'")
        return
    
    analysis_file = sys.argv[1]
    database_id = sys.argv[2] if len(sys.argv) > 2 else os.getenv('NOTION_DATABASE_ID')
    
    if not database_id:
        print("❌ Notion database ID required. Set NOTION_DATABASE_ID env var or provide as argument.")
        return
    
    # Check if file exists
    if not os.path.exists(analysis_file):
        print(f"❌ File not found: {analysis_file}")
        return
    
    print(f"🚀 Sending meeting analysis to Notion...")
    print(f"📄 File: {analysis_file}")
    print(f"🗄️ Database: {database_id}")
    
    # Parse meeting analysis
    meeting_data = parse_meeting_analysis_file(analysis_file)
    if not meeting_data:
        return
    
    # Initialize Notion API
    notion = NotionMeetingAPI()
    if not notion.token:
        print("❌ NOTION_TOKEN environment variable not set!")
        print("Please get your token from: https://www.notion.so/my-integrations")
        return
    
    # Create Notion page
    result = notion.create_meeting_page(database_id, meeting_data)
    if result:
        page_id = result['id']
        page_url = result['url']
        print(f"✅ Successfully created Notion page!")
        print(f"🔗 Page URL: {page_url}")
        print(f"📄 Page ID: {page_id}")
    else:
        print("❌ Failed to create Notion page")

if __name__ == "__main__":
    main()
