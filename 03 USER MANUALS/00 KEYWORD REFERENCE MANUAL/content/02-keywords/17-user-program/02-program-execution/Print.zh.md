---
keyword: Print
summary: 用户程序语句，向上位机输出文本字符串。
availability:
  standalone: []
  central-i:
  - v5
can_code: 827
attributes:
  access: rw
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Print

用户程序语句，向上位机输出文本字符串。

## 概述

`Print` 在用户程序运行时通过通信通道输出文本字符串，用于程序执行期间的状态或调试消息。它是非轴函数，不保存至闪存。仅在 Central-i（v5）上可用；在独立控制器上，`Print` 请求将返回"不支持"错误。

## 工作原理

`Print` 旨在从用户程序内部调用，而非作为上位机直接指令。程序编译时，每个打印字符串字面量存储在程序内存中；运行时，`Print` 语句将该字符串的地址传递给固件，固件通过服务该程序的通信通道流式输出文本。文本入队后，程序继续执行下一行。

由于消息在活动通信通道上发送，它将出现在连接控制器的上位机工具中——使 `Print` 可用于跟踪程序流程、报告中间值，或标示某一分支已被执行。它不影响运动或任何关键字值。

## 示例

```text
; 在用户程序内部
Print "Homing complete"      ; 向上位机发送状态消息
Print "Entering phase 2"     ; 跟踪程序执行了哪个分支
```

## 另请参阅

- [ProgRun](ProgRun.md) — 启动用户程序
- [ProgStat](ProgStat.md) — 用户程序运行状态
