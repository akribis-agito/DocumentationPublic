---
keyword: MotorTempUsed
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 398
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorTempUsed

**Definition**

MotorTempUsed defines the temperature sensor type.

| Value | Descriptions                                                        |
|-------|---------------------------------------------------------------------|
| 0     | None (or if thermostat is connected to digital input)               |
| 1     | PT100                                                               |
| 2     | Thermostat (if thermostat is connected to temperature sensor input) |
