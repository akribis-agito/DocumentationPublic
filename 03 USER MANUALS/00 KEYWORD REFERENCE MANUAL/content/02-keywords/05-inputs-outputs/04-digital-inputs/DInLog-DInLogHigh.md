# DInLog/DInLogHigh

**Definition:**

DInLog/DInLogHigh inverts the logic for selected digital inputs through XOR operation.

| Bit’s value | Logic    |
|-------------|----------|
| 0           | Default  |
| 1           | Inverted |

For digital inputs 1 to 32,

$$
DInPort\  = \ DInPortBefore\ \hat{}\ DInLog
$$

For digital inputs 33 to 64,

$$
DInPortHigh\  = \ DInPortHighBefore\ \hat{}\ DInLogHigh
$$

**Example:**

If

$$
DInPortBefore\  = \ 15\ (binary\ 00000000\ 00000000\ 00000000\ 00001111)
$$

and

$$
DInLog\  = \ 6\ (binary\ 00000000\ 00000000\ 00000000\ 00000110)
$$

then

$$
DInPort = \ 9\ (binary\ 00000000\ 00000000\ 00000000\ 00001001)
$$

where bits 1 and 2 are inverted (referring to digital input 2 and 3).

**Note:**

This is typically used for limit switches for fail-safe reasons. (i.e.: If limit switch is not connected (input low), then fault is triggered).
