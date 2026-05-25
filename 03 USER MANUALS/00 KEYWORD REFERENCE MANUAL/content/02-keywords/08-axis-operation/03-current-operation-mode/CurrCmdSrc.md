# CurrCmdSrc

**Definition:**

Under current operation mode, CurrCmdSrc is used to set the source of current command, as shown below.

| Value | Source |
|----|----|
| 0 | Analog current command input (defined by [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)) |
| 1 or 2 | User defined values (CurrCmdVal), each with specific timing (CurrCmdHTime) |
| 3 | Master axis current command (axis defined by [CurrRefMaster](../../../02-keywords/08-axis-operation/03-current-operation-mode/CurrRefMaster.md)\] |
