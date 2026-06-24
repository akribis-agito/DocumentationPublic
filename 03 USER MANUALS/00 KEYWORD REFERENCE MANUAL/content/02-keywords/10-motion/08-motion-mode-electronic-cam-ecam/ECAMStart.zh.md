---
keyword: ECAMStart
summary: ECAM 凸轮曲线起始处的 GenData 索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 300
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMStart

ECAM 凸轮曲线起始处的 GenData 索引。

## 概述

`ECAMStart` 定义凸轮曲线起始处的 [GenData](../../20-arrays/GenData.md) 索引。它是一个包含 10 条凸轮曲线的数组，每个元素对应一条曲线。它是整体曲线的下边界，与上边界 [ECAMEnd](ECAMEnd.md) 配对使用；[ECAMStartCyc](ECAMStartCyc.md) 和 [ECAMEndCyc](ECAMEndCyc.md) 则界定重复段。

## 工作原理

`ECAMStart` 必须满足整体凸轮曲线所要求的索引顺序：

$$
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

四个索引关键字将凸轮曲线划分为三个段，控制器随主变量推进依次回放：

| 段 | 索引范围 | 作用 |
|----|----|----|
| 前导段（单次执行） | `ECAMStart` … `ECAMStartCyc` | 主变量进入范围时执行一次；用作导入/加速段。 |
| 重复段 | `ECAMStartCyc` … `ECAMEndCyc` | 重复回放 `abs(ECAMCycles)` 次（参见 [ECAMCycles](ECAMCycles.md)）。 |
| 尾随段（单次执行） | `ECAMEndCyc` … `ECAMEnd` | 主变量离开循环后执行一次；用作导出/减速段。 |

`ECAMStart` 是曲线的第一个条目。当主变量处于或低于映射到 `ECAMStart` 的主位置时（即*预起始*区域），从动件参考被钳位到 `GenData[ECAMStart]`（正 [ECAMGap](ECAMGap.md) 时），使其保持不动而不会超出表格范围；负 `ECAMGap` 时，`ECAMStart` 和 `ECAMEnd` 作为钳位端的角色互换。若主变量到达该钳位时存在待处理的 [StopECAM](StopECAM.md)，则运动在此结束。

即使 `ECAMCycles = 1`（无重复），四个索引关键字仍须设置为非零值并满足上述顺序；`ECAMStartCyc` 和 `ECAMEndCyc` 仍界定重复段，只是该段仅执行一次，因此整体曲线跨越 `ECAMStart` … `ECAMEnd`。四个索引中任一为 `0` 表示该表格未使用，ECAM 运动启动时将被拒绝。

## 示例

```text
AECAMStart[1]=1      ; 凸轮曲线 1 从 GenData 索引 1 开始
AECAMStart[1]       ; 读取当前值
```

## 另请参阅

- [ECAMEnd](ECAMEnd.md) — 整体曲线的结束索引
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — 重复段的边界
- [ECAMGap](ECAMGap.md) — 主值到索引的映射及方向
- [GenData](../../20-arrays/GenData.md) — 存储凸轮曲线的数组
