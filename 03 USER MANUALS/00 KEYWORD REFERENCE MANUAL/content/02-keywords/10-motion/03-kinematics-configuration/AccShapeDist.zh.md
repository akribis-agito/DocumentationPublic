---
keyword: AccShapeDist
summary: 定义加速度整形曲线的逐段距离数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 163
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - 0
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AccShapeDist

定义加速度整形曲线的逐段距离数组。

## 概述

`AccShapeDist` 是一个数组（10 个可用条目，索引 1–10），用于定义加速度整形曲线中每个分段的**距离到目标阈值**。它与 [AccShapeFact](AccShapeFact.md) 一起规定加速度幅值在运动过程中如何分布，以减小机械振动。仅当启用 [AccShapeOn](AccShapeOn.md) 时才应用整形。它是一个轴相关数组，保存至闪存，可在任何时候更改。

## 工作原理

每个控制周期，规划器将到目标的剩余距离 `|AbsTrgt − PosRef|` 与这些阈值进行比较，并使用匹配的 [AccShapeFact](AccShapeFact.md) 条目作为加速度缩放比例。阈值按**最接近目标优先**进行解释：第一个其距离超过剩余距离的条目选定该分段。如果剩余距离大于所有阈值，则因子为 `1.0`（无整形）。

这些值与位置采用相同的用户单位。您**无需**按顺序输入它们——写入任何 `AccShapeDist`/`AccShapeFact` 元素时，控制器会在使用前将（距离，因子）对按距离升序重新排序。该数组声明大小为 11，以便命令索引可以从 `1` 开始；只有索引 1–10 携带数据。完整的查找机制参见 [AccShapeOn](AccShapeOn.md)。

## 示例

```text
AAccShapeDist[1]=5000    ; nearest band: remaining distance < 5000 user units
AAccShapeDist[2]=8000    ; next band: 5000 .. 8000 user units
AAccShapeDist[1]        ; query first segment distance
```

### 边界情况

- **电机失能：** 保持各值；不运行规划器。
- **越界写入：** 参数系统钳位到 `0`–`2³¹−1`（v4）或 `0`–`2⁵¹−1`（v5）；负值被拒绝。
- **索引 `[0]`：** 在用户可见空间中不存在；该关键字为 1 索引（条目 `[1]` … `[10]`）。读取 `[0]` 返回错误。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 距离 `|AbsTrgt − PosRef|` 在环绕后以主编码器单位表示，因此整形分段行为保持一致。
- **存在活动故障：** 轴被禁用；该表在故障期间得以保留。
- **其他运动模式：** 只有 PTP 系列规划器会查询该表；其他场合忽略。
- **运动中实时更改：** 允许；控制器在每次写入后重新排序（距离，因子）对，因此查找在下一个周期使用新表。
- **重复或零距离：** 重新排序后，多个具有相同阈值的条目会合并到首次遇到的那个；零距离条目有效（作为最近分段）。

## 版本间的变更

在 **v5（central-i）** 中，距离阈值为 64 位（与 64 位位置流水线匹配），从而提供 frontmatter 中所示的更大范围；整形机制在其他方面不变。**v5 仅限 central-i**，因此在 standalone 上阈值仍为 v4 的 32 位值。

## 另请参阅

- [AccShapeOn](AccShapeOn.md) — 启用加速度整形
- [AccShapeFact](AccShapeFact.md) — 逐段加速度缩放因子
