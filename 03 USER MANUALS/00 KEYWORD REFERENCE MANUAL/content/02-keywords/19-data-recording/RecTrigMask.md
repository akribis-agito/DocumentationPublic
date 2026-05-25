# RecTrigMask

**Definition:**

RecTrigMask masks the bits of the values used in trigger comparison operation. Trigger source value (from RecTrigSrc) and trigger comparison values (RecTrigVal and RecTrigValMax) will be masked.

Masking allows the trigger to activate based on single or multiple selected bits. Each index of RecTrigMask refers to a different trigger of different scope.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Masking is only applicable if the trigger source (RecTrigSrc) is of fixed-point data type (32-bit int or 64-bit long). By default, RecTrigMask value is -1 (0 x FFFF FFFF FFFF FFFF), where no bits are masked and trigger comparison operation uses the unaltered values. The masking is done using bitwise AND operation.

$$
Masked\ value\  = (Original\ value)\ \&\ \left( RecTrigMask\lbrack x\rbrack \right)
$$

<span class="mark">**DN:** Issue with the RecTrigMask range (masking issue).</span>

**Example:**

Assuming the second trigger of first scope is to be activated upon the rising edge of acceleration bit of axis A MotionStat, the following settings are required:

1.  RecTrigTyp\[2\] = 5 (rising edge)

2.  RecTrigSrc\[2\] = 32 (AMotionStat as the trigger source variable)

3.  RecTrigMask\[2\] = 16 (masking bit 4)

4.  RecTrigVal\[2\] = 0 (to trigger when rising edge above this value is detected)
