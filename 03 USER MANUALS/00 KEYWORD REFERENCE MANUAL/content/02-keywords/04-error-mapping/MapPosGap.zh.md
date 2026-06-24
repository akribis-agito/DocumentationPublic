---
keyword: MapPosGap
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 325
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
  - 8000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
summary: 相邻误差映射点之间的编码器计数间距。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MapPosGap

相邻误差映射点之间的编码器计数间距。

## 概述

`MapPosGap` 是一个按维度划分的数组（`[1]`/`[2]`/`[3]`），用于设置沿每个误差映射维度相邻修正点之间的位置间距（以编码器计数为单位）。较大的间距将相同数量的点（[MapLength](MapLength.md)）分散到更宽的范围，从而给出较粗的分辨率；较小的间距则在较短范围内给出更精细的修正。它与 [MapStartPos](MapStartPos.md)（起始）和 [MapLength](MapLength.md)（数量）一起定义了 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 的查找网格。

它是一个轴相关数组，保存至闪存，在轴处于运动中或电机使能时不能更改。

## 工作原理

间距是将编码器读数转换为表索引的分母：

$$
\text{index}_f = \frac{\text{PosBeforeCorrection} - \text{MapStartPos}[d]}{\text{MapPosGap}[d]}
$$

为了在实时控制中断中保持低开销，每当写入 `MapPosGap` 时，控制器会预先计算倒数 $1 / \text{MapPosGap}[d]$（作为单精度浮点数），并在每个周期乘以它。由此产生两个后果：

- **不得为零。** 零间距会导致除以零，因此如果你将其设为 0，固件会静默地替换为默认值 `1000`。
- **上限 8,000,000。** 该倒数保存在 32 位浮点数中（24 位尾数）；范围被限制以使间距被精确表示且索引保持准确。

`index_f` 的整数部分选择较低的网格点；小数部分是朝向下一个点的插值权重。

## 示例

```text
AMapPosGap[1]=1000   ; correction points 1000 encoder counts apart
AMapPosGap[1]        ; read the spacing for the first dimension
```

### 边界情况

- **索引 0** — 无效；有效索引为 `MapPosGap[1]`/`[2]`/`[3]`。`MapPosGap[0]` 不存在。
- **写入时电机使能/运动中** — 在电机使能或轴处于运动中时被拒绝。
- **零值** — 静默替换为默认值 `1000`，以保持倒数有定义。
- **超出范围** — 超出 `1`–`8 000 000` 的值被拒绝（8 M 上限保证精确的浮点倒数）。
- **`MapType = 0`** — 值已存储但不被查询。
- **保存** — 可保存至闪存；倒数在每次写入时以及上电时重新计算。
- **平台** — 在 standalone v4、central-i v4 和 central-i v5 上相同。

## 参见

- [MapLength](MapLength.md) — 每个维度的修正点数量
- [MapStartPos](MapStartPos.md) — 每个维度的起始位置
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) — 每个点处的修正值
- [Pos](../10-motion/01-kinematics-status/Pos.md) / [PosBeforeMap](PosBeforeMap.md) — 修正后与修正前的反馈
