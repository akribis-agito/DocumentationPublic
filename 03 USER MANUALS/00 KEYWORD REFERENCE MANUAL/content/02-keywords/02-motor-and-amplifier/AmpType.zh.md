---
keyword: AmpType
summary: 选择轴驱动其电机的方式——使用内置驱动器，或通过模拟/数字指令使用外部驱动器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 226
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
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    range:
    - 0
    - 8
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AmpType

选择轴驱动其电机的方式——使用内置驱动器，或通过模拟/数字指令使用外部驱动器。

## 概述

`AmpType` 定义轴所使用的驱动器模式。视 Agito 产品而定，轴可以直接驱动其内部 PWM 驱动器，或通过模拟或数字指令与外部驱动器对接。该选择决定了轴产生何种指令信号，以及哪些相关关键字适用——例如外部模拟模式使用 [AAmpFullScale](AAmpFullScale.md) 来缩放输出。各产品可用的驱动器功能请联系 Agito。

由于 `AmpType` 是保存至闪存的轴相关参数，因此无法在电机使能或运动中更改；应在轴配置期间（通常在 PCSuite 设置页面）进行设置，然后执行 `Save`。

> [!note] 状态：partial
> 前置数据将 `AmpType` 标记为 `partial`。在 v4 上固件范围为 0–7；v5（central-i）将其扩展至 0–8。选择产品不支持的值时，将在电机使能时被拒绝，并触发控制器故障 [1053](../../04-error-codes/controller-error-codes.md)（"AmpType value not allowed for this product"）。

## 工作原理

`AmpType` 决定轴是闭合其**自身电流环**还是将其委托出去。对于**内部换相**模式——内置 PWM 驱动器（0）、线性适配器（7）以及（v5）数字 SPI（8）——控制器运行完整的内部电流/换相环，并直接驱动功率级（0），或为外部功率级发出由此得到的相电流参考（7、8）。对于其余模式，轴被标记为**外部驱动**：跳过内部电流环，控制器仅发出指令信号（模拟电流、模拟速度或脉冲方向）供外部驱动器据此闭环。

更改 `AmpType` **仅对无刷电机的内部换相模式**重新置位换相：[StatReg](../07-status-and-faults/StatReg.md) 换相位被清除，电机使能前需重新定相。对于外部驱动模式，轴在换相方面不再被视为无刷电机，因此跳过此重新置位。

| AmpType | 驱动器模式 | 电流环 |
|----|----|----|
| 0 | 内置 PWM 驱动器——控制器直接驱动功率级。 | 内部 |
| 1 | 保留（曾为 central-i）。请勿使用。 | — |
| 2 | 外部驱动器，模拟**电流**指令。电流参考（[CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)）通过 [AAmpFullScale](AAmpFullScale.md) 缩放为模拟量输出电压。 | 外部 |
| 3 | 外部驱动器，数字**脉冲方向（PD）**指令。控制器输出步进/方向脉冲；许多检查（电流环、换相）被绕过。 | 外部 |
| 4 | 内置**线性**驱动器（保留产品）。该轴为外部驱动：跳过内部电流环，仅发出模拟**电流**指令——即由 [LAmpFullScale](LAmpFullScale.md) 缩放的电流参考（与模式 2 相同的指令路径）。 | 外部 |
| 5 | 外部驱动器，模拟**速度**指令。速度参考（[VelRef](../10-motion/01-kinematics-status/VelRef.md)）通过 [AAmpFullScale](AAmpFullScale.md) 缩放为模拟量输出电压。 | 外部 |
| 7 | 外部**线性适配器**：控制器仍运行其内部换相/电流环，并将两个相电流参考（[IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)）作为模拟电压输出（由 [AAmpFullScale](AAmpFullScale.md) 缩放）。 | 内部 |

在 **v5（central-i）** 中还存在另外两种模式：

| AmpType | 驱动器模式 | 电流环 |
|----|----|----|
| 6 | 带位置反馈的数字脉冲方向指令。外部驱动。 | 外部 |
| 8 | 数字 SPI：控制器运行其内部换相/电流环，并将两个相电流参考（[IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)）作为数字 SPI 代码输出——即模拟线性适配器（模式 7）的数字对应形式。由于其保持内部换相，因此换相/自动定相和电流环整定如同无刷电机一样适用。 | 内部 |

> [!note]
> 数值 6 在数值上落入 v4 的 0–7 范围内，但模式 6 仅在 v5 上可用；在 v4 上，模式 6 和 8 不可用。

### 外部模式的输出缩放

对于模拟指令模式（2、5、线性适配器 7 以及内置线性 4），模拟量输出电压为参考值乘以固定系数 `10000 / FullScale`（因此满量程参考 → 10 000 mV = 10 V）。每当 `AmpType`、[AAmpFullScale](AAmpFullScale.md) 或 [LAmpFullScale](LAmpFullScale.md) 更改时，该系数都会重新计算。电机失能时，模拟输出被强制为零。各模式的单位和示例参见 [AAmpFullScale](AAmpFullScale.md)。

### 各远程单元的允许值（v5 central-i）

在 v5（central-i）上，连接管理器会根据链路上检测到的远程单元类别校验 `AmpType`：

| 远程单元类别 | 允许的 `AmpType` |
|---|---|
| 内置驱动器单元 | 0（内置 PWM） |
| 模拟/脉冲方向适配器 | 2（模拟电流）、3（PD）、5（模拟速度）、6（带反馈的 PD） |
| 线性/数字 SPI 适配器 | 7（线性适配器）、8（数字 SPI） |
| 远程 I/O 单元 | 任意 `AmpType` |

若配置的 `AmpType` 与检测到的单元不匹配（或单元类型未知），则该设备被断开连接，其 [CIStatus](../01-system/05-central-i/CIStatus.md) / [CIIdentity](../01-system/05-central-i/CIIdentity.md) 被清除。v4 的设备集更窄（没有模式 6/8，且只有一个此类适配器类别映射到模式 7）。

## 示例

```text
AAmpType=0           ; use the built-in PWM amplifier
AAmpType=2           ; external amplifier, analog current-reference command
AAmpType            ; query the current amplifier mode
```

## 版本间变更

| | v4（standalone 与 central-i） | v5（central-i） |
|---|---|---|
| 范围 | 0–7 | 0–8 |
| 新增模式 | — | 6（带反馈的 PD）、8（数字 SPI 相电流） |

v5 仅适用于 central-i；在 standalone 产品上 `AmpType` 保持 v4 范围 0–7。

## 另请参阅

- [AAmpFullScale](AAmpFullScale.md) — 外部模拟模式（2、5、7；v5 中还包括 8）的满量程输出缩放
- [LAmpFullScale](LAmpFullScale.md) — 内置线性驱动器（模式 4）的满量程选择
- [MotorType](MotorType.md) — 连接到驱动器的电机类型
- [StatReg](../07-status-and-faults/StatReg.md) — 换相状态位（`AmpType` 更改时被清除）
