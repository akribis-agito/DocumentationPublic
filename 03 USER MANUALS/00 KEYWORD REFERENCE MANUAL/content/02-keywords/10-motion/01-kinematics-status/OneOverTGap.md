# OneOverTGap

**Condition:**

OneOverTGap is only supported by non-Central-i products and when digital incremental encoder (EncType = 1) is used.

**Definition:**

OneOverTGap is used to define the required change/gap in hardware encoder counter that triggers the saving of polling counter.

$$
User\ defined\ gap = 2^{OneOverTGap}\ 
$$

The polling and delta counters will reset after saving of polling counter, for the next detection.

**Note:**

The gap of at least 4 ( O n e O v e r T G a p ≥ 2 ) will provide a more accurate velocity reading because it will not be affected by the shift between the A and B encoder signals (which is not always exactly by 90 degrees).

Please refer to the [Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md) keyword for more information.
