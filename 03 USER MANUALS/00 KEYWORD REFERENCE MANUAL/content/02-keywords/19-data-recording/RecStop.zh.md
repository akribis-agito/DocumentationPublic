---
keyword: RecStop
summary: 停止所选示波器上的记录的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 250
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
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
# RecStop

停止所选示波器上的记录的命令。

## 概述

`RecStop` 命令所选示波器停止记录。可在记录的任意阶段调用，也是重新配置示波器的第一步。若调用 `RecStop` 时记录仍在进行，[RecDataA/RecDataB](RecDataA-RecDataB.md) 的元数据将更新，以报告实际已完成的记录长度。每个数组索引对应一个示波器。

| 索引 | 说明 |
|-------|------------------------------|
| 1     | 第一示波器 |
| 2     | 第二示波器（如适用） |

## 工作原理

`RecStop` 的行为取决于示波器当前的 [RecStat](RecStat.md)：

- 若示波器仍在填充触发前数据或等待触发（状态 1 或 2），则记录以状态 6（触发前停止）结束。此时不存在可用的已触发数据集，[RecUpload](RecUpload.md) 将对该示波器报错。
- 若触发已被检测且记录正在进行（状态 3），则记录以状态 5（已停止）结束。[RecDataA/RecDataB](RecDataA-RecDataB.md) 中的元数据长度将被改写为实际已捕获的点数，使上传仅返回真实数据。
- 若示波器处于空闲、已停止或已完成状态，`RecStop` 不执行任何操作，也不视为错误。

## 示例

```text
ARecStop[1]          ; stop recording on the first scope
ARecStop[2]          ; stop recording on the second scope
```

## 另请参阅

- [RecStart](RecStart.md) — 开始记录
- [RecStat](RecStat.md) — 记录状态
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — 停止时更新的元数据
