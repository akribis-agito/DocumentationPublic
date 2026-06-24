# 位置限位保护

Agito 同时支持**硬件**位置限位和**软件**位置限位。

**软件限位**（[FwdPLim](FwdPLim.md) / [RevPLim](RevPLim.md)）定义了允许的运动范围。如果运动指令的目标位置超出软件限位，则该指令会在 [Begin](../../../10-motion/04-motion-command/Begin.md) 处被拒绝，并将该拒绝记录到 [ErrLog](../../../07-status-and-faults/ErrLog.md) 中。运动过程中，会持续检查在不超出软件限位的前提下安全减速并停止所需的距离。如果轴正在接近某一限位——例如在点动模式下——规划器会减速并使轴在限位位置停止。停止原因记录在 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) 中（`6` = 反向软件限位，`7` = 正向软件限位）。此停止使用紧急减速 [EmrgDec](../../../10-motion/03-kinematics-configuration/EmrgDec.md)，而非常规的 [Decel](../../../10-motion/03-kinematics-configuration/Decel.md)。

**硬件限位**是表示轴已到达行程末端的外部信号。限位传感器的配置通过 [DInMode](../../../05-inputs-outputs/04-digital-inputs/DInMode.md) 完成。[LimitsStat](LimitsStat.md) 反映两个限位开关输入的状态（已触发/未触发）（位 `0` = RLS，位 `1` = FLS）。当某个硬件限位传感器被触发时，朝向该限位方向的运动指令将作为指令/消息错误被拒绝，并将该拒绝记录到 [ErrLog](../../../07-status-and-faults/ErrLog.md) 中。

运动过程中，会持续检查限位传感器的状态。如果运动方向上的限位被触发，规划器会以 [EmrgDec](../../../10-motion/03-kinematics-configuration/EmrgDec.md) 减速并使轴停止。停止原因记录在 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) 中（`4` = 反向限位开关，`5` = 正向限位开关）。

位置限位机制从不禁用轴，也不会引发 [ConFlt](../../../07-status-and-faults/ConFlt.md)——它仅指令一次受控减速。它独立于运动保护的跟随误差跳闸（[MaxPosErr](../general-maximum-limits/MaxPosErr.md)、[MaxVelErr](../general-maximum-limits/MaxVelErr.md)），也独立于硬件保护掩码 [ProtectMask](../../01-general-protection/ProtectMask.md)。
