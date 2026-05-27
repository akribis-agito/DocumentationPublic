---
keyword: HomeStat
summary: Read-only bit-field reporting the homing status of the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 111
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeStat

Read-only state of the home digital input for the axis.

## Overview

Despite its name, `HomeStat` is *not* a homing-process status word. It reports the present logic state of the discrete input that has been assigned the **Home** function: `1` when the home input is asserted, `0` when it is not. The homing *process* is tracked separately by [HomingStat](HomingStat.md) (per-step status and error codes) and [HomingStep](HomingStep.md) (the current step).

`HomeStat` is updated every time the home input is sampled. A transition either way (0→1 or 1→0) is what the homing engine and [StopOnHome](StopOnHome.md) react to — see "How it works". It is an axis-scoped, read-only variable that is not saved to flash.

## How it works

When an input is configured with the Home function, the controller samples it and maintains `HomeStat` as the debounced level of that input. On any change of level it raises an internal one-cycle "home change" pulse; this pulse is what:

- the [StopOnHome](StopOnHome.md) mechanism uses to stop a move, and
- the "Jog until a change in the Home discrete input" homing step (instruction `11` in [HomingDef](HomingDef.md)) waits for to complete.

The step `11` logic also reads `HomeStat` at the start of the move to decide direction: if `HomeStat` is `0` the configured jog speed is used as-is; if `HomeStat` is `1` the direction is inverted, so the axis always moves toward the edge of the home flag.

| HomeStat | Meaning |
|---|---|
| 0 | The home input is not asserted. |
| 1 | The home input is asserted. |

If no input is assigned the Home function, `HomeStat` stays at its default and never changes.

## Examples

```text
AHomeStat           ; 0 = home input not asserted, 1 = asserted
```

## See also

- [StopOnHome](StopOnHome.md) — stops a move on a change of this input
- [HomingStat](HomingStat.md) — the actual homing-process status and error codes
- [HomingStep](HomingStep.md) — the current homing step
- [HomingDef](HomingDef.md) — step 11 jogs until this input changes
- [HomingOn](HomingOn.md) — starts the homing process
