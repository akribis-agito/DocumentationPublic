---
keyword: LockEventInit
summary: "Initializes the unified lock/event configuration by learning the firmware-to-hardware capture offset (mode 1 only)."
availability:
  standalone: []
  central-i:
  - v5
can_code: 832
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LockEventInit

Initializes the unified lock/event configuration by learning the firmware-to-hardware capture offset; meaningful only when [LockEventMode](LockEventMode.md) = 1.

> Available from v5 (central-i) only.

## Overview

`LockEventInit` is a command keyword used by the unified lock/event scheme ([LockEventMode](LockEventMode.md) = 1). When you run it, the controller samples the internal hardware capture counter and computes the offset between it and the value you read back in the controller (such as `Pos`, `AuxPos`, or `VEncValue`, depending on the configured capture source). That offset is what lets captured positions be reported in the same units and reference you use elsewhere.

In mode 1 this step is your responsibility: you run `LockEventInit` once the lock/event source is fully configured and the axis is stationary, before arming [LockEn](LockEn-AuxLockEn.md) or [EventOn](../../18-event-generation/EventOn.md). In the legacy mode ([LockEventMode](LockEventMode.md) = 0) the controller learns this offset automatically when the feature is armed, so the command is not used there.

## How it works

When you run `LockEventInit` with [LockEventMode](LockEventMode.md) = 1 and an applicable capture source configured, the controller:

1. Reads the current hardware capture counter.
2. Computes the offset against the matching firmware-reported position for the configured source (main-encoder position, auxiliary-encoder position, or virtual-encoder value).
3. Marks the lock/event subsystem as initialized and sets [LockEventStat](LockEventStat.md) to `1` (ready).

Because the offset is sampled at the moment you run the command, the capture source must be stationary while you run it; otherwise the learned offset will not match later captures.

### Behavioral notes

- **Mode 1 only.** Running `LockEventInit` while [LockEventMode](LockEventMode.md) = 0 (legacy mode) has no effect and is rejected with an error, since the offset is already learned automatically in that mode. Use it only after selecting mode 1.
- **Required before arming in mode 1.** With [LockEventMode](LockEventMode.md) = 1, attempting to arm [LockEn](LockEn-AuxLockEn.md) = 1 or [EventOn](../../18-event-generation/EventOn.md) = 1 before `LockEventInit` has been run is rejected; the controller returns an error indicating the offset has not been initialized. Run `LockEventInit` first, then arm.
- **Re-run after configuration changes.** Any change to the capture source after initialization invalidates the learned offset. Some such changes (for example changing the encoder hardware source) reset [LockEventStat](LockEventStat.md) to the not-initialized state automatically, but the controller cannot detect every case. As a rule, run `LockEventInit` again after any change to the lock/event source configuration and before the source starts moving.

## Examples

```text
ALockEventMode=1      ; select the unified lock/event scheme
ALockSrc=16           ; configure the capture source/edge (central-i main encoder index)
                      ; ... make sure the axis is stationary ...
ALockEventInit        ; learn the firmware/hardware offset
ALockEventStat        ; should read 1 (initialized and ready)
ALockEn=1             ; now allowed; arm event-based feedback logging
```

## See also

- [LockEventMode](LockEventMode.md) — selects legacy vs. unified mode (this command applies in mode 1)
- [LockEventStat](LockEventStat.md) — reports whether initialization has been done
- [LockEn](LockEn-AuxLockEn.md) — arms event-based feedback logging
- [LockSrc](LockSrc-AuxLockSrc.md) — selects the trigger source and edge
- [EventOn](../../18-event-generation/EventOn.md) — arms event generation
