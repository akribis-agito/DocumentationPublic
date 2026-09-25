---
keyword: PushEvSelect
summary: 按轴设置的待发送推送事件类型位掩码。
availability:
  standalone: []
  central-i:
  - v5
can_code: 908
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvSelect

按轴设置的待发送推送事件类型位掩码。

## 概述

`PushEvSelect` 选择控制器在每个轴上检测哪些[推送事件](00-overview.md)类型。它适用于作用范围为**轴**的事件类型；控制器级类型在 [PushEvSelSys](PushEvSelSys.md) 中选择。只有当 [PushEvEnable](PushEvEnable.md) 也为 1 时才会发送事件。

该关键字是由两个 32 位掩码组成的轴相关数组，可通过 [Save](../02-operation/Save.md) 保存至闪存。默认值为 0，即未选择任何类型。

| 索引 | 事件类型 |
|---|---|
| `[1]` | 类型 1-32：类型 *k* 对应位 *k*−1 |
| `[2]` | 类型 33-64：类型 *k* 对应位 *k*−33 |

数组从 1 开始索引；`PushEvSelect[0]` 不存在。

## 事件类型

| 类型 | 位 | `[1]` 中的掩码 | 名称 |
|---|---|---|---|
| `1` | 0 | `1` | Profile ended（曲线结束）—— 该轴不再被指令运动。其数据字段参见[概述](00-overview.md) |

类型 1 是本版本中唯一的类型。其他类型的位会被存储，但不起作用。由于每个索引都是有符号 32 位值，置位第 31 位（类型 32 或类型 64）的掩码需写为负数。

## 示例

```text
APushEvSelect[1]=1   ; axis A: send Profile ended
CPushEvSelect[1]=1   ; axis C: the same
APushEvSelect[1]=0   ; axis A: send nothing
APushEvSelect[1]     ; read axis A's mask for types 1-32
```

## 另请参阅

- [Push Events 概述](00-overview.md) — 事件类型目录和数据包格式
- [PushEvEnable](PushEvEnable.md) — 总开关
- [PushEvSelSys](PushEvSelSys.md) — 控制器级事件类型的对应掩码
