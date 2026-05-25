# RecLength

**Definition:**

RecLength is an array that defines the number of data points to capture per parameter, thereby determining the period of the recording.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

The period of data recording is as shown.

$$
Period\ of\ recording\ for\ scope\ x\ \lbrack s\rbrack = \frac{RecLength\lbrack x\rbrack \bullet RecGap\lbrack x\rbrack}{Controller\ cycle\ rate\ \lbrack Hz\rbrack}
$$
