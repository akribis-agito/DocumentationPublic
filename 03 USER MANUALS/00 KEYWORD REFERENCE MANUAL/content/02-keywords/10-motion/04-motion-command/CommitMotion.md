---
keyword: CommitMotion
summary: "Command that commits a staged on-the-fly change to a running sine point-to-point move."
availability:
  standalone: []
  central-i:
  - v5
can_code: 844
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
# CommitMotion

Command that commits a staged on-the-fly change to a running sine point-to-point move.

## Overview

`CommitMotion` applies a change to a sine point-to-point move **while that move is already running**, without stopping and re-issuing it. You stage the new move parameters with the axis still in motion, then call `CommitMotion` to ask the controller to recalculate the profile and transition to the new target seamlessly. It is an axis-related command function and carries no value.

It is only meaningful in the sine point-to-point modes ([MotionMode](../02-motion-configuration/MotionMode.md) = 20, sine PTP, and 21, sine PTP repetitive) while the axis is in motion. In any other mode, or when the axis is not in motion, the command is rejected.

Available on central-i (v5).

## How it works

When `CommitMotion` is issued the controller hands the staged change to the profiler and waits for it to decide whether the change can be applied at the current point in the move:

1. **Eligibility check.** The command is rejected immediately unless the axis is in motion ([MotionStat](../05-motion-status/MotionStat.md) bit 0 set) **and** in a sine point-to-point mode ([MotionMode](../02-motion-configuration/MotionMode.md) = 20 or 21). Otherwise it returns a "must be a valid motion mode" error.
2. **Profiler evaluation.** The profiler examines the running move and either accepts the change (there is enough of the move left to retarget cleanly) or rejects it (for example the move is too close to its end to recalculate in time). Each handshake step has a one-second timeout; a timeout is reported as an error.
3. **Recalculation and transition.** If accepted, the new sine profile is computed and the profiler transitions to it on the fly. The controller can **acknowledge the commit in advance of the actual profile transition** — the acknowledgement tells you the change has been accepted and will be applied at the appropriate point in the move, rather than waiting for the transition itself to complete. This keeps the commit responsive and lets a repetitive move continue without interruption.

If any step fails or times out, `CommitMotion` returns an error and the move continues unchanged on its original profile.

## Examples

Retarget a running sine PTP move without stopping it:

```text
AMotionMode=20       ; sine point-to-point
AAbsTrgt=100000      ; initial target
ABegin               ; start the sine PTP move
                     ; ... while it is running, stage a new target ...
AAbsTrgt=150000      ; new target
ACommitMotion        ; apply the new target on the fly; OK = accepted, error = rejected/timed out
```

### Edge cases

- **Not in motion** — rejected; there is no running move to commit a change to.
- **Wrong motion mode** — rejected unless the active mode is sine PTP (20) or sine PTP repetitive (21).
- **Too late in the move** — the profiler may reject the change when there is not enough of the move left to recalculate and transition; the original move finishes unchanged.
- **Timeout** — if the profiler does not respond within about one second at any handshake step, the command returns an error.
- **Read-only / function** — `CommitMotion` is a command (issue it to trigger it); it carries no value to write.
- **Platform** — v5 central-i only.

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects the sine point-to-point modes (20 / 21) this command operates on
- [Begin](Begin.md) — starts the move that `CommitMotion` later retargets
- [MotionStat](../05-motion-status/MotionStat.md) — in-motion bit that must be set for the command to be accepted
- [Stop](Stop.md) — controlled stop, the alternative when a change cannot be committed on the fly
