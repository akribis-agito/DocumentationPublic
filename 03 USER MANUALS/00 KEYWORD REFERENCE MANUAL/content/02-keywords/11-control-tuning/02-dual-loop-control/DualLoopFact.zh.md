---
keyword: DualLoopFact
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 270
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 6553600
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 双环控制中对速度环信号进行单位匹配的缩放系数。
---
# DualLoopFact

用于双环控制中速度环信号单位匹配的缩放系数。

## 概述

`DualLoopFact` 对速度环信号进行缩放，使速度参考与速度反馈共享相同单位——即使位置（负载）反馈与速度（电机）反馈可能具有不同分辨率。位置环输出和速度参考以负载单位表示，而速度反馈来自电机编码器；`DualLoopFact` 用于协调两者。

当负载与电机反馈分辨率相同（缩放比例为 1）时，`DualLoopFact` 设为 `65536`（默认值）。在轴运动中或电机使能时不可更改。

## 工作原理

`DualLoopFact` 是一个定点系数，`65536` 表示比例为 1。控制器按以下方式推导速度环的工作缩放比例。在普通单轴双环中，`DualLoopFact` 仅影响速度环信号；它不会重新缩放位置限位（[FwdPLim](../../../02-keywords/06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../../02-keywords/06-protections/03-motion/position-limit-protection/RevPLim.md)）、位置/速度误差限值或整形后的位置参考，因为位置环闭合于负载编码器，该编码器已经以负载单位表示。由 `DualLoopFact` 进行的额外重缩放仅适用于龙门双环控制场景（参见[龙门控制 - 双环控制](../../../02-keywords/12-gantry-control/04-dual-loop-gantry-control/00-overview.md)）。

为保持精度，控制器根据 `DualLoopFact` 是否不低于 `65536`（比例 ≥ 1）或低于 `65536`（比例 &lt; 1）来选择应用缩放的位置：

| `DualLoopFact` | 速度环参考缩放 | 速度反馈缩放 | 公共单位 |
|---|---|---|---|
| ≥ 65536（比例 ≥ 1） | 不变（增益为 1） | 电机速度 × (`DualLoopFact` / 65536) | 主/负载编码器计数 |
| &lt; 65536（比例 &lt; 1） | × (65536 / `DualLoopFact`) | 不变（增益为 1） | 辅助/电机编码器计数 |

两种情况下，参考与反馈最终均使用相同单位——分辨率较高的那个——因此速度环在匹配信号上运行。

所使用的缩放系数 $k$ 为：

$$
k = \frac{65536}{\text{DualLoopFact}}
$$

$k$ 定义如下：

$$
k = \frac{\text{motor feedback count per physical unit}}{\text{load feedback count per physical unit}} = \frac{\text{load feedback physical unit per count}}{\text{motor feedback physical unit per count}}
$$

因此 DualLoopFact 为：

$$
\text{DualLoopFact} = \frac{65536 \cdot \text{motor feedback physical unit per count}}{\text{load feedback physical unit per count}}
$$

## 示例

电机反馈使用 4µm SINCOS 编码器，4096 倍插值（4000 nm / 4096 = 0.9765625 nm/count）。

负载反馈使用 200nm SINCOS 编码器，8192 倍插值（200 nm / 8192 = 0.0244140625 nm/count）。

则：

$$
\text{DualLoopFact} = \frac{65536 \cdot 0.9765625}{0.0244140625} = 2621440
$$

```text
ADualLoopFact=2621440  ; set the load-to-motor scaling factor
ADualLoopFact          ; read back the factor
```

## 另请参阅

- [DualLoopOn](DualLoopOn.md) — 启用双环控制
- [DualLoopStat](DualLoopStat.md) — 当前激活的双环状态
- [DualEncSwapOn](DualEncSwapOn.md) — 伪双环，使用该系数将辅助反馈换算至负载单位
