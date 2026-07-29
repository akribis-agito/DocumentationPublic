---
keyword: AAmpFullScale
summary: 外部驱动器的满量程指令值，将轴指令缩放到模拟或 SPI 输出。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 228
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 100
  - 10000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AAmpFullScale

外部驱动器的满量程指令值，将轴指令缩放到模拟或 SPI 输出。

## 概述

`AAmpFullScale` 设置当轴驱动**外部驱动器**时所用的满量程值。它定义了哪个指令幅值对应于最大输出电平，以便控制器能将其内部参考（电流、速度或相电流）缩放到外部驱动器所期望的物理输出上。

该关键字适用于 [AmpType](AmpType.md) 的外部/直线模拟指令模式：2（模拟电流）、5（模拟速度）和 7（直线适配器）。它对内置 PWM 驱动器无效；内置**直线**驱动器（模式 4）改用 [LAmpFullScale](LAmpFullScale.md)。在轴配置期间将其与 [AmpType](AmpType.md) 一起设置；由于它是轴范围且保存至闪存，无法在电机使能或运动中更改。

## 工作原理

固件将 `AAmpFullScale` 转换为一个固定缩放因子

$$
factor\ \left\lbrack \frac{mV}{mA\ or\ count/s} \right\rbrack = \frac{10000}{\text{AAmpFullScale}}
$$

从而使等于 `AAmpFullScale` 的参考在模拟输出上恰好产生 10 000 mV（10 V）。每当 [AmpType](AmpType.md) 或 `AAmpFullScale` 更改时，该因子都会被重新计算。每个控制周期模拟输出为 `factor × reference`；当电机失能时，输出被强制为 0。

被缩放的参考 —— 从而也是 `AAmpFullScale` 的单位 —— 取决于所选的 [AmpType](AmpType.md)：

| AmpType | 被缩放的参考 | AAmpFullScale 单位 |
|---|---|---|
| 2（模拟电流指令） | 电流参考（[CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)），一个通道 | mA per 10 V |
| 5（模拟速度指令） | 速度参考（[VelRef](../10-motion/01-kinematics-status/VelRef.md)），一个通道 | count/s per 10 V |
| 7（直线适配器） | 两个相电流参考（[IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)），两个通道 | mA per 10 V |

例如，当 `AmpType = 2`、`AAmpFullScale = 5000`（mA）且电流参考为 3000 mA 时：

$$
AOutPort = \frac{\text{CurrRef}}{\text{AAmpFullScale}} \cdot 10000 = \frac{3000}{5000} \cdot 10000 = 6000\ \lbrack mV\rbrack
$$

在 [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md) 上产生 6000 mV。在直线适配器模式（7）下，相同的因子被独立应用于两个相电流参考，驱动两个模拟通道。

### 数字 SPI 指令（AmpType = 8，v5 central-i）

在 v5 中，`AmpType = 8` 驱动一个数字 SPI 适配器。控制器仍在内部换相，并像直线适配器（模式 7）那样转换相同的两个相电流参考（[IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)），但将每个发出为一个 16 位 SPI 码（0…65535），而不是模拟电压。该缩放因子使用数字满码，而不是 10 000 mV：

$$
factor\ \left\lbrack \frac{count}{mA} \right\rbrack = \frac{32768}{\text{AAmpFullScale}}
$$

中间码 32768 表示 0 A；相电流被映射为 `32768 + factor × PhaseCurr`，并饱和到 0…65535 范围。因此，等于 `AAmpFullScale` 的相电流将达到范围顶端（即高于中间码 32768 计数的半摆幅）。

在施加该系数之前，可以为相电流加上一个每相偏置（mA）——见 [ExtCurrCmdOfs](../09-current-and-voltage/04-motor-measurement/ExtCurrCmdOfs.md)；映射后的代码变为 `32768 + factor × (PhaseCurr + ExtCurrCmdOfs)`。实际发送给驱动器的代码由 [ExtCurrCmdVal](../09-current-and-voltage/04-motor-measurement/ExtCurrCmdVal.md) 报告。

## 示例

```text
AAAmpFullScale=5000      ; 5000 mA corresponds to full-scale (10 V) analog output
AAAmpFullScale          ; query the current full-scale value
```

## 另请参阅

- [AmpType](AmpType.md) —— 选择本缩放所适用的外部驱动器指令模式
- [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md) —— 由缩放后指令驱动的模拟输出端口
- [CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md) —— 在模式 2 和 7 中被缩放的电流参考
- [ExtCurrCmdOfs](../09-current-and-voltage/04-motor-measurement/ExtCurrCmdOfs.md) —— 数字 SPI 模式（8）下在该系数之前施加的每相 mA 偏置
