from keyworddocgen.frontmatter import split_doc, render_doc


BODY = "# PosGain\n\n**Definition:**\n\nProportional gain.\n"


def test_split_no_frontmatter_returns_empty_and_full_body():
    fm, body = split_doc(BODY)
    assert fm == {}
    assert body == BODY


def test_split_existing_frontmatter():
    text = "---\nkeyword: PosGain\ncan_code: 100\n---\n" + BODY
    fm, body = split_doc(text)
    assert fm["keyword"] == "PosGain"
    assert fm["can_code"] == 100
    assert body == BODY


def test_render_roundtrips_body_verbatim():
    fm = {"keyword": "PosGain", "can_code": 100}
    out = render_doc(fm, BODY)
    fm2, body2 = split_doc(out)
    assert fm2 == fm
    assert body2 == BODY


def test_render_preserves_key_order():
    fm = {"keyword": "PosGain", "summary": "x", "can_code": 100}
    out = render_doc(fm, BODY)
    assert out.index("keyword") < out.index("summary") < out.index("can_code")


def test_render_emits_no_yaml_aliases_for_equal_values():
    # Two override cells with identical range lists must not produce &id/*id.
    fm = {
        "overrides": {
            "standalone.v4": {"range": [1, 5]},
            "central-i.v4": {"range": [1, 5]},
        }
    }
    out = render_doc(fm, BODY)
    assert "&id" not in out and "*id" not in out
    fm2, _ = split_doc(out)
    assert fm2["overrides"]["central-i.v4"]["range"] == [1, 5]
