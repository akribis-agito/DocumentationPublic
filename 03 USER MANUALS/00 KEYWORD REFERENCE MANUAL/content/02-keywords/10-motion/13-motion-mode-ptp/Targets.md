---
keyword: Targets
summary: Array of target positions (user units) for multi-target point-to-point motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 376
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
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
# Targets

Flash-stored array of target positions (user units), available for user programs.

## Overview

`Targets` is a small, flash-backed, axis-scoped array of position values in user units. It is intended as convenient persistent storage for a set of named destinations that a [user program](../../../01-keyword-usage-and-syntax/syntax.md) can read and then load into [AbsTrgt](AbsTrgt.md) (or convert into [RelTrgt](RelTrgt.md)) before each [Begin](../04-motion-command/Begin.md). It is read/write and saved to flash, so the destinations survive a power cycle.

## How it works

`Targets` is a **storage array, not an automatic motion queue.** It is a flash-stored parameter, but no motion engine, profiler or interpreter logic reads it — it is simply persistent storage. The trajectory profiler always moves toward the single target [AbsTrgt](AbsTrgt.md); to walk through several positions you read `Targets[n]` into `AbsTrgt` yourself between moves.

### Array size and indexing

The array holds **three usable entries**. As with all keyword arrays, index `0` is reserved so that command indexes start at `1`, giving valid indexes `Targets[1]`, `Targets[2]`, `Targets[3]`. Each entry has the same full position range as `AbsTrgt`.

## Examples

```text
ATargets[1]=10000    ; store destination 1 in flash
ATargets[2]=20000    ; store destination 2
ATargets[3]=30000    ; store destination 3
AAbsTrgt=10000       ; later: load a stored destination into the active target
ABegin               ; and move there
```

To step through all three from a user program, copy each entry into `AbsTrgt` and `Begin` in turn, waiting for in-target between moves.

## Changes between versions

In **v5 (central-i)** the entries are 64-bit integers with the larger range shown in the frontmatter, matching the 64-bit position pipeline. **v5 is central-i only**, so on standalone `Targets` remains a v4 32-bit array.

## See also

- [AbsTrgt](AbsTrgt.md) — the single active target a stored value is loaded into
- [RelTrgt](RelTrgt.md) — single relative target distance
- [Begin](../04-motion-command/Begin.md) — start a move toward the loaded target
