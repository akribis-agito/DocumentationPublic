---
keyword: DOutLog
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 212
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutLog

**Definition:**

DOutLog inverts the logic for selected digital outputs, in 0-based indexing form.

$$
DOutPortFinal\  = \ DOutPort\ \hat{}\ DOutLog
$$

| Bit’s value | Logic    |
|-------------|----------|
| 0           | Default  |
| 1           | Inverted |

DOutPortFinal (internal variable) will be used for physical circuit of digital outputs.

**Example:**

If

$$
DOutPort\  = \ 7\ (binary\ 00000000\ 00000000\ 00000000\ 00000111)
$$

and

$$
DOutLog\  = \ 3\ (binary\ 00000000\ 00000000\ 00000000\ 00000011)
$$

then

$$
DOutPortFinal = \ 4\ (binary\ 00000000\ 00000000\ 00000000\ 00000100)
$$

where bits 0 and 1 are inverted (referring to digital output 1 and 2).

**Note:**

DOutLog also applies to digital outputs that are assigned with hardware or software functionalities.
