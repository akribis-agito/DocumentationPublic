---
summary: AGM800-EC 时间与单位
last_updated: '2026-10-10'
doc_revision: '2026.10'
---
# AGM800-EC 时间与单位

AGM800-EC（Identity 产品类型 16）采用标称 **16,000 Hz** 控制频率，每周期 **62.5 µs**。时间换算使用该频率，内部定点累加器仍采用 `2^14 = 16384` 比例。这两个数值不可互换。

## 指令与状态换算

下表列出固定时间域换算。对于可写关键字，写入时乘以系数；读取时除以系数。整数存储和整数响应需舍入。嵌入式 `UsrUnits`、`AuxUsrUnits`、`PDUsrUnits` 不再作用于这些条目。位置关键字仍使用各自的位置比例。主机的全局工程单位功能是另一层设置。

| 关键字 | 系数 |
|---|---|
| [Vel](../../10-motion/01-kinematics-status/Vel.zh.md) | 1.024 |
| [AuxVel](../../10-motion/01-kinematics-status/AuxVel.zh.md) | 1.024 |
| [PDVel](../../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.zh.md) | 1.024 |
| [VelErr](../../10-motion/01-kinematics-status/VelErr.zh.md) | 1.024 |
| [VelRef](../../10-motion/01-kinematics-status/VelRef.zh.md) | 1.024 |
| [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.zh.md) | 1.024 |
| [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.zh.md) | 1.024 |
| [StuckVel](../../06-protections/03-motion/motor-stuck-protection/StuckVel.zh.md) | 1.024 |
| [InjectVelAmp](../../13-injection/InjectVelAmp.zh.md) | 1.024 |
| [Accel](../../10-motion/03-kinematics-configuration/Accel.zh.md) | 1.048576 |
| [Decel](../../10-motion/03-kinematics-configuration/Decel.zh.md) | 1.048576 |
| [Speed](../../10-motion/03-kinematics-configuration/Speed.zh.md) | 1.024 |
| [EmrgDec](../../10-motion/03-kinematics-configuration/EmrgDec.zh.md) | 1.048576 |
| [dPosRef](../../10-motion/01-kinematics-status/dPosRef.zh.md) | 1.024 |
| [DualStuckVel](../../06-protections/03-motion/dual-loop-stuck-protection/DualStuckVel.zh.md) | 1.024 |
| [ScheduleVel](../../11-control-tuning/01-general-keywords/ScheduleVel.zh.md) | 1.024 |
| [InTargetVelTh](../../10-motion/05-motion-status/InTargetVelTh.zh.md) | 1.024 |
| [SpeedChgNew](../../10-motion/03-kinematics-configuration/SpeedChgNew.zh.md) | 1.024 |
| AutoGVelTh | 1.024 |
| AutoGAccTh | 1.048576 |
| [MaxVelErrOL](../../06-protections/03-motion/general-maximum-limits/MaxVelErrOL.zh.md) | 1.024 |
| [CNCAVel](../../10-motion/09-motion-mode-cnc/CNCAVel-CNCBVel.zh.md) | 1.024 |
| [MapErrOnStep](../../04-error-mapping/MapErrOnStep.zh.md) | 1.024 |
| [JerkInAcc](../../10-motion/03-kinematics-configuration/JerkInAcc.zh.md) | 1.073741824 |
| [JerkInDec](../../10-motion/03-kinematics-configuration/JerkInDec.zh.md) | 1.073741824 |
| [RetractSpeed](../../08-axis-operation/02-position-operation-mode/RetractSpeed.zh.md) | 1.024 |
| [VecSpeed](../../10-motion/10-motion-mode-vector/VecSpeed.zh.md) | 1.024 |
| [VecAccel](../../10-motion/10-motion-mode-vector/VecAccel.zh.md) | 1.048576 |
| [VecDecel](../../10-motion/10-motion-mode-vector/VecDecel.zh.md) | 1.048576 |
| [VecEmrgDec](../../10-motion/10-motion-mode-vector/VecEmrgDec.zh.md) | 1.048576 |
| [VecdPosRef](../../10-motion/10-motion-mode-vector/VecdPosRef.zh.md) | 1.024 |
| [CNCBVel](../../10-motion/09-motion-mode-cnc/CNCAVel-CNCBVel.zh.md) | 1.024 |
| [ddPosRef](../../10-motion/01-kinematics-status/ddPosRef.zh.md) | 1.048576 |
| [dddPosRef](../../10-motion/01-kinematics-status/dddPosRef.zh.md) | 1.073741824 |

`MapErrOnStep` 是无量纲斜坡步长，不是速度；其内部计数器满量程仍为 16384。

## 时间

毫秒关键字使用 **16 个采样/ms**。例如，100 ms 对应 1600 个内部采样。以周期为单位的计数器和记录时间戳仍返回周期数：1000 个周期等于 62.5 ms。控制器元数据同时报告内部原始范围、默认值和换算系数。将这些原始值除以系数，并考虑整数舍入，才能解释为指令单位；不要将内部限值直接视为指令限值。例如，MapErrOnStep 报告的内部最大值为 16384，系数为 1.024；EC 接受的最大指令为 16000。

以下关键字使用毫秒换算：

`StuckTime`, `MaxVBusTime`, `InjectTimeOn`, `RptWait`, `DualStuckTime`, `ScheduleTime`, `InTargetTime`, `CurrCmdHTime`, `CurrCmdCntr`, `BrakeLockTime`, `BrakeRelTime`, `PDEndTime`, `UPMRptTime`, `ForceCmdHTime`, `ForceCmdCntr`, `ForceInTTime`.

传统 AGM800 的换算保持不变。此处为固件的标称换算约定，并非已完成物理硬件时序验证的声明。
