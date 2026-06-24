---
keyword: AccShapeFact
summary: 加速度整形曲线的逐段加速度缩放因子数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 164
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AccShapeFact

加速度整形曲线的逐段加速度缩放因子数组。

## 概述

`AccShapeFact` 是一个数组（10 个可用条目，索引 1–10），用于定义加速度整形曲线中每个分段的加速度缩放因子。每个元素规定在相应分段（其距离到目标分段由 [AccShapeDist](AccShapeDist.md) 设置）期间应用的最大加速度的比例。仅当启用 [AccShapeOn](AccShapeOn.md) 时才应用整形。它是一个轴相关数组，保存至闪存，可在任何时候更改。

## 工作原理

当到目标的剩余距离落入由 [AccShapeDist](AccShapeDist.md) 定义的分段内时，匹配的 `AccShapeFact` 条目被读取为**按 65536 缩放的定点小数**，并乘入该周期的加速度和减速度限值：

```text
factor      = AccShapeFact[n] / 65536
AccelFinal  = Accel × AccelFact × factor
DecelFinal  = Decel × AccelFact × factor
```

| AccShapeFact value | Resulting factor |
|---|---|
| 65536 | ×1.0 (full acceleration) |
| 49152 | ×0.75 |
| 32768 | ×0.5 |
| 16384 | ×0.25 |
| 0 | ×0 (no acceleration in this band) |

各因子与其距离配对，并在该表被写入时重新排序为距离升序，因此 `AccShapeFact[n]` 中的值始终与 `AccShapeDist[n]` 同行。数组大小为 11 以允许基于 1 的命令索引；只有索引 1–10 被使用。完整机制参见 [AccShapeOn](AccShapeOn.md)。

## 示例

```text
AAccShapeFact[1]=32768   ; first (nearest-target) band runs at half acceleration
AAccShapeFact[2]=65536   ; second band at full acceleration
AAccShapeFact[1]        ; query first segment factor
```

### 边界情况

- **电机失能：** 保持各值；不运行规划器。
- **越界写入：** 参数系统拒绝负值；范围为 `0`–`2³¹−1`（高于 `65536` 的值被接受并作为大于 1 的乘子，将加速度缩放至高于所配置的 `Accel`）。
- **索引 `[0]`：** 在用户可见空间中不存在；该关键字为 1 索引。读取 `[0]` 返回错误。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 整形因子按每个周期从距离分段中选取；环绕不改变到目标的距离。
- **存在活动故障：** 轴被禁用；该表得以保留。
- **其他运动模式：** 仅由 PTP/重复 PTP 规划器以及间接位置跟随和间接齿轮跟随规划器查询；点动、操纵杆速度和直接模式忽略该表。
- **运动中实时更改：** 允许；控制器在每次写入后重新排序，新因子在下一个周期生效。
- **`AccShapeFact = 0`：** 该分段内加速度为零——规划器将在该分段内保持当前速度，既不加速也不减速，直至退出该分段。这会延长运动时间，通常不是用户想要的结果。

## 另请参阅

- [AccShapeOn](AccShapeOn.md) — 启用加速度整形
- [AccShapeDist](AccShapeDist.md) — 逐段距离
