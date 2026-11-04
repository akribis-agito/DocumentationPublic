import pytest

from keyworddocgen.merge import FactsAlreadyRecorded, merge_scan


def attrs(**over):
    base = {
        "access": "rw", "scope": "axis", "flash": True, "type": "array",
        "array_size": 6, "data_type": "int32", "ok_in_motion": True,
        "ok_motor_on": True, "units": "none", "range": [0, 20000],
        "default": 0, "scaling": 1.0, "implemented": "final",
    }
    base.update(over)
    return base


def cell(can_code=100, products=(), **over):
    return {"can_code": can_code, "attributes": attrs(**over), "products": list(products)}


def both(**over):
    return {"controller": cell(**over), "ci-master": cell(**over)}


def test_first_append_sets_primary_and_availability():
    fm = merge_scan({}, both(), mode="append")
    assert fm["availability"] == ["controller", "ci-master"]
    assert fm["can_code"] == 100
    assert fm["attributes"]["range"] == [0, 20000]
    assert fm["overrides"] == {}
    assert "products" not in fm


def test_controller_is_primary_and_ci_master_differences_are_overrides():
    scan = {"controller": cell(range=[-2147483648, 2147483647]),
            "ci-master": cell(range=[-2251799813685248, 2251799813685247], data_type="int64")}
    fm = merge_scan({}, scan, mode="append")
    assert fm["attributes"]["data_type"] == "int32"
    assert fm["overrides"] == {
        "ci-master": {"range": [-2251799813685248, 2251799813685247], "data_type": "int64"}}


def test_can_code_divergence_recorded_in_overrides():
    scan = {"controller": cell(can_code=468), "ci-master": cell(can_code=348)}
    fm = merge_scan({}, scan, mode="append")
    assert fm["can_code"] == 468
    assert fm["overrides"]["ci-master"] == {"can_code": 348}
    # reconstruct round-trip keeps the override
    fm = merge_scan(fm, scan, mode="overwrite")
    assert fm["overrides"]["ci-master"] == {"can_code": 348}


def test_ci_master_only_keyword_is_primary_ci_master():
    fm = merge_scan({}, {"controller": None, "ci-master": cell(can_code=700)}, mode="append")
    assert fm["availability"] == ["ci-master"]
    assert fm["can_code"] == 700
    assert fm["overrides"] == {}


def test_products_union_follows_availability():
    scan = {"controller": cell(products=["agd155-ec", "agd101-ec-34a"]),
            "ci-master": cell(products=["agm800-ec"])}
    fm = merge_scan({}, scan, mode="append")
    assert fm["products"] == ["agd101-ec-34a", "agd155-ec", "agm800-ec"]
    assert list(fm).index("products") == list(fm).index("availability") + 1
    # a re-scan where every product has it drops the list
    fm = merge_scan(fm, both(), mode="overwrite")
    assert "products" not in fm


def test_append_errors_if_facts_already_recorded():
    fm = merge_scan({}, both(), mode="append")
    with pytest.raises(FactsAlreadyRecorded):
        merge_scan(fm, both(), mode="append")


def test_overwrite_replaces_facts():
    fm = merge_scan({}, both(), mode="append")
    fm = merge_scan(fm, both(default=9), mode="overwrite")
    assert fm["attributes"]["default"] == 9


def test_absent_from_every_type_is_an_error():
    with pytest.raises(ValueError):
        merge_scan({"keyword": "Gone"}, {"controller": None, "ci-master": None}, mode="overwrite")


def test_v1_front_matter_is_replaced_not_merged():
    v1 = {
        "keyword": "PosGain", "summary": "Gain.", "can_code": 348,
        "availability": {"standalone": ["v4"], "central-i": ["v4", "v5"]},
        "attributes": attrs(range=[0, 5]),
        "overrides": {"standalone.v4": {"can_code": 468}},
        "removed_in": ["v5"],
    }
    fm = merge_scan(v1, both(range=None), mode="overwrite")
    assert fm["availability"] == ["controller", "ci-master"]
    assert fm["can_code"] == 100
    assert fm["overrides"] == {}
    assert "removed_in" not in fm
    assert fm["attributes"]["range"] is None      # the v4-era range is not carried over
    assert list(fm)[:3] == ["keyword", "summary", "can_code"]


def test_overwrite_keeps_known_value_when_rescan_returns_null():
    # A symbol that scans as null must not downgrade a previously-resolved
    # range/default of the same product type to null.
    fm = merge_scan({}, both(range=[0, 20], default=5), mode="append")
    fm = merge_scan(fm, both(range=None, default=None), mode="overwrite")
    assert fm["attributes"]["range"] == [0, 20]
    assert fm["attributes"]["default"] == 5


def test_null_guard_is_per_product_type():
    scan = {"controller": cell(range=[0, 20]), "ci-master": cell(range=[0, 30])}
    fm = merge_scan({}, scan, mode="append")
    fm = merge_scan(fm, both(range=None), mode="overwrite")
    assert fm["attributes"]["range"] == [0, 20]
    assert fm["overrides"]["ci-master"]["range"] == [0, 30]


def test_overwrite_still_applies_a_real_range_change():
    fm = merge_scan({}, both(range=[0, 20]), mode="append")
    fm = merge_scan(fm, both(range=[0, 30]), mode="overwrite")
    assert fm["attributes"]["range"] == [0, 30]


def test_overwrite_fills_in_a_newly_resolved_value():
    # null -> a real value is a legitimate improvement, not blocked by the guard
    fm = merge_scan({}, both(range=None), mode="append")
    fm = merge_scan(fm, both(range=[0, 20]), mode="overwrite")
    assert fm["attributes"]["range"] == [0, 20]


def test_preserves_existing_summary_and_category():
    fm = {"summary": "Proportional gain.", "category": "control-tuning"}
    fm = merge_scan(fm, both(), mode="append")
    assert fm["summary"] == "Proportional gain."
    assert fm["category"] == "control-tuning"


def test_per_product_overrides_are_keyed_by_catalog_id():
    scan = {"controller": {**cell(range=[-16000, 16000]),
                           "product_overrides": {"agd155-ec": {"range": [-8000, 8000]}}},
            "ci-master": {**cell(range=[-25500, 25500]),
                          "product_overrides": {"agm800-ec": {"scaling": 1.024}}}}
    fm = merge_scan({}, scan, mode="append")
    assert fm["attributes"]["range"] == [-16000, 16000]
    # Type delta first, then each product's delta from its own type's cell.
    assert fm["overrides"] == {
        "ci-master": {"range": [-25500, 25500]},
        "agd155-ec": {"range": [-8000, 8000]},
        "agm800-ec": {"scaling": 1.024},
    }
    # A rescan without them drops them.
    fm = merge_scan(fm, both(), mode="overwrite")
    assert fm["overrides"] == {}
