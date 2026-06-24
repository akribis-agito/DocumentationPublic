---
keyword: ParamCS
summary: 只读校验和，覆盖控制器的参数集，用于验证配置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 428
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 4
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
# ParamCS

只读校验和，覆盖控制器的参数集，用于验证配置。

## 概述

`ParamCS` 是一个只读、1 索引的数组，保存对控制器参数集计算得出的校验和。上位机可以读取它来验证设备上存储的参数是否与预期配置匹配——例如确认一批单元配置完全相同——而无需下载并比较完整的参数列表。在 [Save](../02-operation/Save.md) 前后比较 `ParamCS` 也可确认存储的配置是否发生变更。

## 工作原理

校验和在保存参数集时重新计算。固件遍历每个已保存的参数值：每个 32 位值被拆分为高 16 位和低 16 位两半，两半均（以 16 位回绕方式）累加到一个运行总和中。带缩放存储的值首先转换回其原始（未缩放）整数形式，因此校验和反映的是存储表示而非显示的用户单位值。数组参数的元素 `[0]` 被排除（它从不上传），因此数组内容从元素 `[1]` 开始参与计算。

并行维护三个总和，它们仅在包含哪些网络标识参数上有所不同。它们填充三个可用元素：

| Index | 覆盖范围 |
|-------|--------|
| [1] | **除**以太网 IP 地址和以太网 MAC 地址外的所有参数 |
| [2] | **除**以太网 MAC 地址外的所有参数 |
| [3] | 所有参数，包括 IP 和 MAC |

（该数组声明为四个槽位；元素 `[0]` 未使用，以便通信索引从 1 开始。）

之所以采用三种变体，是因为网络标识因单元而异：比较 `ParamCS[1]` 可让上位机确认两台单元具有相同的*功能*配置，即使它们的 IP 和 MAC 地址不同；而 `ParamCS[3]` 验证包括网络标识在内的精确匹配。

## 示例

```text
AParamCS[1]         ; checksum ignoring IP and MAC (compare functional config across units)
AParamCS[2]         ; checksum ignoring only the MAC address
AParamCS[3]         ; checksum over the full parameter set
```

## 另请参阅

- [ParamAbout](ParamAbout.md) — 单个参数的元数据
- [Save](../02-operation/Save.md) — 将参数持久化至闪存（重新计算校验和）
- [Identity](Identity.md) — 控制器识别信息与功能标志
