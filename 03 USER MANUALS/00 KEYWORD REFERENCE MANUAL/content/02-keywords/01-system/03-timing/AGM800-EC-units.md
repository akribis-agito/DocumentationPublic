---
summary: AGM800-EC timing and units
last_updated: '2026-10-10'
doc_revision: '2026.10'
---
# AGM800-EC timing and units

AGM800-EC (Identity product type 16) uses a nominal **16,000 Hz** control rate: **62.5 µs per cycle**. Time conversions use this rate; internal fixed-point accumulators keep their `2^14 = 16384` scale. These two numbers are not interchangeable.

## Command and status conversion

The table lists the fixed time-domain conversions. For writable keywords, writes multiply by the factor; reads divide by it. Integer storage and integer replies require rounding. Embedded `UsrUnits`, `AuxUsrUnits` and `PDUsrUnits` do not apply to these entries. Position keywords retain their position scaling. Host global engineering-unit settings are a separate layer.

| Keyword | Factor |
|---|---|
| [Vel](../../10-motion/01-kinematics-status/Vel.md) | 1.024 |
| [AuxVel](../../10-motion/01-kinematics-status/AuxVel.md) | 1.024 |
| [PDVel](../../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md) | 1.024 |
| [VelErr](../../10-motion/01-kinematics-status/VelErr.md) | 1.024 |
| [VelRef](../../10-motion/01-kinematics-status/VelRef.md) | 1.024 |
| [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) | 1.024 |
| [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.md) | 1.024 |
| [StuckVel](../../06-protections/03-motion/motor-stuck-protection/StuckVel.md) | 1.024 |
| [InjectVelAmp](../../13-injection/InjectVelAmp.md) | 1.024 |
| [Accel](../../10-motion/03-kinematics-configuration/Accel.md) | 1.048576 |
| [Decel](../../10-motion/03-kinematics-configuration/Decel.md) | 1.048576 |
| [Speed](../../10-motion/03-kinematics-configuration/Speed.md) | 1.024 |
| [EmrgDec](../../10-motion/03-kinematics-configuration/EmrgDec.md) | 1.048576 |
| [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) | 1.024 |
| [DualStuckVel](../../06-protections/03-motion/dual-loop-stuck-protection/DualStuckVel.md) | 1.024 |
| [ScheduleVel](../../11-control-tuning/01-general-keywords/ScheduleVel.md) | 1.024 |
| [InTargetVelTh](../../10-motion/05-motion-status/InTargetVelTh.md) | 1.024 |
| [SpeedChgNew](../../10-motion/03-kinematics-configuration/SpeedChgNew.md) | 1.024 |
| AutoGVelTh | 1.024 |
| AutoGAccTh | 1.048576 |
| [MaxVelErrOL](../../06-protections/03-motion/general-maximum-limits/MaxVelErrOL.md) | 1.024 |
| [CNCAVel](../../10-motion/09-motion-mode-cnc/CNCAVel-CNCBVel.md) | 1.024 |
| [MapErrOnStep](../../04-error-mapping/MapErrOnStep.md) | 1.024 |
| [JerkInAcc](../../10-motion/03-kinematics-configuration/JerkInAcc.md) | 1.073741824 |
| [JerkInDec](../../10-motion/03-kinematics-configuration/JerkInDec.md) | 1.073741824 |
| [RetractSpeed](../../08-axis-operation/02-position-operation-mode/RetractSpeed.md) | 1.024 |
| [VecSpeed](../../10-motion/10-motion-mode-vector/VecSpeed.md) | 1.024 |
| [VecAccel](../../10-motion/10-motion-mode-vector/VecAccel.md) | 1.048576 |
| [VecDecel](../../10-motion/10-motion-mode-vector/VecDecel.md) | 1.048576 |
| [VecEmrgDec](../../10-motion/10-motion-mode-vector/VecEmrgDec.md) | 1.048576 |
| [VecdPosRef](../../10-motion/10-motion-mode-vector/VecdPosRef.md) | 1.024 |
| [CNCBVel](../../10-motion/09-motion-mode-cnc/CNCAVel-CNCBVel.md) | 1.024 |
| [ddPosRef](../../10-motion/01-kinematics-status/ddPosRef.md) | 1.048576 |
| [dddPosRef](../../10-motion/01-kinematics-status/dddPosRef.md) | 1.073741824 |

`MapErrOnStep` is a dimensionless ramp step, not a velocity; its internal counter full scale remains 16384.

## Time

Millisecond keywords use **16 samples/ms**. For example, 100 ms corresponds to 1600 internal samples. Cycle counters and cycle-based logging timestamps still return cycles: 1000 cycles equals 62.5 ms. Controller metadata reports raw internal ranges and defaults alongside the conversion factor. Divide those raw values by the factor to interpret them in command units, allowing for integer rounding; do not treat raw bounds as command bounds. For example, MapErrOnStep reports an internal maximum of 16384 and a factor of 1.024; its largest accepted EC command is 16000.

The millisecond conversion applies to:

`StuckTime`, `MaxVBusTime`, `InjectTimeOn`, `RptWait`, `DualStuckTime`, `ScheduleTime`, `InTargetTime`, `CurrCmdHTime`, `CurrCmdCntr`, `BrakeLockTime`, `BrakeRelTime`, `PDEndTime`, `UPMRptTime`, `ForceCmdHTime`, `ForceCmdCntr`, `ForceInTTime`.

Legacy AGM800 conversions remain unchanged. These are the firmware’s nominal conversion rules, not a claim of physical timing qualification.
