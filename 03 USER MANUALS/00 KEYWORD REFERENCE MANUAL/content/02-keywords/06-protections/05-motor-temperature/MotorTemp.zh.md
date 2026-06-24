---
keyword: MotorTemp
summary: 只读的实测电机温度（在当前固件中标记为未实现）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 400
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
  - -40
  - 150
  default: 25
  scaling: 1.0
  implemented: not_implemented
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MotorTemp

只读的实测电机温度，单位为 °C（在关键字表中标记为未实现）。

## 概述

`MotorTemp` 报告电机温度（单位 °C），由接入温度传感器输入的 RTD/PT100 传感器导出。它为只读、轴相关，且不保存至闪存。其保护限值为 [MaxMotorTemp](MaxMotorTemp.md)；该值是否被读取由 [MotorTempUsed](MotorTempUsed.md) 控制。

> **关键字标记为未实现：** 在关键字参数表中，`MotorTemp` 条目被标记为未实现，因此它并未作为完全发布的关键字对外提供。底层的温度值*确实*在内部计算并使用（用于过温保护和告警），但在依赖所报告的数值之前，请向 Agito 确认传感器/硬件支持情况。其默认报告值为 25 °C。

## 工作原理

### 测量流程（传感器 → °C）

在采样 RTD 的产品上，控制器每个保护周期（约每毫秒一次）采样一次原始 RTD ADC 字，并通过固定的线性公式将其直接转换为 °C（无用户缩放，`scaling = 1.0`）：

$$
\text{MotorTemp} = 133 - \left\lfloor \frac{ADC \times 393}{2^{n}} \right\rfloor
$$

其中移位量 `n` 取决于产品：

| 产品 / 型号 | 移位量 `n` | 读取的轴 |
|-------------------|-----------|-----------|
| AG100（单通道 PT100） | 10 | 仅 A |
| 3 通道 RTD 产品 | 16 | A、B、C |

`133 − …` 这种形式意味着较大的 ADC 读数（较高的传感器电阻）对应较低的温度；所报告的值落在该关键字的 −40…150 °C 范围内。

### 该值的使用方式

控制器每毫秒将电机温度与 [MaxMotorTemp](MaxMotorTemp.md) 及其导出的告警阈值进行比较——但**仅当 [MotorTempUsed](MotorTempUsed.md) ≠ 0 时**。如果传感器类型为“none”（`MotorTempUsed = 0`），则完全跳过电机温度检查。故障/告警阈值参见 [MaxMotorTemp](MaxMotorTemp.md)，4 级告警参见 [StatReg](../../07-status-and-faults/StatReg.md) 第 15–16 位。

## 示例

```text
AMotorTemp          ; read axis A's motor temperature (°C)
```

## 另请参阅

- [MaxMotorTemp](MaxMotorTemp.md) — 过温故障限值（及告警阈值）
- [MotorTempUsed](MotorTempUsed.md) — 传感器类型选择（控制读取与保护）
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 15–16 位报告电机温度告警等级
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障码 1040（电机温度过高）
