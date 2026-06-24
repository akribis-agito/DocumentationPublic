---
keyword: SetPDPos
summary: 指令，用于在不移动轴的情况下预设或重新归零脉冲方向位置计数器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 156
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# SetPDPos

指令，用于在不移动轴的情况下预设或重新归零脉冲方向位置计数器。

## 概述

`SetPDPos` 是一条将脉冲方向输入位置计数器 [PDPos](PDPos.md) 设置为指定值的指令。它可在不物理移动轴的情况下对 P/D 计数器重新归零或预设，适用于将解码后的计数器对齐至已知参考位置。这是一个轴相关指令函数，轴在运动中时不可发出（电机可以处于使能状态）。

## 工作原理

`SetPDPos` 将计数器设置为提供的值，并将派生速度 [PDVel](PDVel.md) 清零。后续每周期的变化量从新的基准值开始累加。

它**不**影响 [Begin](../04-motion-command/Begin.md) 处锁存的值：在有效的直接/间接 P/D 运动期间，运动相对于该锁存值计量，因此在运动中途预设计数器会引起偏移——请在发出 `Begin` 之前进行预设。这是 P/D 输入的 [SetPosition](../03-kinematics-configuration/SetPosition.md) 类比，后者用于预设轴的反馈位置。

## 示例

```text
ASetPDPos=0          ; 将 P/D 计数器重新归零
ASetPDPos=100000     ; 将 P/D 计数器预设为已知值
```

## 参见

- [PDPos](PDPos.md) — 此指令所设置的计数器
- [PDSubType](PDSubType.md) — P/D 输入信号格式
- [PDFact](PDFact.md) — P/D 输入缩放因子分子
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — 轴反馈位置的类似预设指令
