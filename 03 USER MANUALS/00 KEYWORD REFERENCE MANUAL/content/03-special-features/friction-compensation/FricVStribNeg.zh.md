---
keyword: FricVStribNeg
summary: 负方向的 Stribeck 速度，单位为 counts/s（方法 4 和 5）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 922
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricVStribNeg

> **AGM800-EC** — 关键字换算采用 16,000 Hz 控制频率，内部值与外部值之间的比例为 `1.024`。读取时除以此系数；允许的写入操作乘以此系数，整数值需舍入。参见 [AGM800-EC 时间与单位](../../02-keywords/01-system/03-timing/AGM800-EC-units.zh.md)。

负方向的 Stribeck 速度，单位为 counts/s（方法 4 和 5）。

## 概述

`FricVStribNeg` 是在负方向上，起动电平衰减到库仑电平所跨越的速度。单位为 counts/s，以正数输入。适用于 AGM800 和 AGM800-EC（central-i v5）。它是 5.3.0 新增的关键字（CAN 代码 922，在 rc4 中为 `StribEps`）。

## 工作原理

方法 4（LuGre）和 5（Stribeck）使用曲线

$$
F_c + (F_s - F_c)\,e^{-(v/V_s)^2}
$$

其中 $V_s$ 为 `FricVStribNeg`，$F_s$ 为 [FricIStatNeg](FricIStatNeg.md)，$F_c$ 为 [FricINeg](FricINeg.md)。在 $v = V_s$ 时，起动超出量约剩 37%；到 $2V_s$ 时低于 2%。取值小则起动峰短而陡；取值大则额外电流持续更久。取值为 0 则去掉起动峰（轴一开始运动，输出即为库仑电平）。

死区带（[FricVBandNeg](FricVBandNeg.md)）与 Stribeck 速度是两个独立的设置：死区带负责过零，Stribeck 速度负责起动。方法 1 至 3 不使用 `FricVStribNeg`。

## 示例

```text
AFricVStribNeg=3000     ; 起动峰在约 3000 counts/s 范围内衰减
```

## 另请参阅

- [FricVStribPos](FricVStribPos.md) — 另一方向的 Stribeck 速度
- [FricMethod](FricMethod.md) — 方法 5 公式
- [摩擦前馈](00-overview.md)
