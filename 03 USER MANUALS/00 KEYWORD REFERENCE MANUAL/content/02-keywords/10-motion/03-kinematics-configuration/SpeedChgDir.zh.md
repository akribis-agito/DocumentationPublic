---
keyword: SpeedChgDir
summary: 选择动态速度更改触发器生效的运动方向。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 347
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
# SpeedChgDir

选择动态速度更改触发器生效的运动方向。

## 概述

`SpeedChgDir` 指定动态速度更改事件生效的运动方向。只有当轴沿所选方向运动时，越过 [SpeedChgPos](SpeedChgPos.md) 才会触发切换到 [SpeedChgNew](SpeedChgNew.md)。整个功能必须通过 [SpeedChgOn](SpeedChgOn.md) 启用。它是保存至闪存的轴相关参数，并可在任意时刻更改，包括运动期间。

## 工作原理

`SpeedChgDir` 选择对照 [SpeedChgPos](SpeedChgPos.md) 的比较中哪一侧准备触发器：

| SpeedChgDir | 触发更改的条件 |
|---|---|
| 0 | 参考**升高至**超过 `SpeedChgPos`（等待更高位置）。用于正向运动的轴。 |
| 1 | 参考**降低至**低于 `SpeedChgPos`（等待更低位置）。用于反向运动的轴。 |

将 `SpeedChgDir` 设置为与轴经过 `SpeedChgPos` 时的运动方向一致；如果设置到错误的一侧，越界条件将永远不满足，也不会发生更改。完整机制和时序图参见 [SpeedChgOn](SpeedChgOn.md)。

例如，当正向点动且你希望在越过 `SpeedChgPos = 80000` 后减速时，设置 `SpeedChgDir = 0`（在正向越界时触发）。对于应在越过 `SpeedChgPos = 20000` 后加速的反向点动，设置 `SpeedChgDir = 1`。

## 示例

```text
ASpeedChgDir=0       ; fire when reference rises above SpeedChgPos (forward)
ASpeedChgDir=1       ; fire when reference falls below SpeedChgPos (reverse)
ASpeedChgDir        ; query current value
```

### 边界情况

- **电机失能：** 数值被保持。
- **超范围写入：** 参数系统拒绝 `0`–`1` 之外的值。
- **仿真模式（`MotorType` = 5）：** 触发器正常触发。
- **ModRev 环绕：** 比较侧在环绕时不变。请注意，正向运动的轴在 `SpeedChgPos = 0` 附近环绕时，会从 `ModRev` 向下越过至 `0` *再向上*；此时触发器将在配置方向上的第一次此类越界时触发。
- **存在故障：** 数值被保留。
- **方向错误：** 如果 `SpeedChgDir` 选择了与实际运动相反的一侧，触发器将永远不会触发。该关键字本身不检测运动方向——它是一个比较侧，而非“等待方向”。

## 另请参阅

- [SpeedChgOn](SpeedChgOn.md) — 启用动态速度更改
- [SpeedChgPos](SpeedChgPos.md) — 触发更改的位置
- [SpeedChgNew](SpeedChgNew.md) — 触发时应用的新速度
