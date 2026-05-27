---
keyword: CISyncDef
summary: Per-axis array defining the parameters exchanged synchronously each control cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 506
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
# CISyncDef

Per-axis array defining the parameters exchanged synchronously each control cycle.

## Overview

`CISyncDef` is a per-axis array that defines the Central-i **synchronous channel** for a port — the cyclic, fixed-format data that the master and remote exchange every control cycle (current command and control bits out to the remote; encoder position, currents, status and digital/analog inputs back). It is the synchronous counterpart of [CIOfflineDef](CIOfflineDef.md), which configures the occasional offline (mailbox) channel. The definition is saved to flash and is intended to take effect when [CIConnect](CIConnect.md) brings the link up. Index `[0]` is unused; the definition occupies `[1]` and `[2]`.

## How it works

The synchronous message layout for each device class (amplifier or I/O unit) is fixed by the Central-i protocol: the master sends a master-to-remote frame and receives a remote-to-master frame within each cycle, with the frame fields and lengths determined by the connected device type. `CISyncDef` holds the per-port synchronous-channel definition; the live frame contents are placed automatically by the firmware in the control interrupt according to the device class reported in [CIIdentity](CIIdentity.md).

> Note: in the firmware examined, the per-cycle synchronous frame layout is selected from the connected device class rather than from these two array elements — the active sync code does not read `CISyncDef`. The array is defined and stored per port as the synchronous-channel definition; configure the link timing in [CILinkConfig](CILinkConfig.md) and the device class in [CIDeviceType](CIDeviceType.md) to control the synchronous exchange.

## Examples

```text
ACISyncDef[1]       ; read the first synchronous-channel definition element
ACISyncDef[2]       ; read the second synchronous-channel definition element
```

## See also

- [CILinkConfig](CILinkConfig.md) — frame timing for the synchronous (and offline) channels
- [CIDeviceType](CIDeviceType.md) — device class that fixes the sync frame layout
- [CIOfflineDef](CIOfflineDef.md) — offline-channel definition
- [CIConnect](CIConnect.md) — initiate the link
