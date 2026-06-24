---
keyword: ECAMMaster
summary: 复杂 CAN 编码，用于为每个 ECAM 凸轮曲线选择主变量来源。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 309
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMMaster

复杂 CAN 编码，用于为每个 ECAM 凸轮曲线选择主变量来源。

## 概述

`ECAMMaster` 是定义 ECAM 运动中主变量来源的[复杂 CAN 编码](../../../01-keyword-usage-and-syntax/complex-can-code.md)（CCC）。它是一个包含 10 条凸轮曲线的数组，每个元素对应一条曲线。随着主值的变化，从轴的位置参考将跟踪存储在 [GenData](../../20-arrays/GenData.md) 中的凸轮曲线，间距由 [ECAMGap](ECAMGap.md) 定义。

CCC 编码了任意可读关键字的关键字名、轴号和数组索引，因此主变量可以是另一轴的位置（[Pos](../01-kinematics-status/Pos.md) 或 [PosRef](../01-kinematics-status/PosRef.md)）、辅助编码器（[AuxPos](../01-kinematics-status/AuxPos.md)）、计数器、通用存储元素或任何其他可读参数。所选来源必须是参数（而非指令/函数）；CCC 的轴号和数组索引对该关键字必须有效。默认值 `0` 不可用作主变量，必须在 ECAM 运动启动前进行设置。

## 工作原理

主变量来源在 ECAM 运动启动（[Begin](../04-motion-command/Begin.md)）时解析一次，使用当前活动凸轮曲线（[ECAMTableNum](ECAMTableNum.md)）对应的 CCC。控制器随后在每个控制周期跟踪主值的*变化量*，而非绝对值：

- 每个控制周期对主值进行采样，并将与上一周期的差值累积到内部主位置中。跟踪增量使 ECAM 即使在主变量来源超出数值范围后也能正常工作——这对由自由运行计数器或辅助位置驱动的无限凸轮运动非常有用（参见 [ECAMCycles](ECAMCycles.md)）。
- 累积的主位置随后通过 [ECAMGap](ECAMGap.md) 映射为凸轮表中的小数索引；从轴参考从 [GenData](../../20-arrays/GenData.md) 中对应索引处读取，并在相邻条目间进行线性插值（索引计算方法参见 [ECAMGap](ECAMGap.md)）。
- 在 **v5** 上，主变量可以是 32 位或 64 位整数、单精度或双精度浮点数，控制器以其原生类型读取。在 **v4** 上，主变量来源始终以 32 位值读取，因此 64 位、单精度或双精度主变量来源仅在 v5 上能被正确读取。

如果来源关键字的 CCC 无效（未知关键字、轴号超出范围、索引超出范围，或指向函数而非参数），则 [Begin](../04-motion-command/Begin.md) 将被拒绝并报错，ECAM 运动不会启动。

## 示例

```text
AECAMMaster[1]      ; 读取凸轮曲线 1 的主变量 CCC
```

## 另请参阅

- [ECAMGap](ECAMGap.md) — 主值间距及主值到索引的映射
- [ECAMMasterIni](ECAMMasterIni.md) — 运动启动时的初始主值偏置
- [ECAMTableNum](ECAMTableNum.md) — 选择活动凸轮曲线（及对应的 `ECAMMaster`）
- [GenData](../../20-arrays/GenData.md) — 存储凸轮曲线的数组
- [复杂 CAN 编码](../../../01-keyword-usage-and-syntax/complex-can-code.md) — 来源关键字的编码方式
