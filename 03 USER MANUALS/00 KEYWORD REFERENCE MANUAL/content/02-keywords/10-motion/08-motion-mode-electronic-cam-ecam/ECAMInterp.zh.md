---
keyword: ECAMInterp
summary: 保留的内部 ECAM 关键字（未实现）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 308
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
  - 0
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMInterp

保留的内部 ECAM 关键字（未实现）。

## 概述

`ECAMInterp` 是 ECAM 运动组中的保留关键字，用于选择凸轮表条目之间所用的插值模式。它是一个包含 10 个凸轮曲线的数组，每个曲线对应一个元素。其有效范围固定为 `[0, 0]`，因此唯一接受的值为 `0`。

相邻 [GenData](../../20-arrays/GenData.md) 条目之间的插值当前始终为**线性**——控制器按主轴位置的小数部分对两个相邻表值进行混合（映射方式参见 [ECAMGap](ECAMGap.md)）。目前不支持选择其他插值模式。

线性混合以优于单采样分辨率的精度执行，而非从一个表条目直接跳至下一个，因此从动件参考在各凸轮点之间平滑前进。由于从动件速度（以及由此导出的速度/加速度前馈）是该参考的每周期变化量，正是这种子采样混合使指令速度在各表条目处保持连续，而非在每个条目处发生跳变。这也是相邻凸轮表条目差值不得超过内部单采样限值的原因（参见 [ECAMGap](ECAMGap.md)）：该限值约束了参考在一个控制周期内的最大变化速率。

> **文档待补充：**`ECAMInterp` 当前为保留关键字，尚未实现（`implemented: not_implemented`）。仅接受 `0`；未定义任何依赖值的行为。

## 示例

```text
AECAMInterp[1]      ; 读取凸轮曲线 1 的（保留）插值模式
```

## 另请参阅

- [ECAMGap](ECAMGap.md) — 主轴到索引的映射及所应用的线性插值
- [GenData](../../20-arrays/GenData.md) — 存储凸轮曲线的数组
- [运动模式——电子凸轮（ECAM）](00-overview.md) — ECAM 运动概述
