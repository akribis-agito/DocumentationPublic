# AInFilt

AInFilt defines the digital low pass filter coefficient. The array index corresponds to the index of the analog input (i.e.: AInFilt\[2\] refers to analog input 2).

The filtered output of the current controller cycle ($y_{i}$) is a function of

1.  the filter input of the current controller cycle ($u_{i}$)

2.  the filtered output of the last controller cycle ($y_{i - 1}$)

where

$$
y_{i} = \frac{AInFilt}{65536}u_{i} + \left( 1 - \frac{AInFilt}{65536} \right)y_{i - 1}
$$

To get unfiltered analog input value where $y_{i} = u_{i}$, user should set AInFilt=65536.
