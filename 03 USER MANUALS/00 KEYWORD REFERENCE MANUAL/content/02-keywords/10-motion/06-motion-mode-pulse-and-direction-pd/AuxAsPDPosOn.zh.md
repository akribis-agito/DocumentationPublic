---
keyword: AuxAsPDPosOn
summary: 将脉冲方向输入接入辅助编码器反馈（双环），而非默认的跨轴辅助来源。
availability:
  standalone: []
  central-i:
  - v5
can_code: 686
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AuxAsPDPosOn

将脉冲方向输入接入辅助编码器反馈（双环），而非默认的跨轴辅助来源。

## 概述

`AuxAsPDPosOn` 选择每个轴的**辅助**位置和速度的来源。它使能一种双环配置，其中**脉冲方向（P/D）输入被作为增量式辅助编码器读取**，从而允许轴在使用电机反馈闭环的同时，将第二个传感器接入 P/D 输入。

这是一个控制器级（非轴）设置，保存至闪存，取值为 0 或 1（默认 0）。在电机使能或运动中时不能更改。支持具有 P/D 输入的多轴单元。

> 仅适用于 v5（Central-i）。

## 工作原理

| 值 | 各轴辅助反馈来源 |
|---|---|
| 0（默认） | 各轴的辅助反馈取自另一轴的主反馈（默认跨轴映射）。 |
| 1 | 各轴的辅助反馈（[AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md)）取自**该轴自身的 P/D 输入计数器**（[PDPos](PDPos.md) / [PDVel](PDVel.md)）。 |

设置为 1 时，控制器在每个控制周期将各轴的 P/D 计数器及其变化率复制到该轴的辅助位置和速度中。P/D 输入因此充当双环方案中的辅助增量编码器（例如，电机编码器用于主环，外部光栅尺通过 P/D 输入用作辅助）。设置为 0 时，辅助反馈保持默认行为，P/D 输入仍可用于 PD 运动。

由于该标志会更改所有轴的辅助反馈接线，应在调试期间一次性配置（电机关闭，无运动）。在用作辅助反馈之前，使用常规 P/D 缩放和方向关键字设置 P/D 计数器的缩放比例和方向。

> **关于名称的说明：** 该关键字读作"辅助作为 P/D 位置"。实际数据流为 P/D 输入 → 辅助反馈：使能时，各轴的 P/D 计数器提供 [AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md)，即 P/D 输入被**用作**辅助编码器。上述描述遵循该行为。

## 示例

```text
AAuxAsPDPosOn=1          ; use the P/D inputs as the auxiliary encoder (dual loop)
AAuxAsPDPosOn=0          ; default auxiliary feedback source
AAuxAsPDPosOn            ; read the current setting
```

（`AuxAsPDPosOn` 是控制器级设置；命令语法仍需要轴字母前缀。）

## 另请参阅

- [PDPos](PDPos.md) / [PDVel](PDVel.md) — 使能时复制到辅助反馈的 P/D 计数器及其变化率
- [AuxPos](../01-kinematics-status/AuxPos.md) / [AuxVel](../01-kinematics-status/AuxVel.md) — 该设置所重定向的辅助反馈
