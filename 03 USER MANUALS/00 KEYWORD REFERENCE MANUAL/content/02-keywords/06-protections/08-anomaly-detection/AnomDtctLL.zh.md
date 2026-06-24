---
keyword: AnomDtctLL
summary: 下限表，按被监测运动定义滤波信号据以校验的预期分段的下边界。
availability:
  standalone: []
  central-i:
  - v5
can_code: 777
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
# AnomDtctLL

下限表，按被监测运动定义滤波信号据以校验的预期分段的下边界。

## 概述

`AnomDtctLL` 是异常检测预期分段的下边界。它与上限表 [AnomDtctUL](AnomDtctUL.md) 一起，描述了被监测信号随运动推进的正常形态。当滤波后的被监测信号在该运动点处低于下限时，检测器触发（停止行为参见 [AnomDtctCnfg](AnomDtctCnfg.md)）。

该表很大，因为它为若干个被监测运动中的每一个存储一条完整曲线，沿每个运动逐点采样。

该关键字自 v5（central-i）起可用。

## 工作原理

该表按每个被监测运动划分为一个块（最多四个运动）。每个块保存最多 256 个点。随着运动推进，检测器每次推进一个点；[AnomDtctGap](AnomDtctGap.md) 设定每个点在移动到下一个点之前保持多少个控制周期。比较从每个运动块的**第二个**槽位开始，每个 gap 窗口推进一个槽位——每个块的第一个槽位（索引 1、257、513、769）保存一个值,但从不与信号进行比较。

该数组是 1-indexed（索引 0 为保留）；最高可用索引比前置元数据中的 `array_size` 小 1。各块按顺序排布，与 [AnomDtctUL](AnomDtctUL.md) 对应（下面的索引范围显示值的*存储*位置）：

| 索引范围 | 被监测运动 |
| --- | --- |
| 1 – 256 | 运动 0 |
| 257 – 512 | 运动 1 |
| 513 – 768 | 运动 2 |
| 769 – 1024 | 运动 3 |

每个索引处的值以所选被监测信号的原生单位进行比较（`AnomDtctLL` 本身不携带单位换算）。当前运动的活动下限镜像到 [AnomDtctSt](AnomDtctSt.md) 元素 3，因此你可以读取检测器据以比较的值。

用一条下包络填充该表，使其舒适地位于已知良好运动期间所见信号的下方，为正常的周期间变化留出余量。上包络写入 [AnomDtctUL](AnomDtctUL.md)。当滤波后的值在任一侧超出分段时，检测器报告异常。

## 示例

```text
AAnomDtctLL[1]=-12000    ; first stored slot of motion 0 (not compared; the walk starts at index 2)
AAnomDtctLL[2]=-12500    ; first compared lower-limit point of motion 0
AAnomDtctLL[257]=-8000   ; first stored slot of motion 1's block (not compared; comparison starts at index 258)
AAnomDtctLL[2]           ; read the first compared lower-limit point
```

## 另请参阅

- [AnomDtctUL](AnomDtctUL.md) — 分段的上边界
- [AnomDtctGap](AnomDtctGap.md) — 每个表点所跨越的控制周期
- [AnomDtctCnfg](AnomDtctCnfg.md) — 监测源和运动选择
- [AnomDtctSt](AnomDtctSt.md) — 活动限值和滤波后的值
