---
keyword: BoardTemp
summary: 只读的控制器板温度（°C）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 397
attributes:
  access: ro
  scope: non-axis
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
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BoardTemp

只读的控制器板温度（°C）。

## 概述

`BoardTemp` 报告控制器板的温度，由板载数字传感器测量，单位为 °C。它为只读，不保存至闪存，并且始终可用——在 standalone 上为非轴范围（所有轴共用一个值），在 Central-i 上为按轴。功率级（IPM）温度请参见 [PwrTemp](PwrTemp.md)。

## 工作原理

### 测量

在控制器类产品上，板传感器通过 I²C 读取：I²C 模块在启动时预先配置为读取温度器件，并在每个后台轮次将结果复制到 `BoardTemp`。读数为 255 表示“未连接传感器”（例如 AGC301，其传感器位于驱动器板上），并报告为 0 °C。在 Central-i 主站上，板温度读取目前未启用，因此 `BoardTemp` 在此保持其默认值。

### 过温保护（固定限值）

与 [PwrTemp](PwrTemp.md)/[MaxPwrTemp](MaxPwrTemp.md) 不同，板温度故障使用 **75 °C 的固定限值**，而非用户关键字。当电机使能且不在仿真模式时：

```text
if (BoardTemp > 75 °C)   →   disable axis, raise the board over-temperature fault
```

[ConFlt](../../07-status-and-faults/ConFlt.md) 随后显示故障码 1060（板温度过高）。

### 告警分段（与 PwrTemp 共用）

`BoardTemp` 与 `PwrTemp` 共同作用于 [StatReg](../../07-status-and-faults/StatReg.md) 中相同的**功率/板温度**告警字段（位 11–12）——告警等级取两者中较高者。固定的板温度分段边界为：

| `BoardTemp` 分段 | StatReg 等级 | PCSuite LED |
|------------------|---------------|-------------|
| < 66 °C | 0 — none | off |
| 66…69 °C | 1 — low | yellow |
| 69…72 °C | 2 — medium | orange |
| > 72 °C | 3 — high | red |
| > 75 °C | fault (`ConFlt` = 1060) | — |

在较新的 Central-i 远程单元上，板温度告警分段边界由远程单元报告的按轴限值推导得出（按 88 / 92 / 96 %），而非固定的 66 / 69 / 72 °C 值；板过温故障限值在 standalone 和 Central-i 上均保持固定的 75 °C。

### 边界情况

- **电机失能：** 与 [MaxPwrTemp](MaxPwrTemp.md) 一样，过温跳闸以电机使能为门控条件，因此在轴禁用状态下发生的板过热不会跳闸——故障仅在下次重新使能时触发。
- **仿真模式：** 在仿真模式中跳过此跳闸。
- **无传感器（AGC301 等）：** I²C 返回 255 → `BoardTemp` 报告为 0 °C，固定 75 °C 跳闸永不触发。
- **固定限值：** 板限值在 standalone v4 上**不**可配置——它是固定的 75 °C 常量。仅 [MaxPwrTemp](MaxPwrTemp.md) 可由用户设置。
- **共用告警字段：** [StatReg](../../07-status-and-faults/StatReg.md) 位 11–12 承载 [PwrTemp](PwrTemp.md) 和 `BoardTemp` 告警等级中的较高者。
- **清除故障：** ConFlt 码 1060 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目仍保留。
- **哪个轴跳闸：** 对应的 [ErrLog](../../07-status-and-faults/ErrLog.md) 条目会标记跳闸的轴——高 8 位中的来源标记承载基于 1 的轴号（轴 A = 1），与低位中的故障码 1060 一同记录——因此在多轴单元上你可以分辨出是哪个轴发生了故障。
- **HWProtectBits / ProtectMask：** 板过温跳闸无法通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。

## 示例

```text
ABoardTemp          ; controller board temperature (°C)
```

## 另请参阅

- [PwrTemp](PwrTemp.md) — 功率级（IPM）温度
- [MaxPwrTemp](MaxPwrTemp.md) — 功率级过温限值（用户设置）
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 11–12 承载合并的功率/板温度告警
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障码 1060（板温度过高）
