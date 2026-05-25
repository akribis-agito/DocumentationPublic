# Axis operation

Depending on application, user can operate in different control mode (e.g. position control mode for point-to-point motion, current control mode for slave driver application, etc.).

User can choose to switch the control mode (OperationMode)

1.  manually

2.  by command keyword

3.  by assigning conditions for automatic transition, or

4.  by digital input defined by [DInMode](../../02-keywords/05-inputs-outputs/04-digital-inputs/DInMode.md)

For **manual** transition, user can assign to OperationMode keyword directly.

For **command keyword** (GoToCurrMode, GoToForceMode, GoToPosMode), user can call the command directly. Unlike manual transition, this method will ensure proper preparation is performed before control mode is finally changed.

For **condition assignment**, related keywords are used for condition checking. If conditions are satisfied, control mode switches accordingly by the controller. Various switching modes are available.

The following table shows the summary of axis operation keywords.

| No. | Sub-section             | Keywords      | Summary |
|-----|-------------------------|---------------|---------|
| 1   | General keywords        | MotorOn       |         |
| 2   | General keywords        | OperationMode |         |
| 3   | General keywords        | OpenLoopCurr  |         |
| 4   | General keywords        | OpenLoopOn    |         |
| 5   | General keywords        | OpenLoopVolt  |         |
| 6   | Position operation mode | BeginOnToPos  |         |
| 7   | Position operation mode | GoToPosMode   |         |
| 8   | Position operation mode | ModeSwitchPos |         |
| 9   | Position operation mode | PosPosFlag    |         |
| 10  | Position operation mode | PosPosTh      |         |
| 11  | Position operation mode | RetractSpeed  |         |
| 12  | Position operation mode | RetractTarget |         |
| 13  | Current operation mode  | CurrAInTh     |         |
| 14  | Current operation mode  | CurrCmdCntr   |         |
| 15  | Current operation mode  | CurrCmdHTime  |         |
| 16  | Current operation mode  | CurrCmdIndex  |         |
| 17  | Current operation mode  | CurrCmdSlope  |         |
| 18  | Current operation mode  | CurrCmdSrc    |         |
| 19  | Current operation mode  | CurrCmdVal    |         |
| 20  | Current operation mode  | CurrCurrTh    |         |
| 21  | Current operation mode  | CurrCurrThDir |         |
| 22  | Current operation mode  | CurrPosErrTh  |         |
| 23  | Current operation mode  | CurrPosTh     |         |
| 24  | Current operation mode  | CurrPosThDir  |         |
| 25  | Current operation mode  | GoToCurrMode  |         |
| 26  | Force operation mode    | Force         |         |
| 27  | Force operation mode    | ForceAInTh    |         |
| 28  | Force operation mode    | ForceCmdCntr  |         |
| 29  | Force operation mode    | ForceCmdHTime |         |
| 30  | Force operation mode    | ForceCmdIndex |         |
| 31  | Force operation mode    | ForceCmdSlope |         |
| 32  | Force operation mode    | ForceCmdSrc   |         |
| 33  | Force operation mode    | ForceCmdVal   |         |
| 34  | Force operation mode    | ForceErr      |         |
| 35  | Force operation mode    | ForceInTStat  |         |
| 36  | Force operation mode    | ForceInTTime  |         |
| 37  | Force operation mode    | ForceInTTol   |         |
| 38  | Force operation mode    | ForcePosErrTh |         |
| 39  | Force operation mode    | ForceRef      |         |
| 40  | Force operation mode    | ForceSamples  |         |
| 41  | Force operation mode    | GoToForceMode |         |
