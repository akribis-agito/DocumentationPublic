---
summary: 报告 A 组（或 B 组）当前活动 CNC 段的减速度。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CNCADecel/CNCBDecel

报告 A 组（或 B 组）当前活动 CNC 段的减速度。

## 概述

`CNCADecel`（及其对应项 `CNCBDecel`）是只读参数，以用户单位每秒平方报告 A 组（或 B 组）当前活动 CNC 段路径速度曲线的减速度。它反映压入队列的段中编码的减速度。该参数为非轴只读参数，不保存至闪存。

## 工作原理

当路径接近当前活动段末尾时，控制器根据距段长度 [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) 的剩余距离、当前减速度 `CNCADecel` 以及目标段末速度 [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) 计算减速限值。当路径速度 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 超过该限值时，规划器以 `CNCADecel` 制动，使路径速度在段终点恰好达到末速度。这种前瞻机制使连续段能够以非零转角速度混合。

若某段以过高速度进入，无法在剩余距离内以 `CNCADecel` 制动至其末速度，控制器将针对该段剩余部分提高减速度（一次性重新计算更高速率），而非强制产生速度跳变。

### 轨迹数学

每个控制周期，控制器计算在剩余距离内仍能制动至段末速度的最高路径速度，使用标准运动学关系：

$$v_{\text{brake}} = -\,a_{\text{eff}}\,T_s + \sqrt{a_{\text{eff}}^{\,2}\,T_s^{\,2} + 2\,a_{\text{eff}}\,(\text{CNCAAbsTrgt} - \text{CNCAPosRef}) + \text{CNCAEndSpeed}^2}$$

其中 $T_s$ 为控制周期时间，$a_{\text{eff}}$ 为本周期实际生效的减速度（如下所述，报告的 `CNCADecel` 乘以时间缩放因子的平方）。当当前路径速度 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 超过 $v_{\text{brake}}$ 时，规划器制动，使 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 在 [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 到达 [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) 时恰好等于 [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md)。

若某段以过高速度进入，无法以当前减速度在剩余距离内制动至末速度，直接跳到 $v_{\text{brake}}$ 将产生速度跳变。仅当该跳变大于当前路径速度的 1% 时，控制器才针对该段剩余部分切换至一次性重新计算的更高减速度：

$$a_{\text{new}} = \frac{\text{CNCAdPosRef}^2 - \text{CNCAEndSpeed}^2}{2\,(\text{CNCAAbsTrgt} - \text{CNCAPosRef})}$$

以确保路径在终点仍达到末速度；较小的偏差则直接将路径速度吸附到减速曲线上处理。

每个周期实际使用的有效减速度，是报告的段值乘以实时时间缩放因子 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 的平方：有效减速度 = `CNCADecel × (CNCAPercents/100)²`。纯速度倍率 [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) **不**缩放减速度。这是*正常*制动速率；紧急停止时使用独立的、更大的速率 [CNCAEmrgDec/CNCBEmrgDec](CNCAEmrgDec-CNCBEmrgDec.md)。

`CNCADecel` 作用于**路径**（合成）速度；几何关系将制动分配到各成员轴。

### CNCB 说明

`CNCBDecel` 报告独立第二 CNC 组的相同量。

## 示例

```text
ACNCADecel          ; 读取 A 组当前活动段减速度
ACNCBDecel          ; 读取 B 组当前活动段减速度
```

## 另请参阅

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — 当前活动段加速度
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — 减速前瞻所针对的目标速度
- [CNCAEmrgDec/CNCBEmrgDec](CNCAEmrgDec-CNCBEmrgDec.md) — 紧急停止减速度（独立，更大）
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 以其因子的平方缩放减速度
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已排队的段数据
