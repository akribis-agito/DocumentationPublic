# TorqCompMode

**Condition:**

TorqCompMode is only applicable when OperationMode = 2 or 3 (velocity or position operation mode).

**Definition:**

TorqCompMode is used to define the source of the loop’s current compensation, as shown.

| TorqCompMode | Current compensation value |
|----|----|
| -1 | 0 (no compensation) |
| 0 | Value is from analog input (see [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md), torque compensation selection). |
| 1 | TorqCompFix\[1\] |
| 2 | TorqCompFix\[2\] |
| 3 | TorqCompFix\[3\] |
| 4 | TorqCompFix\[4\] |
| 5 | TorqCompFix\[5\] |

Please refer to the block diagram in [Control tuning – Feedforwards](../../../02-keywords/11-control-tuning/05-feedforwards/00-overview.md) for location of this compensation.
