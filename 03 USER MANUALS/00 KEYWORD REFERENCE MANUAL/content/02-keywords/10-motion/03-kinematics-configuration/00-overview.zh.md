# 运动学参数配置

运动学参数配置用于塑造运动的速度曲线。这些关键字大多可在运动前和运动期间设置，因为运动曲线是实时计算的。轨迹规划器以加速度速率将轴加速至巡航速度，保持该速度，然后以减速度速率制动；加加速度设置对拐角进行圆滑处理，以柔化运动的起点和终点。

![速度曲线：梯形与 S 曲线](velocity-profile.svg)

下面是与运动学相关的关键字。

| No. | Keyword | Summary |
|-----|---------|---------|
| 1 | [Accel](Accel.md) | 运动的加速度速率（曲线的前沿斜坡）。 |
| 2 | [Decel](Decel.md) | 运动的减速度速率（曲线的后沿斜坡）。 |
| 3 | [Speed](Speed.md) | 规划器加速趋向的巡航（目标）速度。 |
| 4 | [AccelFact](AccelFact.md) | 同时应用于 `Accel` 和 `Decel` 的整数倍乘子。 |
| 5 | [EmrgDec](EmrgDec.md) | 用于限位/受控停止原因的紧急减速度速率。 |
| 6 | [Jerk](Jerk.md) | 二阶 S 曲线平滑窗口（`2^Jerk` 个周期）。 |
| 7 | [JerkInAcc](JerkInAcc.md) | 加速阶段的加加速度限值（三阶曲线）。 |
| 8 | [JerkInDec](JerkInDec.md) | 减速阶段的加加速度限值（三阶曲线）。 |
| 9 | [JerkMode](JerkMode.md) | 选择规划器阶数（参见运动配置）。 |
| 10 | [AccShapeOn](AccShapeOn.md) | 启用距离到目标的加速度整形。 |
| 11 | [AccShapeDist](AccShapeDist.md) | 加速度整形的逐段距离阈值。 |
| 12 | [AccShapeFact](AccShapeFact.md) | 加速度整形的逐段加速度缩放因子。 |
| 13 | [SpeedChgOn](SpeedChgOn.md) | 启用位置触发的运行中速度变更。 |
| 14 | [SpeedChgPos](SpeedChgPos.md) | 触发速度变更的位置。 |
| 15 | [SpeedChgNew](SpeedChgNew.md) | 在触发点应用的新速度。 |
| 16 | [SpeedChgDir](SpeedChgDir.md) | 触发生效的方向。 |
| 17 | [RefOffsetSamp](RefOffsetSamp.md) | 参考偏置接入所历经的伺服采样数。 |
| 18 | [RefOffsetStep](RefOffsetStep.md) | 参考偏置的逐采样幅值。 |
| 19 | [SetPosition](SetPosition.md) | 在不移动电机的情况下重新定义轴位置。 |
| 20 | [ZeroPosErr](ZeroPosErr.md) | 通过将参考对齐到反馈来将位置误差清零。 |

点到点目标 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) 和 [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) 在“运动模式 – 点到点”下描述。
