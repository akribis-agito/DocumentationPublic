# Pos

**Definition:**

Pos reports the encoder feedback, in terms of main user unit (configurable by UsrUnits). Since Pos is used for position loop feedback in non-gantry mode. its definition will change depending on the gantry mode and dual-loop condition.

| Conditions | Default control (non-gantry mode) Dual-loop control (non-gantry mode) Gantry mode (regardless of dual-loop condition) | Pseudo dual-loop control (non-gantry mode) |
|---|---|---|
| Definition | Main encoder reading after the modulo operation block. **Unit: Main encoder count** | Auxiliary encoder reading after decoding but scaled up to main encoder unit.<br> $$Pos = AuxPos \bullet \frac{DualLoopFact}{65536}$$ **Unit: Main encoder count** |

Pos can be set to any desired value at any time via [SetPosition](../../../02-keywords/10-motion/03-kinematics-configuration/SetPosition.md) function (instead of setting Pos directly). Its value is reset to 0 upon power up.
