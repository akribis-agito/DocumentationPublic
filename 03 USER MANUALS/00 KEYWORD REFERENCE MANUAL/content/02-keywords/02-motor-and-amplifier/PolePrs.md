---
keyword: PolePrs
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 54
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 50
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
---
# PolePrs

**Condition:**

This keyword is only used when MotorType = 3, 4 or 7.

**Definition:**

PolePrs defines the number of magnet pole pairs (1 pole pair equals to 1 north and 1 south poles) with varying definitions depending on the motor type. User must set correct value to ensure feedback and commutation work normally, and to prevent possible damage.

The table below shows how PolePrs is defined depending on motor type.

| MotorType               | PolePrs descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 (Linear DC brushless) | PolePrs is the number of pole pairs per magnetic period. In short, user must always set PolePrs = 1 for linear brushless motor.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 4 (Rotary DC brushless) | PolePrs is the number of pole pairs per mechanical revolution of rotary motor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 7 (Stepper closed loop) | PolePrs is the number of electrical cycles (1 electrical cycle = 1 set of full-step excitation sequence) per mechanical revolution of 2-phase stepper motor. In 1 electrical cycle, there are total of 4 full steps. Normally, stepper motor manufacturers specify the resolution in terms of physical angle per one full step. This means in 1 revolution, the number of electrical cycles is $$PolePrs = \ \ \frac{360\lbrack physical\ deg\rbrack}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$ |
