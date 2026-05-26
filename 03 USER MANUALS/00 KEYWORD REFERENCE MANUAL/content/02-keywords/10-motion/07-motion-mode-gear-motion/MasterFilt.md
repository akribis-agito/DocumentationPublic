---
keyword: MasterFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 161
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 64
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFilt

**Condition:**

MasterFilt is only used in the direct gear motion ([MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 5).

**Definition:**

MasterFilt defines the digital filter coefficient of first order low pass filter, applied onto the scaled delta of MasterPos since the start of motion.

The filter formula is as shown, where time $t = kT_{s}$ and $T_{s}$ is controller sampling time (typically 61µs).

$$
y_{k} = \frac{MasterFilt}{64}u_{k} + \left( 1 - \frac{MasterFilt}{64} \right)y_{k - 1}
$$

According to backward-Euler estimation, MasterFilt should be selected according to following formula below where $f_{c}$ is filter cut-off frequency, in Hz. By default, MasterFilt = 3 and it corresponds to 128.2Hz cut-off frequency.

$$
MasterFilt = 64\left( \frac{2\pi f_{c}T_{s}}{1 + 2\pi f_{c}T_{s}} \right)
$$
