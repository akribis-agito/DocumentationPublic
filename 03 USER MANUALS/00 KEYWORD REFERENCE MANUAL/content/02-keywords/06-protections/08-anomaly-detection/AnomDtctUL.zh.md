---
keyword: AnomDtctUL
summary: 上限表，按被监测运动定义滤波后信号所要比较的期望分段的上边界。
availability:
  standalone: []
  central-i:
  - v5
can_code: 776
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 1025
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AnomDtctUL

上限表，按被监测运动定义滤波后信号所要比较的期望分段的上边界。

## 概述

`AnomDtctUL` 是异常检测期望分段的上边界。它与下限表 [AnomDtctLL](AnomDtctLL.md) 一起描述了被监测信号随运动推进时的正常形状。当滤波后的被监测信号在运动的该位置上升超过当前生效的上限时，检测器跳闸（停止行为参见 [AnomDtctCnfg](AnomDtctCnfg.md)）。

该表很大，因为它为多个被监测运动中的每一个存储了完整的曲线，沿每个运动逐点采样。

该关键字自 v5（central-i）起可用。

## 工作原理

该表按每个被监测运动划分为一个块（最多四个运动）。每个块最多容纳 256 个点。随着运动推进，检测器逐点前进；[AnomDtctGap](AnomDtctGap.md) 设定每个点在移动到下一个点之前保持多少个控制周期。比较从每个运动块的**第二**个槽开始，每经过一个 gap 窗口前进一个槽 —— 每个块的第一个槽（索引 1、257、513、769）存有数值，但从不与信号进行比较。

该数组为 1 索引（索引 0 为保留）；最高可用索引比 frontmatter 中的 `array_size` 小 1。各块依次连续排列（下表的索引范围表示数值*存储*的位置）：

| 索引范围 | 被监测运动 |
| --- | --- |
| 1 – 256 | motion 0 |
| 257 – 512 | motion 1 |
| 513 – 768 | motion 2 |
| 769 – 1024 | motion 3 |

每个索引处的值以所选被监测信号的原生单位进行比较（`AnomDtctUL` 本身不带单位换算）。当前运动的生效上限会镜像到 [AnomDtctSt](AnomDtctSt.md) 的元素 4，以便你读取检测器正在比较的对象。

用一条上包络线填充该表，使其稳妥地高于已知良好运动期间所见的信号，并为正常的逐周期波动留出余量。下包络线放入 [AnomDtctLL](AnomDtctLL.md)。

## 示例

```text
AAnomDtctUL[1]=12000     ; first stored slot of motion 0 (not compared; the walk starts at index 2)
AAnomDtctUL[2]=12500     ; first compared upper-limit point of motion 0
AAnomDtctUL[257]=8000    ; first stored slot of motion 1's block (not compared; comparison starts at index 258)
AAnomDtctUL[2]           ; read the first compared upper-limit point
```

## 另请参阅

- [AnomDtctLL](AnomDtctLL.md) —— 分段的下边界
- [AnomDtctGap](AnomDtctGap.md) —— 每个表点所跨越的控制周期数
- [AnomDtctCnfg](AnomDtctCnfg.md) —— 被监测源与运动选择
- [AnomDtctSt](AnomDtctSt.md) —— 生效限值与滤波后值
