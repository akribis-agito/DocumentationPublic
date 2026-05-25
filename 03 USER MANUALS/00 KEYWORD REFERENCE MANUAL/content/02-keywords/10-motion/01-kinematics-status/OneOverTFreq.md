# OneOverTFreq

**Condition:**

OneOverTFreq is only supported by non-Central-i products and when digital incremental encoder (EncType = 1) is used.

**Definition:**

OneOverTFreq is used to define down-sampling factor for the hardware polling frequency in Vel\[4\] measurement, where

$$
Polling\ frequency\lbrack Hz\rbrack = \frac{Hardware\ base\ frequency\lbrack Hz\rbrack}{2^{OneOverTFreq}}
$$

Please refer to the [Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md) keyword for more information.
