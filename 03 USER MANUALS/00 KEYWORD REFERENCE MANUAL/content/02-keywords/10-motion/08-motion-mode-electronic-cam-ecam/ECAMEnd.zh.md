---
keyword: ECAMEnd
summary: ECAM 凸轮曲线结束处的 GenData 索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 303
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMEnd

ECAM 凸轮曲线结束处的 GenData 索引。

## 概述

`ECAMEnd` 定义凸轮曲线结束处的 [GenData](../../20-arrays/GenData.md) 索引。它是一个包含 10 个凸轮曲线的数组，每个曲线对应一个元素。它是整体曲线的上边界，与下边界 [ECAMStart](ECAMStart.md) 配对，而 [ECAMStartCyc](ECAMStartCyc.md) 和 [ECAMEndCyc](ECAMEndCyc.md) 则界定重复段。

## 工作原理

`ECAMEnd` 必须满足整体凸轮曲线的推导顺序约束：

$$
\text{ECAMStart} \leq \text{ECAMStartCyc} < \text{ECAMEndCyc} \leq \text{ECAMEnd}
$$

`ECAMEnd` 是曲线的最后一个条目，终止在所有重复循环完成后从 `ECAMEndCyc` 到 `ECAMEnd` 运行的尾部单次段（参见 [ECAMStart](ECAMStart.md) 中的段表）。当主轴处于或超过映射到 `ECAMEnd` 的主轴位置（*结束后*区域）时，从动件参考被钳位至 `GenData[ECAMEnd]`，使从动件保持在曲线末端位置不变。这适用于 [ECAMGap](ECAMGap.md) 的任意符号：负的 `ECAMGap` 通过内部对主轴读数取反来反转方向，但结束后钳位仍使用 `GenData[ECAMEnd]`（开始前钳位仍使用 `GenData[ECAMStart]`）。若在主轴到达该钳位时存在待处理的 [StopECAM](StopECAM.md)，则运动在此结束。

在仅保留起始段（`ECAMCycles = 2147483647`）或完全无尾部（`ECAMCycles = -2147483648`）的无限循环模式下，`ECAMEndCyc` 到 `ECAMEnd` 之间的表条目将被忽略——参见 [ECAMCycles](ECAMCycles.md)。

## 示例

```text
AECAMEnd[1]=100      ; 凸轮曲线 1 在 GenData 索引 100 处结束
AECAMEnd[1]         ; 读取当前值
```

## 另请参阅

- [ECAMStart](ECAMStart.md) — 整体曲线的起始索引（段模型与钳位）
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — 重复段的边界
- [ECAMCycles](ECAMCycles.md) — 忽略尾部段的无限循环模式
- [GenData](../../20-arrays/GenData.md) — 存储凸轮曲线的数组
