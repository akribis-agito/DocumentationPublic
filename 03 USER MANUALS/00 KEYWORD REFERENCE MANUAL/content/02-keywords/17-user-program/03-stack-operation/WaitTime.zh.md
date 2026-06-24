---
keyword: WaitTime
summary: 将当前任务暂停指定的毫秒数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 193
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
  - 10000000
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# WaitTime

将当前任务暂停指定的毫秒数。

## 概述

`WaitTime` 是一条用户程序指令，用于将当前任务的执行暂停指定的毫秒时长。它是 [WaitStatus](WaitStatus.md)（等待状态条件）的时间驱动对应指令。可在运动中及电机使能状态下使用。该关键字为非轴指令，不保存至闪存。

## 工作原理

线程首次到达该指令时，`WaitTime` 以请求的时长初始化每线程毫秒倒计时，并将线程标记为等待；倒计时在后台递减。在倒计时大于零期间，线程保持等待并让出执行权，其他线程可继续运行。倒计时归零后，等待结束，线程从下一条指令恢复执行；下次再到达 `WaitTime` 时，将重新开始新的等待。时长以毫秒为单位，范围为 0 至 10000000 ms。

## 示例

```text
AWaitTime,1000      ; pause the current task for 1000 ms (1 second)
```

## 另请参阅

- [WaitStatus](WaitStatus.md) — 使任务等待直到状态达到某值
