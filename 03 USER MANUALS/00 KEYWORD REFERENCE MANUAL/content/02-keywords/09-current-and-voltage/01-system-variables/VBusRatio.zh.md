---
keyword: VBusRatio
summary: 只读：直流母线前馈当前施加的电压缩放比值。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 879
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: [0, 10]
  default: 1.0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# VBusRatio

只读：直流母线前馈当前施加的电压缩放比值。

## 概述

`VBusRatio` 报告驱动器当前为补偿母线变动而对其电压输出施加的缩放系数。它是判断 [AdVBusEn](AdVBusEn.md) 是否在起作用、以及作用强度的观测量。

```text
VBusRatio = 电机使能时的标称母线 / 滤波后的实测母线
```

## 工作原理

- **1.0** — 母线处于电机使能时锁存的数值；未施加补偿。
- **大于 1.0** — 母线已跌落，驱动器正在放大其输出。
- **小于 1.0** — 母线高于标称值，通常出现在制动回馈期间，驱动器正在缩小输出。

> **注意：** 该值被钳位在补偿器的权限范围 **[0.8, 1.2]** 内。读数持续停在 1.2 表示母线跌落已超出本功能允许纠正的范围——这是有价值的诊断信息，因为它说明限制来自电源而非补偿。

> **示例演算：** 在弱电源上剧烈加速的过程中，观测到比值从 1.0000 升至 1.2000 并保持不变，而母线仍在继续下降。此后的部分完全未被补偿。

### 使用方式

在弱电源上诊断某一轴时，请同时记录 `VBusRatio` 与 [VBus](VBus.md)。比值长时间停在钳位值，是电源相对该运动容量不足的直接证据，任何调试都无法替代更刚硬的母线。

### 边界情况

- **只读：** 写入将被拒绝。
- **默认值为 1.0** 而非 0，因此在首个控制周期之前该值为中性，而不会被读作完全衰减。
- **禁用时读为 1.0：** 当 [AdVBusEn](AdVBusEn.md) 为 0 时不计算该比值，保持为 1.0。

## 示例

```text
VBusRatio?            ; 读取当前比值
```

## 另请参阅

- [AdVBusEn](AdVBusEn.md) — 使能本参数所报告的功能
- [VBus](VBus.md) — 实测母线电压
