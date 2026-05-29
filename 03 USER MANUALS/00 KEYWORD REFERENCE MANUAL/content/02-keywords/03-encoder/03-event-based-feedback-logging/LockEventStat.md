---
keyword: LockEventStat
summary: Reports the initialization state of the lock/event subsystem.
availability:
  standalone: []
  central-i:
  - v5
can_code: 833
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LockEventStat

Reports the initialization state of the lock/event subsystem.

> Available from v5 (central-i) only.

## Overview

`LockEventStat` is a read-only status that tells you whether the lock/event subsystem is ready to be armed. It reflects how the firmware-to-hardware capture offset is being handled under the current [LockEventMode](LockEventMode.md), and in the unified mode whether the required [LockEventInit](LockEventInit.md) step has been completed.

Use it as a precondition check before arming [LockEn](LockEn-AuxLockEn.md) or [EventOn](../../18-event-generation/EventOn.md) when running the unified scheme.

## How it works

`LockEventStat` is recomputed whenever [LockEventMode](LockEventMode.md) is written, whenever [LockEventInit](LockEventInit.md) completes, and whenever a configuration change affects the capture source.

| Value | Meaning |
|-------|---------|
| 0 | Legacy mode ([LockEventMode](LockEventMode.md) = 0). No manual initialization is needed — the offset is learned automatically when Lock or Event is armed. |
| 1 | Unified mode ([LockEventMode](LockEventMode.md) = 1) and initialized: [LockEventInit](LockEventInit.md) has been run and the subsystem is ready to arm. |
| -1 | Unified mode ([LockEventMode](LockEventMode.md) = 1) but not yet initialized: run [LockEventInit](LockEventInit.md) before arming Lock or Event. |

A `-1` reading appears when [LockEventMode](LockEventMode.md) is set to `1` and the offset has not been computed since power-up, or when a configuration change has invalidated a previously computed offset. In particular, a change to `EncSinCosHWEn` (the encoder/lock-event capture-source selector) is detected automatically and returns this status to `-1`. In that state, arming [LockEn](LockEn-AuxLockEn.md) or [EventOn](../../18-event-generation/EventOn.md) is rejected until [LockEventInit](LockEventInit.md) is run.

## Examples

```text
ALockEventMode=1      ; select the unified scheme
ALockEventStat        ; reads -1 until LockEventInit has been run
ALockEventInit        ; learn the offset (axis stationary)
ALockEventStat        ; now reads 1 (ready to arm)
ALockEventMode=0      ; revert to legacy mode
ALockEventStat        ; reads 0 (no manual init needed)
```

## See also

- [LockEventMode](LockEventMode.md) — selects legacy vs. unified mode
- [LockEventInit](LockEventInit.md) — performs the initialization that drives this status to `1`
- [LockEn](LockEn-AuxLockEn.md) — arms event-based feedback logging
- [EventOn](../../18-event-generation/EventOn.md) — arms event generation
