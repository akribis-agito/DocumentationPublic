---
keyword: LockEventMode
summary: 'Selects the lock/event operating mode: legacy auto-init (0) or the unified scheme that requires LockEventInit (1).'
availability:
  standalone: []
  central-i:
  - v5
can_code: 831
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -1
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LockEventMode

Selects the lock/event operating mode: legacy auto-init (`0`) or the unified scheme that requires [LockEventInit](LockEventInit.md) (`1`).

> Available from v5 (central-i) only.

## Overview

`LockEventMode` chooses how the event-based feedback-logging ("position lock" / "capture") and event-generation features acquire the offset they need between the value you read back in the controller (such as `Pos`, `AuxPos`, or `VEncValue`) and the internal hardware capture counter that does the latching. That counter starts from an arbitrary offset, so the firmware has to learn the difference once before captured positions can be reported in the units you expect.

There are two ways to learn that offset:

- **Mode 0 (legacy / backward compatible)** — the offset is learned automatically the moment you arm the feature, i.e. when [LockEn](LockEn-AuxLockEn.md) or [EventOn](../../18-event-generation/EventOn.md) transitions from `0` to `1`. This matches the behavior of earlier firmware, so existing configurations keep working unchanged.
- **Mode 1 (unified scheme)** — the offset is *not* learned on arming. Instead you run the [LockEventInit](LockEventInit.md) command yourself, with the axis stationary, before arming Lock or Event. This gives you control over exactly when the offset is sampled, which matters when the capture source may be moving at the instant you would otherwise arm.

The setting is stored in flash, so the selected mode survives a power cycle. The default is `0` (legacy behavior).

## How it works

| Value | Meaning |
|-------|---------|
| 0 | Legacy / backward-compatible mode. The firmware-to-hardware offset is learned automatically when Lock or Event is armed. No manual initialization is needed; [LockEventStat](LockEventStat.md) reports `0`. |
| 1 | Unified mode. You must run [LockEventInit](LockEventInit.md) (axis stationary) to learn the offset before arming Lock or Event. Arming without having run it is rejected. |

### Effect on the status keyword

Writing `LockEventMode` immediately re-evaluates [LockEventStat](LockEventStat.md):

- Setting `LockEventMode=0` sets the status to `0` (legacy mode, ready).
- Setting `LockEventMode=1` sets the status to `1` if the offset has already been computed since power-up, or to the "not initialized" state if it has not — in which case you must run [LockEventInit](LockEventInit.md) before arming.

### When re-initialization is needed (mode 1)

Any configuration change that alters the capture source invalidates a previously learned offset. For example, changing the encoder hardware source clears the "initialized" condition and returns [LockEventStat](LockEventStat.md) to the not-initialized state, so [LockEventInit](LockEventInit.md) must be run again before arming. The firmware can only detect some such changes automatically, so as a rule run [LockEventInit](LockEventInit.md) after any change to the lock/event source configuration and before the capture source starts moving.

## Examples

```text
ALockEventMode=1      ; select the unified lock/event scheme
ALockEventInit        ; learn the firmware/hardware offset (axis stationary)
ALockEn=1             ; now allowed; arm event-based feedback logging
ALockEventMode=0      ; revert to legacy auto-initialize behavior
ALockEventMode        ; read back the configured mode
```

## See also

- [LockEventInit](LockEventInit.md) — runs the manual offset initialization required by mode 1
- [LockEventStat](LockEventStat.md) — reports whether the lock/event subsystem is initialized
- [LockEn](LockEn-AuxLockEn.md) — arms event-based feedback logging
- [LockSrc](LockSrc-AuxLockSrc.md) — selects the trigger source and edge
- [EventOn](../../18-event-generation/EventOn.md) — arms event generation
