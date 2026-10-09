---
keyword: CommitMotion
summary: Command that commits a staged on-the-fly change to a running sine point-to-point move.
availability:
  standalone: []
  central-i:
  - v5
can_code: 844
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-10'
doc_revision: '2026.10'
---
# CommitMotion

Command that commits a staged on-the-fly change to a running sine point-to-point move.

## Overview

`CommitMotion` applies a change to a sine point-to-point move **while that move is already running**, without stopping and re-issuing it. You stage the new move parameters with the axis still in motion, then call `CommitMotion` to ask the controller to recalculate the profile and transition to the new target seamlessly. It is a non-axis command with an axis-mask value: write `ACommitMotion=1` for axis A, `ACommitMotion=2` for B, or `ACommitMotion=3` for A and B together. Bit 0 selects A, bit 1 selects B, and subsequent bits select subsequent axes.

It is only meaningful in the sine point-to-point modes ([MotionMode](../02-motion-configuration/MotionMode.md) = 20, sine PTP, and 21, sine PTP repetitive) while the axis is in motion. In any other mode, or when the axis is not in motion, the command is rejected.

Available on central-i (v5). Command text still requires the communication prefix: use `ACommitMotion=...`. The mask, rather than the prefix, selects the axes.

The six-axis AGM800-EC configuration accepts only axes A–F in the mask (bits 0–5). A mask containing an unsupported axis returns error 170 before any selected axis is committed, including mixed masks such as 65 (A and G). A supported mask must still pass the motion-mode checks below. A zero mask is outside the command range. See [Identity](../../01-system/01-status/Identity.md) field 23 for the servo-axis count.

## How it works

When `CommitMotion` is issued the controller hands the staged change to the profiler and waits for it to decide whether the change can be applied at the current point in the move:

1. **Eligibility check.** The command is rejected immediately unless the axis is in motion ([MotionStat](../05-motion-status/MotionStat.md) bit 0 set) **and** in a sine point-to-point mode ([MotionMode](../02-motion-configuration/MotionMode.md) = 20 or 21). Otherwise it returns a "must be a valid motion mode" error.
2. **Profiler evaluation.** The profiler examines the running move and either accepts the change (there is enough of the move left to retarget cleanly) or rejects it (for example the move is too close to its end to recalculate in time). Each handshake step has a one-second timeout; a timeout is reported as an error.
3. **Recalculation and transition.** If accepted, the new sine profile is computed and the profiler transitions to it on the fly. The controller can **acknowledge the commit in advance of the actual profile transition** — the acknowledgement tells you the change has been accepted and will be applied at the appropriate point in the move, rather than waiting for the transition itself to complete. This keeps the commit responsive and lets a repetitive move continue without interruption.

### The recalculation window

The new profile is not computed instantaneously; the controller reserves a **fixed window of 16 control-loop cycles** (1&nbsp;ms at the default control rate) for the background recalculation, and the accept/reject decision in step 2 is made against that fixed window. Because the window is a constant, it is the **same regardless of move length** — only how much of the running move remains in front of it matters. Two distinct errors come out of this:

- **Window does not fit (error 387).** Raised up front at the initial check when the time left before the move would otherwise end is shorter than the 16-cycle window, so the recalculation could not finish in time even if it started immediately. For a repetitive move ([MotionMode](../02-motion-configuration/MotionMode.md) = 21) the remaining-time budget also includes the inter-repeat dwell ([RptWait](../02-motion-configuration/RptWait.md)), so a commit issued late in a repeat can still fit if enough dwell follows.
- **Recalculation did not finish in the window (error 388).** Raised when the 16-cycle countdown reaches zero before the background recalculation has completed. In this case the commit is abandoned and the original move continues unchanged.

Both 387 and 388 apply to sine PTP (mode 20) and sine PTP repetitive (mode 21).

If any step fails or times out, `CommitMotion` returns an error and the move continues unchanged on its original profile.

## Examples

Retarget a running sine PTP move without stopping it:

```text
AMotionMode=20       ; sine point-to-point
AAbsTrgt=100000      ; initial target
ABegin               ; start the sine PTP move
                     ; ... while it is running, stage a new target ...
AAbsTrgt=150000      ; new target
ACommitMotion=1       ; commit axis A; OK = accepted, error = rejected/timed out
```

### Edge cases

- **Not in motion** — rejected; there is no running move to commit a change to.
- **Wrong motion mode** — rejected unless the active mode is sine PTP (20) or sine PTP repetitive (21).
- **Too late in the move** — the profiler may reject the change when there is not enough of the move left to recalculate and transition (error 387, the 16-cycle window does not fit in the time remaining); the original move finishes unchanged.
- **Recalculation overran** — if the background recalculation does not complete within the 16-cycle window the commit is abandoned (error 388) and the original move continues unchanged.
- **Timeout** — if the profiler does not respond within about one second at any handshake step, the command returns an error.
- **Axis mask** — write the mask to execute the command; it is not a stored setting.
- **Platform** — v5 central-i only.

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects the sine point-to-point modes (20 / 21) this command operates on
- [Begin](Begin.md) — starts the move that `CommitMotion` later retargets
- [MotionStat](../05-motion-status/MotionStat.md) — in-motion bit that must be set for the command to be accepted
- [RptWait](../02-motion-configuration/RptWait.md) — inter-repeat dwell that extends the commit budget for a repetitive (mode 21) move
- [Stop](Stop.md) — controlled stop, the alternative when a change cannot be committed on the fly
