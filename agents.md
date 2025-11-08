# AGENTS.md  
*(Pacha-Structured Story Framework)*

## 1. Storyworld Overview

**Working Title:** *[Pacha Story]*  
**Story Essence:** A weaving of beings, times, and spaces across the three Pachas — **Hana (upper)**, **Kay (living)**, and **Ukhu (inner/ancestral)**.  
**Genre/Mode:** Mythic-historical fiction grounded in Andean cosmology and ecological memory.  
**Temporal Logic:** Non-linear, recursive, relational. Time is not a sequence but a field of echoes.  
**Intent:** To embody *Pacha* — the unity of space, time, and being — through narrative pattern and reciprocity.

## 2. Relational Voices

Instead of a single point of view, the story is told through **multiple resonant voices** that move between worlds.

| Voice | Domain | Tone / Register | Mode of Speech |
|-------|---------|----------------|----------------|
| Human (protagonist or wanderer) | Kay Pacha | intimate, sensory | dialogue, thought |
| Ancestor / Memory | Ukhu Pacha | slow, echoing | dream, ritual fragment |
| Elemental Being (mountain, river, wind) | Hana or Kay | cyclic, impersonal | sound, silence, symbol |
| Collective Voice (community, ritual chorus) | All | rhythmic, shared | chant, pattern |

> Voices are not “characters” but *threads of perception* that braid and unbraid through the story.

## 3. Weavings (Story Units)

Replace scenes or chapters with **Weavings** — intersections of beings, moments, and meanings.

Each Weaving entry (in your writing files) should contain:

```yaml
weaving_id: W07
domain: kay
threads_continued: [hana:W02, ukhu:W04]
event_form: encounter, ritual, memory
transformation: “realization of shared ancestry”
symbolic_motif: hummingbird / obsidian mirror
```

**Guidelines for Weavings:**
- Begin with **the meeting of presences** (not exposition).  
- Let each Weaving **transform** a relation — not just reveal information.  
- Allow threads to **recur** in altered forms (echo, inversion, reflection).  
- End not on “resolution,” but on *vibration* — something felt across worlds.

## 4. Entities and Relations

All presences — human, animal, place, or spirit — are **Entities** within the web of *Pacha*.  
Define them by *domain, essence, and reciprocity*, not by traits or goals.

Example entries:

```yaml
- Entity: Apu Qocha (Mountain Spirit)
  Domain: Hana Pacha
  Essence: Withholds rain until remembered
  Relations: Protector of valley, appears in thunder
  Material Presence: granite, shadow, dream-image

- Entity: Naira (Human)
  Domain: Kay Pacha
  Essence: Seeks her ancestor’s reflection
  Relations: Child of the wind, kin to the obsidian stone
  Appears Through: ritual gestures, silence, breath
```

## 5. Relational Map (Digital Quipu / Khipu)

The story’s structure is not a line but a **field of knots**.  
Use a **digital quipu map** to trace:
- **Cords:** threads of relation (e.g., human ↔ ancestor ↔ landscape)
- **Knots:** transformations (moments of exchange or revelation)
- **Colors / Textures:** emotional or elemental tones

Suggested data format:

```yaml
cords:
  - name: "Blood & River"
    connects: [Naira, River Spirit]
    color: blue-red
    knots:
      - weaving_id: W03
        transformation: “first recognition of shared song”
      - weaving_id: W10
        transformation: “return of water after offering”
```

Visualize through your Codex or Obsidian graph — each knot links back to a Weaving.

## 6. Ethical & Aesthetic Principles

| Do | Don’t |
|----|--------|
| Honor silence, pause, and return | Force linear causality |
| Let the land speak through detail | Treat nature as backdrop |
| Allow multiple times to coexist | Collapse events into chronology |
| Write through reciprocity: every act changes both sides | Center human will or mastery |
| Use sensory language (sound, color, texture) as emotion | Over-explain or rationalize mystery |
| Weave relationships, not outcomes | Build toward a single climax or resolution |

> Every sentence should *breathe with exchange*.  
> Every description should *acknowledge its source*.

## 7. Maintenance Practice (Living Document)

After each writing session:
1. Update your **Khipu Log** — note which threads tightened, loosened, or echoed.  
2. Add new *Weavings* and *Relations* to this document or your quipu map.  
3. Reflect briefly on one question:  
   > “What changed in the balance between worlds today?”

Optional digital extensions:
- Auto-generate quipu visualization from YAML tags.  
- Annotate recurring symbols or sensory motifs.  
- Track “energetic flow” between Pachas (which domain is most active).

## 8. Technical Metadata (for Codex Integration)

```yaml
schema_version: 1.0
story_mode: pacha
domains: [hana, kay, ukhu]
core_files:
  - AGENTS.md
  - WEAVINGS/
  - ENTITIES/
  - KHIPU_MAP.yaml
  - THEMES.md
codex_visualization: digital_quipu
```
