# 稳定性诊断

稳定性诊断在运行时监测闭环状态，若检测到振荡或噪声过大，会在不稳定环路损坏电机或负载之前关断轴。

系统提供两个独立的检测器。电流环稳定性检测器将测量到的电机电流的方差与指令电流参考的方差进行比较：当电机电流的波动远大于指令且跟踪误差持续偏大时，则判定电流环出现振荡。位置/速度（PIV）噪声检测器在轴保持指令静止时监测电流参考的方差，此时参考值应保持平稳；若方差偏高，则表明噪声或抖动正通过位置/速度环传导。

两个检测器均在滑动窗口内计算运行统计量，并与轴峰值电流限值导出的阈值进行比较。阈值被超出时，检测器关断电机并记录控制器故障，通过 [ConFlt](../../07-status-and-faults/ConFlt.md) 上报：电流环不稳定对应故障码 1071，PIV 噪声/抖动过高对应故障码 1072。每个检测器还提供只读状态数组，整定期间可查看实时统计量和当前生效的阈值。

这些关键字仅从 v5（central-i）起可用。

以下是稳定性诊断关键字汇总。

| 序号 | 关键字 | 说明 |
|----|----|----|
| 1 | [CurrStbleDtct](CurrStbleDtct.md) | 电流环稳定性检测器使能 |
| 2 | [CurrStbleErr](CurrStbleErr.md) | 电流环跟踪误差阈值（占峰值电流限值的百分比） |
| 3 | [CurrStbleSTD](CurrStbleSTD.md) | 电流环方差阈值（占峰值电流限值的百分比） |
| 4 | [CurrStbleStat](CurrStbleStat.md) | 电流环稳定性检测器状态数组 |
| 5 | [PIVNoiseDtct](PIVNoiseDtct.md) | PIV 噪声检测器使能 |
| 6 | [PIVNoiseSTD](PIVNoiseSTD.md) | PIV 噪声方差阈值（占峰值电流限值的百分比） |
| 7 | [PIVNoiseWSize](PIVNoiseWSize.md) | PIV 噪声采样窗口大小 |
| 8 | [PIVNoiseStat](PIVNoiseStat.md) | PIV 噪声检测器状态数组 |
