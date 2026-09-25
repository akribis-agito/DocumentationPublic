# Push Events

**Overview:**

Push events let the controller tell the host that something happened, **unprompted**, instead of the host finding out by polling. Polling costs link bandwidth and CPU on both ends, is up to one poll period late, and can miss an event that starts and ends between two polls. A pushed event carries its own timestamp, taken in the control interrupt when the event was detected.

Events travel on the controller's **push socket**, TCP port **50010**, the same connection that carries user-program `printf` output. The host connects to it; the controller only sends on it. Each packet is marked as push-event data (`SOURCE = 2`), so one reader can separate events from `printf` text.

## Event types

This firmware defines one event type.

| Type | Name | Scope | Sent when | data1 | data2 | data3 | data4, data5 |
|---|---|---|---|---|---|---|---|
| `1` | Profile ended | axis | the in-motion bit of [MotionStat](../../10-motion/05-motion-status/MotionStat.md) falls from 1 to 0 on that axis | position ([Pos](../../10-motion/01-kinematics-status/Pos.md)) | position error ([PosErr](../../10-motion/01-kinematics-status/PosErr.md)) | [MotionReason](../../10-motion/05-motion-status/MotionReason.md) | `0` |

**Profile ended marks the end of the commanded trajectory, not the settled position.** The event is sent when the controller stops commanding the move, whether the move completed, was stopped or aborted, or hit a limit; data3 (`MotionReason`) says which. The axis may still be settling. If you must act only once the axis is physically at its target, wait for [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) instead.

An event is detected on an **edge**, so one move ending produces exactly one record. Position and position error are sent as the controller's internal values (main-encoder counts), not converted to user units.

## Keyword summary

| Keyword | Role |
|---|---|
| [PushEvEnable](PushEvEnable.md) | Master on/off switch. Any 0↔1 change empties the event queue |
| [PushEvSelect](PushEvSelect.md) | Per-axis mask of the event types to send |
| [PushEvSelSys](PushEvSelSys.md) | Mask for controller-wide event types (none defined yet) |
| [PushEvFlushMs](PushEvFlushMs.md) | Longest wait before a queued event is sent |
| [PushEvFillPct](PushEvFillPct.md) | Queue fill level that forces a send |
| [PushEvStat](PushEvStat.md) | Free rows in the event queue (read-only) |
| [PushEvLost](PushEvLost.md) | Events dropped since the last packet was sent |
| [PushEvTotLost](PushEvTotLost.md) | Events dropped since power-on |

## Quick start

```text
APushEvSelect[1]=1   ; axis A: send type 1 (Profile ended)
BPushEvSelect[1]=1   ; axis B: the same
APushEvEnable=1      ; start detecting and sending events
```

Connect the host to port 50010 before or after enabling. `PushEvSelect`, `PushEvSelSys`, `PushEvFlushMs` and `PushEvFillPct` are saved to flash with [Save](../02-operation/Save.md). `PushEvEnable` is not, so push events are always off after power-up until the host enables them.

## How it works

1. **Detection.** Every control cycle, for each axis, the controller checks the selected event types. A detected event is written as one fixed-size record into an event queue of **64 rows**, with a timestamp. Nothing is formatted or sent at this point.
2. **Sending.** The controller's background loop sends the queue when either trigger fires: more than [PushEvFlushMs](PushEvFlushMs.md) has passed since the last successful send, or the queue is at least [PushEvFillPct](PushEvFillPct.md) percent full. It sends at most one packet per background pass, of up to 28 events, oldest first.
3. **Removal.** Events are removed from the queue only once the whole packet has been handed to the controller's TCP stack for sending. If a send is refused, for example because no host is connected, the events stay queued and the controller tries again on a later pass.

Detection does not depend on the connection. With no host connected, events keep being queued. When the queue is full, each **new** event is dropped and counted in [PushEvLost](PushEvLost.md) and [PushEvTotLost](PushEvTotLost.md), so a queue that filled while nobody was reading holds the **first** 64 events, not the last. To start a session with an empty queue, write `PushEvEnable=0` and then `PushEvEnable=1`.

When a push-event packet and a `printf` packet are both ready, the event packet is sent first and `printf` waits for a later pass. In any pass where the controller attempts a push-event send, successful or not, `printf` does not send, so a pass never makes more than one send on the push socket. `PushEvFlushMs` and `PushEvFillPct` apply to events only; `printf` output keeps its own fixed timing.

> **A host that connects to the push port must keep reading it.** Push events use the same blocking send as `printf`. If a host is connected to port 50010 but stops reading, each send attempt can hold the controller's background loop for up to about 6 seconds. The controller makes at most one such attempt per background pass, and retries on later passes until the host reads again or disconnects. While the loop is held, commands from the Ethernet command port and the serial ports wait, including a command to turn push events off; Modbus TCP requests are still serviced. The background watchdog, which fires after 10 seconds without a completed pass, is not expected to trip, but this bound comes from the firmware design and has not been measured on hardware. Do not leave a client connected to port 50010 without reading it.

## Packet format

Most users read events through host software. The layout below is for writing your own client. All multi-byte values are little-endian and packed, with no padding.

```text
"1.2,1."          ASCII envelope: push version 1, SOURCE 2 (push events), data version 1
header   7 bytes
record  50 bytes  × n
'>' CR            terminator (0x3E 0x0D)
```

Header:

| Offset | Field | Type | Meaning |
|---|---|---|---|
| 0 | n | uint8 | Number of records in this packet (1-28) |
| 1 | missed | uint16 | Events dropped since the last successful send; the value of [PushEvLost](PushEvLost.md) when the packet was built, capped at 65535 |
| 3 | freeRows | uint16 | Free queue rows when the packet was built, before these records were removed (see [PushEvStat](PushEvStat.md)) |
| 5 | reserved | uint16 | Always `0` |

Record:

| Offset | Field | Type | Meaning |
|---|---|---|---|
| 0 | type | uint8 | Event type (see *Event types*). Type `0` is never sent |
| 1 | axis | uint8 | Axis the event belongs to (`0` = A, `1` = B, …), or `0xFF` for a controller-wide event |
| 2 | timeSec | uint32 | Whole seconds since power-on (the value of [Time](../03-timing/Time.md)) when the event was detected |
| 6 | timeTick | uint32 | Position within that second, in units of 1/16384 s. It advances in steps of 16 (about 1 ms) |
| 10 | data1 | double | Type-specific |
| 18 | data2 | double | Type-specific |
| 26 | data3 | double | Type-specific |
| 34 | data4 | double | Type-specific |
| 42 | data5 | double | Type-specific |

The DATA length is always `7 + 50 × n` bytes, so a client can check a packet by arithmetic. The event time is `timeSec + timeTick / 16384` seconds. Data fields a type does not use are sent as `0.0`.

A packet can be cut short if a send is interrupted part-way, for example when the connection breaks. A client that finds a stretch of the stream that is not a complete packet should resynchronise: scan for the next envelope (`1.<SOURCE>,<version>.`; `printf` packets with `SOURCE = 1` share the stream) and confirm it with `n` and the `7 + 50 × n` length.

## Product availability

Push events exist on the **AGM800** (Central-i master, v5) only. On every other product, and on AGM800 firmware that predates push events, the eight `PushEv*` keywords are **absent**: reading or writing them by name returns the unknown-keyword error. A host can therefore detect support by trying to read `PushEvEnable`. It can also test [Identity](../01-status/Identity.md)`[62]` bit `0x40`, which is set when the firmware supports push events. `Identity[75]` reports the event-queue depth (64).

Push events are separate from [Event generation](../../18-event-generation/00-overview.md), which produces position-synchronised output pulses in hardware. If you need a signal at the exact moment an axis passes a position, use event generation. Push events report to the host over Ethernet.
