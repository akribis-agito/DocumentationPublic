# MotorLearnSta

**Definition:**

MotorLearnSta is a read-only parameter that reports the current status of the motor learning process. It is an axis-related status variable and is not saved to flash.

| Value | Meaning |
|---|---|
| 0 | Not active (no learning in progress) |
| 1 | Automatic-mode learning in process |
| 2 | Manual-mode learning in process |
| 3 | Automatic-mode learning finished successfully |
| 4 | Automatic-mode learning failed |
| 5 | Stopped — motor turned off unexpectedly during learning (see [MotorReason](../../02-keywords/07-status-and-faults/MotorReason.md)) |

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnRes](MotorLearnRes.md), [MotorLearnPl](MotorLearnPl.md)
