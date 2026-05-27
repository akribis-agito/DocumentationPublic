---
keyword: CiMuxSel
summary: Per-axis array selecting which physical port is routed through the Central-i multiplexer.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 552
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CiMuxSel

Per-axis array selecting which physical port is routed through the Central-i multiplexer.

## Overview

`CiMuxSel` is a per-axis (per-port) array that chooses **which signal** the Central-i I/O multiplexer routes on that port — independently at the master end and at the remote end. It is the "what" of the multiplexer; [CiMuxDir](CiMuxDir.md) is the "which way". Together they let one master share a routed I/O signal across its ports. The array is saved to flash. Index `[0]` is unused; the two selection elements are `[1]` and `[2]`.

## How it works

| Index | Element | Meaning |
|-------|---------|---------|
| [1] | Master-side select | Written into this port's multiplexer register in the master FPGA |
| [2] | Remote-side select | Sent to the remote unit (combined with the [CiMuxDir](CiMuxDir.md) direction bit) and written into the remote's multiplexer register |

When [CiMuxDir](CiMuxDir.md) is written (it drives the multiplexer update), the firmware writes `CiMuxSel[1]` for every port into the master's port multiplexer registers, and for every *connected, non-simulated* port sends `CiMuxSel[2]` to the remote in the same offline message that carries the direction bit (the remote stores select and direction in a single 32-bit register). Writing `CiMuxSel` alone updates the stored values; the configuration is pushed to hardware when [CiMuxDir](CiMuxDir.md) is set.

## Examples

```text
ACiMuxSel[1]        ; read the master-side multiplexer select for this port
ACiMuxSel[2]        ; read the remote-side multiplexer select for this port
```

## See also

- [CiMuxDir](CiMuxDir.md) — multiplexer direction (triggers the hardware update)
- [CIConnect](CIConnect.md) — a port must be connected for its remote select to be sent
- [CIGlobalStat](CIGlobalStat.md) — which ports are connected
