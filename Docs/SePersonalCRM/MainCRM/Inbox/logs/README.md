# Processing Logs

This folder contains detailed logs of all inbox processing sessions.

---

## Log Types

### **Stage 1: Inbox → Processing Tasks**
**Filename:** `YYYY-MM-DD-inbox-to-processing-log.md`

**Purpose:** Documents transfer of messages from inboxes to Processing Tasks

**Contains:**
- Source messages with timestamps
- Decomposition into processing steps
- Which processing tasks were created
- NO execution details (that's Stage 2)

**Example:** `2025-11-03-inbox-to-processing-log.md`

---

### **Stage 2: Processing Tasks Execution**
**Filename:** `YYYY-MM-DD-processing-execution-log.md`

**Purpose:** Documents execution of processing tasks

**Contains:**
- What information was gathered
- Which profiles/files were updated
- What work tasks were created
- Time spent, decisions needed
- Full execution details

**Example:** `2025-11-03-processing-execution-log.md`

---

## Why Two Stages?

**Problem:** When you have multiple inboxes (email, Telegram, LinkedIn, AI inbox), processing items one-by-one can miss dependencies.

**Example:**
- Email: "Meeting with Fund X postponed"
- Telegram: "Fund X wants intro call Friday"
- LinkedIn: "Fund X partner connected"

If you process email first (mark meeting postponed), you miss that Telegram/LinkedIn have updates about the same fund!

**Solution:**
1. **Stage 1:** Collect ALL updates from ALL inboxes first
2. **Review:** See all related items together
3. **Stage 2:** Process with full context, spot connections, avoid duplicate work

---

## Log Naming Convention

**Format:** `YYYY-MM-DD-[process-type]-log.md`

**Process Types:**
- `inbox-to-processing` - Stage 1 (collection)
- `processing-execution` - Stage 2 (execution)
- `bulk-sync` - Large sync operations (e.g., sync all Telegram contacts)
- `cleanup` - Archive/cleanup operations
- `migration` - Data migration tasks

**Examples:**
- `2025-11-03-inbox-to-processing-log.md`
- `2025-11-03-processing-execution-log.md`
- `2025-11-05-bulk-sync-log.md`

---

## Usage

### When Processing Inbox:

**Stage 1:**
```bash
# Load all inboxes
python3 telegram_inbox_sync.py  # AI inbox
python3 gmail_sync.py --all      # Email
# (future: LinkedIn, etc.)

# Create inbox-to-processing log
# Agent creates processing tasks
```

**Stage 2:**
```bash
# Review processing_tasks.md
# Execute all tasks

# Create processing-execution log
# Agent updates profiles, creates work tasks
```

### Finding Logs:

**By date:** `ls -la | grep 2025-11-03`
**By type:** `ls -la | grep inbox-to-processing`
**Recent:** `ls -lat | head -5`

---

## Archive Policy

**Keep:**
- Last 90 days: All logs
- 90-365 days: Monthly summary logs only
- 365+ days: Quarterly summary logs only

**Archive to:** `logs/archive/YYYY/` when logs get old

---

## References

**Related Files:**
- `../telegram ai inbox archive.md` - Archived inbox messages (links to these logs)
- `../processing_tasks.md` - Active processing tasks
- `../../Tasks/work_tasks.md` - Work tasks created from processing

**Workflow Docs:**
- `../inbox_processing_rules.md` - Complete inbox processing guide (two-stage system, examples, rules)

---

**Last Updated:** November 3, 2025

