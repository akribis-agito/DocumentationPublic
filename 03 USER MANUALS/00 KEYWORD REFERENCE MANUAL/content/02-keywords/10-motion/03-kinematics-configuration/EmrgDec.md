---
keyword: EmrgDec
summary: Emergency deceleration rate applied on Abort or fault, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 140
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# EmrgDec

Emergency deceleration rate applied on `Abort` or fault, in user units per second squared.

## Overview

`EmrgDec` is the deceleration rate the profiler substitutes for [Decel](Decel.md) when a move is halted by an emergency or limit condition rather than by a normal [Stop](../04-motion-command/Stop.md). It is usually set higher than `Decel` so the axis comes to rest as quickly as it safely can. It is read/write, axis-scoped, saved to flash, and can be changed at any time, including during motion.

## How it works

`EmrgDec` is not used during a normal move. The profiler swaps it in for the deceleration rate only when the [MotionReason](../05-motion-status/MotionReason.md) is one of the emergency/limit cases:

| Stop condition ([MotionReason](../05-motion-status/MotionReason.md) value) | Stop rate used |
|---------------|----------------|
| Reverse / forward limit switch (`MotionReason` = 4 / 5) | `EmrgDec × AccelFact` |
| Reverse / forward software position limit (`MotionReason` = 6 / 7) | `EmrgDec × AccelFact` |
| Controlled stop by input signal (`MotionReason` = 28) | `EmrgDec × AccelFact` |
| Normal [Stop](../04-motion-command/Stop.md) / end of move (`MotionReason` = 1 / 0) | `Decel × AccelFact` |

When `EmrgDec` is selected, the profiler also forces `JerkMode` internally to OFF for that stop, so the emergency deceleration is applied **without jerk smoothing** — the priority is to stop quickly, not smoothly.

Like the other rates, `EmrgDec` is multiplied by [AccelFact](AccelFact.md) each cycle, and the deceleration-distance lookahead then uses this scaled value so the axis still decelerates to rest at the limit/target rather than overshooting.

### Relationship to Abort

An [Abort](../04-motion-command/Abort.md) halts motion immediately. Note that the `EmrgDec`-rate path is driven by the [MotionReason](../05-motion-status/MotionReason.md) conditions above (limit switches = 4 / 5, software limits = 6 / 7, and controlled stop by input = 28); a normal `Stop` ([MotionReason](../05-motion-status/MotionReason.md) = 1) uses `Decel`. Set `EmrgDec ≥ Decel` so that any of these emergency stops is at least as aggressive as a normal one.

## Examples

```text
AEmrgDec=1000000     ; emergency deceleration (user units/s^2)
AEmrgDec             ; read current value
```

## Changes between versions

In **v4** `EmrgDec` is a 32-bit integer; in **v5 (central-i)** it is a single-precision float. The substitution logic and `AccelFact` scaling are unchanged. **v5 is central-i only.**

## See also

- [Decel](Decel.md) — normal deceleration rate (used by `Stop`)
- [Accel](Accel.md) — acceleration rate
- [AccelFact](AccelFact.md) — integer multiplier also applied to `EmrgDec`
- [Abort](../04-motion-command/Abort.md) — immediate stop command
- [Stop](../04-motion-command/Stop.md) — controlled stop (uses `Decel`, not `EmrgDec`)
- [MotionReason](../05-motion-status/MotionReason.md) — reason codes (4 / 5 / 6 / 7 / 28) that select the `EmrgDec` rate
