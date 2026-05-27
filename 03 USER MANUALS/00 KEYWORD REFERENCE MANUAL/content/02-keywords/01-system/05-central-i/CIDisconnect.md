---
keyword: CIDisconnect
summary: Command that terminates the active Central-i link on the selected axis port.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 505
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIDisconnect

Command that terminates the active Central-i link on the selected axis port.

## Overview

`CIDisconnect` terminates the active Central-i link on the selected axis port. After it runs, the port stops the cyclic real-time data exchange and stays down until a subsequent [CIConnect](CIConnect.md) is issued. It is a function keyword (no value) and cannot be run while the motor is on or in motion.

## How it works

`CIDisconnect` moves the port's connection state machine into the disconnect state (the firmware tears the link down from there) and immediately clears the per-axis status and identity arrays for that port:

- every reported element of [CIStatus](CIStatus.md) is zeroed, so the state machine reads `0` (disabled) and the error counters reset;
- every element of [CIIdentity](CIIdentity.md) is zeroed, since the previously connected device's identity is no longer valid;
- the port's connected bit in [CIGlobalStat](CIGlobalStat.md) is cleared once the disconnect completes.

The same teardown happens automatically when [CIDeviceType](CIDeviceType.md) is changed to a value that differs from the currently connected device — the firmware forces a disconnect so the port can reconnect with the new role.

## Examples

```text
ACIDisconnect        ; tear down the Central-i link on the selected axis
ACIStatus[1]         ; reads 0 (disabled) after the disconnect completes
```

## See also

- [CIConnect](CIConnect.md) — initiate the link
- [CIAutoConnect](CIAutoConnect.md) — connect automatically at power-up
- [CIStatus](CIStatus.md) — link state (cleared by this command)
- [CIIdentity](CIIdentity.md) — device identity (cleared by this command)
- [CIGlobalStat](CIGlobalStat.md) — system-wide connection summary
