---
keyword: Compare
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 195
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# Compare

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

`Compare` is a user-program low-level language keyword. The syntax related to `Compare` is usually generated automatically by the PC Suite during compilation.

`Compare` pops two variables from the numeric stack and compares them as required:
- If the result is `true`, it pushes `1` onto the stack.
- If the result is `false`, it pushes `0` onto the stack.

The index value determines which operation is performed. The operands should be pushed to the stack before `Compare` is called.

The result is pushed onto the numeric stack. If this function is called from communication, the value is also sent through communication.

**Operations** (`pop1` is the top value in the stack, `pop2` is the next value):

| Value | Operation | True if           |
| ----- | --------- | ----------------- |
| 2     | `==`      | pop1 == pop2      |
| 3     | `>`       | pop1 > pop2       |
| 4     | `>=`      | pop1 >= pop2      |
| 5     | `<`       | pop1 < pop2       |
| 6     | `<=`      | pop1 <= pop2      |
| 7     | `!=`      | pop1 != pop2      |
| 8     | Zero      | pop1 == 0         |
| 9     | Not Zero  | pop1 != 0         |

(The values start at 2 for compatibility with other functions.)
