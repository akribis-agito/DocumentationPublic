---
keyword: ForceRefFOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 579
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
summary: 使能力指令参考滤波器。
---
# ForceRefFOn

使能力指令参考滤波器。

## 概述

`ForceRefFOn` 是施加于力指令的一阶低通滤波器的开关：

| 值 | 行为                                                    |
|----|---------------------------------------------------------|
| 0  | 滤波器旁路——力参考等于原始指令                          |
| 1  | 滤波器使能——截止频率由 [ForceRefFilt](ForceRefFilt.md) 设置 |

默认值为 `0`（滤波器禁用）。该关键字保存至闪存。

## 工作原理

当 `ForceRefFOn = 1` 时，滤波器系数由 [ForceRefFilt](ForceRefFilt.md) 计算得出，原始力指令每个周期经过低通滤波后产生力参考 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md)。当 `ForceRefFOn = 0` 时，滤波器系数被设置为使滤波器直通指令，`ForceRef` 直接跟随原始指令。

写入 `ForceRefFOn` 后，系数立即重新计算。该设置适用于 [ForcePIVOn](ForcePIVOn.md) 选择的两种力控制结构。

## 示例

```text
AForceRefFOn[1]=1       ; enable the force-command reference filter
AForceRefFOn[1]=0       ; bypass the filter
AForceRefFOn[1]         ; read the filter switch
```

## 另请参阅

- [ForceRefFilt](ForceRefFilt.md) — 该滤波器使能时使用的截止频率
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — 滤波后的力参考
- [Force control](00-overview.md) — 力环结构概述
