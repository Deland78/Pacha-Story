# Visual Quipu Builder

This folder holds generated graph assets (DOT/SVG/PNG/PDF) plus helper scripts for visualizing the digital quipu.

## Quick Start
1. Ensure dependencies:
   - Python 3 with PyYAML (already required for `update_khipu.py`).
   - (Optional) Graphviz `dot` in PATH for SVG/PNG/PDF rendering.
2. Run the builder script from repo root:
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File "Visual Quipu Builder/build_quipu_visual.ps1"
   ```
   - Generates `Visual Quipu Builder/quipu.dot` (always).
   - Attempts `Visual Quipu Builder/quipu.svg` by default; add more formats via `-Formats`.
3. Open `quipu.svg` (or PNG/PDF) to explore the cords, knots, and weavings.

## Customizing Output
- Specify formats (always includes DOT):
  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File "Visual Quipu Builder/build_quipu_visual.ps1" -Formats dot,png
  ```
- Point to a different repo root if running from another directory:
  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File "Visual Quipu Builder/build_quipu_visual.ps1" -Base "G:/Shared drives/K-D/stories/Collab/Pacha-Story"
  ```
- Silence per-file logs with `-Quiet` when scripting.

## Automation Ideas
- Add the script to your local `pre-commit` or task runner after `python update_khipu.py` to keep visuals fresh.
- The repo’s `.githooks/pre-commit` already invokes this script (or a Python fallback) so quipu diagrams update automatically whenever you commit from this repo.
- Pair with a file watcher (e.g., `watchexec`, `Invoke-WebRequest`) to re-render whenever `KHIPU_MAP.yaml`, `WEAVINGS/`, or `ENTITIES/` change.
- Drop the resulting SVG/PNG into `Visual Quipu Builder/` subfolders if you maintain versioned snapshots.

Keep the quipu visualization synced after each weaving/entity update and every collaborator will share the same relational map.
