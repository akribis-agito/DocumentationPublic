from pathlib import Path

from keyworddocgen.defines import DefineTable

FIX = Path(__file__).parent / "fixtures"


def make_table():
    return DefineTable.from_headers([FIX / "defs.h"])


def test_parses_plain_int():
    assert make_table().resolve("POSGAIN_MAX") == 20000


def test_strips_trailing_comment():
    assert make_table().resolve("CONTROL_SIZE") == 6


def test_resolves_arithmetic_expression():
    assert make_table().resolve("CONTROL_SIZE-1") == 5


def test_resolves_symbol_arithmetic():
    assert make_table().resolve("DERIVED_MAX") == 40000


def test_non_numeric_returns_none():
    assert make_table().resolve("DONTCARE") is None


def test_unknown_symbol_returns_none():
    assert make_table().resolve("NOPE") is None
