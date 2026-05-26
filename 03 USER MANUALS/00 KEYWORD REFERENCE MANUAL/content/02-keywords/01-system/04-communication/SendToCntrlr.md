---
keyword: SendToCntrlr
summary: Partially-implemented function that routes a parameter write to another controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 484
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# SendToCntrlr

Partially-implemented function that routes a parameter write to another controller.

## Overview

`SendToCntrlr` routes a parameter write to another controller over the communication bus. It accepts an array of values that encode the target controller address, the parameter code, and the data payload. It is flagged **partially implemented**, so full behaviour may depend on the specific firmware build. For single CAN parameter writes to a remote node, the [RemoteCAN](RemoteCANSend.md) group is the more direct mechanism.

## See also

- [RemoteCANSend](RemoteCANSend.md) — send a single CAN write to a remote node
- [CANAddr](CANAddr.md) — CAN addressing
