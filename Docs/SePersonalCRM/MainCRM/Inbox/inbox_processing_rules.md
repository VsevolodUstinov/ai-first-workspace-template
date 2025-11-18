# Inbox Processing Rules

**Status:** 🔬 ALPHA - Testing on Telegram AI inbox only, manual checkpoints required

---

## System: Three-Stage Processing

**Why?** Multiple inboxes (email, Telegram, LinkedIn) can have related messages about same person/fund. Need to collect ALL context before processing to catch dependencies.

**Example:** Email says "Meeting postponed", Telegram says "Let's meet Friday", LinkedIn shows connection. Without collecting all first → miss that they're about same person.

---

## Workflow

```
"Process inbox" → STAGE 1 → Checkpoint 1 → Archive
                     ↓
               processing_tasks.md created
                     ↓
"Process tasks" → STAGE 2 → Checkpoint 2 → Cleanup
                     ↓
                work_tasks.md populated
                     ↓
"What to work on?" → STAGE 3 → Execute with user
```

---

## Stage 1: Inbox → Processing Tasks

**User:** "Process inbox"

**Agent:**
1. **LOADS required context files:**
   - `Context/Contacts_Actual.md` (FULL FILE - required to recognize existing contacts)
   - `Tasks/work_tasks.md` (FULL FILE - required to understand what's actively in progress)
2. Syncs `telegram ai inbox.md` (alpha: manual only, NOT auto)
3. Reads all new messages
4. **SEARCHES** Contacts_Actual.md for any people mentioned in messages (check existing contacts first)
5. **CREATES** `processing_tasks.md` entries (decomposed steps for each message)
6. **SHOWS:** "Created X processing tasks - please review processing_tasks.md"
7. **🛑 CHECKPOINT 1:** User reviews actual file, confirms or requests changes
8. **ONLY after "looks good, proceed":**
   - Archives messages to `telegram ai inbox archive.md` (with log links)
   - Creates Stage 1 log
   - Removes messages from inbox
9. **STOP** - Don't execute Stage 2 yet

**Key:** Processing tasks CREATED first, user reviews actual file, THEN archives. If user says "fix X", messages stay in inbox, agent adjusts processing_tasks.md and shows again.

**CRITICAL:** Always load full Contacts_Actual.md AND work_tasks.md BEFORE processing messages to have full context of existing contacts and active work.

---

## Stage 2: Processing Tasks → Work Tasks

**User:** "Process tasks"

**Agent:**
1. Executes all `processing_tasks.md` steps:
   - Sync communications (Telegram, email, LinkedIn)
   - Download meeting transcripts to contact folders, review them, and update contacts accordingly
   - Research new contacts (web + LinkedIn)
   - Create/update contact profiles
   - Update `Contacts_Actual.md` for active fundraising/sales/networking contacts
   - Update company cards when multiple contacts from same company/fund
   - Update `Context/Talking_Points.md` if new company achievements/milestones discovered
   - **Tasks are atomic**: one checkbox = one complete action, details in parentheses (not sub-items)
2. **CHECK for Work Tasks updates:**
   - Based on processed messages, evaluate if any work_tasks.md items should be updated
   - **PROPOSE** updates to user with default action: "Based on [message/event], I propose to [add/update/remove] task: [specific change]. OK?"
   - ONLY if user confirms ("OK", "yes", "looks good") → update work_tasks.md
   - Examples: Remove completed tasks, add urgent new tasks, update deadlines
3. Creates work tasks for decisions (ONLY if explicitly mentioned in communications or by user)
4. Marks items complete in `processing_tasks.md`
5. **SHOWS:** "Synced/updated/created: [summary]"
6. **🛑 CHECKPOINT 2:** Waits for "processing correct, finalize"
7. **After approval:** 
   - Creates Stage 2 log with all completed tasks
   - **DELETES all content from `processing_tasks.md`** (except header)
   - File should be empty - like new, ready for next batch
   - **Commits and pushes to git** (user approval at Checkpoint 2 = consent to commit)
   
**Key:** Checkpoint BEFORE cleanup. After approval, file becomes completely clean and changes are committed.

**Talking Points Updates**: Update `Context/Talking_Points.md` when discovering:
- New company metrics/milestones (ARR, new clients, pilots)
- Major hires or team updates
- Product launches or feature releases
- Speaking engagements, media coverage, events
- Fundraising developments (commitments, new investors)
- Keep chronological, add to relevant sections

**CRITICAL: DO NOT Invent Tasks**
- ❌ NO "prepare for meeting" tasks (unless user explicitly requests)
- ❌ NO "research before call" tasks (unless user explicitly requests)
- ❌ NO "follow up after meeting" tasks (unless explicitly discussed with contact)
- ✅ ONLY add tasks that are explicitly mentioned in communications or requested by user

---

## Stage 3: Work on Tasks

**User:** "What should I work on?" (or session start)

**Agent:**
1. Reviews `work_tasks.md`
2. **SHOWS:**
   - Top priorities (P0/P1 with deadlines)
   - I can do autonomously: [list]
   - Need your decision: [list]
3. **PROPOSES:** "Shall we [specific task]?"
4. User picks → Agent helps execute → Marks complete

**Autonomous examples:**
- Send deck to X (draft message, user approves)
- Research Y background (show findings)
- Sync Telegram for Z (show summary)

**Decision examples:**
- Review request (user decides action)
- Schedule meeting (user picks timing)
- Strategic choices

---

## Files

**`processing_tasks.md`** - Temporary (Stage 2 workspace, cleaned after Checkpoint 2)
**`work_tasks.md`** - Persistent (user's to-do, organized by P0/P1/P2/P3)
**`Contacts_Actual.md`** - Backlog (historical agreements, not immediate work)

---

## Checkpoints (Alpha)

**CHECKPOINT 1:** After creating processing_tasks.md, BEFORE archiving inbox messages
**CHECKPOINT 2:** After executing processing, BEFORE cleanup/logs

**Purpose:** User confirms before committing. If stop mid-process, original data remains for debugging/iteration.

**Approval phrases:** "looks good", "proceed", "correct, finalize"
**Rejection phrases:** "wait", "fix X", "change Y" → Agent iterates

---

## Alpha Constraints

- Telegram AI inbox ONLY (not email/LinkedIn yet)
- Manual trigger (not auto-sync)
- Checkpoints required (no skipping)
- Testing on individual messages

**When ready:** Add email, LinkedIn; reduce checkpoint frequency; automate syncs.

---

## Quick Reference

**"Process inbox"** → Stage 1 → Checkpoint 1 → Archive
**"Process tasks"** → Stage 2 → Checkpoint 2 → Cleanup  
**"What to work on?"** → Stage 3 → Suggest priorities/autonomous
**"Let's do X"** → Stage 3 execute

---

**Last Updated:** November 6, 2025 (Added meeting transcript processing rules)
