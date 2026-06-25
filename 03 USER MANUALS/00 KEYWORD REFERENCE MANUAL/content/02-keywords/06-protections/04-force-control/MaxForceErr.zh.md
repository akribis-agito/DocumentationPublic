---
keyword: MaxForceErr
summary: 闭环力控制中允许的最大力误差；超出即触发故障。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 585
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
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MaxForceErr

闭环力控制中允许的最大力误差；超出即触发故障。

## 概述

`MaxForceErr` 是**闭环**力控制模式下允许的最大力误差。如果力误差（指令力 − 测量力）的幅值超过该阈值，控制器将禁用轴并触发故障。该参数为轴相关参数，保存至闪存，可在任何时刻更改，包括运动中（范围 0…327680，默认 2000）。开环对应项参见 [MaxForceErrOL](MaxForceErrOL.md)。

## 工作原理

在力控制环中，驱动器由滤波后的力参考与测量力构成力误差，然后将其绝对值与当前生效的力误差限值进行比较：

```text
ForceErr = (filtered force reference) − (measured force)
if (|ForceErr| > active force-error limit)
    → disable axis, append to ErrLog
```

所触发的故障码取决于当前环路是闭环还是开环：

| 情形 | 所用限值 | 显示的 ConFlt 码 |
|-----------|------------|-------------------|
| 闭环力控制 | `MaxForceErr` | ConFlt 码 1045（力误差过高） |
| [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0，或在电流参考点处进行直接信号注入 | [MaxForceErrOL](MaxForceErrOL.md) | ConFlt 码 1057（开环力误差过高） |
| 在速度、位置或**力**参考点处进行直接信号注入 | `MaxForceErr`（力保持闭环） | ConFlt 码 1045 |

重要提示：在**力参考点**处注入会使力误差限值仍保持为 `MaxForceErr`，而非 `MaxForceErrOL`——在该情形下只有位置误差限值和速度误差限值切换为各自的开环对应项。力限值的开环切换仅在 [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) 非零，或在电流参考点处启用了直接信号注入模式（[InjectType](../../13-injection/InjectType.md) = 某种直接类型且 [InjectPoint](../../13-injection/InjectPoint.md) = 电流参考）时才发生。另外，如果未定义模拟力反馈，环路会触发 [ConFlt](../../07-status-and-faults/ConFlt.md) 码 1046（无力反馈）故障。

### 边界情形

- **电机失能：** 力环不运行，因此不检查该限值；误差被复位，并在下次电机使能时重新初始化。
- **未定义模拟力反馈：** 一旦力控制运行，无论误差多小，环路都会立即触发 [ConFlt](../../07-status-and-faults/ConFlt.md) 码 1046 故障。
- **模式依赖：** 该检查属于闭环力控制环。在不运行该环的模式下（例如仅电流控制而无经 PIV 的力控制），误差被强制为零，限值无法触发。
- **清除故障：** ConFlt 码 1045 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目保留。
- **HWProtectBits / ProtectMask：** 力误差触发不可通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅涵盖硬件保护位）。

## 示例

```text
AMaxForceErr[1]=2000   ; trip axis A if closed-loop force error exceeds 2000
AMaxForceErr           ; read the current limit
```

## 另请参阅

- [MaxForceErrOL](MaxForceErrOL.md) —— 开环力误差限值
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) —— 被限制的实时力误差
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 故障码 1045（力误差超出限值）
