---
keyword: ECAMCycles
summary: 周期性 ECAM 凸轮曲线的重复次数（含无限循环模式）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 305
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMCycles

周期性 ECAM 凸轮曲线的重复次数（含无限循环模式）。

## 概述

`ECAMCycles` 定义重复/周期性凸轮曲线的重复次数。它是一个包含 10 个凸轮曲线的数组，每个曲线对应一个元素。与 [ECAMGap](ECAMGap.md) 的符号共同决定整体 ECAM 配置；当前循环由 [ECAMCycCount](ECAMCycCount.md) 报告。重复段由 [ECAMStartCyc](ECAMStartCyc.md) 和 [ECAMEndCyc](ECAMEndCyc.md) 界定。

## 工作原理

| 值 | ECAM 属性 |
|----|----|
| -2147483648 | 无限循环 ECAM，无起始段也无结束段 |
| 2147483647 | 无限循环 ECAM，仅有起始段 |
| \> 0 | 具有起始段和结束段的 ECAM，以及在起始位置同侧重复 ECAMCycles 次的周期性曲线 |
| \< 0 | 双向 ECAM，具有起始段和结束段，以及在起始位置两侧各半的 2\*abs(ECAMCycles) 次周期性曲线 |

`ECAMCycles` 的符号决定循环相对于主轴起始位置（由 [ECAMMasterIni](ECAMMasterIni.md) 设定）的布局：

- **正值 `ECAMCycles`** — 所有循环位于同一侧；主轴预期从其起始位置正向通过 `ECAMCycles` 个循环。[ECAMCycCount](ECAMCycCount.md) 的范围为 `1 … ECAMCycles`。
- **负值 `ECAMCycles`** — 循环对称分布在起始位置两侧，因此主轴可向任意方向运动。总计 `2*abs(ECAMCycles)` 个循环，`ECAMCycCount` 可取负值，范围为 `-ECAMCycles + 1 … ECAMCycles`。

对于两种**无限循环**哨兵值，控制器将曲线标记为无限循环，并在内部将其视为 2 循环（或 −2 循环）曲线，每当主轴到达循环边界时主窗口简单滚动，从而曲线无限重复，不存在正向（对于 `-2147483648` 也不存在负向）主轴限制。在无限循环模式下，`ECAMEndCyc` 到 `ECAMEnd` 之间的尾部条目（对于 `-2147483648`，还有 `ECAMStart` 到 `ECAMStartCyc` 之间的前导条目）将被忽略。待处理的 [StopECAM](StopECAM.md) 可干净地退出无限循环模式（详见该页面）。

> **注意：**`ECAMCycles` 描述的是同一曲线的重复次数，而非重复编号。若 `ECAMCycles = 1`，则无重复：`ECAMStartCyc` 和 `ECAMEndCyc` 无关紧要，因为该范围内的曲线已由 `ECAMStart` 和 `ECAMEnd` 包含。总之，`abs(ECAMCycles)` 必须大于 1 才能产生重复。`ECAMCycles` 不得为 `0`；循环次数为零的 [Begin](../04-motion-command/Begin.md) 将被拒绝。

## 示例

```text
AECAMCycles[1]=3     ; 凸轮曲线 1 的周期性曲线重复 3 次
AECAMCycles[1]      ; 读取当前值
```

有关曲线逻辑的更多信息，请参阅 [运动模式——电子凸轮（ECAM）](00-overview.md) 中的图示。

## 另请参阅

- [ECAMCycCount](ECAMCycCount.md) — 当前循环索引
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — 重复段的边界
- [ECAMMasterIni](ECAMMasterIni.md) — 在循环布局中设置起始位置
- [ECAMGap](ECAMGap.md) — 主轴值的间距与排列
- [StopECAM](StopECAM.md) — 优雅退出，包括从无限循环模式退出
