---
keyword: VEncSrc
summary: 选择用于生成虚拟编码器位置的源信号。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 614
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VEncSrc

选择用于生成虚拟编码器位置的源信号。

## 概述

`VEncSrc` 选择虚拟编码器所跟踪的内部变量。所选变量由 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 缩放，以 [VEncType](VEncType.md) 设置的格式发出，并（对于脉冲/方向）由 [VEncDelay](VEncDelay.md) 定时，从而在虚拟编码器使能（[VEncOn](VEncOn.md) = 1）时产生生成的编码器信号。它是一个保存至闪存的轴相关参数，可在电机使能或运动中更改。

## 工作原理

`VEncSrc` **不是一个小型枚举列表**——它是一个编码后的*关键字命令代码*，组合了一个关键字、其轴及数组索引。控制器在配置时将其解析为指向相应内部变量的指针。每个控制周期虚拟编码器读取该变量，因此任何可读取的控制器变量都可以作为源——例如另一个轴的位置 [Pos](../../10-motion/01-kinematics-status/Pos.md) 或参考值 [PosRef](../../10-motion/01-kinematics-status/PosRef.md)。

在 v4 固件中，源始终以 **32 位整数**读取，因此原生为 64 位整数、float 或 double 的源将无法被正确读取。v5 Central-i 固件记录源的真实数据类型（32 位整数、64 位整数、float 或 double）并据此读取，然后将读取值转换为 32 位整数以用于跟踪。

如果所选源本身在取模下回绕（[ModRev](../04-modulo-mode/ModRev.md)），固件会检测到回绕（大于源取模范围一半的跳变）并补偿跟踪存储，使生成的输出保持连续。

为给定源写入的数值是该关键字的命令代码；请从 PCSuite 或关键字参考中获取，而不要猜测。

## 示例

```text
AVEncSrc            ; query the configured virtual encoder source code
```

## 另请参阅

- [VEncOn](VEncOn.md) — 使能虚拟编码器
- [VEncType](VEncType.md) — 输出信号格式
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 缩放比例的分子 / 分母
- [Pos](../../10-motion/01-kinematics-status/Pos.md) / [PosRef](../../10-motion/01-kinematics-status/PosRef.md) — 典型源变量
