---
keyword: BuffStatus
summary: Read-only array reporting the state of the spline buffer motion mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 549
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 9
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
# BuffStatus

Read-only array reporting the state of the spline buffer motion mode.

## Overview

`BuffStatus` is a read-only, eight-element array (indices `[1]` to `[8]`) that describes both the **configuration** of a spline-buffer group and its **live playback state**. The configuration elements are filled when [BuffCalc](BuffCalc.md) runs; the playback elements advance every control cycle while the move is in progress. The same array is maintained on every member axis. It is not saved to flash.

## How it works

### Element layout

| Index | Meaning |
|---|---|
| [1] | Group membership, packed. The low 8 bits hold the **primary axis number**; the upper bits hold the **member-axis set** as a bitmask (bit *n* set means axis *n* is a member). |
| [2] | Peak speed of the computed trajectory for this axis, in counts per second. |
| [3] | Peak acceleration of the computed trajectory for this axis, in counts per second squared. |
| [4] | Cycle currently being played (1 = first cycle). Increments at each cycle boundary; the move ends once it would exceed [BuffCycles](BuffCycles.md). |
| [5] | Index of the point currently being output within the cycle (1 = first point). Advances by one each control cycle and wraps to 1 at the cycle boundary. |
| [6] | Index of the last point in the cycle — equal to the last [BuffTime](BuffTime.md) time stamp, i.e. the number of interpolated samples in one cycle. |
| [7] | First member axis of the group (the axis the controller uses to drive index/cycle bookkeeping). |
| [8] | Cycle-boundary flag: 1 on the first sample of a new cycle (other than the very first), 0 otherwise. Used internally to capture the per-cycle origin and to act on a pending [StopBuff](../04-motion-command/StopBuff.md). |

The primary axis in `[1]` is what [StopBuff](../04-motion-command/StopBuff.md) targets, and `[2]`/`[3]` let you check the move's peak speed and acceleration against the drive's limits before running it.

### How the buffer fills and drains

[BuffCalc](BuffCalc.md) **fills** the internal store with one interpolated point per servo sample, from the start of the cycle up to the last [BuffTime](BuffTime.md) time stamp — element `[6]` is the count of those points. During motion the profiler **drains** the store one point per control cycle: each cycle it advances the in-cycle index `[5]`, reads that point, adds the captured start position, and outputs it as [PosRef](../01-kinematics-status/PosRef.md). When `[5]` passes `[6]` it wraps to 1 and the cycle counter `[4]` increments, replaying the same stored points for the next cycle.

<svg xmlns="http://www.w3.org/2000/svg" width="560" height="200" font-family="sans-serif" font-size="12">
  <text x="10" y="20" font-weight="bold">Spline buffer: fill once, drain every cycle</text>
  <text x="10" y="48">BuffCalc fills the store with one point per sample (index 1 .. [6]):</text>
  <rect x="20" y="58" width="420" height="24" fill="none" stroke="#333"/>
  <line x1="62" y1="58" x2="62" y2="82" stroke="#bbb"/>
  <line x1="104" y1="58" x2="104" y2="82" stroke="#bbb"/>
  <line x1="146" y1="58" x2="146" y2="82" stroke="#bbb"/>
  <line x1="356" y1="58" x2="356" y2="82" stroke="#bbb"/>
  <line x1="398" y1="58" x2="398" y2="82" stroke="#bbb"/>
  <text x="30" y="75">1</text>
  <text x="72" y="75">2</text>
  <text x="114" y="75">3</text>
  <text x="240" y="75">. . .</text>
  <text x="406" y="75">[6]</text>
  <text x="10" y="118">Profiler drains one point per control cycle to PosRef:</text>
  <rect x="120" y="130" width="42" height="24" fill="#cfe3ff" stroke="#333"/>
  <text x="132" y="147">[5]</text>
  <line x1="162" y1="142" x2="300" y2="142" stroke="#333" marker-end="url(#a)"/>
  <text x="310" y="146">PosRef (+ start position)</text>
  <path d="M 141 130 q 40 -22 40 0" fill="none" stroke="#333" marker-end="url(#a)"/>
  <text x="186" y="120">index advances each cycle</text>
  <text x="20" y="184">At index [5] &gt; [6]: wrap [5] to 1, increment cycle [4]; end when [4] &gt; BuffCycles.</text>
  <defs>
    <marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
</svg>

### End of motion

The move ends when cycle `[4]` exceeds [BuffCycles](BuffCycles.md), or earlier at the next cycle boundary if [StopBuff](../04-motion-command/StopBuff.md) was requested. In the spline-buffer mode the controller streams pre-computed points directly, so there is no separate deceleration ramp — the trajectory is already shaped by its edge conditions ([BuffEdgeMode](BuffEdgeMode.md)). While playing, the output is still clamped to the software position limits, so a buffered point beyond a limit is held at the limit.

## Examples

```text
ABuffStatus[1]      ; packed: low byte = primary axis, upper bits = member set
ABuffStatus[4]      ; cycle currently playing
ABuffStatus[5]      ; point index within the current cycle
ABuffStatus[6]      ; points per cycle (= last BuffTime value)
```

## See also

- [BuffCalc](BuffCalc.md) — fills the internal store and writes the configuration elements
- [BuffCycles](BuffCycles.md) — repeat count compared against cycle index [4]
- [BuffTime](BuffTime.md) — last time stamp equals the points-per-cycle in [6]
- [PosRef](../01-kinematics-status/PosRef.md) — reference fed by the drained points
- [StopBuff](../04-motion-command/StopBuff.md) — ends playback at the next cycle boundary (targets the primary in [1])
