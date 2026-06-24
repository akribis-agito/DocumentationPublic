---
keyword: DoNothing
summary: 用于检查通信响应能力的空操作命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 239
attributes:
  access: ro
  scope: non-axis
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# DoNothing

用于检查通信响应能力的空操作命令。

## 概述

`DoNothing` 不执行任何动作。它的唯一用途是为上位机提供一条无害的命令，以便在需要确认控制器是否在线并正在响应时发送——实际上相当于一次通信“ping”。它可以在任何时候安全发出，包括在电机使能或运动中时。

## 工作原理

当控制器收到 `DoNothing` 时，它不会改变任何内容，并立即返回标准的“OK”确认。因此，上位机仅凭收到回复这一事实即可确认链路处于活动状态。

该命令还充当固件对“空”消息的响应：如果控制器仅收到一个回车符（无论是否带有轴地址，且没有其他内容），它会将该输入视为 `DoNothing` 并予以确认，而不是报告语法错误。因此，在空白终端行上按 Enter 键是无害的。

## 示例

```text
ADoNothing           ; issue a no-op; a normal acknowledgement confirms the link
```

## 另请参阅

- [About](../01-status/About.md) — 上位机/诊断命令
