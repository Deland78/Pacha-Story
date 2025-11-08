# Notion Dashboard Layout: Pacha Story HQ

## Purpose
Provide a single-page cockpit for the collaboration, surfacing progress, sprint focus, emotional intent, and the newest work items while embedding AI-generated context in the sections where it matters.

## Page Structure (Top → Bottom)
1. **Header Callout**
   - Title: "Pacha Story HQ – Dashboard"
   - Subheading: Current goal or milestone (editable text block).
   - Quick Links: buttons to `Cord Board`, `Scene Drafts`, `Research Library`, `AI Collaboration Hub`, `Story Bible`.

2. **Progress Strip (three columns)**
   - **Cord Progress Board (Column 1)**
     - Embed filtered database view from `Cord Board` showing each cord with properties `Status`, `Word Goal`, `Latest Update`.
     - Display as a table sorted by `Status` priority (`Locked`, `In Review`, `Draft`, `Idea`).
     - Summary pill above table: "Cords locked / total" rollup.
   - **Sprint Countdown (Column 2)**
     - Embed filtered view from `Sprint Log` limited to the current sprint (property `Status` = `Active`).
     - Show target deliverables checklist (synced block from sprint page) and `Review Date` countdown.
     - Add progress bar widget (formula: completed tasks / total tasks).
   - **Emotional Focus tracker (Column 3)**
     - Create simple linked view from `Story Bible – Emotional Beats` (or master note) filtered to items tagged `This Week`.
     - Include property `Target Feeling` + brief note on desired emotional shift.

3. **Scene Drafts Feed**
   - Linked database view from `Scene Drafts` sorted by `Last Edited` descending; limit to 5 entries.
   - Visible columns: `Title`, `Cord`, `Status`, `Last Edited`, `Needs Approval` (status).
   - Color-code `Status` pills (`Draft`, `Needs Review`, `Approved`, `Locked`).
   - Add formula badge "AI Latest" that surfaces last AI tool used (see AI highlights below).

4. **Distributed AI Highlights**
   - Within Scene Draft cards, expose properties `Last AI Pass` (multi-select: ChatGPT / Claude) and `AI Summary` (brief note). Ensure property appears in the feed view.
   - For Research Library, below the Scene Drafts feed embed a linked view filtered to `Source Type = AI Summary` and `Needs Approval = true`.
   - In Cord Progress board, include property `AI Continuity Check` to display latest audit date.

5. **Research Snapshot & Assets**
   - Two-column section beneath AI highlights.
     - Column A: `Research Library` filtered to `Status = In Queue` & `Owner = Me/Dad`, view = list.
     - Column B: `Assets & Visuals` gallery (linked database or Notion gallery) featuring latest uploads (Staff God sketches, quipu diagrams, etc.).

6. **Changelog & Decisions Tracker**
   - Embed the `Changelog & Decisions` table showing last 10 entries, sorted by date descending.
   - Include a button "Add Decision" linked to template for quick updates.

7. **Daily Digest / Summary Section**
   - Synced block where Claude drops the daily email summary content for archival.
   - Include toggle `Past digests` listing recent entries for quick review.

8. **Automation & Reminder Footer**
   - Checklist reminding: "Review AI changes", "Update emotional focus", "Lock completed scenes".
   - Link to SOP pages (`AI Collaboration Guidelines`, `Workspace Guide`).

## Color & Status Conventions
- Use Notion default colors:
  - `Needs Review` = orange; `Needs Approval` = red; `Approved` = green; `Locked` = gray.
  - Emotional focus tag colors: Awe (blue), Resilience (purple), Grief (pink), Acceptance (teal).
- Add icons/emojis for quick scanning (e.g., 🌌 for emotional focus, 📨 for daily digest).

## Mobile Considerations
- Collapse Progress Strip into toggles for mobile view.
- Scene Drafts feed should remain as the first visible database on mobile.

## Future Enhancements (notes for later)
- Option to convert Progress Strip into synced blocks reusable per sprint.
- Potential central AI feed if distributed highlights become cluttered.
- Upgrade to formula-driven KPI (e.g., % completion per cord) once data matures.
