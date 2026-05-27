---
keyword: CIAutoConnect
summary: When enabled, establishes the Central-i connection automatically at power-up.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 500
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIAutoConnect

When enabled, establishes the Central-i connection automatically at power-up.

## Overview

`CIAutoConnect = 1` causes the controller to run the Central-i connection sequence for this axis's port automatically during start-up, without an explicit [CIConnect](CIConnect.md) from the host. `CIAutoConnect = 0` (default) leaves the port disconnected until the host connects manually. The setting is axis-related and saved to flash, so it persists across resets.

## How it works

During boot, after the ports are initialised, the controller scans every port. If **any** port has `CIAutoConnect = 1` it first waits a short settling time so the remote units can power up, then for each auto-connect port it runs the same connection sequence as [CIConnect](CIConnect.md):

- For a real remote, the per-port state machine is driven from reset all the way to the synchronised state (or to the error state) in a tight loop, since interrupts are not yet running. On success the connect-time special-parameter setup runs and the port begins cyclic exchange.
- For a **simulation** device type ([CIDeviceType](CIDeviceType.md) set to a simulation class), the port is marked connected immediately and [CIIdentity](CIIdentity.md) is filled with default channel counts — no physical link is attempted.

Because auto-connect happens before the host is involved, the resulting link state is reported through [CIStatus](CIStatus.md) and [CIGlobalStat](CIGlobalStat.md), which the host can poll after start-up. A per-port internal "skip" flag can suppress auto-connect for a port that has just been reconfigured, so it does not connect with stale settings.

## Examples

```text
ACIAutoConnect=1     ; auto-connect this axis's Central-i port at startup
ACIAutoConnect=0     ; leave the port disconnected until CIConnect is issued
```

## See also

- [CIConnect](CIConnect.md) — the connection sequence this triggers (run manually)
- [CIDisconnect](CIDisconnect.md) — tear down the link
- [CIDeviceType](CIDeviceType.md) — selects real vs simulation behaviour at auto-connect
- [CIStatus](CIStatus.md) / [CIGlobalStat](CIGlobalStat.md) — resulting link state
