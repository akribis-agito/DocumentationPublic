# DualEncMode

**Condition:**

This keyword is only used when DualLoopOn=1 and DualEncSwapOn=1.

**Definition:**

DualEncMode is used to activate/deactivate range-limited dual-loop control.

| DualEncMode | Descriptions |
|----|----|
| 0 | Pseudo dual-loop control is always used regardless of position |
| 1 | Dual-loop control is only used for a defined position range. Pseudo dual-loop control is used outside of this range. |
