---
keyword: HomingStep
summary: 只读数值，指示回零引擎已执行到的回零步骤编号。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 385
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
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
# HomingStep

只读索引，指示回零引擎已执行到的回零步骤编号。

## 概述

`HomingStep` 是一个只读的轴作用域状态变量（不保存至闪存），用于报告回零引擎在 [HomingDef](HomingDef.md) 定义的序列中已执行到的步骤编号。通过监控该值可跟踪多步回零过程的进度。它与 [HomingStat](HomingStat.md) 配合使用——`HomingStat` 报告由 [HomingOn](HomingOn.md) 启动的回零运行的整体状态（当前步骤、成功或错误码）。

## 工作原理

回零引擎维护一个从 1 开始的内部步骤指针。每个控制周期将该指针复制到 `HomingStep` 中。当某步骤完成后，指针递增，`HomingStep` 移至下一个待处理步骤；回零结束时，该值保持结束时所到达的步骤编号。在 `HomingStat` 同样报告当前活动步骤期间，两者的数值相同；回零结束后，`HomingStat` 切换为 `100`（成功）或负数错误码，而 `HomingStep` 保留最终步骤编号。

`HomingStep` 在回零未运行时保留最后一次到达的步骤编号——两次运行之间不会重置为 `1`——因此应与 [HomingStat](HomingStat.md) 一起读取（`HomingStat` 在上电或复位后第一次运行前报告 `0`）。

## 示例

```text
AHomingStep         ; 回零引擎已到达的步骤编号
```

## 另请参见

- [HomingStat](HomingStat.md) — 回零运行的整体状态及错误码
- [HomingOn](HomingOn.md) — 启动回零过程
- [HomingDef](HomingDef.md) — 定义所计步骤
