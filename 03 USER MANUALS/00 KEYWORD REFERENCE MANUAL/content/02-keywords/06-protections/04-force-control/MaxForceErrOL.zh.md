---
keyword: MaxForceErrOL
summary: 开环力控制中允许的最大力误差；超出即触发故障。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 591
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 327680
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MaxForceErrOL

开环力控制中允许的最大力误差；超出即触发故障。

## 概述

`MaxForceErrOL` 是**开环**力控制模式下允许的最大力误差（OL = open loop，开环）。它是 [MaxForceErr](MaxForceErr.md) 的开环对应项，默认值刻意取得更大（50000 对比 2000），因为环路开环时力误差自然更大。该参数为轴相关参数，保存至闪存，可在任何时刻更改，包括运动中（范围 0…327680）。

## 工作原理

力环对 `|ForceErr|` 施加单一的当前生效力误差限值；驱动器在开环力运行时将该限值切换为 `MaxForceErrOL`，在正常闭环控制时切换为 [MaxForceErr](MaxForceErr.md)。在以下情况下选用开环限值：

- [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) 非零，**或**
- 在**电流参考注入点**处启用了**直接**信号注入模式（[InjectType](../../13-injection/InjectType.md) = 某种直接注入类型且 [InjectPoint](../../13-injection/InjectPoint.md) = 电流参考）。

重要的错误状态提示：在**力参考注入点**处注入**不会**将力切换为 `MaxForceErrOL`——在该情形下力环仍为闭环，因此力仍使用 `MaxForceErr`，触发时会引发 ConFlt 码 1045。在力参考注入期间，只有位置误差限值和速度误差限值切换为各自的开环对应项。同样地，在速度或位置参考点处注入也会使力保持使用 `MaxForceErr`。完整映射参见 [MaxForceErr](MaxForceErr.md)。

当在该状态下超出限值时，环路禁用轴，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示 ConFlt 码 1057（开环力误差过高），以区别于闭环的 ConFlt 码 1045。写入该关键字会重新评估当前生效的限值，因此更改立即生效。

### 边界情形

- **电机失能：** 力环不运行；不检查开环限值。
- **闭环运行：** 当 [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) = 0 且无直接电流参考注入时，该限值不生效——触发改用 [MaxForceErr](MaxForceErr.md)（ConFlt 码 1045）。
- **范围溢出：** 超出 `0…327680` 的写入将被拒绝并返回超范围错误，限值保持其先前值；被接受的写入会立即重新执行限值选择，因此若开环力运行正在进行，新值会立刻生效。
- **清除故障：** ConFlt 码 1057 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目保留。
- **HWProtectBits / ProtectMask：** 开环力误差触发不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅涵盖硬件保护位）。

## 示例

```text
AMaxForceErrOL[1]=50000   ; trip axis A if open-loop force error exceeds 50000
AMaxForceErrOL            ; read the current limit
```

## 参见

- [MaxForceErr](MaxForceErr.md) —— 闭环力误差限值
- [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) —— 选择开环运行
- [InjectType](../../13-injection/InjectType.md) / [InjectPoint](../../13-injection/InjectPoint.md) —— 同样会选择该限值的信号注入
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 故障码 1057（开环力误差超出限值）
