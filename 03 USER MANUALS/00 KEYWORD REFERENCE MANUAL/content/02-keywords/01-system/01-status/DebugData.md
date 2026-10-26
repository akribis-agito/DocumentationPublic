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
overrides:
  central-i.v5:
    array_size: 356
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# DebugData

Array reserved for Agito feature development and testing.

## Overview

`DebugData` is a large scratch array reserved for Agito feature development and testing (200 elements on most builds, larger on some). Its contents and meaning are **not fixed** and may change between firmware builds, so it should not be used in production integrations.

## How it works

`DebugData` is a single shared, non-axis array that firmware modules read and write directly to expose internal values or to inject test conditions during development. Individual elements are addressed by named indices inside the firmware, so what any given element means depends entirely on the build. Examples of the kinds of uses it serves include capturing control-interrupt timing (counters latched at the start, mid-point and end of the real-time interrupt), simulating digital-input states for testing, reporting the I²t motor-power-limit value, and snapshotting profiler / position-reference signals for waveform demonstrations.

Outside the versioned window below, assignments change as features are developed and the array has no stable layout. Treat any value read from `DebugData` as meaningful only in the context of the exact firmware build that produced it.

## Versioned ISR timing window (pre-release AGM800 / AGM800-EC)

These Zynq builds allocate 356 elements (indices 0–355). The diagnostic latch
remains at 300–331. The dedicated timing window is 332–355; other builds may
not expose it. Pin the firmware image and check signature `0x49535133` before
interpreting these fields.

| Indices | Meaning |
| --- | --- |
| 332 | Request/state: 0 off, 1 start/reset, 2 running, 3 freeze, 4 frozen |
| 333 | Window signature/version |
| 334–335 | Global-timer frequency (Hz), nominal interrupt period (counts) |
| 336 | Observed completed ticks |
| 337–338 | Last/maximum handler-body duration |
| 339–340 | Last/maximum offline/event phase duration |
| 341–342 | Last/maximum summed queue-helper duration per tick |
| 343–344 | Last/maximum interrupt-entry gap |
| 345–346 | Gaps above 1.5 nominal periods; body spans reaching the period |
| 347–348 | Last/maximum helper calls per tick |
| 349–350 | First/last entry timestamp, low 32 bits |
| 351–355 | Phase duration, helper sum, entry gap, task selector before increment, and tick number from the maximum body-duration sample |

Version 1 (`0x49535131`) exposes only indices 332–350. Version 2 adds same-tick peak correlation; independent maxima can occur on different ticks.

Write only the request field. Wait for state 4 before reading a snapshot; frozen
results remain stable until the next start/reset. Convert duration counts using
index 334. Capture adds probe overhead; the body span excludes the FIQ wrapper,
compiler prologue/epilogue and publication after the last timer read. Entry-gap
counts do not replace a hardware missed-interrupt counter. A passing observed
window does not prove worst-case timing or qualify another hardware setup.

## Examples

```text
ADebugData[1]       ; read a development scratch value (meaning is build-specific)
```

## See also

- [RNDDebug](../02-operation/RNDDebug.md) — related development/debug command

Version 3 (`0x49535133`) preserves the version 2 fields and orders each timer read with compiler memory barriers and CPU DSB/ISB instructions. Versions 1/2 used volatile MMIO alone. Earlier probe overhead is included; barriers after the final timer read, final publication and the FIQ wrapper are excluded. Keep capture versions separate when comparing timings.
