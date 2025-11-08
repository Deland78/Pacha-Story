\
#!/usr/bin/env python3
"""
update_khipu.py
Scans WEAVINGS/ and ENTITIES/ to (re)build the indices in KHIPU_MAP.yaml.

Usage:
  python update_khipu.py [--base PATH] [--dry-run]

- Requires PyYAML: pip install pyyaml
- Only updates the `entities_index` and `weavings_index` sections.
- Preserves other keys in KHIPU_MAP.yaml.
"""

import argparse
import os
import re
from typing import List, Dict

try:
    import yaml  # type: ignore
except Exception as e:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", flush=True)
    raise

def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def save_yaml(data: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def read_entity_id(path: str) -> str:
    try:
        doc = load_yaml(path)
        eid = doc.get("entity_id") or doc.get("id") or ""
        if not eid:
            # infer from filename
            eid = os.path.splitext(os.path.basename(path))[0]
        return str(eid)
    except Exception:
        return os.path.splitext(os.path.basename(path))[0]

def read_weaving_id(path: str) -> str:
    try:
        doc = load_yaml(path)
        wid = doc.get("weaving_id") or doc.get("id") or ""
        if not wid:
            wid = os.path.splitext(os.path.basename(path))[0]
        return str(wid)
    except Exception:
        return os.path.splitext(os.path.basename(path))[0]

def collect_entities(entities_dir: str) -> List[Dict[str, str]]:
    out = []
    for name in sorted(os.listdir(entities_dir)):
        if not name.lower().endswith(".yaml"):
            continue
        if name.startswith("_") or name.upper() == "README.MD":
            continue
        path = os.path.join(entities_dir, name)
        eid = read_entity_id(path)
        out.append({"id": eid, "file": f"ENTITIES/{name}"})
    return sorted(out, key=lambda x: x["id"])

def collect_weavings(weavings_dir: str) -> List[Dict[str, str]]:
    out = []
    for name in sorted(os.listdir(weavings_dir)):
        if not name.lower().endswith(".yaml"):
            continue
        if name.startswith("_") or name.upper() == "README.MD":
            continue
        path = os.path.join(weavings_dir, name)
        wid = read_weaving_id(path)
        out.append({"id": wid, "file": f"WEAVINGS/{name}"})
    # Sort W## numerically if they look like that; else lexicographic
    def sort_key(item):
        m = re.match(r"[Ww](\d+)", item["id"])
        return (0, int(m.group(1))) if m else (1, item["id"])
    return sorted(out, key=sort_key)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=".", help="Base directory containing KHIPU_MAP.yaml, WEAVINGS/, ENTITIES/")
    ap.add_argument("--dry-run", action="store_true", help="Show changes without writing file")
    args = ap.parse_args()

    base = os.path.abspath(args.base)
    khipu_path = os.path.join(base, "KHIPU_MAP.yaml")
    entities_dir = os.path.join(base, "ENTITIES")
    weavings_dir = os.path.join(base, "WEAVINGS")

    if not os.path.isfile(khipu_path):
        raise SystemExit(f"Missing {khipu_path}")
    if not os.path.isdir(entities_dir):
        raise SystemExit(f"Missing {entities_dir}")
    if not os.path.isdir(weavings_dir):
        raise SystemExit(f"Missing {weavings_dir}")

    doc = load_yaml(khipu_path) or {}

    new_entities = collect_entities(entities_dir)
    new_weavings = collect_weavings(weavings_dir)

    # Attach or replace sections
    doc["entities_index"] = new_entities
    doc["weavings_index"] = new_weavings

    if args.dry_run:
        print("# entities_index")
        print(yaml.safe_dump({"entities_index": new_entities}, sort_keys=False, allow_unicode=True))
        print("# weavings_index")
        print(yaml.safe_dump({"weavings_index": new_weavings}, sort_keys=False, allow_unicode=True))
    else:
        save_yaml(doc, khipu_path)
        print(f"Updated {khipu_path}")
        print(f"- entities_index: {len(new_entities)} entries")
        print(f"- weavings_index: {len(new_weavings)} entries")

if __name__ == "__main__":
    main()
