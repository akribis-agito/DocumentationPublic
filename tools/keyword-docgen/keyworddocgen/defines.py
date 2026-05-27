"""Parse C #define constants from headers and resolve integer expressions."""

from __future__ import annotations

import ast
import operator
import re
from pathlib import Path

_DEFINE_RE = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)\s+(.+?)\s*$")
_LINE_COMMENT = re.compile(r"//.*$")
_BLOCK_COMMENT = re.compile(r"/\*.*?\*/")

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.floordiv,
    ast.USub: operator.neg,
}


class DefineTable:
    def __init__(self, raw: dict[str, str]):
        self._raw = raw
        self._cache: dict[str, int | None] = {}

    @classmethod
    def from_headers(cls, paths: list[Path]) -> "DefineTable":
        raw: dict[str, str] = {}
        for path in paths:
            text = Path(path).read_text(errors="replace")
            for line in text.splitlines():
                m = _DEFINE_RE.match(line)
                if not m:
                    continue
                name, value = m.group(1), m.group(2)
                value = _LINE_COMMENT.sub("", value)
                value = _BLOCK_COMMENT.sub("", value)
                value = value.strip()
                if value:
                    raw[name] = value
        return cls(raw)

    def resolve(self, expr: str) -> int | None:
        """Resolve an expression to an int, or None if non-numeric/unknown."""
        expr = expr.strip()
        if expr in self._cache:
            return self._cache[expr]
        result = self._resolve(expr, set())
        if isinstance(expr, str) and re.fullmatch(r"[A-Za-z_]\w*", expr):
            self._cache[expr] = result
        return result

    def _resolve(self, expr: str, seen: set[str]) -> int | None:
        # Substitute known symbols with their raw definitions, recursively.
        def repl(m: re.Match) -> str:
            name = m.group(0)
            if name in seen:
                raise ValueError(f"cyclic define: {name}")
            if name in self._raw:
                inner = self._resolve(self._raw[name], seen | {name})
                if inner is None:
                    raise ValueError("non-numeric")
                return str(inner)
            raise ValueError(f"unknown symbol: {name}")

        # Strip C casts such as "(long double)", "(long long)", "(unsigned long)"
        # which appear on develop's 64-bit range macros, e.g. POS_MAX = (long double) LONG64_MAX.
        expr = re.sub(
            r"\(\s*(?:unsigned\s+|signed\s+)?"
            r"(?:long|short|int|char|float|double)(?:\s+(?:long|double|int|char))*\s*\)",
            " ", expr,
        )
        try:
            substituted = re.sub(r"[A-Za-z_]\w*", repl, expr)
            node = ast.parse(substituted.strip(), mode="eval").body
            return self._eval(node)
        except (ValueError, SyntaxError, TypeError):
            return None

    def _eval(self, node: ast.AST) -> int:
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](self._eval(node.left), self._eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](self._eval(node.operand))
        raise ValueError("unsupported expression")
