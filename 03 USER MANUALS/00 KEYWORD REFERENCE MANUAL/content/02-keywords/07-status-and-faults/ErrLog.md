---
keyword: ErrLog
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 235
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 65
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ErrLog

**Definition:**

ErrLog is an array that holds the error log of the controller. When an error occurs, two values are saved in ErrLog:

- Axis and error code

- Error time (in seconds, counting from when the unit was powered on)

The axis and error code of the first error that occurs is logged in ErrLog\[1\] and the error time of the first error is in ErrLog\[2\]. Subsequent errors are saved in higher array locations, ErrLog\[3\] and ErrLog\[4\], and thereafter. When the end of the array is reached, it circles back to the first error and overwrites it.

The axis and error code are stored together, with the axis information (see table below) in the upper 8 bits, and the error code (see [Error Codes](#error-codes)) in the lower 24 bits.

| Axis | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value (upper 8 bit) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

The time of the error in ErrLog is in seconds since power on.

The best way to look at ErrLog is by using the PCSuite software. PCSuite will translate the error code to text and the time since power up to clock reading according to the PC clock.
