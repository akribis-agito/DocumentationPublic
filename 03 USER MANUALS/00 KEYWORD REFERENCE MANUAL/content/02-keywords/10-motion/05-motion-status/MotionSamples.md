---
keyword: MotionSamples
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 267
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotionSamples

**Condition:**

It is only used when OperationMode = 2 or 3.

**Definition:**

MotionSamples reports the move and settle times of the last completed motion. The value is in the unit of number of controller cycles (typically 1 cycle equals to $T_{s} = \frac{1}{16384}Hz = 61.03515\mu s$).

Each array element represents different time, as shown.

| Index | Descriptions |
|----|----|
| 1 | Motion profile time |
| 2 | The time from the start of motion until the axis starts to settle into the target for at least InTargetTime. |
| 3 | The time from the start of motion until the axis settles into the target for at least InTargetTime. |
| 4 | The time from the end of motion profile until the axis starts to settle into the target for at least InTargetTime. |

In summary,

$$
MotionSamples\lbrack 2\rbrack = \ MotionSamples\lbrack 1\rbrack + \ MotionSamples\lbrack 4\rbrack
$$

$$
MotionSamples\lbrack 3\rbrack = \ MotionSamples\lbrack 2\rbrack + \frac{InTargetTime}{T_{s}}\ 
$$

**Example:**

![image30.emf](../../../assets/image30.emf)

The plot above shows an example of MotionSamples. Since MotionSamples is in controller cycles, multiplication by sampling time (here, it is $T_{s} = 61.03515\mu s$) is needed to get the time in SI unit.
