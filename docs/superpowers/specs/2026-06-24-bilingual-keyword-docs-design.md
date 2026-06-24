# Bilingual (English + Simplified Chinese) Keyword Documentation

**Date:** 2026-06-24
**Status:** Design approved — pending spec review
**Scope:** 3 repos — `DocumentationPublic` (source + publishing), `PC-Toolsets` (C#/WPF consumer), `agito-tracker` (React consumer)

## Problem

The ~920 firmware keyword reference docs in `DocumentationPublic` are English-only. Two
downstream apps already have bilingual UI chrome (PC-Toolsets: `zh-CN` via `.resx` +
Windows Registry locale; agito-tracker: `en`/`zh` via `strings.js` + `useT` + a language
toggle), and both already display these keyword docs — but the docs themselves are served
untranslated. We want Simplified-Chinese translations of the docs plus a publishing "hook"
so each app serves the right language automatically from the locale it *already* tracks,
with no new language-selection UI anywhere.

## Key facts that shape the design

- The `keyword` frontmatter field is an **immutable, language-neutral join key** (e.g.
  `AutoExec`). It is identical across languages and never changes.
- Frontmatter **facts are generated from firmware** (CAN code, range, availability,
  access, scope, units, …) and are **language-neutral**. They are never hand-edited.
  Only prose needs translating: the `summary` one-liner and the markdown body.
- `manifest.json` (per-doc: `path`, `keyword`, `last_updated`, `doc_revision`, `sha256`)
  is the index both consumers fetch. The Python `keyword-docgen` generator only rewrites
  frontmatter facts and **preserves the body**, so translated prose can coexist safely.
- PC-Toolsets fetches docs live from `akribis-agito/DocumentationPublic` →
  `03 USER MANUALS/00 KEYWORD REFERENCE MANUAL/`, diffing against `manifest.json`,
  verifying `sha256`, rendering in a WebView2 SPA at route `#/kw/<Keyword>`.
- agito-tracker reads the same docs and parses frontmatter + prose in
  `src/components/library/keywordDoc.js`.

## Decisions (locked)

1. **Layout:** self-contained sidecar `<Keyword>.zh.md` files alongside each English
   `<Keyword>.md`, in the same folder.
2. **Rollout:** translate all ~920 docs in one swarm run.
3. **Branching:** `DocumentationPublic` and `PC-Toolsets` each get a worktree + feature
   branch + PR. `agito-tracker` is worked in place and pushed directly (no PR).
4. **Variant:** Simplified Chinese only (`zh-CN`).

## Component 1 — DocumentationPublic: bilingual source + the hook

### Sidecar files

For each `<Keyword>.md`, add `<Keyword>.zh.md` in the same directory. The `.zh.md` is
**self-contained** so a consumer can render it from a single fetch:

- Frontmatter: a **copy of the generated language-neutral facts** (identical to the
  English file), plus `language: zh-CN`, plus a **translated `summary`**.
- Body: the **translated prose**.

Facts live in both files but are owned by the generator in both — they are never
hand-edited and cannot diverge (see generator changes).

### Generator (`keyword-docgen`) changes

- **Fact propagation:** when syncing/refreshing facts (`append`/`overwrite` flows),
  write the same facts into the `.zh.md` sidecar, **preserving its Chinese prose body**
  (reuse the existing body-preserving logic already used for English files). Set/keep
  `language: zh-CN` and do not overwrite the translated `summary`.
- **Versioning:** the `version` command stamps each `.zh.md` with its own `sha256`,
  `last_updated`, and `doc_revision`, and includes it in `manifest.json` (see below).
- **RAG export:** `rag-export` emits zh chunks carrying `language: zh-CN` metadata;
  the English chunks are unchanged.

### manifest.json — additive, backward-compatible

English records stay **byte-for-byte unchanged** so currently-deployed PC-Toolsets clients
keep working (English-only) until they update. Each record gains an additive `variants`
object that old parsers ignore:

```jsonc
{
  "keyword": "AutoExec",
  "path": ".../AutoExec.md",          // unchanged
  "sha256": "...",                     // unchanged
  "last_updated": "...",               // unchanged
  "doc_revision": "...",               // unchanged
  "variants": {                        // NEW — ignored by old parsers
    "zh-CN": { "path": ".../AutoExec.zh.md", "sha256": "..." }
  }
}
```

Consumers select a variant by their UI locale and **fall back to English** when a
`zh-CN` variant is absent for a given keyword.

## Component 2 — Translation rules (the swarm must obey these)

Translate **only natural-language prose**: the `summary` field and the body section text
(Overview / How it works / Examples narration / See also prose).

**Leave verbatim (do NOT translate):**

- Keyword names and mnemonics (`AutoExec`, `PosFiltDef`, …).
- Command syntax, including axis-prefix forms like `AKeyword[1]` and `AKeyword[1]=value`
  (never a `?` query suffix).
- Code examples and code fences.
- Numeric values, ranges, units tokens, bit/register references, CAN codes.
- Array examples — kept **1-indexed** (`keyword[1]` is the first element; `keyword[0]`
  does not exist).

**No enrichment.** This is pure translation of existing prose — no new technical claims,
no added explanation, no firmware internals (file/function/variable/`#define`/register
names). This matters especially for the **sensitive control-tuning docs** (domain
`11-control-tuning`): translate what is there, add nothing.

**Consistency.** A shared **glossary/termbase** of motion-control terms is built first and
every translation is checked against it so terminology is consistent across all 920 docs.

**Verification.** Each translated doc gets a verify pass confirming: (a) terminology
matches the glossary, (b) no facts/numbers/syntax were altered, (c) keyword names and code
left verbatim, (d) section structure preserved, (e) no enrichment introduced.

## Component 3 — PC-Toolsets (C#/WPF): auto-switch by locale

- `DocsSync/DocsEndpoints.cs` + `DocsSync/DocsSyncEngine.cs`: when the registry locale is
  `zh-CN`, resolve `variants["zh-CN"].path` from the manifest and fetch it (plus English
  as fallback) through the existing manifest-diff → fetch → `sha256`-verify → cache
  pipeline. Cache both variants locally.
- `DocsSync/DocsManifest.cs`: extend the deserialized model with the optional `variants`
  field.
- `HelpLib/Docs/KeywordDocResolver.cs`: **unchanged** — the keyword id is language-neutral
  (exact match + axis-prefix-strip fallback still apply).
- Viewer: the WebView2 SPA (`viewer.html`, route `#/kw/<Keyword>`) loads the `zh-CN` file
  when locale is `zh-CN`, English otherwise. **No new UI** — it follows the language the
  app already has.

## Component 4 — agito-tracker (React): pick variant in the loader

- `src/components/library/keywordDoc.js`: when `language === "zh"` (from the existing
  `LanguageContext`), request `<Keyword>.zh.md`; otherwise `<Keyword>.md`. Fall back to
  English on 404.
- Reuses the existing i18n / pinyin infrastructure — **no new language toggle**.
- Direct push to the latest branch, no PR.

## Execution shape

- **Worktrees:** one in `DocumentationPublic` (feature branch: translations + generator +
  manifest changes), one in `PC-Toolsets` (feature branch: consumer changes).
  `agito-tracker` worked in place and pushed.
- **Translation swarm:** a Workflow that (1) builds the glossary, (2) translates each doc,
  (3) verifies each doc, **writing each `<Keyword>.zh.md` straight to disk in the
  DocumentationPublic worktree as it completes**. On-disk incremental output makes the run
  crash-safe and resumable — a compaction or kill mid-run does not lose completed work.
- **Scale note:** 920 docs × (translate + verify) is a large, token-heavy run; incremental
  on-disk writes make it resumable.

## Out of scope / non-goals

- Traditional Chinese (`zh-TW`) — Simplified only.
- Translating the generated frontmatter facts — they are language-neutral.
- New language-selection UI in either consumer — both already track a locale.
- Changing the `keyword` join key or the English docs' content.

## Open risks

- **Deployment ordering:** the additive `variants` field keeps old PC-Toolsets clients
  working, but a client must be updated to *serve* Chinese. PRs gate that update.
- **Generator regression:** fact propagation into `.zh.md` must preserve the translated
  body; covered by tests before the full swarm run.
- **Glossary quality** drives translation consistency; build and sanity-check it before
  fanning out.
