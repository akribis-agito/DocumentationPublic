---
summary: Command that pushes a new motion segment into the CNC FIFO queue A (or B).
---
# CNCAPushType/CNCBPushType

Command that pushes a new motion segment into the CNC FIFO queue A (or B).

## Overview

`CNCAPushType` (and its `CNCBPushType` counterpart on the second CNC engine) opens a new segment in the CNC segment queue (FIFO) for queue A (or B). The single command value packs both the **segment type** (line, arc, helix, delay, etc.) and the list of **involved axes**. After the type is pushed, the segment's parameters are supplied one at a time with [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md); the segment becomes a fully-formed queue entry only once the last required parameter has been pushed. Over Ethernet, [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) can push the type and all parameters in one message.

It is a non-axis command function that can be issued at any time, including during motion, so the host can keep refilling the queue while the controller plays back the segments already in it.

## How it works

### The push → queue → playback → drain pipeline

The CNC pipeline is a producer/consumer queue:

1. The host **pushes** segments: one `CNCAPushType` (which reserves the segment and records how many parameters it expects) followed by exactly that many `CNCAPushParam` writes (or a single `CNCAPushSeg` over Ethernet).
2. Each fully-pushed segment is **queued** in the segment FIFO ([CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)), in push order.
3. The motion engine **plays back** the oldest queued segment, advancing the path one control sample at a time. When a segment ends, the engine takes the next one (skipping over any non-motion segments such as delays or I/O writes until it reaches the next motion segment).
4. As each segment is consumed it **drains** from the queue, freeing its space for new pushes.

If the engine reaches the point where it needs a new segment but the queue holds no fully-formed motion segment — either because it is empty, or because the host is still mid-way through pushing the last segment's parameters — the motion ends (**underrun**). To avoid an underrun, keep pushing so that at least one complete segment is always queued ahead of the one being played. Monitor free space with [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md).

### Command value encoding

The command value is a 32-bit field. The top byte selects the segment type; the lower 24 bits select up to six involved axes, four bits each, in order:

| Bits | Field | Meaning |
|----|----|----|
| 31–24 | Segment type | One of the values in the table below. |
| 23–20 | Involved axis 1 | Axis index: `0` = A, `1` = B, `2` = C, … `14` = the 15th axis. `15` = no axis in this slot. |
| 19–16 | Involved axis 2 | As above. |
| 15–12 | Involved axis 3 | As above. |
| 11–8 | Involved axis 4 | As above. |
| 7–4 | Involved axis 5 | As above. |
| 3–0 | Involved axis 6 | As above. |

A slot value of `15` means "no axis here", so the number of involved axes is the count of slots holding a value below 15.

### Segment types

The number of [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) values a segment needs depends on its type and, for the variable types, on how many axes are involved.

| Type | Segment | Involved axes | Parameters required |
|----|----|----|----|
| 1 | Linear move | 1–6 | `2 + (number of involved axes)`: one target position per axis, then path speed and end speed. |
| 2 | Arc | exactly 2 | 10: target 1, target 2, centre 1, centre 2, direction, speed, end speed, extra full circles, plus 2 internal values (push 0). |
| 3 | Helix | 3–6 | `6 + (number of involved axes)`: per-axis targets, centre 1, centre 2, direction, pitch, speed, end speed. |
| 4 | Delay | 0 | 1: delay time in milliseconds. |
| 5 | Set vector dynamics | 0 | 4: speed percentage, acceleration, deceleration, jerk. |
| 6 | Set corner parameters | 0 | 6: corner type, corner radius method, radius/error, axis acceleration, minimum corner angle, axis-acceleration limit type. |
| 7 | Set initial positions | 1–6 | one start position per involved axis. Allowed **only** as the first segment of an empty queue. |
| 8 | Write digital output port | 0 | 2: axis selection, value to write. |
| 9 | Write to array | 0 | 4: array selection, axis selection, index, value. |
| 10 | Relative / absolute targets | 0 | 1: `0` = relative, `1` = absolute. |
| 11 | Coordinate offsets | 1–6 | one offset per involved axis. |
| 12 | Wait on array value | 0 | 5: array selection, axis selection, index, trigger type, trigger value. |
| 13 | Assign positions | 1–6 | one position per involved axis. |
| 14 | Automatic corner | exactly 2 | 10 internal values (push 0); the controller fills in the calculated corner. |
| 15 | Set per-axis maximum velocity jump | 1–6 | `1 + (number of involved axes)`: a maximum velocity jump per axis, then the velocity-jump mode. |
| 16 | Set per-axis maximum acceleration | 1–6 | one maximum acceleration per involved axis. |
| 17 | Write multiple array values | 0 | 7: array selection, axis selection, index, then four values. |
| 18 | Write multiple array values then wait | 0 | 10: as type 17, plus trigger index, trigger type, trigger value. |
| 19 | Modify CNC position filter | 0 | 6: filter enable, filter type, then four filter parameters. |
| 20 | 3D arc | exactly 3 | 20: three targets, three centre coordinates, three additional, direction, speed, end speed, extra full circles, plus internal values (push 0). Not available on standalone drives. |
| 21 | Wait on input | 0 | 6: input selection, axis selection, analog-input index, digital-input mask, trigger type, trigger value. |
| 22–25 | Spatial-events setup / table / fixed-gap | 0 | type-specific; configure position-triggered output events along the path. |

Segment type ordering rules: a "set initial positions" segment (type 7) is accepted only as the first push into an empty queue; if it is omitted, the first **motion** segment must be a linear move (type 1), and an automatic corner (type 14) cannot be the first or second motion segment.

## Examples

```text
ACNCAPushType=value  ; open a new segment of the encoded type/axes in FIFO A
```

For a linear move on axes A and B (type 1, axis-1 = 0, axis-2 = 1, remaining slots = 15), the value is `0x0101FFFF` followed by four `CNCAPushParam` writes (target A, target B, speed, end speed).

### Walk-through: queue and run a two-line move on queue A

Push two consecutive linear segments on axes A and B, then start the motion. The second segment has `EndSpeed = 0` so the path stops on the last segment without an underrun. The motion uses an A-B linear move (type 1, two involved axes), so each `PushType` is followed by exactly `2 + 2 = 4` `PushParam` writes: target A, target B, path speed, end speed.

```text
; --- 1) Make sure the queue is empty before staging a fresh path ---
ACNCAClear                    ; clear any leftovers from the previous run

; --- 2) Push segment 1: A -> 10000, B -> 5000, path 4000, end 4000 ---
ACNCAPushType=0x0101FFFF      ; type 1 = linear, axes A (0) and B (1)
ACNCAPushParam=10000          ; target A
ACNCAPushParam=5000           ; target B
ACNCAPushParam=4000           ; path speed
ACNCAPushParam=4000           ; end speed (still moving into segment 2)

; --- 3) Push segment 2: A -> 20000, B -> 5000, path 4000, end 0 (stop) ---
ACNCAPushType=0x0101FFFF
ACNCAPushParam=20000
ACNCAPushParam=5000
ACNCAPushParam=4000
ACNCAPushParam=0              ; end speed 0 -> path stops on this segment

; --- 4) Confirm both segments are fully formed before Begin ---
ACNCAStatus[5]                ; 0 = last pushed segment is closed (ready)

; --- 5) Arm the CNC engine and watch the queue drain ---
AMotionMode=11                ; CNCA motion (CNCB = 17)
ABegin                        ; engine starts playing the oldest queued segment
ACNCAStatus[10]               ; CNC motion bit-field (bit 0 set while moving)
ACNCAStatus[7]                ; free words -- grows as each segment drains
ACNCAStatus[6]                ; queue position of the segment currently playing
```

Keep pushing while `Begin` runs to chain longer paths -- the engine underruns if it needs a new segment but the queue holds no closed one. Use [StopCNCA](StopCNCA.md) to decelerate the path cleanly before the queue empties; use [CNCAClear](CNCAClear-CNCBClear.md) to flush pending segments after a stop.

## See also

- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — supply the segment parameters
- [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) — push a full segment in one Ethernet message
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — queue depth, free space and motion state
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — clear all pending segments
