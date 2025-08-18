#!/usr/bin/env python3
"""
Notion API Integration Script
Purpose: Fetch data from Notion pages and databases
"""

import requests
import json
import os
from datetime import datetime
import sys

class NotionAPI:
    def __init__(self, token=None):
        self.token = token or os.getenv('NOTION_TOKEN')
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
    
    def get_page_content(self, page_id):
        """Fetch page content from Notion"""
        try:
            url = f"{self.base_url}/pages/{page_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None
    
    def get_page_blocks(self, page_id):
        """Fetch all blocks from a Notion page"""
        try:
            url = f"{self.base_url}/blocks/{page_id}/children"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching blocks: {e}")
            return None
    
    def extract_text_from_blocks(self, blocks_data):
        """Extract text content from Notion blocks"""
        if not blocks_data or 'results' not in blocks_data:
            return ""
        
        text_content = []
        
        for block in blocks_data['results']:
            block_type = block.get('type', '')
            
            if block_type == 'paragraph':
                rich_text = block.get('paragraph', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(text.get('plain_text', ''))
            
            elif block_type == 'heading_1':
                rich_text = block.get('heading_1', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"# {text.get('plain_text', '')}")
            
            elif block_type == 'heading_2':
                rich_text = block.get('heading_2', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"## {text.get('plain_text', '')}")
            
            elif block_type == 'heading_3':
                rich_text = block.get('heading_3', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"### {text.get('plain_text', '')}")
            
            elif block_type == 'bulleted_list_item':
                rich_text = block.get('bulleted_list_item', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"- {text.get('plain_text', '')}")
            
            elif block_type == 'numbered_list_item':
                rich_text = block.get('numbered_list_item', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"1. {text.get('plain_text', '')}")
            
            elif block_type == 'quote':
                rich_text = block.get('quote', {}).get('rich_text', [])
                for text in rich_text:
                    text_content.append(f"> {text.get('plain_text', '')}")
            
            elif block_type == 'code':
                rich_text = block.get('code', {}).get('rich_text', [])
                language = block.get('code', {}).get('language', '')
                code_text = ""
                for text in rich_text:
                    code_text += text.get('plain_text', '')
                text_content.append(f"```{language}\n{code_text}\n```")
        
        return '\n'.join(text_content)

def extract_page_id_from_url(url):
    """Extract page ID from Notion URL"""
    # Remove query parameters
    url = url.split('?')[0]
    
    # Extract the last part which should be the page ID
    parts = url.split('/')
    page_id = parts[-1]
    
    # Remove any additional formatting
    page_id = page_id.split('-')[-1]
    
    return page_id

def main():
    if len(sys.argv) < 2:
        print("Usage: python notion-fetch.py <notion_url> [output_file]")
        print("Example: python notion-fetch.py https://ellyanalytics.notion.site/VP-level-performance-marketing-consultant-public-speaker-1cf9786215cf808f8f8aee0f52f3cbc5?pvs=74")
        sys.exit(1)
    
    notion_url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "notion_content.md"
    
    # Extract page ID from URL
    page_id = extract_page_id_from_url(notion_url)
    print(f"Extracted page ID: {page_id}")
    
    # Initialize Notion API
    notion = NotionAPI()
    
    if not notion.token:
        print("Error: NOTION_TOKEN environment variable not set")
        print("Please set your Notion API token:")
        print("export NOTION_TOKEN='your_token_here'")
        sys.exit(1)
    
    # Fetch page content
    print("Fetching page content...")
    page_data = notion.get_page_content(page_id)
    
    if not page_data:
        print("Failed to fetch page content")
        sys.exit(1)
    
    # Fetch page blocks
    print("Fetching page blocks...")
    blocks_data = notion.get_page_blocks(page_id)
    
    if not blocks_data:
        print("Failed to fetch page blocks")
        sys.exit(1)
    
    # Extract text content
    print("Extracting text content...")
    content = notion.extract_text_from_blocks(blocks_data)
    
    # Add page metadata
    page_title = ""
    if 'properties' in page_data and 'title' in page_data['properties']:
        title_prop = page_data['properties']['title']
        if 'title' in title_prop and title_prop['title']:
            page_title = title_prop['title'][0]['plain_text']
    
    # Create markdown content
    markdown_content = f"""# {page_title}

**Source:** {notion_url}  
**Fetched:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

{content}

---
*Content fetched from Notion using notion-fetch.py*
"""
    
    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Content saved to: {output_file}")
    print(f"Page title: {page_title}")
    print(f"Content length: {len(content)} characters")

if __name__ == "__main__":
    main() 