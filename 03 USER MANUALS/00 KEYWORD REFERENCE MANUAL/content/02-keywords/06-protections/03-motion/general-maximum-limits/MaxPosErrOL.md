# MaxPosErrOL

**Definition:**

MaxPosErrOL defines maximum allowable absolute position error ([PosErr](../../../../02-keywords/10-motion/01-kinematics-status/PosErr.md)) while in open loop condition during [injection](../../../../02-keywords/13-injection/00-overview.md). If the absolute value of PosErr exceeds MaxPosErrOL, the axis will be instantaneously disabled, and an error is thrown to ConFlt.
