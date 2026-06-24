"""Read and write Obsidian-style frontmatter while preserving the prose body."""

from __future__ import annotations

from pathlib import Path

import yaml

_FENCE = "---\n"

# Frontmatter keys that hold AUTHORED prose (per language), not generated
# language-neutral facts. These are never copied from the English file into a
# translated sidecar — the sidecar keeps its own translated values.
_AUTHORED_PROSE_KEYS = ("summary",)
# The language marker is owned by the sidecar (always zh-CN there), and absent
# (== en) on the English file.
_LANGUAGE_KEY = "language"
_ZH_LANGUAGE = "zh-CN"
_ZH_SUFFIX = ".zh.md"


class _NoAliasDumper(yaml.SafeDumper):
    """Dumper that never emits YAML anchors/aliases (&id / *id), so equal
    values (e.g. identical override ranges) are written out in full."""

    def ignore_aliases(self, data):
        return True


def split_doc(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Body is preserved exactly."""
    if not text.startswith(_FENCE):
        return {}, text
    rest = text[len(_FENCE):]
    end = rest.find("\n" + _FENCE.strip() + "\n")
    if end == -1:
        return {}, text
    yaml_block = rest[:end]
    body = rest[end + len("\n" + _FENCE.strip() + "\n"):]
    data = yaml.safe_load(yaml_block) or {}
    return data, body


def render_doc(frontmatter: dict, body: str) -> str:
    """Render frontmatter + body back into a document string."""
    dumped = yaml.dump(
        frontmatter, Dumper=_NoAliasDumper, sort_keys=False,
        default_flow_style=False, allow_unicode=True, width=4096,
    )
    return f"{_FENCE}{dumped}{_FENCE}{body}"


def zh_sidecar_path(en_path) -> Path:
    """Return the zh-CN sidecar path for an English doc: `<Keyword>.md` ->
    `<Keyword>.zh.md` in the SAME folder."""
    en_path = Path(en_path)
    return en_path.with_name(en_path.name[: -len(".md")] + _ZH_SUFFIX)


def is_zh_sidecar(path) -> bool:
    """True if `path` is a `<Keyword>.zh.md` translated sidecar."""
    return Path(path).name.endswith(_ZH_SUFFIX)


def _merge_sidecar_fm(en_fm: dict, zh_fm: dict) -> dict:
    """Build the sidecar's new frontmatter: copy the English (language-neutral)
    facts verbatim, but PRESERVE the sidecar's authored prose (`summary`) and
    force `language: zh-CN`. Key order follows the English file so the facts
    stay in the canonical order; the language marker trails."""
    out: dict = {}
    for key, value in en_fm.items():
        if key == _LANGUAGE_KEY:
            continue  # the English file shouldn't carry one; ignore if it does
        if key in _AUTHORED_PROSE_KEYS and key in zh_fm:
            out[key] = zh_fm[key]      # keep the translated prose
        else:
            out[key] = value           # copy the generated fact
    # Authored prose keys present in the sidecar but absent in English survive.
    for key in _AUTHORED_PROSE_KEYS:
        if key not in out and key in zh_fm:
            out[key] = zh_fm[key]
    out[_LANGUAGE_KEY] = _ZH_LANGUAGE
    return out


def propagate_facts_to_sidecar(en_path, en_fm: dict) -> bool:
    """If a `<Keyword>.zh.md` sidecar exists next to `en_path`, refresh its
    generated facts from `en_fm` while PRESERVING its translated `summary`,
    `language`, and body. Returns True if a sidecar was updated, False if none
    exists (no empty sidecar is ever created)."""
    zh_path = zh_sidecar_path(en_path)
    if not zh_path.exists():
        return False
    zh_fm, zh_body = split_doc(zh_path.read_text())
    new_fm = _merge_sidecar_fm(en_fm, zh_fm or {})
    zh_path.write_text(render_doc(new_fm, zh_body))
    return True
