import pytest

from keyworddocgen.merge import merge_version, VersionAlreadyRecorded


def attrs(**over):
    base = {
        "access": "rw", "scope": "axis", "flash": True, "type": "array",
        "array_size": 6, "data_type": "int32", "ok_in_motion": True,
        "ok_motor_on": True, "units": "none", "range": [0, 20000],
        "default": 0, "scaling": 1.0, "implemented": "final",
    }
    base.update(over)
    return base


def scan_present(can_code=100, **over):
    return {
        "standalone": {"can_code": can_code, "attributes": attrs(**over)},
        "central-i": {"can_code": can_code, "attributes": attrs(**over)},
    }


def test_can_code_divergence_recorded_in_overrides():
    fm = merge_version({}, scan_present(can_code=468), "v4", mode="append")
    fm = merge_version(fm, scan_present(can_code=348), "v5", mode="append")
    assert fm["can_code"] == 348                                   # v5 primary
    assert fm["overrides"]["standalone.v4"]["can_code"] == 468
    # reconstruct round-trip keeps v4 can_code distinct from v5
    fm = merge_version(fm, scan_present(can_code=348), "v5", mode="overwrite")
    assert fm["overrides"]["standalone.v4"]["can_code"] == 468


def test_first_append_sets_primary_and_availability():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    assert fm["availability"] == {"standalone": ["v4"], "central-i": ["v4"]}
    assert fm["attributes"]["range"] == [0, 20000]
    assert fm.get("overrides", {}) == {}


def test_appending_v5_makes_v5_primary_and_demotes_v4():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(range=[0, 100000]), "v5", mode="append")
    assert fm["attributes"]["range"] == [0, 100000]          # v5 is primary
    assert fm["overrides"]["standalone.v4"]["range"] == [0, 20000]
    assert fm["availability"]["standalone"] == ["v4", "v5"]


def test_append_errors_if_version_already_present():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    with pytest.raises(VersionAlreadyRecorded):
        merge_version(fm, scan_present(), "v4", mode="append")


def test_overwrite_replaces_existing_version():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(default=9), "v4", mode="overwrite")
    assert fm["attributes"]["default"] == 9


def test_data_type_divergence_recorded_in_overrides():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    fm = merge_version(fm, scan_present(data_type="float64"), "v5", mode="append")
    assert fm["attributes"]["data_type"] == "float64"
    assert fm["overrides"]["standalone.v4"]["data_type"] == "int32"


def test_absent_keyword_records_removed_in():
    fm = merge_version({}, scan_present(), "v4", mode="append")
    absent = {"standalone": None, "central-i": None}
    fm = merge_version(fm, absent, "v5", mode="append")
    assert fm["removed_in"] == ["v5"]
    assert fm["availability"]["standalone"] == ["v4"]


def test_preserves_existing_summary_and_category():
    fm = {"summary": "Proportional gain.", "category": "control-tuning"}
    fm = merge_version(fm, scan_present(), "v4", mode="append")
    assert fm["summary"] == "Proportional gain."
    assert fm["category"] == "control-tuning"
