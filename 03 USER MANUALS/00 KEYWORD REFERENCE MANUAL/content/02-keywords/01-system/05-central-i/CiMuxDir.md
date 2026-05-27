---
keyword: CiMuxDir
summary: Sets the direction of the Central-i multiplexer (which port the shared bus routes to).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 551
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CiMuxDir

Sets the direction of the Central-i multiplexer (which port the shared bus routes to).

## Overview

`CiMuxDir` sets the **direction** of the Central-i I/O multiplexer, one bit per port. The Central-i network carries a multiplexed I/O signal that can flow either from the master out to a remote unit or from a remote back to the master; `CiMuxDir` chooses which way that signal travels on each port. Together with [CiMuxSel](CiMuxSel.md), which chooses *which* signal is routed, it forms the complete multiplexer configuration so one master can share a routed I/O signal across its ports. It is a non-axis parameter saved to flash. (This feature is implemented on the master hardware that supports it.)

## How it works

`CiMuxDir` is a **bit field** — bit `n` is the direction for port `n`. When the parameter is written, the firmware:

1. writes the per-port select value [CiMuxSel](CiMuxSel.md)`[1]` into each master port's multiplexer register;
2. for every *connected, non-simulated* port, sends an offline (mailbox) message to the remote unit carrying that port's direction bit together with the remote-side select [CiMuxSel](CiMuxSel.md)`[2]` (the two share one 32-bit register in the remote). The direction sense is **inverted** at the remote side, so that one end drives and the other receives;
3. writes `CiMuxDir` to the master's own multiplexer-direction register, which sets the master-side direction for all ports.

Because the master and remote directions are configured in separate steps, there can be a brief moment where both ends drive the line; the hardware transceivers tolerate this short overlap until the master-side direction is set.

The 12-bit range allows a direction bit for each port the hardware provides.

## Examples

```text
ACiMuxDir=1          ; route port 0 in one direction; other ports the other way
ACiMuxDir            ; read the current per-port direction bit field
```

## See also

- [CiMuxSel](CiMuxSel.md) — which signal is routed (master-side and remote-side select)
- [CIConnect](CIConnect.md) — a port must be connected for its remote direction to be sent
- [CIGlobalStat](CIGlobalStat.md) — which ports are connected
