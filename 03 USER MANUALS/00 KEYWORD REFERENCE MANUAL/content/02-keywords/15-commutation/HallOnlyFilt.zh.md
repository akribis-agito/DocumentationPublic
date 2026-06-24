---
keyword: HallOnlyFilt
summary: 在仅霍尔换相模式下，对基于霍尔传感器的换相角施加的数字滤波器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 477
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
  - 99
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# HallOnlyFilt

在仅霍尔换相模式下，对基于霍尔传感器的换相角施加的数字滤波器。

## 概述

`HallOnlyFilt` 设置当轴在仅霍尔换相模式下运行时，对基于霍尔传感器的换相角施加的数字滤波器。较大的值会对霍尔信号施加更多滤波以降低噪声，代价是引入额外的相位滞后。在没有基于编码器的换相可用时，该参数用于平滑由原始霍尔状态（[HallsValue](HallsValue.md)）及其关联角度映射表（[HallsAngle](HallsAngle.md)）导出的换相角。换相方法本身通过 [ComtMode](ComtMode.md) 选择（仅霍尔方法）。该参数为轴作用域且保存至闪存，可随时更改，包括在电机使能或运动中（范围 0–99，默认值 0）。

## 工作原理

在仅霍尔换相模式下，每次霍尔状态切换（每隔 60° 电气角）时，角度将发生突变，产生电压/电流尖峰。`HallOnlyFilt` 施加一阶低通滤波器，将新导出的霍尔角度与上一控制周期的滤波后角度混合。设定值表示为分数 $k = \frac{\text{HallOnlyFilt}}{100}$：

$$
\theta_{filtered} = (1 - k)\cdot\theta_{hall} + k\cdot\theta_{previous}
$$

- `0`（默认值）不施加任何滤波——角度直接跟随原始霍尔状态角度。
- 较大值（最高 `99`）对前一周期角度赋予更高权重，使角度过渡更平滑，但相位滞后更大。

滤波结果即为 [ComtAng](ComtAng.md) 中显示的值。该滤波器仅在通过 [ComtMode](ComtMode.md) 选择仅霍尔换相方法时生效；在基于编码器或切换型方法下无效。

## 示例

```text
AHallOnlyFilt=10     ; apply moderate filtering to the Hall-based angle
AHallOnlyFilt       ; query the current filter setting
```

## 另请参阅

- [HallsValue](HallsValue.md) — 被滤波的原始霍尔传感器状态
- [HallsAngle](HallsAngle.md) — 映射到每个霍尔状态的电角度
- [ComtMode](ComtMode.md) — 选择换相方法
