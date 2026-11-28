"""Product-specific EthernetPort facts survive a keyword manual refresh (#40)."""
from pathlib import Path
import shutil

import pytest

from keyworddocgen.table_parser import collapse_by_product_type, parse_kw_row_table


@pytest.mark.parametrize("master_first", [False, True])
def test_ethernet_port_ceiling(tmp_path, master_first):
    fw = tmp_path / "firmware"
    shutil.copytree(Path(__file__).parent / "fixtures/v5_firmware", fw)
    header = fw / "CommonIncludes/ProductConfig.h"
    first, second = (("CI_MASTER", 65524), ("CONTROLLER", 65535))
    if not master_first:
        first, second = second, first
    with header.open("a") as out:
        for role, ceiling in (first, second):
            out.write(f"\n#if PRODUCT_TYPE == {role}\n#define ETHERNETPORT_MAX {ceiling}\n#endif\n")

    table = fw / "CommonC/AG300_CTL01Params.c"
    source = table.read_text()
    # The test table has ten slots. Use its ordinary scalar row for EthernetPort.
    source = source.replace('"CurrLim"', '"EthernetPort"').replace(
        "(long double)(-CURR_MAX)", "(long double)(0)"
    ).replace("(long double)(CURR_MAX)", "(long double)(ETHERNETPORT_MAX)")
    table.write_text(source)
    cells = collapse_by_product_type(parse_kw_row_table(fw))
    for role, maximum in (("controller", 65535), ("ci-master", 65524)):
        assert cells[role]["EthernetPort"]["attributes"]["range"] == [0, maximum]
