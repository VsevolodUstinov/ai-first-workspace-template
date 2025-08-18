# Notion API Integration

**Purpose**: Fetch content from Notion pages and databases for use in Elly Analytics documentation and processes.

## 🚀 **Setup Instructions**

### 1. **Get Notion API Token**
1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click "New integration"
3. Name it "Elly Analytics Integration"
4. Select the workspace where your pages are located
5. Copy the "Internal Integration Token"

### 2. **Set Environment Variable**
```bash
export NOTION_TOKEN='your_integration_token_here'
```

### 3. **Install Dependencies**
```bash
pip install requests
```

## 📖 **Usage**

### **Fetch Page Content**
```bash
python notion-fetch.py "https://ellyanalytics.notion.site/VP-level-performance-marketing-consultant-public-speaker-1cf9786215cf808f8f8aee0f52f3cbc5?pvs=74"
```

### **Save to Specific File**
```bash
python notion-fetch.py "notion_url" "output_file.md"
```

## 🔧 **Features**

- **Page Content Extraction**: Fetches full page content from Notion
- **Block Processing**: Handles different Notion block types (headings, lists, code, etc.)
- **Markdown Output**: Converts Notion content to markdown format
- **Metadata Preservation**: Includes source URL and fetch timestamp

## 📋 **Supported Block Types**

- Paragraphs
- Headings (H1, H2, H3)
- Bulleted lists
- Numbered lists
- Quotes
- Code blocks

## 🎯 **Use Cases**

1. **Job Descriptions**: Fetch updated job descriptions from Notion
2. **Documentation**: Sync documentation between Notion and local files
3. **Content Management**: Keep local documentation in sync with Notion
4. **Process Documentation**: Extract process documentation for local use

## 🔗 **Related Files**

- `notion-fetch.py` - Main script for fetching Notion content
- `README.md` - This setup guide

---

*Last Updated: July 24, 2025* 