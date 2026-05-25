# AOutShifts

*Legacy keywords*

**Definition:**

AOutShifts defines the number of left-shifting or right-shifting on the analog output, to improve dynamic range. The array index corresponds to the index of the analog output. (i.e.: AOutShifts\[2\] refers to analog output 2).

For AOutShifts, a negative value means right-shifting/division, while a positive value means left-shifting/multiplication. A zero value means no shifting is performed.

For example, if the initial value is -9423 and AOutShifts=-5, the resultant value is -294.

**Note:**

AOutShifts is only applicable when in monitoring mode (AOutMode != 0).
