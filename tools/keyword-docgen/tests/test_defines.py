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


def test_strips_c_casts_on_64bit_ranges():
    # develop writes 64-bit range macros as "(long double) LONG64_MAX"
    t = make_table()
    assert t.resolve("POS64_MAX") == 2251799813685247
    assert t.resolve("POS64_MIN") == -2251799813685248
    assert t.resolve("(long long) LONG64_MAX") == 2251799813685247


def test_resolves_plain_float():
    # e.g. REMOTE_PWM_PERCENT_FACT = 1.526 (scaling factor)
    assert make_table().resolve("PWM_FACT") == 1.526


def test_resolves_float_with_f_suffix():
    # develop float macros carry a C 'f' suffix, e.g. 200.0f / 0.01f
    t = make_table()
    assert t.resolve("FILTFREQ_DFLT") == 200.0
    assert t.resolve("STD_MIN") == 0.01


def test_resolves_float_exponent():
    assert make_table().resolve("FLOAT_MAX") == 3.40282e38


def test_int_result_is_int_not_float():
    # integer macros must stay int (not become 20000.0)
    r = make_table().resolve("POSGAIN_MAX")
    assert r == 20000 and isinstance(r, int)


def test_int_division_stays_int():
    # C integer division of int operands stays integral
    r = make_table().resolve("INT_DIV")
    assert r == 10000 and isinstance(r, int)
