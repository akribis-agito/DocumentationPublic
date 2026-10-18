# 摩擦前馈

AGM800 和 AGM800-EC（central-i v5）具有一个摩擦前馈环节。它根据速度算出轴克服摩擦所需的电流，并把该电流加入前馈通路，使速度环不必先通过跟随误差才发现摩擦。

它不同于 [FrictionComp](FrictionComp.md)。`FrictionComp` 在运动开始时一次性预置速度环积分器；摩擦前馈环节则在每个控制周期起作用。

## 环节示意

$$
\text{FricMethod model} \;+\; \text{quadrant-switching kick} \;\longrightarrow\; \boxed{\pm\,\text{FricLim}} \;\longrightarrow\; \text{feedforward sum} \;\longrightarrow\; \text{CNC skip} \;\longrightarrow\; \boxed{\text{FFFiltOn / FFFiltDef}} \;\longrightarrow\; \text{CurrRef}
$$

1. **模型。** [FricMethod](FricMethod.md) 选择摩擦模型（0 = 关闭，1 至 5）。
2. **象限切换冲击（可选）。** [FricQSCOn](FricQSCOn.md) = 1 时，在起动和换向时叠加短暂的起动冲击（仅方法 0 至 3）。
3. **一个钳位。** [FricLim](FricLim.md) 把总输出限制在 [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md) 的 ±`FricLim` %。
4. **前馈通路。** 钳位后的摩擦电流在 CNC 跳过*之前*、前馈滤波器*之前*加入前馈总和：
   - 在 CNC 段切换时，固件将全部前馈清零两个控制周期。摩擦随其余前馈一起清零——所有前馈遵循同一规则。
   - [FFFiltOn](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltOn.md) = 1 时，摩擦与加速度、速度前馈经过同一个滤波器（[FFFiltDef](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltDef.md)）。
5. **何时运行。** 只要由速度环形成电流参考就运行：位置模式、速度模式，以及 [ForcePIVOn](../../02-keywords/11-control-tuning/07-force-control/ForcePIVOn.md) = 1 的力模式。在速度模式和力模式下，滤波器只承载摩擦，因为 [AccFFW](../../02-keywords/11-control-tuning/05-feedforwards/AccFFW.md) 和 [VelFFW](../../02-keywords/11-control-tuning/05-feedforwards/VelFFW.md) 仅在位置模式下起作用。在其他模式下，该环节关闭，其内部状态被清除。

**读回。** [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md)`[6]` 是滤波器*之前*的摩擦电流。`CurrFFWValues[1]` 是进入电流参考的滤波后总量，现在包含摩擦。

**滤波延迟。** `FFFiltOn` = 1 时，换向处的摩擦阶跃会被滤波器平滑并延迟。如需在换向处获得陡峭的补偿，请在 `FFFiltOn` = 0 下整定，或选择延迟小的滤波器。

## 模型

| `FricMethod` | 模型 | 使用的关键字 |
|---|---|---|
| 0 | 关闭 | — |
| 1 | 过零线性斜坡 | FricIPos/Neg、FricVBandPos/Neg、FricViscous |
| 2 | 滞环（带记忆的切换） | FricIPos/Neg、FricVBandPos/Neg、FricViscous |
| 3 | 间隙（带斜坡的滞环） | FricIPos/Neg、FricVBandPos/Neg、FricViscous |
| 4 | LuGre（刷毛模型） | FricIPos/Neg、FricIStatPos/Neg、FricVStribPos/Neg、FricBrstlStf、FricBrstlDmp、FricViscous |
| 5 | Stribeck | FricIPos/Neg、FricIStatPos/Neg、FricVBandPos/Neg、FricVStribPos/Neg、FricViscous |

方法 5 对速度 $v$（来自 [FricVelSrc](FricVelSrc.md)）和速度反馈 $v_{fb}$，按运动方向取值：

$$
I = \operatorname{sign}(v)\cdot\tanh\!\left(\frac{|v|}{\text{FricVBand}}\right)\cdot\left(\text{FricI} + (\text{FricIStat} - \text{FricI})\,e^{-(v/\text{FricVStrib})^2}\right) + \text{FricViscous}\cdot v_{fb}
$$

各电平取幅值；符号取自运动方向。

## 关键字

| CAN | 关键字 | 设置内容 |
|---|---|---|
| 921 | [FricVStribPos](FricVStribPos.md) | 正方向 Stribeck 速度（counts/s） |
| 922 | [FricVStribNeg](FricVStribNeg.md) | 负方向 Stribeck 速度（counts/s） |
| 925 | [FricLim](FricLim.md) | 整个环节的钳位（PeakCL 的 %） |
| 926 | [FricMethod](FricMethod.md) | 模型：0 关闭，1 线性，2 滞环，3 间隙，4 LuGre，5 Stribeck |
| 927 | [FricVelSrc](FricVelSrc.md) | 速度来源：0 dPosRef，1 VelRef，2 反馈 |
| 928 | [FricIPos](FricIPos.md) | 正方向库仑电平（mA） |
| 929 | [FricINeg](FricINeg.md) | 负方向库仑电平（mA） |
| 930 | [FricVBandPos](FricVBandPos.md) | 正侧过零死区带（counts/s） |
| 931 | [FricVBandNeg](FricVBandNeg.md) | 负侧过零死区带（counts/s） |
| 932 | [FricViscous](FricViscous.md) | 粘性斜率（mA 每 count/s） |
| 933 | [FricIStatPos](FricIStatPos.md) | 正方向起动电平（mA） |
| 934 | [FricIStatNeg](FricIStatNeg.md) | 负方向起动电平（mA） |
| 935 | [FricBrstlStf](FricBrstlStf.md) | LuGre 刷毛刚度 σ0 |
| 936 | [FricBrstlDmp](FricBrstlDmp.md) | LuGre 刷毛阻尼 σ1 |
| 938 | [FricQSCOn](FricQSCOn.md) | 象限切换冲击开/关 |
| 939 | [FricQSCTime](FricQSCTime.md) | 冲击衰减时间常数（µs） |
| 940 | [FricQSCHold](FricQSCHold.md) | 冲击前的保持时间（µs） |

## FricLim

`FricLim` 目前保持现状：整个环节一个钳位，默认值为 `PeakCL` 的 40%。固件不会报告钳位正在限幅。摩擦环节是否需要单独的钳位尚待确定（Firmware-Main #1423）。

## 重力和恒定偏置

摩擦电平只用于摩擦。请将竖直轴的重力、弹簧预紧或其他任何恒定电流放入 [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md)（由 [TorqCompMode](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompMode.md) 选择），而不是 `FricIPos`/`FricINeg`。

## 整定顺序

请在 `FFFiltOn` = 0 下整定，以免滤波器掩盖摩擦的作用。

1. **消除偏置。** 用 [TorqCompMode](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompMode.md) 选择一个固定补偿项（例如 `TorqCompMode` = 1），并设置 [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md) 的对应项（此处为 `TorqCompFix[1]`），使轴静止保持时以及低速向两个方向运动时电流相同。此步骤在 `FricMethod` = 0 下进行。
2. **各方向电平。** 在每个方向以恒定低速运动，将 `FricIPos` 和 `FricINeg` 设为速度环仍需提供的电流。对于方法 4 和 5，接着设置起动电平 `FricIStatPos`/`FricIStatNeg` 和 Stribeck 速度 `FricVStribPos`/`FricVStribNeg`。将死区带 `FricVBandPos`/`FricVBandNeg` 设得略高于速度噪声。
3. **斜率。** 最后，在几个更高的速度下运行，设置 `FricViscous`，使剩余电流不再随速度增大。

如果使用前馈滤波器，再把 `FFFiltOn` 重新打开，并检查换向情况。

## 相对 5.3.0-rc4 的变更

5.3.0 把 rc4 的 Stribeck 前馈并入该环节，成为 `FricMethod` = 5，并更名了若干关键字。**没有兼容层**：在 rc4 下保存的值不会被转换。升级后，请重新输入摩擦设置。

| rc4 关键字（CAN） | 5.3.0 | 说明 |
|---|---|---|
| StribOn (920) | `FricMethod` = 5 | 代码 920 现已不再使用。 |
| StribVs (921) | [FricVStribPos](FricVStribPos.md) / [FricVStribNeg](FricVStribNeg.md) | 现在按方向分别设置；921 为 `FricVStribPos`。 |
| StribEps (922) | [FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md) | tanh 宽度即死区带；922 现为 `FricVStribNeg`。 |
| StribFc (923) | [FricIPos](FricIPos.md) / [FricINeg](FricINeg.md) | 代码 923 现已不再使用。 |
| StribFsEx (924) | [FricIStatPos](FricIStatPos.md) / [FricIStatNeg](FricIStatNeg.md) | 现为绝对电平：rc4 StribFc + StribFsEx。代码 924 现已不再使用。 |
| StribLim (925) | [FricLim](FricLim.md) | 代码不变；现在钳位整个环节。 |
| FricVBlindPos / FricVBlindNeg (930/931) | [FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md) | 已更名，代码不变。 |
| FricSigma0 / FricSigma1 (935/936) | [FricBrstlStf](FricBrstlStf.md) / [FricBrstlDmp](FricBrstlDmp.md) | 已更名，代码不变。 |
| FricCurr (937) | [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md)`[6]` | 代码 937 现已不再使用。 |
| FricQSCDelay (940) | [FricQSCHold](FricQSCHold.md) | 代码不变；单位由控制周期改为 µs。 |

LuGre（方法 4）现在从 `FricVStribPos`/`FricVStribNeg` 读取 Stribeck 速度；在 rc4 中它读取的是死区带。

在 5.3.0 中重现 rc4 的 Stribeck 行为：`FricMethod` = 5，`FricIPos` = StribFc，`FricINeg` = −StribFc，`FricIStatPos` = StribFc + StribFsEx，`FricIStatNeg` = −(StribFc + StribFsEx)，`FricVBandPos` = `FricVBandNeg` = StribEps，`FricVStribPos` = `FricVStribNeg` = StribVs，`FricLim` = StribLim，`FricViscous` = 0，`FricVelSrc` = 0。

## 另请参阅

- [FrictionComp](FrictionComp.md) — 运动开始时一次性预置积分器（另一种机制）
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — 前馈读回
- [前馈](../../02-keywords/11-control-tuning/05-feedforwards/00-overview.md)
