---
keyword: DInMode
summary: Assigns a software function to each digital input, with per-axis targeting.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 225
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DInMode

Assigns a software function to each digital input, with per-axis targeting.

## Overview

`DInMode` assigns a software function to a digital input. The array **index** selects the input (1-based: `DInMode[1]` is input 1, `DInMode[2]` is input 2, …).

## How it works

- The **lower 16 bits** of the value select the function (a numeric functionality code — e.g. `10` = reverse limit switch, FLS).
- **Bits 16–27** select which axes the function applies to; each bit is one axis (A–L), and multiple bits may be set.

| Axis | A | B | C | D | E | F | G | H | I | J | K | L |
|------|---|---|---|---|---|---|---|---|---|---|---|---|
| Value, Bit# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |

**Example:** `CDInMode[2] = 65546` (binary `…0001 0000 0000 0000 1010`):
- Index → 2 (digital input 2)
- Lower 16 bits → 10 (reverse limit switch)
- Bit 16 set → axis B

…so digital input 2 (of axis C) acts as the reverse-limit-switch input for axis B.

## Notes

1. After changing `DInMode[]`, [Save](../../01-system/02-operation/Save.md) and [Reset](../../01-system/02-operation/Reset.md) — some special functions only start (or stop) working after a power cycle.
2. At most **20** special functions may be assigned across the digital inputs; beyond that, only the first 20 are operational. A function applied to two axes counts as two.
3. Functions are evaluated in ascending index order; a duplicate functionality on a later input is ignored (except general-purpose input). No error is raised, but PCSuite shows a warning.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — input states
- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — logic inversion
