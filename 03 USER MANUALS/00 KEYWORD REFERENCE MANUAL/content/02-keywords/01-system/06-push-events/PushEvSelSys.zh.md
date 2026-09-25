---
keyword: PushEvSelSys
summary: 待发送的控制器级推送事件类型位掩码。
availability:
  standalone: []
  central-i:
  - v5
can_code: 912
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
# PushEvSelSys

待发送的控制器级推送事件类型位掩码。

## 概述

`PushEvSelSys` 选择控制器发送哪些控制器级[推送事件](00-overview.md)类型。控制器级事件不属于任何轴，其记录中的 axis 字段为 `0xFF`。属于某个轴的事件类型在 [PushEvSelect](PushEvSelect.md) 中按轴选择。

它与 `PushEvSelect` 采用相同的布局和位规则，但它是单一的非轴设置，可通过 [Save](../02-operation/Save.md) 保存至闪存。默认值为 0。

| 索引 | 事件类型 |
|---|---|
| `[1]` | 类型 1-32：类型 *k* 对应位 *k*−1 |
| `[2]` | 类型 33-64：类型 *k* 对应位 *k*−33 |

数组从 1 开始索引；`PushEvSelSys[0]` 不存在。

> **本版本中尚无控制器级事件类型。** 唯一已定义的类型 Profile ended（类型 1）属于轴。`PushEvSelSys` 会被存储和保存，但目前没有任何事件读取它。设置该关键字是为了将来新增控制器级类型时无需新增关键字即可选择。

## 示例

```text
APushEvSelSys[1]     ; read the mask for types 1-32
APushEvSelSys[1]=0   ; select no controller-wide types (default)
```

## 另请参阅

- [PushEvSelect](PushEvSelect.md) — 按轴的事件类型掩码
- [PushEvEnable](PushEvEnable.md) — 总开关
- [Push Events 概述](00-overview.md)
