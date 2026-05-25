# UnitStat

**Definition:**

UnitStat reports the status of the unit. The bits of UnitStat reflect the following statues

| Bit \# | Status                                  |
|--------|-----------------------------------------|
| 0      | FPGA is faulty.                         |
| 1      | AGD155 FW and FPGA do not match.        |
| 2      | AGD301 FW and FPGA do not match.        |
| 3      | No golden image is present.             |
| 4      | Dynamic brake FW and FPGA do not match. |

Suggestions if warnings appear:
- Ignore if there is no golden image.
- Approach Agito for latest FW and FPGA.
