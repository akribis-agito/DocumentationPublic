---
keyword: MapStartPos
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 323
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
summary: 各误差映射维度的起始位置，以编码器计数表示。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapStartPos

各误差映射维度的起始位置，以编码器计数表示。

## 概述

`MapStartPos` 是一个按维度划分的数组（`[1]` 为第一维，`[2]` 为第二维，`[3]` 为第三维），它定义各误差映射维度第一个修正点的位置，以**编码器计数**表示（修正前，即在 [MapEncoder](MapEncoder.md) 所选源上测得）。它与 [MapPosGap](MapPosGap.md)（间距）和 [MapLength](MapLength.md)（点数）一起，完整描述了 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 条目所覆盖的查找网格。

它是一个保存至闪存的轴相关数组，且无法在轴运动中或电机使能时修改。

## 工作原理

每个控制周期，固件取所选编码器的未修正读数，并将其转换为该维度的小数表索引：

$$
\text{index}_f = \frac{\text{PosBeforeCorrection} - \text{MapStartPos}[d]}{\text{MapPosGap}[d]}
$$

因此维度 `d` 所覆盖的范围为 `MapStartPos[d]` 至 `MapStartPos[d] + (MapLength[d] − 1) × MapPosGap[d]`。**等于或低于** `MapStartPos[d]` 的读数钳位到该维度的第一个点；等于或高于上限的读数钳位到最后一个点——超出范围时修正值保持平直（不外推）。因此应将 `MapStartPos` 设置为使该表覆盖你希望修正的全部行程。

## 示例

```text
AMapStartPos[1]=0        ; first dimension starts at encoder count 0
AMapStartPos[1]=-50000   ; first dimension starts at -50000 counts
AMapStartPos[1]          ; read the start position of the first dimension
```

### 边界情况

- **索引 0** —— 无效；有效索引为 `MapStartPos[1]`（1D）、`[2]`（2D）、`[3]`（3D）。`MapStartPos[0]` 不存在。
- **写入时电机使能 / 运动中** —— 电机使能或轴运动中时拒绝写入。请在电机失能时配置。
- **`MapType = 0`** —— 该值被存储但不被读取；只有 [MapType](MapType.md) 的活动维度才会被使用（1D → 仅 `[1]`；2D → `[1]` 和 `[2]`；3D → 全部三个）。
- **低于范围** —— ≤ `MapStartPos` 的读数钳位到第一个修正条目（保持平直，不外推）。
- **超出范围** —— ≥ `MapStartPos + (MapLength − 1) × MapPosGap` 的读数钳位到最后一个修正条目。
- **编码器计数** —— 单位是所选 [MapEncoder](MapEncoder.md) 上的修正前编码器计数，而非用户单位。
- **保存** —— 可保存至闪存。
- **平台** —— v5 扩展至 64 位；v4 为 32 位。

## 版本间变更

| | v4（standalone 与 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位（`long`） | **64 位（`long long`）** |
| 范围 | ±2,147,483,647 | ±2,251,799,813,685,247 |

在 **v5** 中位置流水线为 64 位，因此映射起始位置以 64 位值存储，以匹配更宽的 [Pos](../10-motion/01-kinematics-status/Pos.md)/[PosBeforeMap](PosBeforeMap.md) 范围。v5 **仅 central-i** 可用；在 standalone 上 `MapStartPos` 仍为 32 位的 v4 值。

## 另请参阅

- [MapLength](MapLength.md) —— 每个维度的修正点数
- [MapPosGap](MapPosGap.md) —— 修正点之间的间距
- [MapEncoder](MapEncoder.md) —— 每个维度的编码器源
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) —— 各点处的修正值
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) —— 修正后与修正前的反馈
