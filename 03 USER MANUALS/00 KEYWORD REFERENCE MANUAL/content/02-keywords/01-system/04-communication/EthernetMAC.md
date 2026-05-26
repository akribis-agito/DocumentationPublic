---
keyword: EthernetMAC
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 602
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
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
# EthernetMAC

**Definition:**

In Ethernet communication, EthernetMAC is a parameter array storing the MAC address in decimal. Each controller on the same network must have a unique MAC address.

For example, if MAC addresss is “00-B0-D0-63-C2-26”, each array element is as follows.

| Parameter         | Hex | Value (decimal) |
| ----------------- | --- | --------------- |
| EthernetMAC\[1\]  | 00  | 0               |
| EthernetMAC\[2\]  | B0  | 176             |
| EthernetMAC\[3\]  | D0  | 208             |
| EthernetMAC\[4\]  | 63  | 99              |
| EthernetMAC\[5\]  | C2  | 194             |
| EthernetMAC\[6\]  | 26  | 38              |
