---
keyword: SpeedChgNew
summary: 动态速度更改期间，当轴到达 SpeedChgPos 时所应用的新速度。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 344
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
  - -1300000000
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# SpeedChgNew

动态速度更改期间，当轴到达 `SpeedChgPos` 时所应用的新速度。

## 概述

`SpeedChgNew` 设定动态速度更改事件期间，当轴到达由 [SpeedChgPos](SpeedChgPos.md) 定义的位置时所应用的新速度，单位为每秒用户单位。该功能必须通过 [SpeedChgOn](SpeedChgOn.md) 启用，而 [SpeedChgDir](SpeedChgDir.md) 选择触发器生效的方向。它是保存至闪存的轴相关参数，并可在任意时刻更改，包括运动期间。

## 工作原理

当触发器触发时，控制器将 `SpeedChgNew` 直接复制到当前的 [Speed](Speed.md) 设置，随后规划器在正常的 [Accel](Accel.md)/[Decel](Decel.md)（以及 jerk）限值下将速度斜坡逼近该值，因此速度平滑变化而非阶跃。`SpeedChgNew` 可以大于或小于原始的 [Speed](Speed.md)；其符号即为新的方向/幅值，单位为每秒用户单位。由于该值仅在越界时刻读取，你可以在此之前的任意时刻更新它。完整的触发机制参见 [SpeedChgOn](SpeedChgOn.md)。

## 示例

```text
ASpeedChgNew=200000  ; speed to switch to (user units/s)
ASpeedChgNew        ; query current value
```

### 边界情况

- **电机失能：** 数值被保持；在下一次准备时使用。
- **超范围写入：** 超出 ±1.3 × 10⁹ 的写入会被拒绝（不会被钳位）；存储值保持不变。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** `SpeedChgNew` 是速率，而非位置；不受影响。
- **存在故障：** 轴被禁用；数值被保留。
- **其他运动模式：** 触发器将新值写入 [Speed](Speed.md)。只有消费 `Speed` 的模式（点动、PTP、重复 PTP、间接模式）会响应；直接模式忽略 `Speed`，因而忽略 `SpeedChgNew`。
- **`SpeedChgNew > MaxVel`：** 不会触发 `Begin` 时检查（触发器发生在运动途中）；速度环将把 [VelRef](../01-kinematics-status/VelRef.md) 钳位至 `MaxVel` 并置位饱和标志。
- **`SpeedChgNew = 0`：** 在点动模式中，轴按 `Decel` 减速至停止；在 PTP 中，运动停滞。

## 另请参阅

- [SpeedChgOn](SpeedChgOn.md) — 启用动态速度更改
- [SpeedChgPos](SpeedChgPos.md) — 触发更改的位置
- [SpeedChgDir](SpeedChgDir.md) — 触发器生效的方向
