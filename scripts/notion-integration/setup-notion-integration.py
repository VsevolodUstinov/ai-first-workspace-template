#!/usr/bin/env python3
"""
Notion Integration Setup Script
==============================

Interactive setup for Notion API integration with sales meeting automation.
Creates database, sets up properties, and tests connection.
"""

import os
import requests
import json
from datetime import datetime

class NotionSetup:
    def __init__(self):
        self.token = None
        self.base_url = "https://api.notion.com/v1"
        self.headers = None
    
    def setup_token(self):
        """Get and validate Notion API token"""
        print("🚀 Notion Integration Setup")
        print("-" * 40)
        
        # Check for existing token
        existing_token = os.getenv('NOTION_TOKEN')
        if existing_token:
            print(f"✅ Found existing NOTION_TOKEN: {existing_token[:20]}...")
            use_existing = input("Use existing token? (y/n): ").lower().strip()
            if use_existing == 'y':
                self.token = existing_token
                self.setup_headers()
                return True
        
        print("\n📋 Steps to get Notion API token:")
        print("1. Go to https://www.notion.so/my-integrations")
        print("2. Click 'New integration'")
        print("3. Name it 'Sales Meeting Automation'")
        print("4. Select your workspace")
        print("5. Copy the 'Internal Integration Token'")
        print()
        
        token = input("🔑 Enter your Notion API token: ").strip()
        if not token.startswith('secret_'):
            print("❌ Token should start with 'secret_'")
            return False
        
        self.token = token
        self.setup_headers()
        
        # Test token
        if self.test_connection():
            print("✅ Token validated successfully!")
            
            # Save to environment
            save_to_env = input("💾 Save token to .env file? (y/n): ").lower().strip()
            if save_to_env == 'y':
                self.save_to_env_file('NOTION_TOKEN', token)
            
            return True
        else:
            print("❌ Token validation failed")
            return False
    
    def setup_headers(self):
        """Setup API headers"""
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
    
    def test_connection(self):
        """Test Notion API connection"""
        try:
            url = f"{self.base_url}/users/me"
            response = requests.get(url, headers=self.headers)
            return response.status_code == 200
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def create_sales_database(self, parent_page_id):
        """Create sales meetings database"""
        database_properties = {
            "Name": {"title": {}},
            "Client": {"rich_text": {}},
            "Meeting Date": {"date": {}},
            "Lead Source": {
                "select": {
                    "options": [
                        {"name": "Inbound", "color": "green"},
                        {"name": "Outbound", "color": "blue"},
                        {"name": "Referral", "color": "purple"},
                        {"name": "Event", "color": "orange"}
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "New Lead", "color": "yellow"},
                        {"name": "Qualified", "color": "blue"},
                        {"name": "Demo Scheduled", "color": "purple"},
                        {"name": "Proposal Sent", "color": "orange"},
                        {"name": "Closed Won", "color": "green"},
                        {"name": "Closed Lost", "color": "red"}
                    ]
                }
            },
            "Next Step": {"rich_text": {}},
            "Session Version": {"rich_text": {}},
            "Meeting ID": {"rich_text": {}},
            "Created": {"created_time": {}}
        }
        
        payload = {
            "parent": {"page_id": parent_page_id},
            "title": [{"text": {"content": "Sales Meeting Analysis"}}],
            "properties": database_properties
        }
        
        try:
            url = f"{self.base_url}/databases"
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error creating database: {e}")
            return None
    
    def get_workspace_pages(self):
        """Get available pages in workspace"""
        try:
            url = f"{self.base_url}/search"
            payload = {
                "filter": {"property": "object", "value": "page"},
                "page_size": 10
            }
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json().get('results', [])
        except Exception as e:
            print(f"❌ Error getting pages: {e}")
            return []
    
    def save_to_env_file(self, key, value):
        """Save environment variable to .env file"""
        env_file = os.path.join(os.path.dirname(__file__), '.env')
        
        # Read existing content
        existing_content = ""
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                existing_content = f.read()
        
        # Update or add the key
        lines = existing_content.split('\n') if existing_content else []
        updated = False
        
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}"
                updated = True
                break
        
        if not updated:
            lines.append(f"{key}={value}")
        
        # Write back
        with open(env_file, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"💾 Saved {key} to {env_file}")

def main():
    """Main setup function"""
    setup = NotionSetup()
    
    # Step 1: Setup token
    if not setup.setup_token():
        return
    
    print("\n" + "="*50)
    print("📊 Setting up Sales Meeting Database")
    print("="*50)
    
    # Step 2: Get parent page
    pages = setup.get_workspace_pages()
    if not pages:
        print("❌ No pages found in workspace")
        print("💡 Create a page in Notion first, then share it with your integration")
        return
    
    print("\n📄 Available pages:")
    for i, page in enumerate(pages):
        title = page.get('properties', {}).get('title', {}).get('title', [{}])[0].get('text', {}).get('content', 'Untitled')
        print(f"{i+1}. {title}")
    
    try:
        choice = int(input(f"\nSelect parent page (1-{len(pages)}): ")) - 1
        parent_page = pages[choice]
        parent_id = parent_page['id']
    except (ValueError, IndexError):
        print("❌ Invalid choice")
        return
    
    # Step 3: Create database
    print(f"\n📊 Creating Sales Meeting database...")
    database = setup.create_sales_database(parent_id)
    
    if database:
        database_id = database['id']
        database_url = database['url']
        
        print("✅ Database created successfully!")
        print(f"🗄️ Database ID: {database_id}")
        print(f"🔗 Database URL: {database_url}")
        
        # Save database ID
        setup.save_to_env_file('NOTION_DATABASE_ID', database_id)
        
        print("\n" + "="*50)
        print("🎉 Setup Complete!")
        print("="*50)
        print("✅ Your Notion integration is ready!")
        print(f"✅ Database created and configured")
        print(f"✅ Environment variables saved to .env")
        print()
        print("🚀 Next steps:")
        print("1. Run the sales meeting processor")
        print("2. Check your Notion database for new entries")
        print()
        print("💡 Environment variables:")
        print(f"   NOTION_TOKEN={setup.token[:20]}...")
        print(f"   NOTION_DATABASE_ID={database_id}")
        
    else:
        print("❌ Failed to create database")

if __name__ == "__main__":
    main()
