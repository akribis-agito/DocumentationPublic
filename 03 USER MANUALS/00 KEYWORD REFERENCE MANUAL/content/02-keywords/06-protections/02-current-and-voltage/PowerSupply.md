---
keyword: PowerSupply
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 401
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
  - 3
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PowerSupply

**Definition:**

PowerSupply defines the type of drive power supply input to the amplifier. User needs to select correct value (for example, in PCSuite configuration page) for proper protection.

The table below shows PowerSupply values and their descriptions.

| PowerSupply | Descriptions           |
|-------------|------------------------|
| 1           | Single-phase AC supply |
| 2           | DC supply              |
| 3           | Three-phase AC supply  |
