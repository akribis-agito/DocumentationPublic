# HomeComtAngWr

**Definition:**

HomeComtAngWr sets the commutation angle to be applied when the axis is initialised at its home position, bypassing a full homing sequence. Writing a previously captured angle (from HomeComtAngRd) allows the controller to resume commutation at the correct electrical angle without re-running homing. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[HomeComtAngOn](HomeComtAngOn.md), [HomeComtAngRd](HomeComtAngRd.md)
