---
keyword: ECAMMasterIni
summary: 运动启动时起始主值相对于 ECAM 范围的偏置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 306
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
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMMasterIni

运动启动时起始主值相对于 ECAM 范围的偏置。

## 概述

`ECAMMasterIni` 表示 ECAM 运动启动时起始主值相对于 ECAM 范围的偏置。它是一个包含 10 条凸轮曲线的数组，每个元素对应一条曲线。它决定了在凸轮范围内主变量的起始位置；其确切作用取决于 [ECAMGap](ECAMGap.md) 的符号和 [ECAMCycles](ECAMCycles.md) 的值。

`ECAMMasterIni` 的符号规则因版本而异。在 **v4** 上，其符号必须与 [ECAMGap](ECAMGap.md) 一致：当 `ECAMGap` 为正时，`ECAMMasterIni` 必须为零或正数；当 `ECAMGap` 为负时，`ECAMMasterIni` 必须为零或负数。在 **v5** 上，`ECAMMasterIni` 无论 `ECAMGap` 符号如何，始终必须为零或正数。在两个版本中，其绝对值都必须足够小，以确保运动启动时不超出第一个重复周期。

## 工作原理

ECAM 运动启动（[Begin](../04-motion-command/Begin.md)）时，控制器将当前主值快照作为主范围的原点。`ECAMMasterIni` 决定该快照在范围内的位置：当 `ECAMMasterIni = 0` 时，主变量从范围起始处开始（正 [ECAMGap](ECAMGap.md) 时为 `GenData[ECAMStart]`）；正值将起始点向曲线中移动相应的主变量单位数，使从动件从凸轮曲线中途某处开始。无论 `ECAMMasterIni` 取何值，从动件的参考均在启动时进行偏置，以避免跳变。

- 对于正 [ECAMGap](ECAMGap.md)，偏置从范围起始处向前测量；对于负 `ECAMGap`，则相对于取反后的主值测量，因此相同的正值仍将起始点向曲线中移动。
- 对于负 [ECAMCycles](ECAMCycles.md)（双向凸轮），`ECAMMasterIni` 定位的是重复区域的*中间点*——即运动启动时主变量预期所在的位置——使曲线可以向两个方向延伸。

允许的最大幅值取决于版本：

- 在 **v4** 上，对所有 `ECAMCycles` 值统一适用一个幅值上限：$\lvert\text{ECAMMasterIni}\rvert \le \lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$。
- 在 **v5** 上，上限取决于 `ECAMCycles`：

| ECAMCycles | ECAMMasterIni 的最大值（v5） |
|------------|--------------------------------|
| 1          | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$ |
| \> 1       | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEndCyc} - \text{ECAMStart})$ |
| \< 0       | $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEndCyc} - \text{ECAMStartCyc})$ |

## 示例

```text
AECAMMasterIni[1]=0  ; 从凸轮曲线 1 的 ECAM 范围起始处开始
AECAMMasterIni[1]   ; 读取当前值
```

有关初始偏置的更多信息，请参阅 [运动模式——电子凸轮（ECAM）](00-overview.md) 中的图示，初始偏置因 ECAMGap 和 ECAMCycles 而有所不同。

## 版本间变更

| | v4（standalone 及 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 / 范围 | 32 位，`-2147483648` … `2147483647` | 64 位，`-2251799813685248` … `2251799813685247` |

在 **v4**（standalone 和 central-i）中，`ECAMMasterIni` 依据单一幅值上限进行校验——对所有 `ECAMCycles` 值，其绝对值不得超过 $\lvert\text{ECAMGap}\rvert \cdot (\text{ECAMEnd} - \text{ECAMStart})$——且其符号必须与 `ECAMGap` 一致（`ECAMGap` 为正时为零或正数，为负时为零或负数）。在 **v5** 中，`ECAMMasterIni` 为 64 位值，范围如前端元数据所示，与该版本使用的 64 位主位置匹配；v5 还引入了上表所示的按 `ECAMCycles` 区分的最大值上限，并要求 `ECAMMasterIni` 无论 `ECAMGap` 符号如何，均为零或正数。**v5 仅限 central-i。**

## 另请参阅

- [ECAMGap](ECAMGap.md) — 主值间距/方向及主值到索引的映射
- [ECAMCycles](ECAMCycles.md) — 曲线重复次数
- [ECAMMaster](ECAMMaster.md) — 选择主变量
