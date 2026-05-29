---
summary: Ratio between a desired user unit and encoder counts for reading position and its derivatives.
---
# UsrUnits/AuxUsrUnits

Ratio between a desired user unit and encoder counts for reading position and its derivatives.

## Overview

`UsrUnits` allows the user to read and write position and its derivatives in units other than encoder counts. It scales the values exchanged with the host (position, velocity, acceleration) so they can be expressed in a convenient engineering unit (e.g. mm) rather than raw counts. The internal control loop always works in counts; `UsrUnits` is applied only at the communication/display layer. `AuxUsrUnits` is the auxiliary-encoder counterpart and operates the same way on the auxiliary feedback position and its derivatives.

> **Note (central-i v5)** — `UsrUnits`/`AuxUsrUnits` is the embedded per-axis scaling. central-i v5 also offers an alternative *global engineering-units feature*, enabled per axis with [UserUnitsEn](../../21-engineering-units/UserUnitsEn.md), which expresses keyword values in configurable engineering units. The two systems are mutually exclusive on the same axis: with `UserUnitsEn = 1` and `UsrUnits`/`AuxUsrUnits` left at a non-default value, accessing an affected keyword is rejected with error `338`. Leave the embedded scaling at its default or set `UserUnitsEn` back to 0 to resolve the conflict.

## How it works

`UsrUnits` is stored as a **16.16 fixed-point ratio**: the effective scale factor is `UsrUnits / 65536` (the fixed-point scaling is 65536, i.e. 16 fractional bits). The default `UsrUnits = 65536` therefore means a factor of 1 (values shown directly in counts).

$$\text{user value} = \frac{\text{counts}}{\bigl(\text{UsrUnits} / 65536\bigr)} = \text{counts} \cdot \frac{65536}{\text{UsrUnits}}$$

When `UsrUnits` is an exact integer multiple of 65536, the firmware takes the fast accurate path and divides the count value by `UsrUnits >> 16` with rounding; otherwise it uses the full fixed-point ratio. Writes (e.g. setting a target) are scaled the inverse way (multiplied by the ratio). The same factor applies to all derivatives, so velocity is reported in user-units/s and acceleration in user-units/s².

To express "*N* encoder counts = 1 user unit", set `UsrUnits = N × 65536`.

## Examples

To read position in mm when 5 encoder counts equal 1 mm, set the ratio to 5 — i.e. `UsrUnits = 5 × 65536 = 327680`. Position is then reported in mm, velocity in mm/s, and acceleration in mm/s².

A second worked case: a rotary motor with `EncRes = 10000` counts/revolution that you want to read in degrees. One degree corresponds to `10000 / 360 ≈ 27.78` counts, so set `UsrUnits = 27.78 × 65536 ≈ 1820445`. The host then sees positions in degrees, velocities in deg/s, and accelerations in deg/s².

```text
AUsrUnits=327680     ; 5 counts per user unit (ratio 5 = 5 x 65536) — mm with 5 counts/mm
AUsrUnits=1820445    ; degrees on a rotary motor with EncRes = 10000
AUsrUnits=65536      ; factor 1 — report directly in encoder counts (default)
```

## See also

- [EncRes](EncRes.md) — raw encoder resolution in counts per pitch or revolution
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position, reported scaled by `UsrUnits`
- [UserUnitsEn](../../21-engineering-units/UserUnitsEn.md) — central-i v5 global engineering-units feature, mutually exclusive with this embedded scaling (error `338`)
- [Engineering Units overview](../../21-engineering-units/00-overview.md) — the global Group / Factor / Unit model
