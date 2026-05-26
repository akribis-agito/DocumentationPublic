---
keyword: EthernetPort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 601
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
  - 65535
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
---
# EthernetPort

**Definition:**

In Ethernet communication, EthernetPort defines the port number. Agito controllers only support port 50,000.
