# Cursor Rules for Sales Meeting Automation

## Demo Behavior Requirements

### 1. Notion Integration Demo
- **ALWAYS show Notion page creation** in demo mode
- **ALWAYS provide mock Notion URLs** when API keys are not configured
- Format: `https://www.notion.so/ellyanalytics/XS-Discovery-Call-Notion-{version}-{mock_id}`
- **ALWAYS show Page Title, URL, and ID** even in demo mode
- Example output:
  ```
  ✅ Mock Notion page created successfully!
  📄 Page Title: XS Discovery Call Notion 04
  🔗 Page URL: https://www.notion.so/ellyanalytics/XS-Discovery-Call-Notion-04-abc123def45604
  📄 Page ID: abc123def45604
  ```

### 2. File Organization Rules
- **Session-based folders**: `{client-name}-v{XX}/`
- **Simple file names**: `internal.md` and `notion.md`
- **Auto-versioning**: v01, v02, v03... for each new session
- **Both files in same version folder** per session

### 3. Workspace Detection
- Auto-detect workspace from script path
- Personal-Super-Agent-Ru → `Marketing-Sales/Sales Calls/`
- Personal-Super-Agent → `Marketing-Sales/Sales Calls/`
- AI-First-Workspace → `Sales Calls/`

## API Integration

### 4. Fireflies.ai Integration
- Demo meeting ID: `01K1ZF3FGSY686JHZV0QSFG57K`
- Demo URL: `https://app.fireflies.ai/view/Elly-Analytics-XS-discovery-call::01K1ZF3FGSY686JHZV0QSFG57K`
- Always use mock data when API_TOKEN not configured

### 5. Notion Integration
- **Real mode**: Requires NOTION_TOKEN and NOTION_DATABASE_ID
- **Demo mode**: Show mock page creation with realistic URLs
- **Page naming**: `{Client Name} Notion {version}`
- **Database fields**: Name, Client, Meeting Date, Lead Source, Status, Next Step

## Error Handling

### 6. Graceful Degradation
- Missing API keys → Demo mode with mock responses
- Network errors → Show error but continue with local file creation
- File conflicts → Auto-increment version numbers

### 7. User Experience
- **Always show progress indicators**: 🚀 📥 ✅ 🤖 💾 📤
- **Always provide clear status messages**
- **Always show file paths and URLs created**
- **Always indicate demo vs real mode**

## Security

### 8. Sensitive Data
- Never log full API tokens (show only first 20 chars)
- Use placeholder data for demos
- Environment variables for all credentials

## Templates

### 9. Analysis Templates
- `prompt_internal.txt` - Team summary format
- `prompt_notion.txt` - Structured CRM format
- English language for all demo workspaces
- Consistent emoji usage for visual clarity

## Integration Points

### 10. Cursor Integration
- Scripts auto-detect workspace context
- Seamless integration with existing folder structures
- No manual path configuration needed
- Compatible with all demo workspaces
