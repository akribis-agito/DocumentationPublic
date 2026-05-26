# Keyword Documentation System & Standard — Design

- **Date:** 2026-05-27
- **Status:** Draft for review
- **Author:** CJ (with Claude)

## 1. Context & goal

The firmware (`Dev/Firmware-Main`) defines every user-facing keyword in a single
table, `KeywordsTableArray`, inside `CommonC/AG300_CTL01Params.c`. Each entry carries
rich metadata: CAN code, mnemonic, type, units, access, motion/motor rules, array vs
scalar, flash persistence, axis relation, implementation status, array size, min/max,
default, and scaling factor.

The documentation repo (`Dev/DocumentationPublic`) holds an Obsidian vault at
`03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/content/` with ~748 preliminary keyword
pages. Today each page is minimal: a title, a one-paragraph `**Definition:**`, and a
`**See also:**` list.

The goal is to turn this into elite, professional reference documentation — accurate
structured facts plus rich prose, diagrams, and examples — across two release lines:

- **v4.x.x** = the firmware **LTS** branch (currently `LTS_v3.X.X`).
- **v5.x.x** = the firmware **develop** branch.

…and across two product families, both already encoded in the firmware as separate
keyword tables in the same file:

- **Standalone** = the `#if PRODUCT_TYPE == CONTROLLER` table.
- **Central-i** = the `#if PRODUCT_TYPE == CI_MASTER` table.

The full enrichment is a multi-session effort. **This spec builds the foundation** —
the data contract, the page standard, and the generator that mines the firmware — and
proves it on one pilot category. It does not attempt to enrich all keywords at once.

## 2. Scope

**In scope**
- The frontmatter schema (the data contract) for keyword pages.
- The enriched-page template and a per-keyword enrichment checklist (the "standard").
- A Python generator that parses `Params.c` and maintains the frontmatter facts.
- A pilot: fully enrich one category (`11-control-tuning`) end-to-end.

**Out of scope (deferred to later cycles)**
- Enriching the remaining 19 categories (each becomes its own small effort).
- Building the public website theme/renderer.
- Building the C# in-product help viewer.
  (Both are downstream display projects that *consume* this contract; this spec only
  guarantees the format serves them.)
- A manual-wide **documentation structure / information-architecture review** (category
  overviews, `03-special-features`, `04-error-codes`, `01-keyword-usage-and-syntax`,
  `05-legacy-keywords`, navigation). This is a separate concern from the per-keyword page
  system and warrants its own brainstorm + spec in a future cycle; noted here so it is not
  lost.

## 3. Locked decisions

| Decision | Choice |
|---|---|
| Page layout | "Article + sidebar" — narrative left, info panel right |
| Attribute divergence display | Latest-version value shown; `●` marks fields that differ; old value on demand |
| Product × version display | 2×2 availability matrix (Standalone/Central-i × v4/v5) driving the panel |
| Data format | YAML frontmatter (facts) + markdown body (prose), one file per keyword |
| Source of facts | Generated from `Params.c` (not hand-authored) |
| Version association | Asserted **manually per run** via a `--version` flag |
| File structure | **Never changed**; generator only updates existing files |
| Undocumented keywords | Listed in a **manifest**, not created as stubs |
| Generator language | Python |
| Pilot category | `11-control-tuning` (56 keywords) |

## 4. Data contract (frontmatter schema)

Facts live in YAML frontmatter, keyed by the `(product, version)` matrix. One **primary
cell** (the latest version of the primary product) is shown in full; every cell that
differs is recorded under `overrides`. Everything the renderer shows — matrix, dots,
hover values — is a pure function of this block.

```yaml
---
keyword: GainPosP
can_code: 211
summary: Proportional gain of the position control loop.
category: control-tuning

# which matrix cells this keyword exists in
availability:
  standalone: [v4, v5]
  central-i:  [v5]

# primary cell = latest version of the primary product (standalone · v5)
attributes:
  access: rw            # RO -> ro, RW -> rw
  scope: axis           # AXIS -> axis, NON_AXIS -> non-axis
  flash: true           # FLASH -> true, NOFLASH -> false
  type: scalar          # NOARRAY -> scalar, ISARRAY -> array
  array_size: 1         # MaxArrayIndex + 1
  data_type: int32      # numeric type; see vocabulary below. Can diverge by version.
  ok_in_motion: true    # OKINMOTN -> true, NOMOTN -> false
  ok_motor_on: true     # OKMTRON -> true
  units: user           # USER_UNITS -> user, NO_USER_UNITS -> none, FUNC_UNITS -> func
  range: [0, 65535]     # MinValue, MaxValue (resolved)
  default: 80           # DefaultValue (resolved)
  scaling: 1            # ScalingFact
  implemented: final    # FINAL -> final, PARTIAL -> partial

# ONLY cells that differ from the primary — drives the ● markers and the matrix
overrides:
  standalone.v4: { data_type: int32, range: [0, 32767], default: 120, access: ro }
  central-i.v5:  { default: 90 }

# optional, set by the generator when a keyword is gone from a scanned version
removed_in: []          # e.g. [v5] if present in v4 scan but absent in v5 scan
---
```

### `data_type` vocabulary

The numeric type of the keyword, which evolves across releases:

| Token | Display label | Availability |
|---|---|---|
| `int32` | 32-bit integer (long) | v4 and below (historical default) |
| `float32` | 32-bit float | v4 (planned) |
| `int64` | 64-bit integer (long long) | v5 |
| `float64` | 64-bit double | v5 |

`data_type` can diverge per cell (e.g. `int32` in v4 → `float64` in v5) and is handled by
the same `overrides` mechanism as any other attribute — a type change needs no special case.
A renderer shows it as a Quick Facts row with a `●` when it differs.

### Source-column mapping

The generator derives `attributes` directly from the `STRUCT_KEYWORDS_TABLE` columns
(order defined in `CommonIncludes/AG300_CTL01Interpreter.h`):

| Frontmatter field | Source column / token |
|---|---|
| `keyword` | Mnemonic (col 2) |
| `can_code` | CANCode (col 1) |
| `attributes.access` | bReadOnly token (`RO`/`RW`) |
| `attributes.ok_in_motion` | bOKInMotion (`OKINMOTN`/`NOMOTN`/`MPNOMOTN`) |
| `attributes.ok_motor_on` | bOKMotorOn (`OKMTRON`/`MPNOMTR`) |
| `attributes.type` / `array_size` | bIsArray + MaxArrayIndex |
| `attributes.data_type` | numeric type encoding (see risks — v4 defaults to `int32`; v5 encoding TBC) |
| `attributes.flash` | bSaveToFlash (`FLASH`/`NOFLASH`) |
| `attributes.scope` | bAxisRelated (`AXIS`/`NON_AXIS`) |
| `attributes.implemented` | bImplemented (`FINAL`/`PARTIAL`) |
| `attributes.units` | bInUserUnits (`USER_UNITS`/`NO_USER_UNITS`/`FUNC_UNITS`) |
| `attributes.range` / `default` / `scaling` | MinValue, MaxValue, DefaultValue, ScalingFact |

Attribute tokens are plain `#define`s in `AG300_CTL01Interpreter.h` and are
self-documenting. Numeric range/default `#define`s (`*_MIN/_MAX/_DFLT`) live in
`AG300_CTL01Params.h`, `AG300_CTL01ParamsCommon.h`, and `CentraliLib.h`; the generator
resolves them (see §6). Internal columns (pointers, function handlers) are ignored.

## 5. Enriched-page template & standard

Each keyword page = **generated frontmatter** + **authored body**, rendered in the
"Article + sidebar" layout. Body section standard:

1. **Overview** *(required)* — what the keyword does, in user terms.
2. **Availability matrix + Quick Facts** — *rendered from frontmatter, never hand-typed.*
3. **How it works** — mechanism; drawio diagram where it aids understanding.
4. **Examples** — real command syntax (set/query).
5. **Changes between versions** *(when applicable)* — authored notes on **behavioral**
   changes between v4 and v5 that an attribute diff cannot capture. This lives in the
   Additional/Notes area and is human-written; the generator never touches it.
6. **See also** — related keywords (existing relative-link convention preserved).

### Per-keyword "done" checklist (uniform quality across sessions)

- [ ] Frontmatter present and current (generator-maintained).
- [ ] Overview rewritten in clear user-facing language.
- [ ] At least one concrete usage example.
- [ ] Diagram added where the mechanism warrants one.
- [ ] "Changes between versions" filled in if behavior differs across v4/v5.
- [ ] See-also links verified.

## 6. Generator pipeline (Python)

A standalone build tool, independent of any display. Run **once per branch checkout**,
with the version asserted manually.

### Operations

```
# On the LTS branch checkout (asserted as v4):
generate append    --version v4 --params <path>/AG300_CTL01Params.c
# On the develop branch checkout (asserted as v5):
generate append    --version v5 --params <path>/AG300_CTL01Params.c

# Refresh/correct an already-scanned version's facts:
generate overwrite --version v5 --params <path>/AG300_CTL01Params.c
```

- **`append`** — reads both product tables (`CONTROLLER` → standalone, `CI_MASTER` →
  central-i) from the given `Params.c`, and adds *this version's* facts to the frontmatter
  of existing docs. The version just scanned becomes the **new primary** in Quick Facts;
  prior primary data is moved into `overrides` as history. Running `append` on each branch
  is what assembles the full 2×2 matrix.
- **`overwrite`** — rescans and **replaces** the facts for the named version (e.g. after a
  firmware fix), leaving other versions and the prose body untouched.

Both operations **only update files that already exist** and **never alter the prose body**
or the file structure.

### Macro resolution

Range/default values are `#define`s. The generator resolves them by either:
- parsing the relevant headers (`Params.h`, `ParamsCommon.h`, `CentraliLib.h`) for the
  `*_MIN/_MAX/_DFLT` symbols, or
- running the C preprocessor (`gcc -E`) over a minimal shim that includes those headers.

The chosen approach is an implementation detail for the plan; both are viable. Unresolved
symbols are reported, not silently dropped.

### Manifest (the backlog)

For every keyword found in `Params.c` that has **no doc file**, the generator appends an
entry to a manifest (e.g. `_manifest/undocumented.md`) recording the keyword and which
version(s)/product(s) it appears in. The manifest is the worklist; once a doc exists, the
next run begins maintaining its facts. Keywords documented but absent from all scanned
versions are flagged for review (candidate `removed_in`).

### Body preservation

The merge step parses each `.md` into (frontmatter, body), rewrites only the frontmatter,
and re-emits the original body verbatim. This guarantees authored prose, examples, and
version-change notes survive every regeneration.

## 7. Consumption contract

Both displays read the same source files; neither is built in this spec.

- **Public website** — a static-site generator (e.g. Quartz/Hugo/MkDocs) reads frontmatter
  + body and renders the Article+sidebar layout, matrix, and dot markers.
- **C# in-product viewer** — reads the same files with **YamlDotNet** (frontmatter) and
  **Markdig** (body), rendering with its own templates.

The format is deliberately language-neutral so a single source of truth feeds both.

## 8. Workflow & sequencing

1. **Build** the schema + generator.
2. **Seed** — run `append` on both branches to populate accurate frontmatter facts across
   all existing docs, and produce the undocumented manifest. (Immediate win: every existing
   page gains correct, version-aware Quick Facts.)
3. **Pilot** — fully enrich `11-control-tuning` (56 keywords) against the standard to
   validate the template end-to-end (prose, diagrams, version-change notes, rendering).
4. **Roll out** — later cycles enrich category by category, each its own small effort,
   draining the manifest over time.

## 9. Risks & open items

- **Macro resolution robustness** — different products/branches may define the same symbol
  differently; the generator must resolve within the correct branch/product context.
- **`data_type` encoding (TBC)** — on the LTS branch every keyword is a 32-bit `long`, so v4
  defaults to `int32`. How v4's planned `float32` and v5's `int64`/`float64` are encoded in
  the develop-branch source (a new table column, a separate type table, or naming
  convention) must be confirmed when the generator is built; until then `data_type` may need
  a manual override path for the new types.
- **Multiple table copies** — `Params.c` also contains an `IS_BOOT_IMAGE` table; the
  generator targets only `CONTROLLER` and `CI_MASTER` and ignores the boot image.
- **Mnemonic stability** — matching docs to keywords relies on the mnemonic; renamed
  keywords across versions will need manual reconciliation (surfaced via the manifest).
- **Rendering of the polished panel in raw Obsidian** — Obsidian shows frontmatter as plain
  properties; the styled Quick Facts panel is produced by the downstream renderers. Optional
  in-vault rendering (Dataview/Templater) is a later nicety, not required here.

## 10. Acceptance criteria for this spec's implementation

- A documented frontmatter schema exists and is applied to the pilot category.
- The Python generator supports `append` and `overwrite` with a `--version` flag, reads both
  product tables, resolves ranges/defaults, preserves prose bodies, and never creates or
  moves files.
- Running the generator on both branches yields correct `availability` matrices and
  `overrides` diffs for the pilot keywords.
- An undocumented-keyword manifest is generated.
- `11-control-tuning` is fully enriched to the per-keyword checklist and renders correctly
  in at least one downstream renderer.
