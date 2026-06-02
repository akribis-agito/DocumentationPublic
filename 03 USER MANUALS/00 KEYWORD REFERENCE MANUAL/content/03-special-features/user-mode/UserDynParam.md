# UserDynParam

**Definition:**

UserDynParam is a general-purpose data array used by special user-defined processing modes. Each element holds a value that the active user-mode algorithm reads or writes at runtime (for example, captured positions or sensor data). The array provides 50 elements, indexed [1] through [50]. It cannot be changed while the axis is in motion or with the motor on. It is a non-axis array parameter and is not saved to flash.

**See also:**

[GenData](../../02-keywords/20-arrays/GenData.md), [UserParam](../../02-keywords/20-arrays/UserParam.md)
