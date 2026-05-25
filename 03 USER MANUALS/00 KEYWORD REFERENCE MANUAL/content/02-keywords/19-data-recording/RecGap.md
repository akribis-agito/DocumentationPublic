# RecGap

**Definition:**

RecGap is an array that defines the down sampling factors on the controller cycle frequency, thereby determining the data recording frequencies.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

The data recording frequency is as shown.

$$
Data\ recording\ frequency\ of\ scope\ x\ \lbrack Hz\rbrack = \frac{Controller\ cycle\ rate\ \lbrack Hz\rbrack}{RecGap\lbrack x\rbrack}
$$
