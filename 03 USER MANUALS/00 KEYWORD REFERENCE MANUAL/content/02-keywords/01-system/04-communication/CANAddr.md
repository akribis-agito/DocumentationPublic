---
keyword: CANAddr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 67
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
  range: null
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
---
# CANAddr

**Definition:**

In CAN bus communication, CANAddr specifies the CAN base address of the node. It is recommended to always set the CAN base address (and therefore the CAN initial address) to a multiple of 16. This is because each controller requires 16 addresses for internal purposes.

DIP switches can be used to specify CAN initial address’ offset from the CAN base address. CAN initial address will wraparound if address after offset overflows past 2032.

The controller receives messages at CAN initial address + 2\*N where N = 0, 1, 2 and so on.
The controller replies to messages at CAN initial address + 2\*N + 1 where N = 0, 1, 2 and so on.

For more information, please refer to communication manual.
