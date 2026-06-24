# 电机与驱动器

**概述：**

要设置一个轴，用户需要提供驱动器和电机信息。根据驱动器和电机的类型，还须配置其他关键字。

[AmpType](AmpType.md) 选择驱动模式（内置驱动器或外部），而 [MotorType](MotorType.md) 选择电机的换相方式。它与极对数（[PolePrs](PolePrs.md)）、编码器分辨率和步进设置（[StepBits](StepBits.md)）一起，馈入换相与电流生成级，其相电流参考在到达功率级之前由满量程设置（[AAmpFullScale](AAmpFullScale.md)、[LAmpFullScale](LAmpFullScale.md)）进行缩放。

![Motor and amplifier interface: AmpType sets the drive mode and MotorType sets commutation; with pole pairs, encoder resolution and stepping settings they feed commutation and current generation, which scales phase-current references by the full-scale settings and sends them to the power stage that drives the motor windings](motor-amplifier-interface.svg)

下表汇总了电机与驱动器关键字。

| No. | Keywords                                                                   | Summary                                                   |
| --- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1   | [AAmpFullScale](../../02-keywords/02-motor-and-amplifier/AAmpFullScale.md) | 外部驱动器的满量程输出值            |
| 2   | [AmpType](../../02-keywords/02-motor-and-amplifier/AmpType.md)             | 轴驱动器模式                                       |
| 3   | [LAmpFullScale](../../02-keywords/02-motor-and-amplifier/LAmpFullScale.md) | 内置直线驱动器的满量程输出选择 |
| 4   | [MagneticPitch](../../02-keywords/02-motor-and-amplifier/MagneticPitch.md) | 直线电机磁极距（以毫米为单位）                |
| 5   | [MotorType](../../02-keywords/02-motor-and-amplifier/MotorType.md)         | 轴电机类型                                       |
| 6   | [PolePrs](../../02-keywords/02-motor-and-amplifier/PolePrs.md)             | 电机的极对数                         |
| 7   | [StepBits](../../02-keywords/02-motor-and-amplifier/StepBits.md)           | 每个电气周期的步进位数              |
| 8   | [StepInMotCurr](../../02-keywords/02-motor-and-amplifier/StepInMotCurr.md) | 运动中使用的步进相电流                     |
| 9   | [StepInPosCurr](../../02-keywords/02-motor-and-amplifier/StepInPosCurr.md) | 静止时使用的步进相电流                  |
