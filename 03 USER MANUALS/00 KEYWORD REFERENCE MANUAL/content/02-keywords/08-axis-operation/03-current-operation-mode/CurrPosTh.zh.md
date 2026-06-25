---
keyword: CurrPosTh
summary: 进入电流模式的位置参考阈值（条件 A）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 426
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrPosTh

进入电流模式的位置参考阈值（条件 A）。

## 概述

`CurrPosTh` 是用于进入电流运行模式第一个条件检查（条件 A）的阈值位置参考（`PosRef`）值。它仅在轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。比较方向由 [CurrPosThDir](CurrPosThDir.md) 设置，且比较是针对*指令*位置参考 `PosRef` 进行的，而非实际反馈位置。

## 工作原理

条件 A 是一个**门**：固件每个周期首先评估它，只有当它通过时才会继续评估条件 B 阈值。方向关键字 [CurrPosThDir](CurrPosThDir.md) 决定比较方式（而 `0` 使条件 A 始终通过，即禁用位置门）：

| CurrPosThDir | 说明                                                 |
|--------------|------------------------------------------------------|
| \< 0         | 若 `PosRef` < `CurrPosTh`，则满足第一个条件。          |
| 0            | 第一个条件满足（无条件）。                             |
| \> 0         | 若 `PosRef` > `CurrPosTh`，则满足第一个条件。          |

进入电流运行模式仍要求第二个条件检查（[CurrPosErrTh](CurrPosErrTh.md)、[CurrAInTh](CurrAInTh.md) 或 [CurrCurrTh](CurrCurrTh.md) 之一）在同一周期内满足。当两个条件都满足时，轴进入电流模式，固件将 [CurrPosThDir](CurrPosThDir.md) 清零为 0（使位置门无条件通过）并清除触发该切换的条件 B 阈值。`CurrPosTh` 本身保留其值；要为后续切换完全重新置位同一位置门，需再次设置 `CurrPosThDir` 和一个条件 B 阈值。概述请参见[电流运行模式](00-overview.md)。

## 示例

```text
ACurrPosThDir=1      ; first condition triggers when PosRef > CurrPosTh
ACurrPosTh=100000    ; position-reference threshold (user units)
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {2, 3}）—— 该条件**不被评估**；阈值在电流或力模式下无效。
- **电机失能** —— 阈值引擎不运行；可接受值，但在电机于速度或位置模式下重新使能之前不会触发切换。
- **`CurrPosThDir = 0`** —— 条件 A 无条件通过；位置阈值本身被忽略（仅条件 B 驱动切换）。
- **触发后** —— 进入电流模式时，固件将 [CurrPosThDir](CurrPosThDir.md) 清零为 `0`（而非 `CurrPosTh` 本身），并清除触发的条件 B 阈值。通过再次写入 `CurrPosThDir` 和一个 B 阈值来重新置位。
- **比较指令而非反馈** —— 使用 `PosRef`（指令值），因此触发与位置误差或跟踪滞后无关，保持一致。
- **`PosRef` 在重新使能时复位** —— 电机使能时位置参考跟踪 `Pos`，因此基于先前 `PosRef` 的过时阈值可能在重新使能时立即突然变为真。
- **保存** —— 可保存至闪存；重启后保持。
- **平台** —— v5 central-i 扩展为 64 位；v4 为 32 位。单位和行为不变。

## 另请参阅

- [CurrPosThDir](CurrPosThDir.md) —— 选择比较方向
- [电流运行模式](00-overview.md) —— 完整的模式切换条件
