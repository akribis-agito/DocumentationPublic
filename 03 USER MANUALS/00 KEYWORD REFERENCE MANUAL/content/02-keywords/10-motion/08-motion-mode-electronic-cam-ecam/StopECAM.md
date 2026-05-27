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

`StopECAM` is the command used to exit ECAM motion gracefully. Unlike the immediate [Stop](../04-motion-command/Stop.md) command, the axis does not quit ECAM outright: the master range shrinks, appending the beginning and ending pattern segments to the existing cycle pattern. ECAM motion ends only once the master value leaves this new, shrunken range. Stopping via `StopECAM` is also reported by [MotionReason](../05-motion-status/MotionReason.md) (reason code 9).

## How it works

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
- [MotionReason](../05-motion-status/MotionReason.md) — reports `StopECAM` as reason code 9
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
