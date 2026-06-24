---
keyword: ProductSN
summary: 包含本单元硬件版本与生产序列号的双元素数组；仅在提升权限下可写，并持久化保存至闪存。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 468
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
overrides:
  central-i.v5:
    can_code: 348
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProductSN

包含本单元硬件版本与生产序列号的双元素数组。

## 概述

`ProductSN` 存储控制器的硬件版本与生产序列号，并将其持久化保存至闪存，因此它们能在重新上电后保留，用于在生产与现场服务中唯一标识某一物理单元。该数组声明为三个槽位；元素 `[0]` 未使用，以便通信索引从 1 开始，从而留下两个可用元素：

| 索引 | 内容 |
|-------|----------|
| [1] | 硬件版本号 |
| [2] | 生产序列号 —— 由年份（2 位）、周数（2 位）与单元计数（4 位）拼接而成 |

![ProductSN[2] format — year, week, unit-count fields](productsn-format.svg)

## 工作原理

`ProductSN` 保存在闪存中。上电时，在控制器从闪存加载其关键字之后，它会将 `ProductSN[1]` 与 `ProductSN[2]` 分别复制到 [Identity](Identity.md) 数组中 —— 复制到 `Identity[3]`（硬件版本）与 `Identity[2]`（序列号）—— 上位机软件从中读取并显示本单元的序列号。该复制仅在该启动加载期间执行；在运行时写入 `ProductSN` 不会更新 `Identity`，因此新写入的序列号在下次上电或 [Reset](../02-operation/Reset.md) 之前不会反映到 `Identity` 中。

## 写入序列号（提升权限）

`ProductSN` 旨在于生产期间一次性编程写入。该写入受到保护：控制器仅在处于**提升（老化）权限**状态时才接受对 `ProductSN` 的写入。若不具备该权限，写入将被拒绝并返回：

> 通信错误 **328** —— “Setting Product Serial Number is not allowed without Elevated Permissions.”

作为一项保护措施，固件会在接受一次 `ProductSN` 写入后立即清除提升权限状态，因此该权限始终只授权**单次**写入 —— 编程写入两个元素需要在每次写入前重新授权。在正常使用中，集成商与最终用户始终只会**读取** `ProductSN`。

## 示例

```text
AProductSN[1]       ; read the hardware version
AProductSN[2]       ; read the production serial number
```

## 另请参阅

- [Identity](Identity.md) —— 向上位机软件暴露序列号（`Identity[2]`）与硬件版本（`Identity[3]`）
- [UnitStat](UnitStat.md) —— 单元硬件/固件健康状态
