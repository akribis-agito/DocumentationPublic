---
keyword: MapStartIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 321
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 300000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: 活动误差映射数据开始处的 MapTable 索引。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapStartIndex

活动误差映射数据开始处的 MapTable 索引。

## 概述

`MapStartIndex` 设置活动误差映射数据开始处的 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 索引。给定映射的修正值不必从第一个表元素开始，因此这允许多个映射共享表区域，或允许跳过未使用的前导条目。修正从此索引开始，跨越由 [MapStartPos](MapStartPos.md)、[MapPosGap](MapPosGap.md) 和 [MapLength](MapLength.md) 定义的点，针对由 [MapType](MapType.md) 选择的维度进行。

它是一个轴相关参数，保存至闪存，在轴处于运动中或电机使能时不能更改。

## 工作原理

`MapStartIndex` 是修正期间每次表读取的基索引——固件的表取值例程将单个基于 1 的索引映射到链接的存储区（`MapTable`，然后是 `MapTableB…MapTableE`），因此索引空间**跨所有五个存储区连续**，并且 `MapStartIndex` 可合法地指向其中任意一个。按维度查找在此基础上添加偏移：

- **1D：** 条目 `MapStartIndex … MapStartIndex + MapLength[1] − 1`。
- **2D：** `index = MapStartIndex + column × MapLength[1] + row`（第一维变化最快）。
- **3D：** `index = MapStartIndex + layer × MapLength[1] × MapLength[2] + column × MapLength[1] + row`。

映射必须能容纳在从 `MapStartIndex` 开始的可用表大小内；该关键字的上界随合并存储区大小变化。由于索引是**基于 1 的**，`MapStartIndex = 1` 选择 `MapTable[1]` 作为第一个条目。

## 示例

```text
AMapStartIndex=1     ; mapping data starts at MapTable[1]
AMapStartIndex=5000  ; mapping data starts 5000 entries in (may fall in a later bank)
AMapStartIndex       ; read the current start index
```

### 边界情况

- **写入时电机使能/运动中** — 在电机使能或轴处于运动中时被拒绝。
- **超出范围** — 超出 `1`–`300 000` 的值被拒绝。
- **超出表范围** — 超过合并存储区大小的值会派发到未初始化内存；需与 [MapLength](MapLength.md) 谨慎配合。
- **`MapType = 0`** — 值已存储但不被查询。
- **基于 1** — `MapStartIndex = 1` 指向 `MapTable[1]`。索引 `0` 无效。
- **保存** — 可保存至闪存。

## 参见

- [MapType](MapType.md) — 选择 1D/2D/3D 映射
- [MapStartPos](MapStartPos.md) — 每个维度的起始位置
- [MapLength](MapLength.md) — 每个维度的点数量
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — 此索引所指向的表
