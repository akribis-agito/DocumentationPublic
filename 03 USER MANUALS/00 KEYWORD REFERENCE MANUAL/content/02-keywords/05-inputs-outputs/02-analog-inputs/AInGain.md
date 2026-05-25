# AInGain

AInGain is the actual analog input gain multiplied by 65536. The multiplication is needed to allow representation of fractions by only using integers. The array index corresponds to the index of the analog input (i.e.: AInGain\[1\] refers to analog input 1).

The input ($u$) and output ($y$) relation of the gain block is as follows.

$$
y = \frac{AInGain}{65536}u
$$

To have unity gain, user should set AInGain=65536.
