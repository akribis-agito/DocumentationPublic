---
keyword: EthernetIP
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 600
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EthernetIP

**Definition:**

In Ethernet communication, EthernetIP is a parameter array storing the IP address.

For example, if IP addresss is “172.1.1.50”, each array element is as follows.

| Parameter        | Value |
| ---------------- | ----- |
| EthernetIP\[1\]  | 172   |
| EthernetIP\[2\]  | 1     |
| EthernetIP\[3\]  | 1     |
| EthernetIP\[4\]  | 50    |
