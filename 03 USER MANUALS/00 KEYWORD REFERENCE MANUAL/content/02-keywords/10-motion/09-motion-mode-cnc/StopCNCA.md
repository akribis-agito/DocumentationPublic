---
keyword: StopCNCA
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 456
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopCNCA

**Definition:**

StopCNCA is a command that stops execution of the CNC motion queue A. The currently executing segment is aborted and the axis decelerates to rest. It is a non-axis command function that can be issued at any time, including during motion.

**See also:**

[StopCNCB](StopCNCB.md), [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)
