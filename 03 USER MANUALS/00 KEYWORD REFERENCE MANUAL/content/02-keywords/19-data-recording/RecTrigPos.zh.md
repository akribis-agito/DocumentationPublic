---
keyword: RecTrigPos
summary: 触发前捕获的 RecLength 百分比（触发前数据）。
availability:
- controller
- ci-master
can_code: 247
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  agc300-et:
    array_size: 2
  agd200-et-2d01:
    array_size: 2
  agd200-et-2d02:
    array_size: 2
  agd200-et-2d05:
    array_size: 2
  agd200-et-2d05-71:
    array_size: 2
  agd155-af-2a06:
    array_size: 2
  agd155-af-2a10:
    array_size: 2
  agd155-ec:
    array_size: 2
  agd155-ec-var34:
    array_size: 2
  agd155-ec-var34-3:
    array_size: 2
  agd156-ec:
    array_size: 2
  agd101-ec-34a:
    array_size: 2
  agd101-ec-17a:
    array_size: 2
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigPos

触发前捕获的 RecLength 百分比（触发前数据）。

## 概述

`RecTrigPos` 定义在触发条件激活之前，从 [RecLength](RecLength.md) 中捕获的数据点百分比。通常在调试时使用，以便监测触发事件发生前的数据。每个数组索引对应一个示波器。有效值为 0 到 100；若值超出此范围，[RecStart](RecStart.md) 将拒绝请求并返回错误 71。

![RecTrigPos splits RecLength into a pre-trigger portion (RecTrigPos percent of RecLength) that captures the samples leading up to the trigger, and a post-trigger portion (the remainder) that captures the samples after the trigger fires](rectrigpos-buffer.svg)

| 索引 | 说明 |
|-------|------------------------------|
| 1     | 第一示波器 |
| 2     | 第二示波器（如适用） |

## 示例

```text
ARecTrigPos[1]=10    ; reserve 10% of RecLength for pre-trigger data
ARecTrigPos[1]      ; query the first scope pre-trigger percentage
```

若 `RecLength[1] = 16384` 且 `RecTrigPos[1] = 10`，则第一示波器将有 1638 个触发前数据点和 14746 个触发后数据点。记录器按每个通道的完整采样次数对触发前点数四舍五入，恰好半个采样点时向上取整。

若 `RecLength[1] = 205` 且 `RecTrigPos[1] = 20`，每个通道将保留 41 个触发前采样点。第 42 个采样点满足触发条件，也是余下 164 个点中的第一个。比例为 0% 时，触发点是第一个保留点。比例为 100% 时，所有保留点都在触发之前。这些位置适用于已配置触发且包含记录器修正的固件。[环形缓冲区头部字段](RecDataA-RecDataB.md) · [固件变更 #2675](https://github.com/akribis-agito/Firmware-Main/pull/2675)

## 另请参阅

- [RecLength](RecLength.md) — 每个参数的总数据点数
- [RecStat](RecStat.md) — 报告触发前数据何时填满
- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
