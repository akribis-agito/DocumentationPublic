---
keyword: PosPosFlag
summary: 进入位置模式所用位置反馈检查的触发方向。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 328
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PosPosFlag

进入位置模式所用位置反馈检查的触发方向。

## 概述

`PosPosFlag` 置位并选择位置反馈条件检查的方向，该检查可自动将轴切换至位置运行模式。它仅在轴处于电流或力运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1 或 4）且换相完成之后，与阈值 [PosPosTh](PosPosTh.md) 一起起作用。当条件满足时，控制器切换至位置模式并将 `PosPosFlag` 清零为 0，因此下一次切换前必须重新置位。

## 工作原理

每个控制周期，在轴已换相且处于电流或力模式时，控制器进行评估：

| PosPosFlag | 检查的条件 | 结果 |
|---|---|---|
| 0 | （无） | 轴保持在现有的电流或力模式。 |
| 1 | [Pos](../../10-motion/01-kinematics-status/Pos.md) &lt; [PosPosTh](PosPosTh.md) | 切换至位置模式。 |
| 2 | [Pos](../../10-motion/01-kinematics-status/Pos.md) &gt; [PosPosTh](PosPosTh.md) | 切换至位置模式。 |

当条件触发时，控制器在同一周期内：

1. 设置 `OperationMode = 3`（位置）；
2. 清除 `PosPosFlag = 0`（一次性——下一次切换需重新置位）；
3. 锁存 [ModeSwitchPos](ModeSwitchPos.md)[2] = `Pos`；
4. 若设置了 [BeginOnToPos](BeginOnToPos.md)，则清除它并启动进入运动（[RetractTarget](RetractTarget.md)/[RetractSpeed](RetractSpeed.md)）。

切换时无需特殊准备，因为在电流和力模式下，位置参考会持续保持与反馈对齐，所以切换是无冲击的（参见 [GoToPosMode](GoToPosMode.md)）。此反馈阈值检查是进入位置模式的**唯一**基于条件的方式；当计划的电流/力命令表到达其末尾时也会自动进入位置模式（参见[电流运行模式](../03-current-operation-mode/00-overview.md) / [力运行模式](../04-force-operation-mode/00-overview.md)）。

## 示例

```text
APosPosTh=100000     ; position threshold (user units)
APosPosFlag=2        ; switch to position mode when Pos > PosPosTh
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {1, 4}）— 不进行评估。该检查要求轴处于电流或力模式。
- **换相前** — 在换相完成之前跳过该检查（`StatReg` 位 0 = 1）。
- **零值** — 取消该检查的置位（轴保持在电流/力模式）。
- **超出范围** — `0`–`2` 之外的值将被拒绝。
- **一次性** — 在切换触发的那个周期自动清零为 `0`；下一次进入需重新置位。
- **保存** — 可保存至闪存；重启后保持。

## 另请参阅

- [PosPosTh](PosPosTh.md) — 与 Pos 比较的位置阈值
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 与阈值比较的反馈值
- [BeginOnToPos](BeginOnToPos.md) — 切换发生时可选的进入运动
- [电流运行模式](../03-current-operation-mode/00-overview.md) — 从电流模式切换
- [力运行模式](../04-force-operation-mode/00-overview.md) — 从力模式切换
