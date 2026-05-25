# CurrCmdSlope

**Condition:**

This keyword is only applicable when CurrCmdSrc = 1 or 2.

**Definition:**

CurrCmdSlope defines the slope for transition from the starting CurrRef value to the existing CurrCmdVal array entry. It is in terms of milliampere per second. Only after the ramping, the timer CurrCmdCntr will begin from 0.

**Example:**

If

- CurrCmdIndex = 2

- CurrCmdCntr = CurrCmdHTime\[2\] (end of current entry)

- CurrRef = CurrCmdVal\[2\] = 340

- CurrCmdVal\[3\] = -500

- CurrCmdSlope\[3\] = 700,

the ramping from 340mA to -500mA will start and be completed in 1.2 seconds.
