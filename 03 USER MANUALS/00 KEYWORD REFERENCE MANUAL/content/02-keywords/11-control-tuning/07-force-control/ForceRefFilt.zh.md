---
keyword: ForceRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 586
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 500000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 力指令参考滤波器的截止频率。
---
# ForceRefFilt

力指令参考滤波器的截止频率。

## 概述

`ForceRefFilt` 定义施加于力指令的一阶低通滤波器的截止频率，以 **Hz/100** 表示（数值为截止频率（赫兹）乘以 100）。滤波结果为力参考 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md)，供力环使用并作为 [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) 报告。

例如，500 Hz 的截止频率应设置为 `ForceRefFilt = 50000`。

取值范围为 `1` 至 `500000`（0.01 Hz 至 5000 Hz）；默认值为 `10000`（100 Hz）。该关键字保存至闪存。仅当 [ForceRefFOn](ForceRefFOn.md) = 1 时，滤波器才有效。

## 工作原理

每个控制周期，原始力指令（来自所选指令源）经过一阶低通滤波段生成 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md)：

$$
\text{ForceRef} = a \cdot \text{command} + (1 - a) \cdot \text{ForceRef}_{\text{prev}}
$$

当滤波器使能（[ForceRefFOn](ForceRefFOn.md) = 1）时，系数由截止频率和控制器采样时间推导得出：

$$
a = 1 - e^{-2\pi \, T_s \, \frac{\text{ForceRefFilt}}{100}}
$$

其中 $T_s$ 为控制器采样时间。`ForceRefFilt` 值越高，截止频率越高，参考响应越快；值越低，对指令的平滑程度越大。当滤波器禁用（`ForceRefFOn = 0`）时，系数强制为 $a = 1$，`ForceRef` 直接等于未滤波的原始指令。

写入 `ForceRefFilt` 后，系数立即重新计算。相同的参考滤波器适用于 [ForcePIVOn](ForcePIVOn.md) 选择的两种力控制结构。

## 示例

```text
AForceRefFOn[1]=1       ; enable the force-command reference filter
AForceRefFilt[1]=50000  ; cut-off 500 Hz (Hz/100)
AForceRefFilt[1]        ; read the cut-off setting
```

## 另请参阅

- [ForceRefFOn](ForceRefFOn.md) — 使能/旁路该参考滤波器
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — 该滤波器产生的滤波力参考
- [Force control](00-overview.md) — 力环结构概述
