---
keyword: ECAMMasterIni
summary: Offset of the starting master value relative to the ECAM range at start of motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 306
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ECAMMasterIni

Offset of the starting master value relative to the ECAM range at start of motion.

## Overview

`ECAMMasterIni` denotes the offset of the starting master value relative to the ECAM range upon start of ECAM motion. It is an array of 10 cam patterns, one element per pattern. It positions where, within the cam range, the master begins when ECAM motion starts; its exact role depends on the sign of [ECAMGap](ECAMGap.md) and the value of [ECAMCycles](ECAMCycles.md).

The sign rule for `ECAMMasterIni` differs by version. On **v4** its sign must match [ECAMGap](ECAMGap.md): when `ECAMGap` is positive `ECAMMasterIni` must be zero or positive, and when `ECAMGap` is negative `ECAMMasterIni` must be zero or negative. On **v5** `ECAMMasterIni` must always be zero or positive, regardless of the `ECAMGap` sign. In both versions it must be small enough that the first repetition cycle is not exceeded when motion starts.

## How it works

When ECAM motion starts ([Begin](../04-motion-command/Begin.md)) the controller snapshots the live master value as the origin of the master range. `ECAMMasterIni` shifts where that snapshot sits *inside* the range: with `ECAMMasterIni = 0` the master begins exactly at the start of the range (`GenData[ECAMStart]` for positive [ECAMGap](ECAMGap.md)); a positive value places the starting point further into the pattern by that many master units, so the follower begins partway along the cam profile. The follower's reference is offset at start so it does not jump regardless of `ECAMMasterIni`.

- For positive [ECAMGap](ECAMGap.md) the offset is measured forward from the start of the range; for negative `ECAMGap` it is measured against the negated master, so the same positive value still places the start point further into the pattern.
- For negative [ECAMCycles](ECAMCycles.md) (bidirectional cam), `ECAMMasterIni` positions the *middle* of the repeating region — the point the master is expected to sit at when motion starts — so the pattern can extend in both directions.

The maximum allowed magnitude depends on the version:

- On **v4** a single magnitude bound applies for every `ECAMCycles` value: $\lvert\text{ECAMMasterIni}\rvert \le \lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$.
- On **v5** the bound depends on `ECAMCycles`:

| ECAMCycles | Maximum value of ECAMMasterIni (v5) |
|------------|--------------------------------|
| 1          | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$ |
| \> 1       | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEndCyc} - \text{ECAMStart})$ |
| \< 0       | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEndCyc} - \text{ECAMStartCyc})$ |

## Examples

```text
AECAMMasterIni[1]=0  ; start at the beginning of the ECAM range for cam pattern 1
AECAMMasterIni[1]   ; read current value
```

Refer to the figures in [Motion mode – Electronic cam (ECAM)](00-overview.md) for more information on the initial offset, which varies according to ECAMGap and ECAMCycles.

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Data type / range | 32-bit, `-2147483648` … `2147483647` | 64-bit, `-2251799813685248` … `2251799813685247` |

In **v4** (standalone and central-i) `ECAMMasterIni` is validated against a single magnitude bound — its absolute value may not exceed $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$ for every `ECAMCycles` value — and its sign must follow `ECAMGap` (zero-or-positive when `ECAMGap` is positive, zero-or-negative when `ECAMGap` is negative). In **v5** `ECAMMasterIni` is a 64-bit value with the wider range shown in the frontmatter, matching the 64-bit master positions used in that version; v5 also introduced the per-`ECAMCycles` maximum-value bounds shown in the table above and requires `ECAMMasterIni` to be zero-or-positive regardless of the `ECAMGap` sign. **v5 is central-i only.**

## See also

- [ECAMGap](ECAMGap.md) — spacing/direction of master values and the master-to-index mapping
- [ECAMCycles](ECAMCycles.md) — number of pattern occurrences
- [ECAMMaster](ECAMMaster.md) — selects the master variable
