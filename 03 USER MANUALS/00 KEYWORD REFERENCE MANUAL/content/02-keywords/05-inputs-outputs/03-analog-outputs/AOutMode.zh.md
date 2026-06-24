---
keyword: AOutMode
summary: 为每个模拟量输出选择直接指令模式或参数监视模式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 220
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AOutMode

为每个模拟量输出选择直接指令模式或参数监视模式。

## 概述

`AOutMode` 设定某个模拟量输出处于**直接指令模式**还是**监视模式**。数组索引即模拟量输出编号（从 1 开始：`AOutMode[1]` 为模拟量输出 1，`AOutMode[2]` 为模拟量输出 2）。该值不是固定枚举——除 `0` 之外，任何值都被解释为标识待仿真参数的 **Complex CAN code (CCC)**。

| Value | Mode |
|-------|------|
| 0 | 直接指令模式——输出跟随 [AOutPort](AOutPort.md) |
| CCC | 监视模式——输出仿真由所给 Complex CAN code (CCC) 标识的参数 |

在监视模式下，被仿真参数被视为毫伏，由 [AOutShifts](AOutShifts.md) 缩放并由 [AOutOffset](AOutOffset.md) 偏置。参见[模拟量输出概述](00-overview.md)。

## 工作原理

写入 `AOutMode[Index]` 会执行两件事：

1. **设置每个输出的直接/监视标志。** 当值为 `0` 时，或当相关驱动器为模拟电流指令/内置直线型时（在这种情况下，DAC 无论如何都在驱动驱动器电流指令），输出被强制进入直接模式。否则，输出被置于监视模式。

2. **将 CCC 解析为参数。** Complex CAN code 打包了三项内容——CAN 关键字代码、轴选择器和数组索引——它们被解包并校验（关键字代码、轴、数组索引，以及目标是否为参数）。然后输出跟踪该参数。若 CCC 无效，输出停留在 0 mV。

对于处于监视模式的输出，每个控制周期内，被监视参数被读取、由 [AOutShifts](AOutShifts.md) 移位、由 [AOutOffset](AOutOffset.md) 偏置、转换为 DAC 码并钳位：

$$
\text{DAC code} = \big((\text{parameter} \ll \text{AOutShifts}) + \text{AOutOffset}\big) \cdot \text{(mV-to-DAC factor)}
$$

（负的 `AOutShifts` 改为右移。）由于被仿真参数被视为毫伏，应选择 `AOutShifts`，使参数的内部范围有效地映射到 ±11905 mV。

每个模拟量输出索引映射到一个固定的 DAC 通道：索引 1 → DAC A，索引 2 → DAC B，索引 3 → C，索引 4 → D。

## 示例

```text
AAOutMode[1]=0       ; direct command mode (output follows AOutPort[1])
AAOutMode[1]=<CCC>   ; monitor a parameter (use its Complex CAN code)
AAOutMode[1]          ; read back the configured mode
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AOutMode[1]`–`AOutMode[4]`。`AOutMode[0]` 不存在。
- **无效 CCC** — 若 Complex CAN code 校验失败（未知关键字、错误的轴、数组索引超出范围，或目标是函数而非参数），则输出被强制为 `0 mV`，而不是跟踪陈旧或未定义的值。
- **强制直接模式** — 若驱动器为模拟电流指令或内置直线型，则无论 `AOutMode` 如何，DAC 都驱动驱动器电流指令；在该情况下设置 CCC 无效。
- **缩放错误** — 在监视模式下，被监视参数被视为毫伏；若没有合适的 [AOutShifts](AOutShifts.md)（v5 上为 [AOutGain](AOutGain.md)），输出会饱和。
- **模式独立性** — `AOutMode` 本身立即生效，且独立于 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 和 `MotorOn`。被监视参数可能是仅在特定模式下才有意义的参数（例如，在电流模式下监视 `VelRef` 显示的是速度环所保持的任意值，而非有效控制量）。
- **保存** — 可保存至闪存；启动时重新加载。
- **平台** — 在 standalone v4、central-i v4 和 central-i v5 上代码路径相同；v5 的差异在于缩放器（[AOutGain](AOutGain.md) 替代 [AOutShifts](AOutShifts.md)）。

## 另请参阅

- [AOutPort](AOutPort.md) — 指令值（仅当此值为 `0` 时使用）
- [AOutShifts](AOutShifts.md) — 应用于被监视参数的 2 的幂缩放
- [AOutOffset](AOutOffset.md) — 输出偏置，在 DAC 转换之前加上
- [analog-output overview](00-overview.md) — 完整信号路径
