"""Read and write Obsidian-style frontmatter while preserving the prose body."""

from __future__ import annotations

import yaml

_FENCE = "---\n"


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
