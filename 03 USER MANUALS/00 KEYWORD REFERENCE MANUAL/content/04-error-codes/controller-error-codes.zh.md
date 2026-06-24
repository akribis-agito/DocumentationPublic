# 控制器错误代码

*错误代码*

控制器运行期间，可能发生导致轴禁用的故障。错误代码被赋值至 [ConFlt](../02-keywords/07-status-and-faults/ConFlt.md) 并记录于 ErrLog。

以下为控制器错误代码及其说明列表。

| 错误代码 | 说明 |
|---|---|
| 0 | 无错误 |
| 1001 | 检测到中止信号 |
| 1002 | 电机相线对地短路 |
| 1003 | 编码器断开连接 |
| 1004 | 未收到 FPGA 看门狗信号 |
| 1005 | PWM 死区时间过短 |
| 1006 | 霍尔输入断开连接 |
| 1007 | 电机堵转 |
| 1008 | 母线电压过高 |
| 1009 | 母线电压过低 |
| 1010 | 逻辑电源电压过高 |
| 1011 | 逻辑电源电压过低 |
| 1012 | 母线电流过高 |
| 1013 | A 相电流过高 |
| 1014 | B 相电流过高 |
| 1015 | C 相电流过高 |
| 1016 | 电机电流过高 |
| 1017 | 驱动器功率超限 |
| 1018 | IPM 温度过高 |
| 1019 | 速度过高 |
| 1020 | 位置误差超限 |
| 1021 | 速度误差超限 |
| 1022 | CPU 温度过高 |
| 1023 | 母线电压过高——超过绝对限值 |
| 1024 | STO1 已激活 |
| 1025 | 检测到过流 |
| 1026 | 辅助编码器断开连接 |
| 1027 | IPM 故障 |
| 1028 | 所选编码器类型当前不受支持 |
| 1029 | 所选辅助编码器类型当前不受支持 |
| 1030 | ECAM 主变量在 1 个采样内变化超过 1 个 ECAM 周期 |
| 1031 | FIFO 到达一个运动段，该段的加速度过小：<br>低于 1/Ts |
| 1032 | 主编码器取模功能不可与输入整形功能同时使用 |
| 1033 | 上电自检（BIT）期间检测到故障，请读取 BITFault 获取故障码 |
| 1034 | STO2 已激活，或驱动器 Vcc 异常 |
| 1035 | 控制器的交流电源被切断 |
| 1036 | 电机 B 检测到过流 |
| 1037 | 内置线性驱动器检测到持续过流 |
| 1038 | 内置线性驱动器检测到过压 |
| 1039 | AAmpType 与 BAmpType 的值冲突，不能一个为线性、一个为 PWM |
| 1040 | 电机温度过高 |
| 1041 | 未知错误代码，请联系 Agito |
| 1042 | 驱动器隔离 5V 故障 |
| 1043 | CI 通信断开 |
| 1044 | 电机电流超过 I2T |
| 1045 | 力误差超限 |
| 1046 | 力控制：模拟力反馈未定义 |
| 1047 | 编码器或 I/O 的某一 5V 输出引脚触发了电流限制，<br>请检查硬件连接！ |
| 1048 | 同组另一轴电机关闭 |
| 1049 | 双环速度差异过大 |
| 1050 | 外部故障输入（如外部驱动器）已激活 |
| 1051 | 内部继电器仍处于断开状态，请在上电后等待更长时间再使能电机 |
| 1052 | STO2 已激活 |
| 1053 | 本产品不允许使用该 AmpType 值 |
| 1054 | 交流电源至少一路必需相位被切断 |
| 1055 | 开环模式下位置误差超限 |
| 1056 | 开环模式下速度误差超限 |
| 1057 | 开环模式下力误差超限 |
| 1058 | 10.5V 电源欠压（阈值 8V） |
| 1059 | 电机 C 检测到过流 |
| 1060 | 产品温度（BoardTemp）过高 |
| 1061 | 龙门另一成员轴电机关闭 |
| 1062 | 外部请求受控停止触发故障：停止完成，电机已禁用 |
| 1063 | 同组另一轴电机关闭 |
| 1064 | 编码器正弦/余弦读取错误 |
| 1065 | 堵转检测已激活，电机正在关闭 |
| 1066 | 虚拟编码器每次中断的脉冲数超过最大允许值 |
| 1067 | 系统检测到异常/碰撞（仅 v5） |
| 1068 | 绝对值编码器错误位已置位，读头可能异常，或编码器刻度尺需检查 |
| 1069 | 绝对值编码器 CRC 校验失败超过 EncAbsErrTime 设定的时间阈值，噪声水平可能过高 |
| 1070 | 绝对值编码器无法检测到，疑似断开连接 |
| 1071 | 检测到电流环不稳定（仅 v5） |
| 1072 | 检测到高噪声/抖动（仅 v5） |
| 1080 | 未检测到定相结果（仅 v5） |
| 1081 | CPU 后台循环看门狗超时 |

## 常见保护的跳闸条件

每种禁用轴的保护均有与客户关键字相关联的定义跳闸条件。某些故障在单个采样越限时立即触发；另一些故障则需在消抖期间（以控制器采样数计）持续满足条件后才会触发。下表汇总了最常见的故障码；表中列出的限值名称为可调节的已记录关键字。

| 故障码 | 跳闸条件 | 消抖 |
|---|---|---|
| 1003 | 硬件报告主编码器断开或错误 | 立即（硬件） |
| 1007 | 速度持续低于/等于 [StuckVel](../02-keywords/06-protections/03-motion/motor-stuck-protection/StuckVel.md) 且电机电流持续高于/等于 [StuckCurr](../02-keywords/06-protections/03-motion/motor-stuck-protection/StuckCurr.md) | 持续 [StuckTime](../02-keywords/06-protections/03-motion/motor-stuck-protection/StuckTime.md) 个采样 |
| 1008 | 母线电压超过 [MaxVBus](../02-keywords/06-protections/02-current-and-voltage/MaxVBus.md) | 持续 [MaxVBusTime](../02-keywords/06-protections/02-current-and-voltage/MaxVBusTime.md) 个采样 |
| 1009 | 母线电压低于/等于 [MinVBus](../02-keywords/06-protections/02-current-and-voltage/MinVBus.md) | 立即（单个采样） |
| 1013–1016 | 相电流或电机电流超过过流限值 | 持续 4 个连续采样 |
| 1018 | 功率级温度超过 [MaxPwrTemp](../02-keywords/06-protections/07-board-temperature/MaxPwrTemp.md) | 单个采样 |
| 1019 | 速度反馈幅值超过 1.25 × [MaxVel](../02-keywords/06-protections/03-motion/general-maximum-limits/MaxVel.md) | 单个采样 |
| 1020 | 位置误差幅值超过 [MaxPosErr](../02-keywords/06-protections/03-motion/general-maximum-limits/MaxPosErr.md)（开环变体 `1055`） | 单个采样 |
| 1021 | 速度误差幅值超过 [MaxVelErr](../02-keywords/06-protections/03-motion/general-maximum-limits/MaxVelErr.md)（开环变体 `1056`） | 单个采样 |
| 1023 | 母线电压超过绝对限值 [MaxVBusAbs](../02-keywords/06-protections/02-current-and-voltage/MaxVBusAbs.md) | 立即（无消抖） |
| 1040 | 电机温度超过 [MaxMotorTemp](../02-keywords/06-protections/05-motor-temperature/MaxMotorTemp.md)；仅在使用电机温度传感器时有效（[MotorTempUsed](../02-keywords/06-protections/05-motor-temperature/MotorTempUsed.md) ≠ 0） | 单个采样 |
| 1049 | 双环速度差超过 [DualStuckVel](../02-keywords/06-protections/03-motion/dual-loop-stuck-protection/DualStuckVel.md) | 持续 [DualStuckTime](../02-keywords/06-protections/03-motion/dual-loop-stuck-protection/DualStuckTime.md) 个采样 |
| 1060 | 产品温度（[BoardTemp](../02-keywords/06-protections/07-board-temperature/BoardTemp.md)）超过固定内部限值（不可调节） | 单个采样 |
