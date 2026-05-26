---
keyword: ChainAddress
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

ChainAddress sets the CAN address used when the controller is operating in a daisy-chain topology. It is saved to flash and takes effect after reset, allowing a group of controllers to share a communication bus with distinct addresses.

**See also:**

[CANAddr](CANAddr.md), [CANBaud](CANBaud.md)
