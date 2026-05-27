---
keyword: ChainAddress
summary: CAN address used when the controller runs in a daisy-chain topology.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 159
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
  - -1
  - 8
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ChainAddress

CAN address used when the controller runs in a daisy-chain topology.

## Overview

`ChainAddress` sets the address a controller uses on a daisy-chained communication bus, letting a group of controllers share one bus with distinct addresses. The default of `-1` indicates the controller is not assigned a chain position. It is saved to flash and takes effect after a [Reset](../02-operation/Reset.md).

## Examples

```text
AChainAddress=1      ; assign a chain position, then Save and Reset to apply
```

## See also

- [CANAddr](CANAddr.md) — CAN base address
- [CANBaud](CANBaud.md) — CAN bus baud rate
