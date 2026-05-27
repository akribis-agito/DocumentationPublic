---
keyword: CILinkConfig
summary: Per-axis array configuring the physical and protocol parameters of a Central-i port.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 539
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CILinkConfig

Per-axis array configuring the physical and protocol parameters of a Central-i port.

## Overview

`CILinkConfig` is an axis-related array that sets the **frame-timing** of a Central-i port: the points within each communication cycle at which the master sends to the remote and receives back, for both the cyclic *synchronous* traffic and the *offline* (mailbox) traffic. The values are clock counts measured from the start of the cycle. They are saved to flash and written into the port's hardware timing registers when [CIConnect](CIConnect.md) (or [CIAutoConnect](CIAutoConnect.md)) initialises the link, so configure them before connecting. Index `[0]` is unused; the six timing elements run from `[1]` to `[6]`.

## How it works

Each communication cycle has a fixed period. Within it, the master must open its transmit window, then turn the line around to receive the remote's reply, for the synchronous (per-cycle) channel and again for the offline (mailbox) channel. The six elements are the clock offsets for those windows:

| Index | Element | Meaning |
|-------|---------|---------|
| [1] | Sync send-start | When the master starts sending the synchronous (master-to-remote) frame |
| [2] | Sync receive-start | When the master opens its window to receive the remote-to-master sync frame |
| [3] | Sync receive-end | When the master closes the sync receive window (line turnaround) |
| [4] | Offline send-start | When the master starts sending an offline (mailbox) message |
| [5] | Offline receive-start | When the master opens its window to receive the offline reply |
| [6] | Offline receive-end | When the master closes the offline receive window |

An element left at `0` is replaced at connect time by the firmware's built-in default for that timing, so a port can be brought up with `CILinkConfig` all zeros and still use sensible defaults. The values must be ordered consistently within the cycle (send before receive-start, receive-start before receive-end); incorrect timing shows up as synchronous or offline errors in [CIStatus](CIStatus.md).

The channel bit-rate itself is set by the firmware to its default at connect (it is not one of these elements); these elements tune *when* in the cycle each transfer happens, which depends on cable length and the remote device.

## Examples

```text
ACILinkConfig[1]    ; read the sync send-start time for this port
ACILinkConfig[4]    ; read the offline send-start time for this port
```

## See also

- [CIDeviceType](CIDeviceType.md) — expected device class for the port
- [CIConnect](CIConnect.md) — applies these timings when the link comes up
- [CIStatus](CIStatus.md) — sync/offline errors caused by bad timing
- [CISyncDef](CISyncDef.md) — synchronous data definition
