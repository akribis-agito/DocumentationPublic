---
keyword: RefOffsetStep
summary: 在参考偏置修正期间每采样施加的位置偏置量。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 166
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -655360
  - 655360
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RefOffsetStep

在参考偏置修正期间每采样施加的位置偏置量。

## 概述

`RefOffsetStep` 设置在参考偏置修正期间每个伺服采样施加的每次增量位置偏置的量值。它与 [RefOffsetSamp](RefOffsetSamp.md)（设置采样数）一起,控制将位置修正引入参考轨迹的速率。它是轴相关参数,不保存至闪存,可在任意时刻更改,包括运动期间。

## 工作原理

当一个修正已置位（[RefOffsetSamp](RefOffsetSamp.md) `> 0`）且轴处于运动中时,控制器在**每个**伺服周期将 `RefOffsetStep` 累加至高精度参考累加器。因此注入的总偏移约为 `RefOffsetStep × RefOffsetSamp`。

该值以参考的**累加器标度**（50.14 / `2^14` 定点参考）累加。这意味着 `RefOffsetStep` 实际上表现得像*速度*：等于 `2^14`（16384）的值对应于每周期偏移一个位置计数,即在斜坡持续期间的恒定速度偏置。请使用较小的值；由于偏置绕过 [Accel](Accel.md)/[Decel](Decel.md) 规划器限制,较大的步长会在参考中产生剧烈的速度跳变。

正的 `RefOffsetStep` 使参考向前偏移,负值则向后。关于置位和自动清除行为,参见 [RefOffsetSamp](RefOffsetSamp.md)。

### 边界情况

- **电机失能 / 非运动中：** 该值被保持；不发生注入（倒计数也被保持）。
- **越界写入：** 超出 frontmatter 中所示 ±（采样率 × 10）范围的值,会以越界错误被拒绝,所存值保持不变（不会被钳位）。v4 和 v5 适用相同范围。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 与 [RefOffsetSamp](RefOffsetSamp.md) 相同；偏置随环绕一并通过。
- **激活故障：** 该值被保留,但倒计数被清除。
- **大值（速度偏置语义）：** 由于 `RefOffsetStep` 累加至 50.14 标度的累加器,值 `16384` 表示每周期一个计数的位置偏置（在标准采样率下相当于约 16384 counts/sec）。设置大于此的值需谨慎——它们在参考中转换为大的速度阶跃,可能使速度环饱和。
- **`RefOffsetStep = 0` 而 `RefOffsetSamp` 非零：** 倒计数仍会运行但不注入任何内容——空操作。
- **其他运动模式：** 在任何置位运动中位的模式下运行。

## 示例

```text
ARefOffsetStep=16384 ; add ~1 position count per servo cycle while armed
ARefOffsetStep=-4096 ; small backward bias per cycle
ARefOffsetStep      ; query current value
```

## 版本间变更

±（采样率 × 10）范围钳位（frontmatter range 中所示）在 v4 和 v5 中均适用；注入机制不变。**v5 仅限 central-i。**

## 参见

- [RefOffsetSamp](RefOffsetSamp.md) — 施加偏置所经历的采样数
- [PosRef](../01-kinematics-status/PosRef.md) — 步长累加的目标参考累加器
