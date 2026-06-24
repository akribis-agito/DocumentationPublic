---
keyword: InTargetVelTh
summary: 在电流/力控制模式下用于判定到位的速度整定窗口（Vel[1]）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 292
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
  - 0
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InTargetVelTh

在电流/力控制模式下用于判定到位的速度整定窗口（Vel[1]）。

## 概述

在电流或力控制运行模式（[OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) `= 1` 或 `4`）下，`InTargetVelTh` 是速度整定窗口，反馈速度 [Vel](../01-kinematics-status/Vel.md) `[1]` 的绝对值必须在该窗口内持续保持 [InTargetTime](InTargetTime.md) 的时间，之后 [InTargetStat](InTargetStat.md) 才会发出到位信号（`InTargetStat = 4`）。对于位置/速度控制，则改用基于位置的窗口 [InTargetTol](InTargetTol.md)。

## 工作原理

在电流/力模式下，每个控制周期对反馈速度进行测试：

$$
|\text{Vel}[1]| \le \text{InTargetVelTh}
$$

其行为与位置模式检查有一处重要区别：比较**每个周期重新执行，不进行锁存**。若 `|Vel[1]| > InTargetVelTh`，控制器强制 `InTargetStat = 2` 并将驻留计数器清零；若在窗口内，则计数器向 `InTargetTime` 累加，`InTargetStat` 锁定为 4——但若速度随后再次超过阈值，状态立即回落至 2。窗口最大值为最高速度，默认值为 `1000`（用户速度单位）。该参数保存至闪存。

驻留计数器机制与基于位置的整定检查相同；请参阅 [InTargetTol](InTargetTol.md) 页面上的时序图（将 `|Vel[1]|` 代替 `|PosErr|`，将 `InTargetVelTh` 代替 `InTargetTol`）。关键区别在于：在电流/力模式下，所得到的状态 4 锁存是*不粘滞的*——一旦速度离开窗口即立即回落至 2。

## 示例

```text
AInTargetVelTh=1000  ; 速度窗口（用户单位/s，默认值）
AInTargetVelTh      ; 读取当前值
```

### 边界情况

- **电机关闭：**值保持不变；`InTargetStat = 0`，不进行检查。
- **超范围写入：**参数系统钳位至 `0`–`1.3 × 10⁹`；负值被拒绝。
- **仿真模式（`MotorType` = 5）：**`Vel[1]` 反映仿真参考值；检查正常运行。
- **ModRev 环绕：**环绕保留 `ΔPos`，因此 `|Vel[1]|` 在环绕时不会出现毛刺。
- **活动故障：**轴被禁用，`InTargetStat = 0`。
- **其他运动模式：**基于速度的整定仅在 `OperationMode` 为电流（1）或力（4）时适用；在位置/速度模式下改用 [InTargetTol](InTargetTol.md)。
- **`InTargetVelTh = 0`：**要求速度恰好为零——在存在任何扰动的物理轴上无法达到。
- **不粘滞：**在电流/力模式下，值 4 在速度再次超过阈值时立即回落至 2——与位置/速度模式（锁存）不同。

## 另请参阅

- [InTargetStat](InTargetStat.md) — 由该窗口门控的整定状态
- [InTargetTime](InTargetTime.md) — 窗口内的最短驻留时间
- [InTargetTol](InTargetTol.md) — 位置整定窗口（位置/速度控制）
- [Vel](../01-kinematics-status/Vel.md) — `Vel[1]` 是与该窗口比较的信号
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — 选择基于电流/力的整定
