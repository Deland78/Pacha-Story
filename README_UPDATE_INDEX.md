# Pacha Scaffold – Auto Index Updater

This script rebuilds `entities_index` and `weavings_index` in `KHIPU_MAP.yaml` by scanning the `ENTITIES/` and `WEAVINGS/` folders.

## Install
```bash
cd pacha_scaffold
python -m venv .venv && source .venv/bin/activate  # or use your preferred environment manager
pip install -r requirements.txt
```

## Run
```bash
python update_khipu.py           # run from inside pacha_scaffold
# or
python update_khipu.py --base /path/to/pacha_scaffold
```

## Dry Run
```bash
python update_khipu.py --dry-run
```

## Notes
- Only the index sections are modified; all other data in `KHIPU_MAP.yaml` is preserved.
- File names that start with `_` or `README.md` are ignored.
- Weaving IDs like `W01` are sorted numerically; otherwise lexicographically.
