---
keyword: CIStatus
summary: Per-axis array reporting the live Central-i port state, error counters, and last-error details.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 508
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 8
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
# CIStatus

Per-axis array reporting the live Central-i port state, error counters, and last-error details.

## Overview

`CIStatus` is a read-only, axis-related array (7 usable elements, indices 1–7) that reports the live state of the Central-i port on the selected axis: its connection state, per-channel error counters, the time and code of the last error, and the port frequency. It is updated in real time. For a one-value summary across all ports use [CIGlobalStat](CIGlobalStat.md); for the connected device's identity use [CIIdentity](CIIdentity.md).

## Element map

| Index | Field | Meaning |
|-------|-------|---------|
| [1] | State machine | Connection state — see the state table below |
| [2] | Reserved | Always reads `0` |
| [3] | Offline error count | Count of offline (non-cyclic) errors: connection-sequence faults (codes 5–14), a failed offline message send (code 5), and failed background reads from the remote (code 10) |
| [4] | Sync error count | Number of synchronous-message (per-cycle) errors (codes 1–4) |
| [5] | Last error time | Time of the last error (seconds since power-on, cf. [Time](../03-timing/Time.md)) |
| [6] | Last error code | Code of the last error — see the error-code table below |
| [7] | Port frequency | Central-i channel bit-rate in MHz (default `10`) |

### Connection state — `CIStatus[1]`

![CIStatus state machine](cistatus-state-machine.svg)

| Value | State | Meaning |
|-------|-------|---------|
| 0 | Disabled | Port not connected (initial / after [CIDisconnect](CIDisconnect.md)) |
| 1 | In process | Connection is being established (after [CIConnect](CIConnect.md)) |
| 2 | Fault | A link error occurred — see `CIStatus[6]` |
| 3 | Connected | Link is up and exchanging data |

### Last error code — `CIStatus[6]`

| Code | Meaning |
|------|---------|
| 1 | CRC error in the first part of the synchronous message |
| 2 | CRC error in the second part of the synchronous message |
| 3 | Synchronous message not sent |
| 4 | Synchronous error timeout |
| 5 | Offline message error |
| 6 | Unexpected Central-i engine version |
| 7 | Device type not supported (contact Agito) |
| 8 | Offline message timeout |
| 9 | Device differs from the one declared in [CIDeviceType](CIDeviceType.md) |
| 10 | Error reading index from device |
| 11 | Adapter requires `AmpType` = analog |
| 12 | Device read from E² differs from FPGA (contact Agito) |
| 13 | Amplifier requires `AmpType` = built-in PWM |
| 14 | Adapter requires `AmpType` = linear-remote |

### What sets the fault state

A connected port leaves state `3` and enters state `2` (fault) when the per-cycle synchronous reply from the remote is not received in time. The firmware treats this as a lost link: it turns the motor off with controller fault [ConFlt](../../07-status-and-faults/ConFlt.md) = 1043, clears the port's connected bit in [CIGlobalStat](CIGlobalStat.md), removes the motor-on command to the remote, and drives the amplifier output to its mid-scale (zero-torque) value. `CIStatus[4]` (sync error count) is incremented, `CIStatus[5]` records the time, and `CIStatus[6]` is set to `4` (synchronous error timeout).

The other synchronous errors — first-part CRC (`CIStatus[6] = 1`), second-part CRC (`CIStatus[6] = 2`), and message-not-sent (`CIStatus[6] = 3`) — are only counted in `CIStatus[4]` and recorded in `CIStatus[5]`/`[6]`; they do not by themselves fault the axis, and the link keeps running. Synchronous errors in the first few control cycles immediately after a connection are ignored (the firmware suppresses them for the first 4 cycles).

## Examples

```text
ACIStatus[1]                   ; connection state (3 = connected)
ACIStatus[6]                   ; last error code (see table)
ACIStatus[4]                   ; count of synchronous-message errors
```

## Edge cases

- **Motor off / motor on / in motion.** `CIStatus` is read-only and always updated — the keyword reflects the live link regardless of motor state.
- **After [CIDisconnect](CIDisconnect.md).** Every reported element is cleared to `0`: state machine reads `0` (disabled), the three error counts reset, and the last-error fields are zeroed.
- **Power-up.** Initial state is `0` (disabled) on every port; [CIAutoConnect](CIAutoConnect.md) drives a port to `1` (in process) then `3` (connected) during boot. Until the port is connected, [CIIdentity](CIIdentity.md) is not meaningful either.
- **Simulation device.** With [CIDeviceType](CIDeviceType.md) set to a simulation class the port jumps straight to `3` (connected) on [CIConnect](CIConnect.md) — the error counters stay at zero because no real frames are exchanged.
- **Standalone product.** Central-i ports do not exist on standalone hardware; the keyword has no meaningful reading there. v5 firmware is central-i only, so `CIStatus` is always relevant in v5.

## See also

- [CIGlobalStat](CIGlobalStat.md) — system-wide connection summary
- [CIIdentity](CIIdentity.md) — connected device identity
- [CIConnect](CIConnect.md) / [CIDisconnect](CIDisconnect.md) — drive the state machine
- [CIDeviceType](CIDeviceType.md) — expected device (error code 9)
