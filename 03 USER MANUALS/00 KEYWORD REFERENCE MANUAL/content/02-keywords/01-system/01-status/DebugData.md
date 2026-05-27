---
keyword: DebugData
summary: Array reserved for Agito feature development and testing.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 224
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 200
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DebugData

Array reserved for Agito feature development and testing.

## Overview

`DebugData` is a large scratch array reserved for Agito feature development and testing (200 elements on most builds, larger on some). Its contents and meaning are **not fixed** and may change between firmware builds, so it should not be used in production integrations.

## How it works

`DebugData` is a single shared, non-axis array that firmware modules read and write directly to expose internal values or to inject test conditions during development. Individual elements are addressed by named indices inside the firmware, so what any given element means depends entirely on the build. Examples of the kinds of uses it serves include capturing control-interrupt timing (counters latched at the start, mid-point and end of the real-time interrupt), simulating digital-input states for testing, reporting the I²t motor-power-limit value, and snapshotting profiler / position-reference signals for waveform demonstrations.

Because these assignments are added and removed as features are developed, the array carries no stable, documented layout. Treat any value read from `DebugData` as meaningful only in the context of the exact firmware build that produced it.

## Examples

```text
ADebugData[1]       ; read a development scratch value (meaning is build-specific)
```

## See also

- [RNDDebug](../02-operation/RNDDebug.md) — related development/debug command
