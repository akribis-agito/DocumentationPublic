---
keyword: PosPosTh
summary: 与 PosPosFlag 配合用于进入位置模式的位置反馈阈值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 329
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
# PosPosTh

与 PosPosFlag 配合用于进入位置模式的位置反馈阈值。

## 概述

`PosPosTh` 是位置反馈阈值（单位为用户单位），由切换轴进入位置运行模式的条件检查与 [Pos](../../10-motion/01-kinematics-status/Pos.md) 进行比较。它与 [PosPosFlag](PosPosFlag.md) 一起使用，后者置位该检查并选择比较方向，且仅在轴处于电流或力运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1 或 4）时起作用。`PosPosTh` 本身是一个持久化设置（切换触发时不会被清除；仅 [PosPosFlag](PosPosFlag.md) 会被清除）。

## 工作原理

每个控制周期，在已换相且处于电流/力模式时，控制器按 [PosPosFlag](PosPosFlag.md) 所选方向将 [Pos](../../10-motion/01-kinematics-status/Pos.md) 与 `PosPosTh` 进行比较：

| PosPosFlag | 条件 | 结果 |
|------------|-----------|--------|
| 0          | （无） | 轴保持在现有的电流或力模式。 |
| 1          | [Pos](../../10-motion/01-kinematics-status/Pos.md) &lt; `PosPosTh` | 切换至位置模式。 |
| 2          | [Pos](../../10-motion/01-kinematics-status/Pos.md) &gt; `PosPosTh` | 切换至位置模式。 |

当条件满足时，控制器切换至位置模式，清除 [PosPosFlag](PosPosFlag.md)，记录 [ModeSwitchPos](ModeSwitchPos.md)[2]，并运行可选的 [BeginOnToPos](BeginOnToPos.md) 进入运动。完整的切换序列参见 [PosPosFlag](PosPosFlag.md)。

## 版本间的变化

在 **v5（central-i）** 中位置流水线为 64 位，因此 `PosPosTh` 是一个 64 位值，具有前言中所示的更大范围；比较逻辑不变。**v5 仅适用于 central-i**，因此在 standalone 上 `PosPosTh` 仍为 v4 的 32 位值。

## 示例

```text
APosPosTh=100000     ; position threshold (user units)
APosPosFlag=1        ; switch when Pos < PosPosTh
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {1, 4}）— 不进行评估。
- **[PosPosFlag](PosPosFlag.md) = 0** — 未置位；`PosPosTh` 被存储但从不比较。
- **比较反馈，而非参考** — 使用 `Pos`；即使因环路尚未接入而位置参考尚未推进，也能正确工作。
- **触发后的持久性** — `PosPosTh` 在切换时**不会**被清除；仅 [PosPosFlag](PosPosFlag.md) 会被清除。通过再次写入 `PosPosFlag` 重新置位。
- **超出范围** — 平台范围之外的值将被拒绝。
- **保存** — 可保存至闪存。
- **平台** — v5 扩展为 64 位；v4 为 32 位。

## 另请参阅

- [PosPosFlag](PosPosFlag.md) — 置位该检查并选择比较方向
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 与此阈值比较的反馈值
- [电流运行模式](../03-current-operation-mode/00-overview.md) — 从电流模式切换
- [力运行模式](../04-force-operation-mode/00-overview.md) — 从力模式切换
