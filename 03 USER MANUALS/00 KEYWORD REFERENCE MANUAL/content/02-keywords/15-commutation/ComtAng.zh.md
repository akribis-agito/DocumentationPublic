---
keyword: ComtAng
summary: 只读的电机瞬时换相（电气）角度，以度为单位乘以 100。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 73
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# ComtAng

只读的电机瞬时换相（电气）角度，以度为单位乘以 100。

## 概述

`ComtAng` 报告控制器用于驱动直流无刷电机相电流的瞬时换相角（电机电角度）。该值以度乘以 100 表示，在下限 0 和上限 35999 之间循环（即 0.00°–359.99°）。

换相使施加的电流矢量与磁场保持偏移，以便电机运动时高效产生力/力矩。`ComtAng` 是控制器当前使用的角度；它由通过 [ComtMode](ComtMode.md) 配置的换相过程建立，并通过 [ComtStatus](ComtStatus.md) 监控。角度来源取决于所配置的方法（例如，通过 [HallsAngle](HallsAngle.md) / [HallsValue](HallsValue.md) 的霍尔传感器，或基于编码器的反馈）。由于该关键字为只读、轴作用域且不保存至闪存，可随时查询，包括电机使能或运动中。

## 工作原理

每个控制周期，控制器从激活的来源计算电角度，然后以百分之一度为单位在此报告：

$$
\text{ComtAng} = \mathrm{round}\!\left(\theta_{elec}\;[\text{rad}] \times \frac{360}{2\pi} \times 100\right)
$$

对于基于编码器的换相，角度来自一个电气周期内的反馈位置（每电气周期计数 = [EncRes](../03-encoder/01-general-settings/EncRes.md) / [PolePrs](../02-motor-and-amplifier/PolePrs.md)，参见 [MotorType](../02-motor-and-amplifier/MotorType.md)）；对于基于霍尔的方法，角度来自 [HallsValue](HallsValue.md) → [HallsAngle](HallsAngle.md) 映射（可选由 [HallOnlyFilt](HallOnlyFilt.md) 平滑）。在老化测试运动期间（[BurnInMode](../../03-special-features/burn-in/BurnInMode.md) 激活，[ComtStatus](ComtStatus.md) `AComtStatus[1]` = `600`），角度来源改为控制器以老化频率驱动的开环角度（而非反馈），因此 `ComtAng` 在测试运行期间连续扫过 0.00°–359.99°（驱动角度在每个控制周期前进前被范围限制在 0°–360° 内）。上述换算完全精确：固件常数等于 360/2π × 100。一旦存在可用的换相角（即 [StatReg](../07-status-and-faults/StatReg.md) 换相完成位（位 0）置位），所报告的值即有意义。对于大多数方法，这是换相完成（[ComtStatus](ComtStatus.md) = `100`）或不需要换相（`200`）时；对于霍尔启动切换方法（`ComtMode[1]=3` 或 `4`），该位在粗略阶段（[ComtStatus](ComtStatus.md) `300`/`400`）即已置位，因此从该点起 `ComtAng` 即在使用中且有意义。`ComtAng` 仅针对无刷电机类型报告；有刷、音圈、仿真和步进类型没有换相角。

## 示例

```text
AComtAng            ; query the instantaneous commutation angle (deg x100)
```

## 另请参阅

- [ComtMode](ComtMode.md) — 确定角度建立方式的换相设置
- [ComtStatus](ComtStatus.md) — 报告换相过程状态
- [HallsAngle](HallsAngle.md) — 各霍尔状态对应的电角度
- [HallsValue](HallsValue.md) — 当前霍尔传感器原始状态
- [StatReg](../07-status-and-faults/StatReg.md) — 位 0 报告换相完成（该角度在置位后有效）
