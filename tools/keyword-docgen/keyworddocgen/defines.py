"""Parse C #define constants from headers and resolve integer expressions."""

from __future__ import annotations

import ast
import operator
import re
from pathlib import Path

_DEFINE_RE = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)\s+(.+?)\s*$")
_LINE_COMMENT = re.compile(r"//.*$")
_BLOCK_COMMENT = re.compile(r"/\*.*?\*/")

# Integer operand path: C integer division stays integral (floordiv).
_INT_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.floordiv,
    ast.USub: operator.neg,
}
# Float operand path: true division so 1526/1000 -> 1.526.
_FLOAT_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}

# A C float literal with an 'f'/'F' suffix, e.g. 200.0f, 0.01f, 1.0e3f.
# Keep the numeric part, drop the suffix (Python can't parse the 'f'). Requires a
# decimal point so it never touches hex literals like 0x1F.
_FLOAT_SUFFIX = re.compile(r"((?:\d*\.\d+|\d+\.\d*)(?:[eE][+-]?\d+)?)[fF]")


class DefineTable:
    def __init__(self, raw: dict[str, str]):
        self._raw = raw
        self._cache: dict[str, int | float | None] = {}

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

    def resolve(self, expr: str) -> int | float | None:
        """Resolve an expression to an int or float, or None if non-numeric/unknown."""
        expr = expr.strip()
        if expr in self._cache:
            return self._cache[expr]
        result = self._resolve(expr, set())
        if isinstance(expr, str) and re.fullmatch(r"[A-Za-z_]\w*", expr):
            self._cache[expr] = result
        return result

    def _resolve(self, expr: str, seen: set[str]) -> int | float | None:
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
        # Drop C float-literal suffixes (200.0f -> 200.0) so they parse as Python.
        expr = _FLOAT_SUFFIX.sub(r"\1", expr)
        try:
            # The lookbehind keeps the 'e' of scientific notation (e.g. 3.4e+38)
            # and hex digits from being mistaken for symbols to substitute.
            substituted = re.sub(r"(?<![\w.])[A-Za-z_]\w*", repl, expr)
            node = ast.parse(substituted.strip(), mode="eval").body
            return self._eval(node)
        except (ValueError, SyntaxError, TypeError):
            return None

    def _eval(self, node: ast.AST) -> int | float:
        if (
            isinstance(node, ast.Constant)
            and isinstance(node.value, (int, float))
            and not isinstance(node.value, bool)
        ):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _INT_OPS:
            left = self._eval(node.left)
            right = self._eval(node.right)
            ops = _INT_OPS if isinstance(left, int) and isinstance(right, int) else _FLOAT_OPS
            return ops[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _INT_OPS:
            val = self._eval(node.operand)
            ops = _INT_OPS if isinstance(val, int) else _FLOAT_OPS
            return ops[type(node.op)](val)
        raise ValueError("unsupported expression")
