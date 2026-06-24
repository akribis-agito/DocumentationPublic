---
keyword: VecMotionStat
summary: 只读枚举值，报告当前向量运动状态（0 未运动，1 运动中，2 已暂停，3 停止中）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 641
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# VecMotionStat

只读枚举值，报告轴当前的向量运动状态。

## 概述

`VecMotionStat` 是只读参数，报告协调向量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的当前状态。上位机程序可通过它跟踪向量运动的进度，并检测运动何时暂停、开始停止或已完成。该参数为轴相关状态变量，不保存至闪存。

`VecMotionStat` 维护在**组主轴**（编号最低的成员轴——参见 [VecMemberAxes](VecMemberAxes.md)）上。主轴运行驱动所有成员的单一路径规划器，因此请在主轴上读取 `VecMotionStat` 以监控整个分组。

## 工作原理

尽管该关键字可保存任意 32 位值，但实际上它报告以下四种枚举状态之一（为单一值，非位掩码）：

| 值 | 状态 | 含义 |
|----|----|----|
| 0 | 未运动 | 该分组上没有向量运动在运行（空闲，或运动已完成、已停止或已中止）。 |
| 1 | 运动中 | 向量运动正沿路径主动运行。 |
| 2 | 已暂停 | 运动被 [VecPause](VecPause.md) = 1 保持；合成速度已斜坡降至零，但运动尚未结束。 |
| 3 | 停止中 | 已请求停止（例如由 [StopVec](StopVec.md)、`Stop` 或受控停止发出）；合成速度正在斜坡降至零，之后该值返回 0。 |

正常运动的典型状态转换：`0` → `1` → （停止时短暂为 `3`，斜坡降速）→ `0`。暂停的运动显示 `1` → `2` → 恢复后 `1`。

## 示例

```text
AVecMotionStat       ; 读取当前向量分组状态（在主轴上读取）
```

如需等待向量运动完成，请轮询主轴上的 `VecMotionStat`，直至其读取为 `0`。

## 参见

- [VecPause](VecPause.md) — 将分组设置为暂停状态（值 2）及恢复
- [StopVec](StopVec.md) — 请求停止状态（值 3），然后返回 0
- [VecMemberAxes](VecMemberAxes.md) — 定义分组及其主轴
- [VecSpeed](VecSpeed.md) — 指令合成速度
