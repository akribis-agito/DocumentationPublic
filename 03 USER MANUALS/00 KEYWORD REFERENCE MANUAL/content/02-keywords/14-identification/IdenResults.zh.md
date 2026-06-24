---
keyword: IdenResults
summary: 只读数组，存储正弦扫频辨识所计算的输入/输出关系。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 127
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 12
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 23
    data_type: float64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IdenResults

只读数组，存储正弦扫频辨识所计算的输入/输出关系。

## 概述

`IdenResults` 存储记录的输入向量与输出向量之间的计算关系。该关键字仅适用于正弦扫频辨识，在 [CalcIden](CalcIden.md) 操作完成后更新。基波（第一谐波）频率是指 [InjectFreq](../13-injection/InjectFreq.md) 中定义的频率。这些数值通过 [PlantModel](PlantModel.md) 向自整定和滤波器设计算法提供输入。

## 工作原理

各数组元素的详细说明如下（数组从 1 开始索引）。每对中较小的索引（1–11）保存所有变型均支持的单一结果集；较大的索引（12–22）仅在 Central-i v5 上存在，保存第二结果集（参见下方双环说明）。

| 索引 | 说明 |
|----|----|
| 1, 12 | 基波正弦频率处输出与输入的幅值比（实部） |
| 2, 13 | 基波正弦频率处输出与输入的幅值比（虚部） |
| 3, 14 | 谐波质量（第二谐波与第一/基波谐波的幅值比），以百分比表示 |
| 4, 15 | 噪声质量（实际输出与建模输出之间误差的均方根值与输出基波正弦幅值之比），以百分比表示 |
| 5, 16 | 基波正弦波输出与输入的幅值比，以 dB/100 表示（原始值为 dB 乘以 100；PCSuite 除以 100 后显示 dB） |
| 6, 17 | 输出与输入基波正弦波之间的相位差，以 deg/100 表示 |
| 7, 18 | 输出基波正弦波的幅值 |
| 8, 19 | 输入基波正弦波的幅值 |
| 11, 22 | 输出基波正弦波的幅值，乘以 1000 |

对于标准辨识，有 1 个输入向量和 1 个输出向量，结果填充在数组索引 1 至 11 中。在 v4（独立 v4 和 Central-i v4）上，仅存在索引 1 至 11 中的单一结果集。

双环系统被控对象辨识及索引 12 至 22 中的第二结果集仅适用于 Central-i v5。在该情况下，有 1 个输入向量和 2 个输出向量。记录顺序为：先是输入，然后是负载端（主编码器）输出，再是电机端（辅助编码器）输出。相应地，负载端（主编码器）输出与输入之间的关系位于索引 1 至 11，电机端（辅助编码器）输出与输入之间的关系位于索引 12 至 22。

### 结果公式

各条目由 [CalcIden](CalcIden.md) 中最小二乘拟合产生的输入和输出基波正弦/余弦系数推导而来。设 $a_{in}, b_{in}$ 为输入基波正弦和余弦系数，$a_{out}, b_{out}$ 为对应的输出系数；$a_2, b_2$ 为输出第二谐波系数。

基波处的复数频率响应 $H = \text{output}/\text{input}$ 为

$$\operatorname{Re}(H) = \frac{a_{out}\,a_{in} + b_{out}\,b_{in}}{a_{in}^2 + b_{in}^2}, \qquad \operatorname{Im}(H) = \frac{-a_{out}\,b_{in} + b_{out}\,a_{in}}{a_{in}^2 + b_{in}^2}$$

分别存储在索引 1（实部）和 2（虚部）中。基波幅值为

$$A_{out} = \sqrt{a_{out}^2 + b_{out}^2}\ \ (\text{index } 7), \qquad A_{in} = \sqrt{a_{in}^2 + b_{in}^2}\ \ (\text{index } 8)$$

索引 11 保存 $A_{out} \times 1000$。增益（索引 5）和相位（索引 6）为

$$[\text{gain}] = 100 \cdot 20\log_{10}|H| \quad (\text{dB}\times 100), \qquad [\text{phase}] = 100 \cdot \frac{180}{\pi}\operatorname{atan2}\!\big(\operatorname{Im}(H), \operatorname{Re}(H)\big) \quad (\text{deg}\times 100)$$

两者均乘以 100 以在通信链路上保持分辨率；PCSuite 除以 100 后显示。质量指标为

$$[\text{harmonic}] = 100 \cdot \frac{\sqrt{a_2^2 + b_2^2}}{A_{out}}\ \%\ \ (\text{index } 3), \qquad [\text{noise}] = 100 \cdot \frac{\sqrt{\tfrac{1}{N}\sum (y_{fit} - y_{out})^2}}{A_{out}}\ \%\ \ (\text{index } 4)$$

其中 $y_{fit}$ 为建模输出，$y_{out}$ 为记录输出，$N$ 为记录长度。谐波质量条目衡量输出第二谐波相对于其基波的大小，噪声质量条目衡量均方根模型拟合残差相对于输出基波的大小。任一值偏高均表明测量存在失真或噪声，辨识点的可靠性较低。

PCSuite 在每次正弦激励后的 [CalcIden](CalcIden.md) 操作完成后读取结果。如需更多信息，请联系 Agito。

![IdenResults captures one point of the identified frequency response: a magnitude value (IdenResults[5] in dB) and a phase value (IdenResults[6] in deg/100) at the fundamental frequency InjectFreq; PCSuite sweeps InjectFreq and concatenates these points into the full magnitude and phase Bode plot used downstream by tuning and filter design](idenresults-bode-points.svg)

## 示例

```text
AIdenResults        ; read all calculated identification results
AIdenResults[5]     ; read amplitude ratio (dB) of output over input at fundamental
```

## 另请参阅

- [CalcIden](CalcIden.md) — 计算并填充这些结果
- [InjectFreq](../13-injection/InjectFreq.md) — 结果所参考的基波正弦频率
- [PlantModel](PlantModel.md) — 用于整定的已辨识被控对象模型
