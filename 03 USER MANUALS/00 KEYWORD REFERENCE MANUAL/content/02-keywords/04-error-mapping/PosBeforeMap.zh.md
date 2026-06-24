---
keyword: PosBeforeMap
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 160
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: false
  units: user
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
summary: 只读的误差映射修正前反馈位置。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PosBeforeMap

只读的误差映射修正前反馈位置。

## 概述

`PosBeforeMap` 报告来自主编码器的轴位置，以用户单位表示，即在应用任何误差映射修正**之前**的位置。修正后的值由 [Pos](../10-motion/01-kinematics-status/Pos.md) 报告；当通过 [MapType](MapType.md) 启用映射时，差值 `Pos − PosBeforeMap` 即为 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 数组贡献的（经斜坡、插值的）修正值。比较两者是验证映射注入多少修正量的标准方法。

它是一个只读、轴相关的状态变量，不保存至闪存。

## 工作原理

`PosBeforeMap` 在**每个**控制周期、误差映射阶段开始时被捕获，作为解码后主编码器读数的快照——在修正分支运行*之前*。它被无条件记录，因此：

- 当映射**关闭**（`MapType = 0`）时，`Pos = PosBeforeMap`（无修正）。两个读数相等。
- 当映射**开启**时，固件根据 [MapEncoder](MapEncoder.md) 所选源计算插值修正值，并构成 `Pos = PosBeforeMap + correction`（修正值按接入斜坡缩放；参见 [MapErrOnStep](MapErrOnStep.md)）。
- 在**仿真**模式下跳过修正，因此同样 `Pos = PosBeforeMap`。

请注意，`PosBeforeMap` 始终跟踪本轴的**主**编码器，即使映射通过 [MapEncoder](MapEncoder.md) 查找不同的编码器——它是映射重塑为 `Pos` 的那个值的修正前基线。

## 示例

```text
APosBeforeMap        ; read the uncorrected feedback position
```

### 边界情况

- **只读** —— 写入被拒绝。
- **映射关闭** —— `PosBeforeMap` 等于 [Pos](../10-motion/01-kinematics-status/Pos.md)；其差值为 `0`。
- **仿真电机** —— 跳过映射；`PosBeforeMap` 等于 `Pos`。
- **仅主编码器** —— 始终反映本轴的主编码器，无论映射为查找选择的源 [MapEncoder](MapEncoder.md) 为何。
- **电机失能** —— 无论如何每个周期都采样；在伺服关闭时对诊断有用。
- **带取模（[ModRev](../03-encoder/04-modulo-mode/ModRev.md) ≠ 0）** —— 在 v5（central-i）上，`PosBeforeMap` 在取模环绕*之后*重新捕获，因此在发生环绕的那个周期它反映回绕后（在范围内）的编码器值。在 v4 上它在环绕*之前*捕获一次，因此在环绕周期它可能瞬间读到略微超出取模范围的值。该差异仅在取模激活时可观察到。
- **平台** —— v5 扩展至 64 位；v4 为 32 位。两种情况下单位均为用户单位。

## 版本间变更

| | v4（standalone 与 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位（`long`） | **64 位（`long long`）** |
| 范围 | ±2,147,483,647 | ±2,251,799,813,685,247 |

在 **v5** 中反馈流水线为 64 位，因此 `PosBeforeMap` 镜像更宽的 [Pos](../10-motion/01-kinematics-status/Pos.md) 范围。v5 **仅 central-i** 可用；在 standalone 上它仍为 32 位的 v4 值。

## 另请参阅

- [Pos](../10-motion/01-kinematics-status/Pos.md) —— 修正后的反馈位置；差值等于映射修正量
- [MapType](MapType.md) —— 启用产生该差值的修正
- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) —— 应用于反馈的修正值
- [MapErrOnStep](MapErrOnStep.md) —— 将修正值接入/退出斜坡，使差值逐渐增大/减小
