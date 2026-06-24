---
keyword: MapEncoder
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 322
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
  - 1
  - 8
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
summary: 选择由哪个轴编码器驱动每个误差映射维度。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapEncoder

选择由哪个轴编码器驱动每个误差映射维度。

## 概述

`MapEncoder` 是一个按维数组，用于选择由哪个编码器提供用于查找误差映射表的*未修正*位置。索引 `[1]` 是第一维（对于 1D，是唯一的维度）；`[2]` 和 `[3]` 为 [MapType](MapType.md) = 2 和 3 添加第二和第三维。所查找的编码器读数即用于索引该表——关于索引如何形成，请参阅 [MapStartPos](MapStartPos.md)/[MapPosGap](MapPosGap.md)/[MapLength](MapLength.md)——因此 2D/3D 映射可以使修正值依赖于不止一个轴的位置。

`MapEncoder` 是一个轴相关数组，保存至闪存，且不能在运动中或电机使能时更改。

## 工作原理

每个元素在一个整数中同时编码*轴*和*主编码器或辅助编码器*的选择。控制器在后台设置期间将其解码，以选择所选编码器的修正前读数：

- **奇数值** → 轴号为 `value >> 1` 的**主**编码器。
- **偶数值** → 轴号为 `(value >> 1) − 1` 的**辅助**编码器（[AuxPos](../10-motion/01-kinematics-status/AuxPos.md)）。

因此映射关系为：

| 值 | 源编码器 |
|:-----:|----------------|
| 1 | 轴 A 主编码器 |
| 2 | 轴 A 辅助编码器 |
| 3 | 轴 B 主编码器 |
| 4 | 轴 B 辅助编码器 |
| … | … （按轴重复该模式） |

默认值为 `1`（本轴自身的主编码器）。为使表构建/修正例程接受该映射，`MapEncoder[1]` **必须**指向本轴自身的主编码器；对于 2D/3D，第二/第三项必须指向处于静止、电机使能状态的轴的**主**编码器（选择错误将引发“must be main encoders” / “must be first encoder”事件）。有效范围为 `1 … (轴数) × 2`；在单轴控制器上只有 `1` 和 `2` 有意义。

## 示例

```text
AMapEncoder[1]=1     ; first dimension uses this axis's main encoder (typical)
AMapEncoder[2]=3     ; second dimension uses axis B's main encoder (2D map)
AMapEncoder[1]       ; read the encoder selected for the first dimension
```

### 边界情况

- **索引 0**——无效；有效索引为 `MapEncoder[1]`/`[2]`/`[3]`。
- **写入时电机使能 / 运动中**——电机使能或轴处于运动中时，写入被拒绝。
- **超出范围**——超出 `1`–`轴数 × 2` 的值被拒绝。
- **`MapEncoder[1]` 错误**——必须指向本轴自身的主编码器，表构建才会接受该映射；否则构建会引发“must be first encoder”事件。
- **2D/3D 需要主编码器**——用于 2D/3D 的附加编码器必须是处于电机使能、静止状态的轴的**主**编码器；用于 `[2]`/`[3]` 的辅助编码器会被拒绝并引发“must be main encoders”事件。
- **`MapType = 0`**——值已存储但不被查询。
- **保存**——可保存至闪存。

## 参见

- [MapType](MapType.md) — 选择 1D/2D/3D 映射
- [MapStartPos](MapStartPos.md) — 每个映射段的起始位置
- [MapLength](MapLength.md) — 每段的修正项数量
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — 按映射位置索引的修正值
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — 修正后与修正前的反馈
- [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) — 辅助编码器读数，可选作映射源
