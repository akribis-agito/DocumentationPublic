---
keyword: CurrFFWValues
summary: 'Read-only feedforward currents: the filtered total and its parts, in mA.'
availability:
  standalone: []
  central-i:
  - v5
can_code: 856
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 7
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrFFWValues

Read-only feedforward currents: the filtered total and its parts, in mA.

## Overview

`CurrFFWValues` lets you read back the feedforward currents of an axis. It is read-only and is not saved to flash. Values are in mA.

| Index | Value |
|---|---|
| `CurrFFWValues[1]` | Total feedforward current after the feedforward filter, as added to the current reference. **Includes the friction current.** |
| `CurrFFWValues[2]` | Velocity feedforward term ([VelFFW](VelFFW.md)) |
| `CurrFFWValues[3]` | Acceleration feedforward term ([AccFFW](AccFFW.md)) |
| `CurrFFWValues[4]` | Jerk feedforward term |
| `CurrFFWValues[5]` | Reserved (reads 0) |
| `CurrFFWValues[6]` | Friction feedforward current, *before* the feedforward filter (AGM800 and AGM800-EC only) |

## How it works

Index 6 is the output of the friction feedforward stage after the [FricLim](../../../03-special-features/friction-compensation/FricLim.md) clamp. It replaces `FricCurr` from 5.3.0-rc4. It reads 0 when the stage is off or not running (for example in current mode).

Index 1 is what the feedforward filter ([FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md)) puts out. The friction current goes through that filter together with the velocity and acceleration terms, so index 1 includes friction. With `FFFiltOn` = 0, index 1 is the plain sum. With `FFFiltOn` = 1, index 1 lags index 6 at reversals. During the two control cycles of a CNC feedforward skip, the feedforward going into the filter is zeroed (friction included), so index 1 drops — straight to 0 with `FFFiltOn` = 0 — while indexes 2 to 6 keep their values. In velocity mode and in force mode with [ForcePIVOn](../07-force-control/ForcePIVOn.md) = 1, the velocity and acceleration terms are not used, and index 1 carries friction only.

In modes where the velocity loop does not form the current reference (for example current mode), index 1 keeps its last value.

On products without the friction feedforward stage the array ends at index 5.

## Examples

```text
ACurrFFWValues[6]     ; friction current before the filter, mA
ACurrFFWValues[1]     ; total feedforward current after the filter, mA
```

## See also

- [Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md) — the friction stage
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — the feedforward filter
- [VelFFW](VelFFW.md) / [AccFFW](AccFFW.md) — reference feedforward gains
