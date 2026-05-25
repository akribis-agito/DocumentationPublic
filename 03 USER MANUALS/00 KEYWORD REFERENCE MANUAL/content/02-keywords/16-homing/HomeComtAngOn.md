# HomeComtAngOn

**Definition:**

HomeComtAngOn enables the automatic commutation angle capture feature during homing. When set to a non-zero value, the controller records the commutation angle at the home position into HomeComtAngWr, which can later be restored with HomeComtAngWr to avoid a homing sequence on subsequent power-ups. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[HomeComtAngWr](HomeComtAngWr.md), [HomeComtAngRd](HomeComtAngRd.md), [HomeStat](HomeStat.md)
