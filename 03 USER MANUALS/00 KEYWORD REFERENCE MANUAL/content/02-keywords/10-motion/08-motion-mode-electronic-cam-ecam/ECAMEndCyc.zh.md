---
keyword: ECAMEndCyc
summary: 周期性/重复 ECAM 凸轮曲线结束处的 GenData 索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 302
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
  default: 100
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
# ECAMEndCyc

周期性/重复 ECAM 凸轮曲线结束处的 GenData 索引。

## 概述

`ECAMEndCyc` 定义周期性/重复凸轮曲线结束处的 [GenData](../../20-arrays/GenData.md) 索引。它是一个包含 10 个凸轮曲线的数组，每个曲线对应一个元素。它是重复段的上边界，该段将被重复 [ECAMCycles](ECAMCycles.md) 次，与下边界 [ECAMStartCyc](ECAMStartCyc.md) 配对。整体曲线由 [ECAMStart](ECAMStart.md) 和 [ECAMEnd](ECAMEnd.md) 界定。

## 工作原理

`ECAMEndCyc` 必须满足整体凸轮曲线的推导顺序约束：

$$
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

`ECAMEndCyc` 是始于 [ECAMStartCyc](ECAMStartCyc.md) 的重复段的上边界（参见 [ECAMStart](ECAMStart.md) 中的前导/重复/尾部段模型）。一个完整循环在主轴单位中跨越 `abs(ECAMGap) * (ECAMEndCyc - ECAMStartCyc)`。当主轴越过映射到 `ECAMEndCyc` 的位置时，控制器进入下一循环：步进 [ECAMCycCount](ECAMCycCount.md) 并累加从动件位置偏移量 `GenData[ECAMEndCyc] - GenData[ECAMStartCyc]`，使从动件平滑连续地前进，而非跳回段的起始值。最后一个循环完成后，控制器播放从 `ECAMEndCyc` 到 [ECAMEnd](ECAMEnd.md) 的尾部单次段。若主轴在单个控制周期内前进超过一个完整循环宽度，则无法解算换绕，控制器将以[控制器错误代码 1030](../../../04-error-codes/controller-error-codes.md) 触发轴故障（电机失能）。

在无限循环模式（`ECAMCycles = 2147483647` 或 `-2147483648`）下，主轴在 `ECAMStartCyc … ECAMEndCyc` 窗口内无限循环；`ECAMEndCyc` 到 `ECAMEnd` 之间的表条目将被忽略。参见 [ECAMCycles](ECAMCycles.md)。

## 示例

```text
AECAMEndCyc[1]=80    ; 凸轮曲线 1 的重复段在 GenData 索引 80 处结束
AECAMEndCyc[1]      ; 读取当前值
```

## 另请参阅

- [ECAMStartCyc](ECAMStartCyc.md) — 重复段的起始索引
- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — 整体曲线的边界（段模型）
- [ECAMCycles](ECAMCycles.md) — 重复段的重复次数
- [ECAMCycCount](ECAMCycCount.md) — 每次换绕时步进的当前循环索引
