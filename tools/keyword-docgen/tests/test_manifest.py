from keyworddocgen.manifest import render_manifest


def test_lists_undocumented_with_products_and_version():
    scanned = {
        "standalone": {"PosGain", "PosKi"},
        "central-i": {"PosGain"},
    }
    documented = {"PosGain"}
    out = render_manifest(scanned, documented, version="v5")
    assert "PosKi" in out
    assert "PosGain" not in out.split("\n\n", 1)[-1]   # documented excluded
    assert "standalone" in out
    assert "v5" in out


def test_empty_when_all_documented():
    scanned = {"standalone": {"PosGain"}, "central-i": set()}
    out = render_manifest(scanned, {"PosGain"}, version="v5")
    assert "PosKi" not in out
