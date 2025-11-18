# Telegram Sync System - Complete Documentation

**Updated**: 2025-10-21  
**Status**: Production ready with user_id caching - **3x faster!** ✅

---

## 🤖 IMPORTANT: Documentation for AI Agents

**This documentation is written FOR AI AGENTS, not humans.**

**What this means**:
- ✅ **Concise & dense** - maximum information, minimum words
- ✅ **Technical precision** - exact implementation details when needed
- ✅ **No hand-holding** - agents can infer context and fill gaps
- ✅ **Structured for parsing** - clear sections, searchable patterns
- ❌ **No unnecessary elaboration** - no "friendly explanations" or verbose descriptions
- ❌ **No redundancy** - each fact stated once, referenced elsewhere if needed

**Human usage instructions**: See `../../.cursorrules` (parent folder) for quick commands. That's what humans should read.

**Agent usage**: Read this file when you need to:
- Understand internal architecture before modifying scripts
- Debug issues with sync system
- Add new features to existing scripts
- Understand data formats and file structures

**Writing style**: Think "technical specification" not "user manual". Dense, precise, searchable.

---

## 🎯 Quick Start

### New Contact (find handle + user_id):
```bash
cd Scripts && source venv/bin/activate

# 1. Search for contact
python3 telegram_find_handles.py --person "New Contact" --search --query "SearchTerm"
# Returns JSON with user_id, e.g., "user_id": 12345678

# 2. Save with user_id (REQUIRED for fast sync!)
python3 telegram_find_handles.py --person "New Contact" --save "@username" --user-id 12345678
```

### Batch Add user_ids to Existing Contacts:
```bash
cd Scripts && source venv/bin/activate
python3 telegram_add_user_ids_batch.py
# Adds user_ids to all contacts automatically
```

### Sync One Contact (incremental):
```bash
cd Scripts && source venv/bin/activate
python3 telegram_sync.py --person "Contact A"
```

### Reload One Contact from Date:
```bash
cd Scripts && source venv/bin/activate
python3 telegram_sync.py --person "Contact A" --since "2025-10-01"
```

### Sync All #DO_SYNC Contacts:
```bash
cd Scripts && source venv/bin/activate
python3 telegram_sync.py --all --report report.txt
```

### Check Sync Status:
```bash
cd Scripts && source venv/bin/activate
python3 telegram_analyze_status.py
# Result → Context/Telegram_Sync_Status.md
```

---

## 📚 Additional Documentation Files

1. **[Telegram_Tags_Guide.md](./Telegram_Tags_Guide.md)** - Tag system (DO_SYNC / DO_NOT_SYNC / NOT_ON_TELEGRAM)
2. **[Telegram_Sync_How_It_Works.md](./Telegram_Sync_How_It_Works.md)** - Technical deep dive
3. **[Telegram_Quick_Reference.md](./Telegram_Quick_Reference.md)** - Command cheat sheet
4. **[Telegram_Sync_Status.md](./Telegram_Sync_Status.md)** - Current contact status (auto-generated)

---

## 🔄 Three Sync Modes

### Mode 1: First Sync (No Timestamp)
**When**: Contact has no `[DONE:...]` timestamp in sync list  
**What happens**: Downloads ALL messages from entire history  
**File**: Creates new file with all messages  

```bash
python3 telegram_sync.py --person "New Contact"
```

**Example output:**
```
📥 First sync: downloading all messages
✅ 115 messages
```

---

### Mode 2: Incremental Sync (Default)
**When**: Contact has `[DONE:...]` timestamp, no `--since` parameter  
**What happens**: Downloads only NEW messages after timestamp  
**File**: Appends new messages to existing file  

```bash
python3 telegram_sync.py --person "Contact A"
```

**Example output:**
```
⚡ Incremental mode: from 2025-10-17T18:00:09
✅ 3 new messages (out of 118 total)
```

**File structure:**
```markdown
# Contact A

## Telegram history with Contact A (handle: @contact_a)

[... old messages ...]

## Update from 2025-10-18T10:30:00
### Messages after 2025-10-17T18:00:09

- 2025-10-18T09:15:00 ➡️: New message 1
- 2025-10-18T08:30:00 ⬅️: New message 2
```

---

### Mode 3: Reload from Date (Explicit --since)
**When**: You specify `--since DATE` parameter  
**What happens**: 
- Preserves messages BEFORE --since date
- Deletes messages AFTER --since date
- Re-downloads messages from --since onwards

**Use cases:**
- Corrupted data period
- Missing messages detected
- Need to refresh specific time range

```bash
python3 telegram_sync.py --person "Contact A" --since "2025-10-01"
```

**Example output:**
```
🔄 Reload mode: rewriting from 2025-10-01T00:00:00
✅ Reloaded 19 messages from 2025-10-01
```

**File structure:**
```markdown
# Contact A

## Telegram history with Contact A (handle: @contact_a)

[... messages before 2025-10-01 - preserved ...]

## Reloaded from 2025-10-01T00:00:00 on 2025-10-17T18:01:18

- 2025-10-16T04:53:05 ➡️: Recent message
- 2025-10-08T20:34:37 ➡️: Message from Oct 8
[... all messages from Oct 1 onwards ...]
```

---

## 🔒 Philosophy: Telegram = Personal Space

**Principles**:
- Telegram is personal space, NOT a work tool by default
- Sync ONLY what's explicitly marked for work
- Default: DO NOT sync
- Explicit control via tags

**Tags**:
- `#DO_SYNC` ✅ - Work (investors, partners, business)
- `#DO_NOT_SYNC` 🚫 - Personal (friends, family)
- `#NOT_ON_TELEGRAM` 📵 - Person not on Telegram
- `#NOT_CONNECTED` 🔌 - On Telegram but not in your contacts

---

## 📁 System Files

**⚠️ Naming Convention**: 
- ALL Telegram scripts MUST start with `telegram_` prefix for consistency and easy identification
- ALL Telegram documentation goes in THIS file only - do NOT create new documentation files
- Keep documentation compact and focused - high information density

```
Scripts/
├── telegram_sync.py                      # ⚡ Sync messages (FAST with user_id!) ← MAIN SCRIPT
├── telegram_find_handles.py              # 🔍 Find handles + user_ids (for new contacts)
├── telegram_add_user_ids_batch.py        # 🚀 Batch add user_ids to all contacts
├── telegram_reload_all.py                # 🔄 Batch reload all contacts (clean files)
├── telegram_contact_preview.py           # 👁️ Preview contact details
├── telegram_analyze_status.py            # 📊 Status analysis
└── telegram_common.py                    # 🔧 Shared utilities (parsing, credentials)

Context/
├── sync_list_telegram.txt             # ← MASTER LIST with handles, user_ids, tags
├── Telegram_Sync_Status.md            # Current contact status report
└── [This folder has detailed docs]

Contacts/
└── [Name]/
    └── [Name] telegram.md             # Generated message history (chronological)
```

---

## 🎨 Master List Format (sync_list_telegram.txt)

```
# New format with user_id (FAST - 3x faster sync!):
Name -> TelegramHandle [ID:user_id] #TAG [DONE:timestamp]

# Examples:
Contact A -> @contact_a [ID:12345678] #DO_SYNC [DONE:2025-10-18T00:25:00]
Contact B -> Contact B Display [ID:23456789] #DO_SYNC [DONE:2025-10-18T00:30:15]
Contact C -> @contact_c [ID:123456] #DO_NOT_SYNC
Contact D #NOT_ON_TELEGRAM
Contact E #NOT_CONNECTED

# Without user_id (slower, will prompt to add user_id):
Name -> TelegramHandle #TAG [DONE:timestamp]

# Format breakdown:
Name                    - Contact name
-> TelegramHandle       - @username or display name
[ID:12345]             - Telegram user_id (REQUIRED for fast sync!)
#TAG                    - DO_SYNC | DO_NOT_SYNC | NOT_ON_TELEGRAM | NOT_CONNECTED
[DONE:2025-10-18T...]  - Last sync timestamp
```

## ⚡ Performance: Why user_id Matters

**Without user_id**: 15-20 seconds per contact (slow iter_dialogs scan)
**With user_id**: 5-6 seconds per contact (direct lookup + early exit)

**Speed improvement**: **3x faster!**

For 64 contacts:
- Without user_id: 15-20 minutes
- With user_id: 6-7 minutes ⚡

**How to add user_ids**:
```bash
# Batch add for all contacts
python3 telegram_add_user_ids_batch.py

# Or manually when adding new contact
python3 telegram_find_handles.py --person "Name" --search
# See user_id in results, then:
python3 telegram_find_handles.py --person "Name" --save "@handle" --user-id 12345678
```

---

## 📊 Quick Reference: When to Use Which Script

### Use `telegram_find_handles.py` when:
1. ✅ Adding new person to list
2. ✅ Don't know their Telegram handle
3. ✅ Need to verify/update existing handle
4. ✅ Want to get user_id for contact

### Use `telegram_sync.py` when:
1. ✅ Handle + user_id already known (exists in sync list)
2. ✅ Regular message updates needed
3. ✅ Batch sync all #DO_SYNC contacts
4. ✅ Need speed (user_id = fast!)

### DON'T use `telegram_sync.py` when:
1. ❌ Contact has no handle (no -> in sync list)
   → First use `telegram_find_handles.py`
2. ❌ Contact has no user_id (no [ID:...])
   → Add user_id first or run `telegram_add_user_ids_batch.py`
3. ❌ Contact tagged #NOT_ON_TELEGRAM
   → Person doesn't use Telegram
4. ❌ Contact tagged #DO_NOT_SYNC (for --all mode)
   → Privacy respected, won't sync

---

## 🚀 Common Scenarios

### Scenario 1: Add New Business Contact

**Interactive workflow (recommended):**
```bash
# 1. Search for handle
python3 telegram_find_handles.py --person "New Contact" --search --query "Contact"
# Returns JSON with user_id:
# {
#   "user_id": 12345678,
#   "username": "@contact_handle",
#   ...
# }

# 2. AI/user confirms which result is correct and notes user_id

# 3. Save handle WITH user_id (IMPORTANT!)
python3 telegram_find_handles.py --person "New Contact" --save "@contact_handle" --user-id 12345678

# 4. First sync (downloads all messages - FAST with user_id!)
python3 telegram_sync.py --person "New Contact"
# Takes 5-6 seconds instead of 15-20!
```

**Result in sync list:**
```
New Contact -> @contact_handle [ID:12345678] #DO_SYNC [DONE:2025-10-18T...]
```

**⚠️ IMPORTANT**: Always save user_id! Without it, sync will fail or be very slow.

---

### Scenario 2: Weekly Update All Contacts

```bash
python3 telegram_sync.py --all --report report.txt
```

**What happens:**
- Processes ONLY contacts with `#DO_SYNC` tag
- Each contact: downloads messages after their own `[DONE:...]` timestamp
- Skips `#DO_NOT_SYNC`, `#NOT_ON_TELEGRAM`, `#NOT_CONNECTED`
- Updates timestamps for all synced contacts
- Generates report with results

---

### Scenario 3: Reload Corrupted Period

```bash
# If you noticed missing/corrupted messages from October
python3 telegram_sync.py --person "Contact A" --since "2025-10-01"
```

**What happens:**
- Preserves messages before Oct 1
- Deletes messages from Oct 1 onwards  
- Re-downloads messages from Oct 1 onwards
- Adds reload marker
- Updates timestamp

---

### Scenario 4: Mark Contact as Personal

```bash
# Edit sync_list_telegram.txt
# Change:  Contact F -> @contact_f #DO_SYNC
# To:      Contact F -> @contact_f #DO_NOT_SYNC

# Next --all run: will skip this contact
```

---

## 📊 Current Statistics

As of 2025-10-18:

- **Total contacts in Contacts/**: 169
- **All contacts tracked in sync list**: 169 ✅
- **Contacts with #DO_SYNC**: 105
  - **With user_ids (FAST)**: 56 contacts ⚡
  - **Without user_ids**: 8 contacts (need handle re-discovery)
  - **Without handles**: 41 contacts (need initial discovery)
- **Contacts with #DO_NOT_SYNC**: 32
- **Contacts with #NOT_ON_TELEGRAM**: 21
- **Contacts with #NOT_CONNECTED**: 11

**Telegram files with messages**: 56+ files
- Successfully synced 56 contacts with full message histories
- Total messages: 1,400+ across all contacts
- Identified 8 contacts with outdated handles (need re-discovery)

---

## ⚡ Next Steps

### For Production Use:

1. ✅ **System is ready** - all contacts tracked, duplicates merged
2. 📥 **Sync all #DO_SYNC contacts** - run `--all` mode
3. 🔍 **Review results** - check generated telegram.md files
4. 🏷️ **Adjust tags** - change any misclassified contacts
5. 🔄 **Weekly updates** - schedule `--all` run

---

## 💡 Pro Tips

1. **@username is best**:
   - Permanent identifier
   - Fast exact match
   - Survives display name changes

2. **Display name is fallback**:
   - Works when no @username
   - Can break if person changes name
   - Script saves both when available

3. **Tags are manual**:
   - Review after first batch sync
   - Change DO_SYNC → DO_NOT_SYNC for personal contacts
   - System respects your privacy choices

4. **Incremental is default**:
   - Fast daily updates
   - Only downloads new messages
   - Use --since only when needed (reload/fix)

5. **Monitor report.txt**:
   - Shows all sync history
   - Helps debug issues
   - Track message counts

---

## 🆘 Troubleshooting

### Contact not found:

```bash
# Check what's in list:
grep -i "name" sync_list_telegram.txt

# Verify handle is correct:
python3 telegram_contact_preview.py --handle @username

# Re-find handle if needed:
python3 telegram_find_handles.py --person "Name" --search
```

### Too many contacts syncing:

```bash
# Check tags:
grep "#DO_SYNC" sync_list_telegram.txt | wc -l

# Add DO_NOT_SYNC tags for personal contacts
```

### Need to update personal contact:

```bash
# Use --person (works even with DO_NOT_SYNC tag):
python3 telegram_sync.py --person "Contact F"
```

### Messages seem incomplete:

```bash
# Reload from specific date:
python3 telegram_sync.py --person "Contact A" --since "2025-09-01"
```

---

## 📨 Inbox Sync (AI Inbox)

**Script**: `telegram_inbox_sync.py`  
**Purpose**: Sync messages from "[AI_INBOX_NAME]" Telegram group (personal inbox)  
**Output**: `../Inbox/telegram ai inbox.md`

### Quick Usage:

```bash
# Incremental sync (default - recommended)
python3 telegram_inbox_sync.py

# Reload all messages
python3 telegram_inbox_sync.py --reload

# Reload from datetime (multiple formats supported)
python3 telegram_inbox_sync.py --since "2025-10-21 14:30"
```

### Implementation Details:

**Group Detection**:
- Group ID: `1234567890` (hardcoded in script - user's personal inbox)
- Direct lookup via `client.get_entity(GROUP_ID)` (fast)
- Fallback: if ID fails, searches by name "[ai_inbox_name]"
- Supports both Channel and Chat types

**Sync Modes**:
1. **Incremental** (default): Appends new messages after last sync timestamp
2. **Reload all** (`--reload`): Rewrites file with all messages
3. **Reload from datetime** (`--since`): Rewrites file with messages from specified time

**State Files**:
- `../Inbox/.last_sync_timestamp` - Last sync time (ISO format) for incremental sync

**Datetime Formats Supported**:
- Date only: `2025-10-21` (defaults to 00:00:00)
- Date + time (minutes): `2025-10-21 14:30`
- Date + time (seconds): `2025-10-21 14:30:45`
- ISO format: `2025-10-21T14:30:00`

**Message Format**:
```
**YYYY-MM-DDTHH:MM:SS** (Sender Name):
Message content

**YYYY-MM-DDTHH:MM:SS** (Sender Name):
🎤 [Voice message]
📝 Transcription: [Auto-transcribed text from Telegram Premium]
```

**Voice Message Transcription**:
- Automatically requests transcription for voice messages via `TranscribeAudioRequest`
- Requires Telegram Premium subscription
- Progressive retry with delays: 0s, 1s, 2s, 3s, 4s, 5s (waits for Telegram to generate transcription)
- Checks `result.pending` flag to determine if still processing
- Transcription appears in markdown output once ready
- Silently skips if unavailable after all retries

**Use Case**: Perfect for multiple syncs per day. User can run incremental sync morning/afternoon/evening to continuously process inbox messages.

**Credentials**: Uses same Telegram credentials as other scripts via `telegram_common.get_telegram_credentials()`

---

**For more details**: See other Telegram_*.md files in this folder

**Last Updated**: 2025-10-21 (Added inbox sync system with datetime-precise --since support)
