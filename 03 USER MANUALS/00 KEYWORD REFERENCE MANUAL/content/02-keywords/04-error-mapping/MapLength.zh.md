---
keyword: MapLength
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 324
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 60000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
summary: 沿每个误差映射维度的修正点数量。
last_updated: '2026-10-17'
doc_revision: '2026.06'
language: zh-CN
---
# MapLength

沿每个误差映射维度的修正点数量。

## 概述

`MapLength` 是一个按维度划分的数组（`[1]`/`[2]`/`[3]`），用于指定沿每个误差映射维度存在多少修正点。它与 [MapStartPos](MapStartPos.md)（点的起始位置）和 [MapPosGap](MapPosGap.md)（间距）一起定义了 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 条目所覆盖的位置范围：维度 `d` 跨越 `MapStartPos[d] … MapStartPos[d] + (MapLength[d] − 1) × MapPosGap[d]`。

它是一个轴相关数组，保存至闪存，可在电机使能时更改，但在轴处于运动中时不能更改。

## 工作原理

`MapLength` 既控制修正范围，也控制映射占用多少表条目。固件直接用它来计算每个维度的**最后**一个表索引，以及行/列/层之间的**步幅**：

| [MapType](MapType.md) | 消耗的表条目 | 内存布局 |
|:---------:|------------------------|---------------|
| 1D | `MapLength[1]` | 单个向量 |
| 2D | `MapLength[1] × MapLength[2]` | `MapLength[2]` 行，每行 `MapLength[1]`（第一维变化最快） |
| 3D | `MapLength[1] × MapLength[2] × MapLength[3]` | `MapLength[3]` 层堆叠的 2D 层 |

由于这些条目作为从 [MapStartIndex](MapStartIndex.md) 开始的一个扁平数组寻址，其总量必须能容纳在合并的 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 存储区内。每个维度值的范围为 `1 … 60000`；对于 2D/3D，真正的约束是其**乘积**。

## 示例

```text
AMapLength[1]=100    ; first dimension has 100 correction points
AMapLength[1]        ; read the number of points in the first dimension
```

### 边界情况

- **索引 0** — 无效；有效索引为 `MapLength[1]`/`[2]`/`[3]`。
- **写入时电机使能/运动中** — 电机使能且静止时接受；轴处于运动中时拒绝（错误 21）。
- **超出范围** — 每个维度超出 `1`–`60 000` 的值被拒绝。
- **乘积溢出** — 对于 2D/3D，各维度的**乘积**必须能容纳在从 [MapStartIndex](MapStartIndex.md) 开始的合并 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 存储区内；参数表不会预先检查此乘积，因此超大映射会读取未初始化的条目。
- **`MapType = 0`** — 值已存储但不被查询。
- **保存** — 可保存至闪存。

> **电机使能时修改映射。** 静止时写入将在下一个控制周期生效。由于映射修正的是反馈（[Pos](../10-motion/01-kinematics-status/Pos.md)），修正后的位置可能发生一次阶跃，伺服会使轴移动该阶跃量。若要使变化平缓（轴仍会移动整个修正量：斜坡退出时一次、斜坡接入时一次），请先将 [MapErrOnStep](MapErrOnStep.md) 设为较小的值（斜坡需要 `16384 / MapErrOnStep` 个周期，例如 `16` 约为 1024 个周期；默认值 `0` 和 `16384` 会在一个周期内接入或断开整个修正，本身就是阶跃），再将 [MapType](MapType.md) 设为 `0`，等待断开斜坡完成（约 `16384 / MapErrOnStep` 个控制周期；`Pos` 等于 `PosBeforeMap` 并不可靠，因为斜坡仍在进行时较小的修正值也可能读数为 0）后再修改映射，然后重新开启 `MapType`，使修正值按斜坡重新接入。断开斜坡完成后，实际施加的偏置保持为 0（[MapErrOffset](MapErrOffset.md) 关键字本身保持其值），重新开启映射后按 [MapErrOffRamp](MapErrOffRamp.md) 斜坡恢复。轴运动中时写入被拒绝（错误 21）。在此更改之前的固件上，电机使能时的写入会被拒绝（错误 22）。

## 另请参阅

- [MapStartPos](MapStartPos.md) — 每个维度的起始位置
- [MapPosGap](MapPosGap.md) — 修正点之间的间距
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — 每个点处的修正值
- [MapStartIndex](MapStartIndex.md) — 映射开始处的表索引
- [MapType](MapType.md) — 选择 1D/2D/3D（设置使用哪些维度）
