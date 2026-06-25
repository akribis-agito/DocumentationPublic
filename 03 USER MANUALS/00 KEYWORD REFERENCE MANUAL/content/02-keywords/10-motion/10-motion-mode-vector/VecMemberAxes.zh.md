---
keyword: VecMemberAxes
summary: 位掩码，用于选择参与协调向量运动的轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 631
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VecMemberAxes

位掩码，用于选择参与协调向量运动的轴。

## 概述

`VecMemberAxes` 是一个位掩码，用于定义哪些轴参与协调向量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）。每个位对应一个轴，控制器据此确定哪些轴需要沿合成向量路径一起驱动，哪些轴不参与。该参数为轴相关参数，保存至闪存，运动过程中不可修改。

## 工作原理

### 每轴对应一位的编码方式

掩码从最低编号轴的第 0 位开始，每轴对应一位进行解码：

| 位 | 设置掩码 | 包含的轴 |
|----|----|----|
| 0 | 0x01 | 第一个（编号最低）轴 |
| 1 | 0x02 | 第二个轴 |
| 2 | 0x04 | 第三个轴 |
| ... | ... | ... |
| 7 | 0x80 | 第八个轴 |

将所需轴的掩码相加即可。例如，`3`（`0x01 + 0x02`）选择前两个轴；`7` 选择前三个轴。范围 `0`-`255` 最多可选择八个轴。

### 设置位置及分组规则

当您发出向量运动指令（在 [MotionMode](../02-motion-configuration/MotionMode.md) = 16 上执行 `Begin`）时，控制器从您发出指令的轴读取 `VecMemberAxes`，并根据该值中置位的位构建分组。运动开始时，控制器验证分组，若违反以下任一规则则拒绝运动：

- 掩码必须包含发出指令的轴本身（其对应位必须置位）。
- 至少必须选择两个轴。
- 对于圆弧运动（[VecType](VecType.md) = 1），必须且仅能选择两个轴。
- 指令必须在分组中**编号最低**的轴上发出——该轴成为运行路径规划器的组主轴。在其他成员轴上发出指令将被拒绝。
- 每个成员轴必须处于电机使能状态，设置为 [MotionMode](../02-motion-configuration/MotionMode.md) = 16，且未处于运动中。从 v5 起，每个成员轴还必须已完成换相。

运动开始后，控制器将主轴的 `VecMemberAxes` 值复制到每个成员轴，使整个分组报告相同的成员信息。分组运动期间，每个成员轴的 [MotionStat](../05-motion-status/MotionStat.md) 中第 19 位（`0x00080000`）也会置位（"属于向量运动分组的成员"）。运动结束后，`VecMemberAxes` 在每个成员轴上被清零。

## 示例

```text
AVecMemberAxes=3        ; 在轴 A 上：将前两个轴（第 0 位和第 1 位）加入向量分组
AVecMemberAxes=7        ; 将前三个轴（第 0、1、2 位）加入分组
AVecMemberAxes          ; 读取轴 A 上的当前成员轴掩码
```

## 另请参阅

- [VecType](VecType.md) — 线性与圆弧向量（圆弧要求恰好两个成员轴）
- [VecAbsTrgt](VecAbsTrgt.md) — 各成员轴上的合成路径距离
- [VecMotionStat](VecMotionStat.md) — 向量分组运动状态
- [MotionStat](../05-motion-status/MotionStat.md) — 第 19 位标记轴为向量分组成员
