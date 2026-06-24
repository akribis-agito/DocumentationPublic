---
keyword: ECAMStartCyc
summary: 循环/重复 ECAM 凸轮曲线起始处的 GenData 索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 301
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
  - 0
  - 1000
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 10000
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMStartCyc

循环/重复 ECAM 凸轮曲线起始处的 GenData 索引。

## 概述

`ECAMStartCyc` 定义循环/重复凸轮曲线起始处的 [GenData](../../20-arrays/GenData.md) 索引。它是一个包含 10 条凸轮曲线的数组，每个元素对应一条曲线。它是重复段的下边界，该段将重复回放 [ECAMCycles](ECAMCycles.md) 次，与上边界 [ECAMEndCyc](ECAMEndCyc.md) 配对使用。整体曲线由 [ECAMStart](ECAMStart.md) 和 [ECAMEnd](ECAMEnd.md) 界定。

## 工作原理

`ECAMStartCyc` 必须满足整体凸轮曲线所要求的索引顺序：

$$
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

`ECAMStartCyc` 与 [ECAMEndCyc](ECAMEndCyc.md) 界定重复段，该段将重复回放 `abs(ECAMCycles)` 次（前导段/重复段/尾随段模型参见 [ECAMStart](ECAMStart.md)）。当主变量推进超过 `ECAMEndCyc` 时，控制器将主窗口向后偏移一个周期宽度，从 `ECAMStartCyc` 重新回放该段，并递增 [ECAMCycCount](ECAMCycCount.md)。一个周期的主变量间距等于 `abs(ECAMGap) * (ECAMEndCyc - ECAMStartCyc)`。

为使从动件在各周期间连续运动（即使 `GenData[ECAMStartCyc]` 与 `GenData[ECAMEndCyc]` 不同），控制器在每个完成的周期上将高度差 `GenData[ECAMEndCyc] - GenData[ECAMStartCyc]` 累加到从轴偏置中（反向步进时则相减）。因此从动件每个周期递增该值，而不会跳回到段的第一个值。

如果主变量在单个控制周期内跳变超过一个完整周期宽度，控制器无法判断其属于哪个周期，将以[控制器错误代码 1030](../../../04-error-codes/controller-error-codes.md) 关断轴（电机失能）。

## 示例

```text
AECAMStartCyc[1]=20  ; 凸轮曲线 1 的重复段从 GenData 索引 20 开始
AECAMStartCyc[1]    ; 读取当前值
```

## 另请参阅

- [ECAMEndCyc](ECAMEndCyc.md) — 重复段的结束索引
- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — 整体曲线边界（段模型）
- [ECAMCycles](ECAMCycles.md) — 重复段的重复次数
- [ECAMCycCount](ECAMCycCount.md) — 当前周期索引，每次环绕时递增
