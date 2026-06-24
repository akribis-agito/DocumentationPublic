---
keyword: CurrCurrThDir
summary: CurrCurrTh 电流参考检查的触发方向。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 343
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCurrThDir

CurrCurrTh 电流参考检查的触发方向。

## 概述

`CurrCurrThDir` 定义用于进入电流运行模式的第二个条件检查（电流参考，`CurrRef`）的触发方向，与阈值 [CurrCurrTh](CurrCurrTh.md) 配合使用。仅当轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。

## 工作原理

| CurrCurrThDir | 说明                                                    |
|---------------|---------------------------------------------------------|
| 0             | 若 `CurrRef` > `CurrCurrTh`，则满足第二个条件。 |
| 1             | 若 `CurrRef` < `CurrCurrTh`，则满足第二个条件。 |

只有当 [CurrCurrTh](CurrCurrTh.md) 非零时方向才有效（`CurrCurrTh` 为 0 会完全解除该检查的武装）。与 [CurrPosThDir](CurrPosThDir.md) 不同，当切换触发时固件**不会**清除该关键字 —— 只有 `CurrCurrTh` 和 `CurrPosThDir` 被清零 —— 因此所选方向在下次重新武装阈值时保持不变。

## 示例

```text
ACurrCurrThDir=1     ; trigger when CurrRef falls below CurrCurrTh
ACurrCurrTh=-2000    ; threshold (mA)
```

### 边界情况

- **模式错误** —— 在 [OperationMode](../01-general-keywords/OperationMode.md) 2 / 3 之外不评估。
- **超出范围** —— 超出 `0`–`1` 的值会被拒绝。
- **保存** —— 可保存至闪存。

## 另请参阅

- [CurrCurrTh](CurrCurrTh.md) — 电流参考阈值
- [Current operation mode](00-overview.md) — 完整的模式切换条件
