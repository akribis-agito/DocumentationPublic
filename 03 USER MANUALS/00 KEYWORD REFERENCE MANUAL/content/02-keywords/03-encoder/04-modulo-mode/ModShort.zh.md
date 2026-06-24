---
keyword: ModShort
summary: 在取模模式下为绝对 PTP 运动选择运动路径（正常、仅正向、仅负向或最短）；仅在 central-i v5 上实现。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 149
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides:
  central-i.v5:
    access: rw
    units: none
    range:
    - 0
    - 3
    implemented: final
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ModShort

在取模模式下为绝对 PTP 运动选择运动路径。

## 概述

`ModShort` 定义了在启用取模模式（`ModRev ≠ 0`）时，绝对点到点（PTP）运动所采用的运动路径。它用于常规运动（[MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) = 1 或 2）或回零过程中（[HomingDef](../../16-homing/HomingDef.md)[1, 11, …, 141] = 12）。它与 [ModRev](ModRev.md)（启用取模环绕）配合使用。由于它是轴相关参数并保存至闪存，因此在电机使能或运动中时无法更改。

> **可用性：** `ModShort` 仅在 **central-i v5** 上实现（范围 0–3）。在 v4（standalone 和 central-i）上未实现且无效——绝对 PTP 运动始终前往字面目标。

## 工作原理

`ModShort` 在指令绝对 PTP 目标（无相对目标）时被评估一次。它在运动开始前，相对于当前参考值重写绝对目标 [AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md)：

| 值 | 说明 | 动作 |
|---|---|---|
| 0 | 轴像直线轴一样移动到目标（如果绝对位置增量超过 `ModRev`，则额外移动一圈或多圈）。 | `AbsTrgt` 不变——移动到字面目标。 |
| 1 | 仅负向。如果目标高于当前位置，则采用最短的仅负向路径；否则像直线轴一样移动。 | 如果 `AbsTrgt` 高于当前参考值，则从 `AbsTrgt` 减去 `ModRev`。 |
| 2 | 仅正向。如果目标低于当前位置，则采用最短的仅正向路径；否则像直线轴一样移动。 | 如果 `AbsTrgt` 低于当前参考值，则向 `AbsTrgt` 加上 `ModRev`。 |
| 3 | 最短路径。即使绝对位置增量超过 `ModRev`，也不额外移动一圈或多圈。 | 计算 `delta = (AbsTrgt − current reference + ModRev) mod ModRev`；如果 `delta ≤ ModRev/2` 则移动 `+delta`，否则移动 `−(ModRev − delta)`。 |

对于值 3，固件将请求的增量折叠到一圈之内，并选择距离不超过半圈的方向，因此轴到达目标的行程绝不会超过 `ModRev/2`。

## 示例

```text
AModShort=0          ; normal (linear-like) path
AModShort=3          ; shortest path
```

## 版本间变更

| | v4（standalone 和 central-i） | v5（central-i） |
|---|---|---|
| 访问 | 未实现（无效） | 读/写，范围 0–3 |

路径选择逻辑仅存在于 v5 固件上；v4 上没有此逻辑。**v5 仅适用于 central-i。**

## 另请参阅

- [ModRev](ModRev.md) —— 启用 `ModShort` 所在的取模模式
- [MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) —— `ModShort` 所适用的运动模式
- [HomingDef](../../16-homing/HomingDef.md) —— 可调用 `ModShort` 的回零定义
