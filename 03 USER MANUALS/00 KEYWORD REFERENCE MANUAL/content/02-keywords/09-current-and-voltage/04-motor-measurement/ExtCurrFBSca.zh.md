---
keyword: ExtCurrFBSca
summary: 将外部模拟电流检测输入转换为电机电流反馈的比例因子（应用于两相）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 866
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20.0
  - 20.0
  default: 0.4
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ExtCurrFBSca

将外部模拟电流检测输入转换为电机电流反馈的比例因子（应用于两相）。

## 概述

`ExtCurrFBSca` 设置将**外部模拟电流检测输入**转换为电流环所使用的电机电流反馈的比例。它适用于通过模拟输入测量电机电流的远程产品，且同一因子应用于两路相电流读数。

它是保存至闪存的轴相关参数。该值为浮点因子，可用范围为 -20.0 至 20.0，默认值为 0.4；符号设定反馈极性。使用它来匹配外部电流检测路径的增益（和方向），使报告的电机电流与实际电流一致。

> 仅自 v5（Central-i）起可用。这是整数形式 [CurrFBFact](CurrFBFact.md) 的 v5 替代项。

## 工作原理

设置该关键字后，控制器会将 `ExtCurrFBSca` 加载为所连接远程设备的电流检测因子（这适用于远程模拟电流反馈驱动器产品）。随后将该远程设备的原始模拟电流反馈码乘以此因子，以获得电机电流反馈。两路相电流使用单一因子，因此它对整个外部电流反馈通道进行统一缩放。所得到的电机电流即为电流环所调节的量，也是 [MotorCurr](../02-motor-variables/MotorCurr.md) 所报告的量。

该因子仅应用于相关远程设备；不使用外部模拟电流检测输入的产品不受影响。

## 示例

```text
AExtCurrFBSca=0.4        ; default scaling
AExtCurrFBSca=-0.4       ; same magnitude, inverted feedback polarity
AExtCurrFBSca            ; read the configured scaling
```

## 另请参阅

- [CurrFBFact](CurrFBFact.md) — 此比例的 v4 整数等效形式
- [MotorCurr](../02-motor-variables/MotorCurr.md) — 由缩放后的外部反馈产生的电机电流
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — 所连接远程设备的驱动器类型
