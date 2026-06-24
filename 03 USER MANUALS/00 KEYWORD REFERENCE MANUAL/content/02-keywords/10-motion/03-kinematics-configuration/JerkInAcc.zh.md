---
keyword: JerkInAcc
summary: 在三阶（无限 snap）曲线的加速阶段所应用的加加速度。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 720
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 100
  - 1000000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    units: user
    range:
    - 10000.0
    - 1.0e+20
    default: 100000000.0
    can_code: 565
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# JerkInAcc

在三阶（无限 snap）曲线的加速阶段所应用的加加速度。

## 概述

`JerkInAcc` 是在三阶轨迹规划器的**加速**阶段所应用的加加速度约束，当 [JerkMode](../02-motion-configuration/JerkMode.md) = 1 时使用。与二阶 [Jerk](Jerk.md)（移动平均指数）不同，`JerkInAcc` 是真正的加加速度限制：它限定运动期间加速度本身上升到峰值 [Accel](Accel.md) 以及从峰值回落的速度，从而圆滑加速斜坡的拐角。其减速阶段的对应参数是 [JerkInDec](JerkInDec.md)。该参数可读写、轴相关、保存至闪存，并可在任意时刻更改，包括在运动中更改。

这个三阶（"无限 snap"）规划器是一个围绕双 S 速度曲线构建的、基于段的结构化生成器。`JerkInAcc` 仅在 `JerkMode = 1` 时被查询；在默认的二阶模式下它无效。

## 工作原理

当 `JerkMode = 1` 时，规划器每个周期运行结构化加加速度规划器，将 `JerkInAcc`（以及 `JerkInDec`）与 [Speed](Speed.md)、[Accel](Accel.md) 和 [Decel](Decel.md) 限值一同用作加加速度约束。规划器按固定的段序列推进，`JerkInAcc` 是在正加加速度和负加加速度加速段中所应用的加加速度幅值。它塑造运动的前半部分：

| 段 | 所用加加速度 |
|---------|-----------|
| 加速，加加速上升 | `+JerkInAcc` —— 加速度向 `Accel` 上升 |
| 加速，恒定 | 0 —— 加速度保持在 `Accel` |
| 加速，加加速下降 | `−JerkInAcc` —— 加速度在巡航处回落到 0 |

更大的 `JerkInAcc` 使加速度更快达到 `Accel` 限值（更陡、更短的 S 过渡）；更小的值则将过渡分散到更长的时间，以获得更平缓的运动。

![三阶速度与加速度曲线段](jerkinacc-segments.svg)

### 内部加加速度上限

在规划器使用 `JerkInAcc` 之前，加速阶段的加加速度会被钳位，使加速度无法在单个控制周期内过冲 [Accel](Accel.md) 限值。有效加加速度被限制为

$$
\dot{a}_{\max} = \tfrac{1}{2}\,\text{Accel}\cdot f_s
$$

其中 $f_s$ 是控制环采样率。在该上限处，加速度从 0 上升到 `Accel` 所需的时间为 $\text{Accel}/\dot a_{\max} = 2/f_s$，即约两个控制周期。因此请求一个高于该上限的 `JerkInAcc` 不会进一步影响加加速上升/下降斜坡的持续时间——该斜坡已经达到离散更新率所允许的最短值。每当规划器（重新）初始化时，包括 `JerkInAcc`、`Accel` 或 `Speed` 更改所触发的即时重新计算，该上限都会根据当前 `Accel` 重新计算。

### 单位与内部缩放（v4）

在 v4 上，`JerkInAcc` 是一个无量纲整数，范围为 100–1,000,000,000（默认 1,000,000）。控制器在规划器中应用该值之前先将其乘以固定因子 1000，因此以 counts/s³ 为单位的有效加加速度约束为：

$$
\text{jerk}_{\text{acc}} = \text{JerkInAcc} \cdot 1000
$$

### 紧急停止

对于限位开关、软件限位和受控停止输入触发的停止，三阶规划器会被旁路：这些情形会强制内部加加速度模式 OFF，并以 [EmrgDec](EmrgDec.md) 减速而不做加加速度整形，因此 `JerkInAcc` 不适用于此类停止。[Abort](../04-motion-command/Abort.md) 完全不进行斜坡减速，也不受 `JerkInAcc` 影响。

### 边界情形

- **电机失能：** 数值被保留；规划器不运行。
- **越界写入：** 参数系统会钳位到 `100`–`1,000,000,000`；超出范围的值被拒绝。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 三阶规划器通过其内部状态跟踪环绕；加加速度约束不受影响。
- **活动故障：** 轴被禁用；重新使能并下一次 `Begin` 时，会重新读取 `JerkInAcc`。
- **其他运动模式：** 当 [JerkMode](../02-motion-configuration/JerkMode.md) = 1 时，由结构化加加速度规划器在受控点到点系列中消耗——PTP（`MotionMode = 1`）、重复 PTP（`MotionMode = 2`）以及操纵杆位置直接/间接模式（`MotionMode = 12 / 13`）。点动（`MotionMode = 0`）、速度/操纵杆速度模式以及不经规划器而驱动位置指令的位置直接（`P`/`D`）模式都会忽略它。
- **运动中实时更改：** 允许且立即应用——当规划器检测到 `JerkInAcc`（或 `Speed`/`Accel`/`Decel`）发生更改时，会在同一周期从当前状态重新规划。在 **v4** 中，这种即时重新规划仅在轴仍处于加速或巡航时发生；一旦轴进入减速阶段，在该次运动的剩余部分中更改会被忽略。在 **v5** 中，重新规划可在任意时刻应用，包括在减速期间。

## 示例

```text
AJerkInAcc=2000000   ; acceleration-phase jerk (× 1000 internally on v4)
AJerkInAcc           ; read current value
```

`JerkInAcc` 仅在 [JerkMode](../02-motion-configuration/JerkMode.md) = 1 时影响运动。

## 版本间变更

| | v4（standalone 与 central-i） | v5（central-i） |
|---|---|---|
| 命令码 | 720 | 565 |
| 数据类型 | 32 位整数 | 浮点数 |
| 单位 | 无，内部值 × 1000 | 用户单位（加加速度以用户单位/s³ 表示，直接使用） |

在 **v5** 中 `JerkInAcc` 是直接以用户加加速度单位表示的浮点值，并传入同一结构化规划器，不带 ×1000 因子。**v5 仅适用于 central-i。**

## 参见

- [JerkInDec](JerkInDec.md) — 减速阶段的加加速度
- [Jerk](Jerk.md) — 二阶 S 曲线设置（机制不同）
- [JerkMode](../02-motion-configuration/JerkMode.md) — 必须为 1，`JerkInAcc` 才生效
- [Accel](Accel.md) — 加加速度所上升到的峰值加速度
- [EmrgDec](EmrgDec.md) — 紧急停止会旁路加加速度规划器
