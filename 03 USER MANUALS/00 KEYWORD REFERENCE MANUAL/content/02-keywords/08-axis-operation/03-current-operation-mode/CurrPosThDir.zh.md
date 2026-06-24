---
keyword: CurrPosThDir
summary: CurrPosTh 位置参考检查的触发方向。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 427
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrPosThDir

CurrPosTh 位置参考检查的触发方向。

## 概述

`CurrPosThDir` 与阈值 [CurrPosTh](CurrPosTh.md) 一起，定义用于进入电流运行模式的第一个条件检查（位置参考）的触发方向。它仅在轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。

## 工作原理

| CurrPosThDir | 说明                                                 |
|--------------|------------------------------------------------------|
| \< 0         | 若 `PosRef` < `CurrPosTh`，则满足第一个条件。          |
| 0            | 第一个条件满足（无条件）。                             |
| \> 0         | 若 `PosRef` > `CurrPosTh`，则满足第一个条件。          |

此关键字同时兼作自动进入的主使能：因为值 0 使条件 A 始终通过，固件将“`CurrPosThDir` = 0”同时用作绕过位置门的设置和未置位状态。当任何条件 B 阈值触发切换进入电流模式时，固件将 `CurrPosThDir` 清回 0，以防止在下一周期立即重新触发；重新设置它（连同一个条件 B 阈值）以置位下一次自动切换。

## 示例

```text
ACurrPosThDir=-1     ; trigger when PosRef < CurrPosTh
ACurrPosTh=50000     ; position-reference threshold
```

### 边界情况

- **零值** —— 条件 A 始终通过；位置阈值实际上被绕过，仅条件 B 关键字驱动切换。
- **任何触发后** —— 进入电流模式时自动清零为 `0`（连同触发的那个条件 B 阈值）。通过再次写入两者来重新置位。
- **模式错误** —— 在 [OperationMode](../01-general-keywords/OperationMode.md) 2 / 3 之外不被评估。
- **超出范围** —— 超出 `-1`–`1` 的值被拒绝。
- **保存** —— 不可保存至闪存；启动时复位为 `0`。

## 另请参见

- [CurrPosTh](CurrPosTh.md) —— 位置参考阈值
- [电流运行模式](00-overview.md) —— 完整的模式切换条件
