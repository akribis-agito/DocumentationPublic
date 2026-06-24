---
keyword: CalcIden
summary: 用于计算正弦扫频辨识中输入/输出正弦关系的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 128
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CalcIden

用于计算正弦扫频辨识中输入/输出正弦关系的指令。

## 概述

`CalcIden` 指示控制器在注入频率 [InjectFreq](../13-injection/InjectFreq.md) 处计算内部记录的输入与输出数据之间的正弦关系。仅适用于正弦扫频辨识。计算完成后，控制器返回 `OK` 消息，结果存储在 [IdenResults](IdenResults.md) 中，并据此构建 [PlantModel](PlantModel.md) 中的已辨识被控对象模型。

## 工作原理

输入和输出数据各自至少须包含 30 个、至多 250 个数据点。`CalcIden` 在 [InjectFreq](../13-injection/InjectFreq.md) 设定的基波频率处对记录向量进行评估，并将幅值和相位关系填入 [IdenResults](IdenResults.md)。

### 机制

`CalcIden` 对每个记录向量进行最小二乘回归，拟合到在注入频率处求值的固定六项模型。对于每个记录采样 $x = 0, 1, \dots, N-1$（其中 $N$ 为记录长度），模型矩阵 $M$ 的一行由六个基函数项构成：

$$M_x = \big[\, \sin(\omega t),\ \cos(\omega t),\ \sin(2\omega t),\ \cos(2\omega t),\ 1,\ t \,\big]$$

其中 $t = x \cdot T_s \cdot \text{RecGap}$ 为采样时刻，$T_s$ 为控制器周期时间（默认 $T_s = 1/16384 \approx 61\ \mu s$），$\text{RecGap}$ 为记录采样之间的周期数，基波角频率为

$$\omega = 2\pi \cdot \frac{[\text{InjectFreq}]}{100}$$

（InjectFreq 以 Hz/100 为单位）。前两项捕获基波正弦和余弦，接下来两项捕获二次谐波，常数项吸收任何直流偏置，线性项 $t$ 吸收记录中的任何漂移。

最小二乘解使用伪逆 $\left(M^{\mathsf T} M\right)^{-1} M^{\mathsf T}$，计算一次后同时应用于输入和输出向量，得到各自的六个拟合系数。记录的输入按原样使用；记录的输出先减去第一个采样值，使拟合相对于起始点进行。输入和输出的基波正弦和余弦系数（$a$ 和 $b$）随后组合成 [IdenResults](IdenResults.md) 中报告的频率响应、幅值和质量项。

### 错误条件

- 若记录长度超出 30 至 250 采样的范围，指令返回错误 103。
- 若记录的参数数量有误，指令返回错误 104。标准辨识记录须恰好包含两个参数（一个输入，一个输出）。在 central-i v5 上，双环辨识记录可包含两个或三个参数（一个输入和一个或两个输出）；参见 [IdenResults](IdenResults.md) 中的双环说明。

## 示例

```text
ACalcIden            ; calculate the sine-sweep relation; results land in IdenResults
```

## 另请参阅

- [IdenResults](IdenResults.md) — 存储计算得到的输入/输出关系
- [InjectFreq](../13-injection/InjectFreq.md) — 用于计算的基波正弦频率
- [PlantModel](PlantModel.md) — 由结果推导出的已辨识被控对象模型
