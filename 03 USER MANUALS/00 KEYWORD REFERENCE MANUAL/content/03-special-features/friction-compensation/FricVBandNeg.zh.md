---
keyword: FricVBandNeg
summary: 负侧的过零死区带，单位为 counts/s（由 FricVBlindNeg 更名）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 931
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
# FricVBandNeg

> **AGM800-EC** — 关键字换算采用 16,000 Hz 控制频率，内部值与外部值之间的比例为 `1.024`。读取时除以此系数；允许的写入操作乘以此系数，整数值需舍入。参见 [AGM800-EC 时间与单位](../../02-keywords/01-system/03-timing/AGM800-EC-units.zh.md)。

负侧的过零死区带，单位为 counts/s（由 FricVBlindNeg 更名）。

## 概述

`FricVBandNeg` 设定速度需要进入负侧多远，摩擦环节才给出完整电平。单位为 counts/s，以正数输入。适用于 AGM800 和 AGM800-EC（central-i v5）。它取代 5.3.0-rc4 中的 `FricVBlindNeg`（CAN 代码不变）。

## 工作原理

零速附近运动方向不确定，该死区带规定环节如何处理：

| 方法 | `FricVBandNeg` 的用途 |
|---|---|
| 1（线性） | 从 0 到库仑电平的斜坡宽度 |
| 2（滞环） | 电平切换到负侧的速度 |
| 3（间隙） | 通往负侧电平的斜坡宽度 |
| 5（Stribeck） | 过零平滑（tanh）建立的宽度 |
| 象限切换 | 死区：速度离开该带之前不施加冲击 |

LuGre（方法 4）不使用死区带，而使用 [FricVStribNeg](FricVStribNeg.md)。死区带为 0 表示"在零速处切换"。在 5.3.0-rc4 下保存的值不会被转换。从 rc4 升级后，请重新输入摩擦设置。

## 示例

```text
AFricVBandNeg=200      ; 速度超过 200 counts/s 后给出完整电平
```

## 另请参阅

- [FricVBandPos](FricVBandPos.md) — 另一侧的死区带
- [FricVStribNeg](FricVStribNeg.md) — Stribeck 速度（不同的参数）
- [摩擦前馈](00-overview.md)
