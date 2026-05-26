---
keyword: DOutPort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 211
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutPort

**Definition:**

DOutPort represents the state of the digital outputs, before XOR operation by DOutLog, in 0-based indexing form.

| Bit’s value | State (Before DOutLog) |
|-------------|------------------------|
| 0           | Off                    |
| 1           | On                     |

DOutPort can be written by user, but only when such digital output(s) are not configured/tied to any functionality or keywords. In other words, DOutPort can be written only if

4.  DOutSelect\[x\] = 0 (where DOutMode is used)

5.  DOutMode\[x\] = 0 (where DOutPort can be set by user)

**Example:**

If DOutPort = 6 (binary 00000000 00000000 00000000 00000<u>11</u>0), output 2 and 3 are in “On” state, while all other outputs are in “Off” state.

**Note:**

1. “ D O u t P o r t = D O u t P o r t | B i t w o r d ” is typically used to set desired bit(s). However, this is not an atomic function, as it requires reading DOutPort, bit manipulation, and then writing back the value. In between, DOutPort might be assigned another value by another process or thread, this change will be overwritten and lost.
2. DOutPort is not saved to flash. Any user-defined digital output states must be rewritten upon power up.
3. The final digital output state may be inverted by DOutLog.
