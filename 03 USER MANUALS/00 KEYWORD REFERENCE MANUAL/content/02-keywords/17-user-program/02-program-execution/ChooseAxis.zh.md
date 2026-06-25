---
keyword: ChooseAxis
summary: 按线程选择各用户程序线程所作用的物理轴的数组参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 563
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ChooseAxis

按线程选择各用户程序线程所作用的物理轴的数组参数。

## 概述

`ChooseAxis` 是一个数组参数，用于选择给定用户程序线程在指令中使用 `P`（或 `p`）轴字母作为占位符（而非固定轴字母）时所作用的物理轴。每个元素对应一个线程；该元素存储的值即为在该线程的轴相关指令中替换 `P` 占位符的轴号。这使多线程程序可同时对不同轴独立运行逻辑。数组以线程号为索引，其大小与最大并发线程数一致。

它与 [ProgTask](ProgTask.md) 所暴露的线程/任务模型配合使用，后者报告与程序执行关联的任务。

## 工作原理

当某线程执行轴字母为 `P` 占位符的关键字（或编码参数引用）时，程序引擎将以该运行线程索引处 `ChooseAxis` 中的轴号进行替换。[PushParam](../03-stack-operation/PushParam.md) 和 [PopParam](../03-stack-operation/PopParam.md) 等栈操作遵循相同规则：轴令牌为 `P` 占位符的编码引用从该线程的 `ChooseAxis` 条目中取得轴号。指定了明确轴字母的指令（例如 `AMotorOn=1`）不受 `ChooseAxis` 影响，始终作用于指定轴。修改某元素只会重定向该线程后续 `P` 占位符指令，不影响其他线程。每个线程各自维护独立条目，因此多个线程可在同一下载程序中并发驱动不同轴。

默认值为 0，因此从未设置 `ChooseAxis` 的线程将 `P` 占位符解析为轴 0。当 `P` 占位符指令直接通过通信（而非运行中的程序）发出时，替换所用轴取自专门为通信通道预留的独立 `ChooseAxis` 条目，而非任何线程的条目。

## 示例

```text
AChooseAxis[1]=0     ; thread 1 resolves the P placeholder to axis 0
AChooseAxis[2]=1     ; thread 2 resolves the P placeholder to axis 1
AChooseAxis[1]      ; query the axis assigned to thread 1
PMotorOn=1           ; runs on the calling thread's ChooseAxis axis
```

## 另请参阅

- [ProgTask](ProgTask.md) — 与运行中的用户程序线程关联的任务
- [ProgRun](ProgRun.md) — 启动用户程序线程
