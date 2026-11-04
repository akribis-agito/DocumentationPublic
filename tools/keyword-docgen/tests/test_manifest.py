from keyworddocgen.manifest import render_manifest


def test_lists_undocumented_with_product_types():
    scanned = {
        "controller": {"PosGain", "PosKi"},
        "ci-master": {"PosGain"},
    }
    documented = {"PosGain"}
    out = render_manifest(scanned, documented)
    assert "| PosKi | controller |" in out
    assert "PosGain" not in out.split("\n\n", 1)[-1]   # documented excluded


def test_empty_when_all_documented():
    scanned = {"controller": {"PosGain"}, "ci-master": set()}
    out = render_manifest(scanned, {"PosGain"})
    assert "PosKi" not in out
