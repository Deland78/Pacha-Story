#!/usr/bin/env python3
"""
export_quipu_graph.py
Generate a Graphviz view of the digital quipu defined in KHIPU_MAP.yaml.

Usage examples:
  python export_quipu_graph.py --output quipu.dot
  python export_quipu_graph.py --format svg --output quipu.svg

The script reads:
- KHIPU_MAP.yaml for cords/knots/colors
- ENTITIES/*.yaml for domains/names (optional but improves labels)
- WEAVINGS/*.yaml for titles/domains (optional but improves labels)

If --format is svg/png/pdf, Graphviz's `dot` binary must be installed and on PATH.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover - dependency guard
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise

BASE_DOMAIN_COLORS = {
    "hana": "#d4af37",   # gold
    "kay": "#8d6e63",    # earth
    "ukhu": "#121418",   # obsidian
}

CORD_COLOR_FALLBACK = "#90a4ae"
WEAVING_NODE_COLOR = "#ffffff"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def slug(text: str) -> str:
    keep = [ch if ch.isalnum() else "_" for ch in text.strip()]
    slugified = "".join(keep).strip("_")
    return slugified or "node"


def escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("\"", "\\\"")


def resolve_color(label: str | None, fallback: str) -> str:
    if not label:
        return fallback
    lower = label.lower()
    if lower in ("gold", "obsidian", "earth", "blue", "red", "gray", "granite"):
        mapping = {
            "gold": "#d4af37",
            "obsidian": "#121418",
            "earth": "#8d6e63",
            "blue": "#1e88e5",
            "red": "#e53935",
            "gray": "#90a4ae",
            "granite": "#9e9e9e",
        }
        return mapping[lower]
    digest = hashlib.md5(label.encode("utf-8")).hexdigest()
    r = int(digest[:2], 16)
    g = int(digest[2:4], 16)
    b = int(digest[4:6], 16)
    # Lighten color for readability
    mix = lambda comp: int((comp + 255) / 2)
    return f"#{mix(r):02x}{mix(g):02x}{mix(b):02x}"


def gather_entities(base: Path) -> Dict[str, dict]:
    entities_dir = base / "ENTITIES"
    results: Dict[str, dict] = {}
    if not entities_dir.is_dir():
        return results
    for path in entities_dir.iterdir():
        if path.name.startswith("_") or path.suffix.lower() != ".yaml" or path.name.lower() == "readme.md":
            continue
        data = load_yaml(path)
        display = data.get("name") or data.get("entity_id") or path.stem
        domain = data.get("domain")
        node_id = f"entity_{slug(display)}"
        results[display] = {
            "node_id": node_id,
            "domain": (domain or "").strip().lower() or None,
            "label": display,
        }
    return results


def gather_weavings(base: Path) -> Dict[str, dict]:
    weavings_dir = base / "WEAVINGS"
    results: Dict[str, dict] = {}
    if not weavings_dir.is_dir():
        return results
    for path in weavings_dir.iterdir():
        if path.name.startswith("_") or path.suffix.lower() != ".yaml" or path.name.lower() == "readme.md":
            continue
        data = load_yaml(path)
        weaving_id = str(data.get("weaving_id") or path.stem)
        domain = (data.get("domain") or "").strip().lower() or None
        title = (data.get("title") or "").strip()
        node_id = f"weaving_{slug(weaving_id)}"
        results[weaving_id] = {
            "node_id": node_id,
            "domain": domain,
            "title": title,
            "weaving_id": weaving_id,
        }
    return results


def ensure_entity_node(name: str, entities: Dict[str, dict]) -> dict:
    existing = entities.get(name)
    if existing:
        return existing
    node = {
        "node_id": f"entity_{slug(name)}",
        "domain": None,
        "label": name,
    }
    entities[name] = node
    return node


def ensure_weaving_node(weaving_id: str, weavings: Dict[str, dict]) -> dict:
    existing = weavings.get(weaving_id)
    if existing:
        return existing
    node = {
        "node_id": f"weaving_{slug(weaving_id)}",
        "domain": None,
        "title": "",
        "weaving_id": weaving_id,
    }
    weavings[weaving_id] = node
    return node


def build_dot(doc: dict, entities: Dict[str, dict], weavings: Dict[str, dict]) -> str:
    color_legend = doc.get("color_legend") or {}
    domain_colors = BASE_DOMAIN_COLORS.copy()
    for domain, color_label in color_legend.items():
        domain = str(domain).strip().lower()
        domain_colors[domain] = resolve_color(str(color_label), domain_colors.get(domain, WEAVING_NODE_COLOR))

    lines: List[str] = []
    lines.append("digraph DigitalQuipu {")
    lines.append('  graph [rankdir=LR, fontname="Helvetica", splines=true, overlap=false];')
    lines.append('  node  [fontname="Helvetica", shape=ellipse];')
    lines.append('  edge  [fontname="Helvetica"];')

    # Entity nodes
    for name in sorted(entities.keys()):
        info = entities[name]
        domain = info.get("domain")
        fill = domain_colors.get(domain, "#f5f5f5") if domain else "#f5f5f5"
        label = info.get("label") or name
        if domain:
            label = f"{label}\\n({domain})"
        lines.append(f'  "{info["node_id"]}" [label="{escape(label)}", style="filled", fillcolor="{fill}", shape="ellipse", penwidth=1.3];')

    # Weaving nodes
    for weaving_id in sorted(weavings.keys()):
        info = weavings[weaving_id]
        label_parts = [info["weaving_id"]]
        title = info.get("title")
        if title:
            label_parts.append(title)
        label = "\\n".join(label_parts)
        domain = info.get("domain")
        fill = domain_colors.get(domain, WEAVING_NODE_COLOR) if domain else WEAVING_NODE_COLOR
        lines.append(f'  "{info["node_id"]}" [label="{escape(label)}", style="filled", fillcolor="{fill}", shape="rect", penwidth=1.1];')

    # Cord nodes and edges
    cords = doc.get("cords") or []
    for cord in cords:
        name = cord.get("name") or "Unnamed Cord"
        node_id = f"cord_{slug(name)}"
        cord_type = cord.get("type") or "cord"
        color_label = cord.get("color") or cord_type
        fill = resolve_color(str(color_label), CORD_COLOR_FALLBACK)
        label = f"{name}\\n[{cord_type}]"
        lines.append(f'  "{node_id}" [label="{escape(label)}", shape="diamond", style="filled", fillcolor="{fill}", penwidth=1.5];')

        # Connect entities to cord
        for entity_name in cord.get("connects", []):
            info = ensure_entity_node(str(entity_name), entities)
            lines.append(
                f'  "{info["node_id"]}" -> "{node_id}" '
                f'[dir=both, arrowhead=none, arrowtail=none, color="#90a4ae", penwidth=1.1];'
            )

        # Connect knots to weavings
        for knot in cord.get("knots", []):
            weaving_id = str(knot.get("weaving_id"))
            weaving = ensure_weaving_node(weaving_id, weavings)
            knot_type = knot.get("knot_type") or "knot"
            transformation = knot.get("transformation") or "transformation"
            echoes = knot.get("echoes") or []
            label_lines = [f"{knot_type}: {transformation}"]
            if echoes:
                label_lines.append(f"Echoes: {', '.join(echoes)}")
            edge_label = "\\n".join(label_lines)
            edge_color = resolve_color(str(color_label), CORD_COLOR_FALLBACK)
            lines.append(
                f'  "{node_id}" -> "{weaving["node_id"]}" '
                f'[label="{escape(edge_label)}", color="{edge_color}", penwidth=1.3];'
            )

    lines.append("}")
    return "\n".join(lines) + "\n"


def write_output(dot_text: str, output: Path, output_format: str) -> None:
    output_format = output_format.lower()
    if output_format == "dot":
        output.write_text(dot_text, encoding="utf-8")
        print(f"Wrote Graphviz DOT to {output}")
        return

    dot_binary = "dot"
    if not shutil.which(dot_binary):  # type: ignore
        raise SystemExit("Graphviz 'dot' executable not found. Install Graphviz or use --format dot.")

    cmd = [dot_binary, f"-T{output_format}"]
    result = subprocess.run(cmd, input=dot_text.encode("utf-8"), capture_output=True)
    if result.returncode != 0:
        raise SystemExit(result.stderr.decode("utf-8") or "Graphviz rendering failed")
    output.write_bytes(result.stdout)
    print(f"Rendered {output_format.upper()} to {output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export the digital quipu to Graphviz")
    parser.add_argument("--base", default=".", help="Project root containing KHIPU_MAP.yaml")
    parser.add_argument("--output", default="quipu.dot", help="Path to write the Graphviz output")
    parser.add_argument("--format", choices=["dot", "svg", "png", "pdf"], default="dot", help="Output format")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = Path(args.base).resolve()
    khipu_path = base / "KHIPU_MAP.yaml"
    if not khipu_path.is_file():
        raise SystemExit(f"Missing {khipu_path}")

    entities = gather_entities(base)
    weavings = gather_weavings(base)
    doc = load_yaml(khipu_path)

    dot_text = build_dot(doc, entities, weavings)

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path

    write_output(dot_text, output_path, args.format)


if __name__ == "__main__":
    import shutil  # local import to keep global scope tidy

    main()
