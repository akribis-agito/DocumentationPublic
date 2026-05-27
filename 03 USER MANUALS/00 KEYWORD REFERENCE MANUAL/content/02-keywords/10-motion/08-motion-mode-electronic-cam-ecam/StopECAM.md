---
keyword: StopECAM
summary: Exits ECAM motion by shrinking the master range, preserving start/end segments.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 310
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
# StopECAM

Exits ECAM motion by shrinking the master range, preserving start/end segments.

## Overview

`StopECAM` is the command used to exit ECAM motion gracefully. Unlike the immediate [Stop](../04-motion-command/Stop.md) command, the axis does not quit ECAM outright: the master range shrinks, appending the beginning and ending pattern segments to the existing cycle pattern. ECAM motion ends only once the master value leaves this new, shrunken range.

Issuing `StopECAM` while an ECAM move is active sets the [MotionStat](../05-motion-status/MotionStat.md) ECAM-stop bit (bit 7, mask `0x80`), marking the move as "ending its ECAM motion", and records [MotionReason](../05-motion-status/MotionReason.md) = 9 (StopECAM). The bit clears together with the other in-motion bits when the move actually ends. The command has no effect if the axis is not currently in an ECAM (direct or indirect) move.

## How it works

When `StopECAM` is accepted, the controller collapses the all-cycles span of the master range onto the *current* cycle: the start- and end-of-all-cycles boundaries are moved to the current cycle's start and end, while the leading and trailing one-shot segments (the lead-in/lead-out "tails", see [ECAMStart](ECAMStart.md)) are preserved and re-attached just outside the current cycle. If the move was an endless ECAM ([ECAMCycles](ECAMCycles.md) = `2147483647` or `-2147483648`), the endless flag is cleared at the same time, so the master range now has finite ends. The cam pattern then runs to completion as the master continues, and the motion ends when the master reaches either shrunken end (the pre-start or post-end clamp).

For the example below (`ECAMGap > 0` and `ECAMCycles = 3`), the axis receives `StopECAM` while the master position is in the middle of the second cycle. The master range shrinks so that $R > P$ and $S < Q$. ECAM motion then ends only when the master becomes lower than or equal to $R$, or higher than or equal to $S$. Note that the slave position reference at $R$ does not necessarily equal that at $P$, since the cam pattern has shrunk; the same is true for $S$ compared to $Q$.

![image51.png](../../../assets/image51.png)

The following picture shows the same stopping logic for the condition when `ECAMCycles < 0`.

![image52.png](../../../assets/image52.png)

If the user wants to stop ECAM motion immediately, the [Stop](../04-motion-command/Stop.md) command can be used instead, so that the slave position reference is unchanged regardless of the master value.

## Examples

```text
AStopECAM            ; gracefully exit ECAM motion
```

## See also

- [Stop](../04-motion-command/Stop.md) — exit ECAM motion immediately
- [MotionStat](../05-motion-status/MotionStat.md) — sets the ECAM-stop bit (bit 7) while the move is ending
- [MotionReason](../05-motion-status/MotionReason.md) — reports `StopECAM` as reason code 9
- [ECAMStart](ECAMStart.md) — the lead-in/lead-out segments preserved by `StopECAM`
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
