---
keyword: SpeedChgPos
summary: 触发飞行速度变更事件的轴位置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 346
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
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# SpeedChgPos

触发飞行速度变更事件的轴位置。

## 概述

`SpeedChgPos` 设置触发飞行速度变更事件的轴位置（以用户单位表示），该事件在 [SpeedChgOn](SpeedChgOn.md) 激活时生效。当轴沿 [SpeedChgDir](SpeedChgDir.md) 选定的方向越过此位置时，指令速度将更新为 [SpeedChgNew](SpeedChgNew.md)。它是一个轴相关参数，保存至闪存，可随时更改，包括在运动过程中。

## 工作原理

越界判定将 `SpeedChgPos` 与**整形后的位置参考**进行比较，而非测量反馈。这与驱动位置环的值相同，因此当规划轨迹经过 `SpeedChgPos` 时，速度变更会确定性地触发，略早于负载实际到达之处。当 [SpeedChgDir](SpeedChgDir.md) `= 0` 时，参考值上升超过 `SpeedChgPos` 时触发事件；当 `= 1` 时，参考值下降低于该值时触发。该值与 [PosRef](../01-kinematics-status/PosRef.md) 采用相同的用户单位。完整机制及时间线图示请参见 [SpeedChgOn](SpeedChgOn.md)。

## 示例

```text
ASpeedChgPos=50000   ; trigger position (user units)
ASpeedChgPos        ; query current value
```

### 边界情况

- **电机失能：** 保留该值；不触发。
- **超范围写入：** 参数系统拒绝超出 ±2³¹−1 的值。
- **仿真模式（`MotorType` = 5）：** 正常触发；仿真参考会像真实参考一样推进越过 `SpeedChgPos`。
- **ModRev 环绕：** 由于环绕同时移动参考值，且 `SpeedChgPos` 需要处于取模坐标系内，因此应将 `SpeedChgPos` 设置在 `[0, ModRev)` 范围内。例如设在 `2 × ModRev` 处的触发将无法到达。
- **存在故障：** 保留该值；运动停止时不触发。
- **置位时已越过触发点：** 在下一个周期触发（比较为电平判定，而非边沿判定）。
- **其他运动模式：** 在任何更新 [PosRef](../01-kinematics-status/PosRef.md) 的模式下都会触发；但随之对 [Speed](Speed.md) 的写入仅在使用 `Speed` 的模式下才有意义。

## 另请参阅

- [SpeedChgOn](SpeedChgOn.md) — 启用飞行速度变更
- [SpeedChgNew](SpeedChgNew.md) — 在触发点应用的新速度
- [SpeedChgDir](SpeedChgDir.md) — 触发生效的方向
- [PosRef](../01-kinematics-status/PosRef.md) — 与 `SpeedChgPos` 进行比较的参考值
