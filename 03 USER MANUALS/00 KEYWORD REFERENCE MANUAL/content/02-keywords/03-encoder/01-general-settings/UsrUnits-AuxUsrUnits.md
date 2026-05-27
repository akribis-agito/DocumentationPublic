---
summary: Ratio between a desired user unit and encoder counts for reading position and its derivatives.
---
# UsrUnits/AuxUsrUnits

Ratio between a desired user unit and encoder counts for reading position and its derivatives.

## Overview

`UsrUnits` allows the user to read the position and its derivatives in units other than encoder counts. It is the ratio between the desired unit and the encoder counts, so position, velocity, and acceleration can be reported in a convenient engineering unit (e.g. mm) rather than raw counts. `AuxUsrUnits` is the auxiliary-encoder counterpart and operates the same way on the auxiliary feedback position and its derivatives.

## Examples

If the user wants to see the position reading in mm and every 5 encoder counts equal 1 mm, set `UsrUnits` to 5. The position is then reported in mm, velocity in mm/s, and acceleration in mm/s².

```text
AUsrUnits=5          ; 5 encoder counts per user unit (e.g. 1 mm)
```

## See also

- [EncRes](EncRes.md) — encoder resolution in counts per pitch or revolution
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position, reported in user units
