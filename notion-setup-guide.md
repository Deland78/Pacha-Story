# Notion Setup Guide for Claude (Pacha Story HQ)

> **Objective:** Build a lean-but-structured Notion teamspace that mirrors the current folder system, enables AI maintenance (ChatGPT + Claude connectors), and supports manual approval, daily digests, and collaborative workflows.

## 0. Prerequisites
1. Verify Claude has the following permissions:
   - Can create teamspaces, databases, and integrations.
   - Email access (or SMTP credentials) to send daily summaries to `korab@example.com` and `dad@example.com` (replace with actual addresses).
2. Ensure the following integrations are available:
   - **ChatGPT Connector** with edit permissions.
   - **Claude Connector** with edit permissions.
   - **Google Drive Integration** with read/write access to `Pacha Story HQ` folder.

## 1. Create the Teamspace
1. Create a teamspace named `Pacha Story HQ`.
2. Add two members with full access: `Korab` and `Dad` (use actual Notion accounts).
3. Within the teamspace, create a root page `Pacha Story HQ – Dashboard` (leave blank for now).

## 2. Create Core Databases
For each database, place it in the teamspace root (same level as Dashboard). Use the exact property names and types listed.

### 2.1 Cord Board
- **Database Type:** Table
- **Properties:**
  | Name | Type | Notes |
  |------|------|-------|
  | Name | Title | Cord identifier (e.g., "Cord 1492") |
  | Timeline | Select | Values: `992`, `1992`, `1452`, `1531`, `1492` |
  | Status | Select | Values: `Idea`, `Draft`, `In Review`, `Locked` |
  | Word Goal | Number | target word count |
  | Latest Update | Date | last significant change |
  | Owner | Person | primary collaborator |
  | Next Action | Text | brief instruction |
  | Key Motifs | Multi-select | e.g., `Meteor`, `Staff God`, `Smallpox` |
  | Needs Approval | Status | Values: `Needs Approval`, `Approved` |
  | AI Continuity Check | Date | last AI audit |
- **Views:**
  - `Progress Table` (default): sort by Status (custom order Locked → In Review → Draft → Idea).
  - `Timeline View`: group by Timeline, show Latest Update.

### 2.2 Scene Drafts
- **Database Type:** Table
- **Properties:**
  | Name | Type | Notes |
  |------|------|-------|
  | Title | Title | scene name |
  | Cord | Relation | link to Cord Board |
  | Timeline | Rollup or Select | auto from Cord relation (if rollup) |
  | Status | Select | `Idea`, `Draft`, `Needs Review`, `Approved`, `Locked` |
  | Last Edited | Last edited time | built-in |
  | Last Author | Person | who touched it last |
  | Word Count | Number | optional manual entry |
  | Emotional Beat | Multi-select | `Restless`, `Acceptance`, etc. |
  | Needs Approval | Status | `Needs Approval`, `Approved` |
  | Last AI Pass | Multi-select | `ChatGPT`, `Claude` |
  | AI Summary | Text | short note of AI output |
  | Research Links | Relation | link to Research Library |
  | Assets | Relation | link to Assets gallery |
- **Views:**
  - `Latest Updates` (default): sort by Last Edited descending, filter Status ≠ Locked.
  - `Needs Review` board: filter Status = Needs Review.
  - `Cord Grouped List`: group by Cord.
- **Template Button:** `New Scene Draft` with placeholder structure (context recap, emotional target, motif checklist).

### 2.3 Characters & Artifacts
- **Database Type:** Gallery
- **Properties:**
  | Name | Type | Notes |
  |------|------|-------|
  | Name | Title | character or artifact |
  | Type | Select | `Character`, `Artifact` |
  | Era | Select | `Pre-Inca`, `Inca`, `Modern` |
  | Role | Text |
  | Emotional Arc | Text |
  | Motifs | Multi-select |
  | Related Scenes | Relation | Scene Drafts |
  | Needs Approval | Status | `Needs Approval`, `Approved` |

### 2.4 Research Library
- **Database Type:** Table
- **Properties:**
  | Name | Type | Notes |
  |------|------|-------|
  | Title | Title | source name |
  | Source Type | Select | `Academic`, `Primary`, `Interview`, `AI Summary` |
  | Citation | Text |
  | Summary | Text |
  | Relevance | Multi-select | `Cosmology`, `Landscape`, etc. |
  | Cross-Checks Needed | Checkbox |
  | Needs Approval | Status | `Needs Approval`, `Approved` |
  | Cord Links | Relation | Cord Board |
  | File | Files & media | for PDFs (sync with Drive) |
  | Owner | Person |
- **Views:** `Reading Queue` filter Needs Approval = Approved AND Cross-Checks Needed = true; `AI Summaries Pending` filter Source Type = AI Summary AND Needs Approval = Needs Approval.

### 2.5 Sprint Log
- **Database Type:** Table
- **Properties:**
  | Name | Type |
  |------|------|
  | Sprint Week | Title |
  | Status | Select (`Planned`, `Active`, `Review`, `Complete`) |
  | Focus Cord | Relation (Cord Board) |
  | Lead | Person |
  | Goals | Text |
  | Deliverables | Checklist |
  | Review Date | Date |
  | AI Support Used | Multi-select |
  | Needs Approval | Status |

### 2.6 Changelog & Decisions
- **Database Type:** Table
- **Properties:**
  | Name | Type |
  |------|------|
  | Date | Date |
  | Decision | Title |
  | File/Area | Select (`Story Bible`, `Scene Drafts`, etc.) |
  | Description | Text |
  | Owner | Person |
  | Needs Approval | Status |

### 2.7 AI Collaboration Hub
- **Database Type:** Table
- **Properties:**
  | Name | Type |
  |------|------|
  | Prompt Summary | Title |
  | Purpose | Select (`Brainstorm`, `Draft`, `Research`, `Audit`) |
  | Input Context | Text |
  | Output Highlights | Text |
  | Linked Scene | Relation (Scene Drafts) |
  | Linked Research | Relation (Research Library) |
  | Connector Used | Select (`ChatGPT`, `Claude`) |
  | Needs Approval | Status |
  | Reviewed By | Person |

### 2.8 Assets & Visuals (optional)
- Gallery storing imagery, diagrams, quipu visuals; include `Needs Approval` status and relations to Scene Drafts.

## 3. Configure Dashboard
Use `notion-dashboard-layout.md` as reference.
1. Populate `Pacha Story HQ – Dashboard` with sections outlined in the layout doc, embedding linked database views.
2. Ensure each view surfaces the `Needs Approval` property.
3. Add quick links callout at top.

## 4. Set Up Integrations & Automations
1. **ChatGPT + Claude Connectors**
   - Enable both connectors with permission to read/write the databases above.
   - Set default behavior: AI-created items start with `Needs Approval` status.
2. **Google Drive Sync**
   - Connect `Research Library` File property to `Pacha Story HQ` folder.
   - Set up two-way sync (uploads in Notion push to Drive).
3. **Manual Approval Workflow**
   - For each database, create saved view `Needs Approval` (filter Needs Approval = `Needs Approval`).
   - Claude should queue AI changes with Status updates; Korab/Dad switch to `Approved` once reviewed.
4. **Daily Digest Email**
   - Build automation (Notion API or external service) to run daily at 20:00 local time:
     - Gather: entries edited in last 24h (Scene Drafts, Research Library, Changelog & Decisions) and outstanding `Needs Approval` items.
     - Set format (see section 5) and send email to both users.
   - Archive the same content in `Daily Digest` synced block on dashboard.

## 5. Daily Email Format
```
Subject: Pacha HQ Digest – {{date}}

Progress Snapshot:
- Cord status summary (Locked/In Review/Draft counts)
- Active sprint checklist (completed / total)

Pending Approvals:
- Scene Drafts: {{list titles}}
- Research: {{list titles}}
- Other: {{list titles}}

Key Changes:
- {{changelog entries}}

Emotional Focus:
- This week’s target: {{value}}
```

## 6. Initial Data Migration
1. Import existing markdown files into their respective databases:
   - `story-summary.md` → Story Bible main page (link back to new database views).
   - `chasqui-profile.md` → Characters & Artifacts entry (`Type = Character`).
   - `celestial-events.md` → Story Bible reference page.
2. Attach supporting assets (e.g., `eclipse_freq_8bit_print.jpg`) into `Assets & Visuals` gallery.
3. Log current decisions in Changelog for historical accuracy.

## 7. Post-Setup Checklist
- [ ] Dashboard sections render correctly on desktop and mobile.
- [ ] Connectors tested by creating sample `Scene Draft` and verifying status default.
- [ ] Daily digest automation test run sent to both users.
- [ ] Approval views shared with both collaborators.
- [ ] Google Drive sync verified with sample file.

## 8. Notes for Future Expansion
- Consider adding formulas for progress percentages once enough data exists.
- Revisit database schemas if you decide to standardize templates (transition from lean to structured).
- Maintain documentation updates in `Changelog & Decisions` whenever Claude adjusts workflows.
