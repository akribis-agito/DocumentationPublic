# MotorReason

**Definition:**

MotorReason stores the reason on why the axis was disabled. MotorReason is reset to 0 upon motor on.

| Value | Description |
|---|---|
| 0 | **NONE** |
| 1 | **CONFLT** A controller fault triggered caused the axis to be disabled. Check ConFlt for more details. |
| 2 | **Digital Input** A command was sent via a digital input to disable the axis. |
| 3 | **User Program (IDE+)** A command was sent via the user program to disable the axis. |
| 4 | **Communication** A command was sent via the communication channel to disable the axis. |
