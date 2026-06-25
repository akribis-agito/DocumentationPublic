---
keyword: MaxPwrTemp
summary: 允许的最高功率级温度（°C）；超过该值将触发保护。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 90
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 20
  - 80
  default: 65
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# MaxPwrTemp

允许的最高功率级温度（°C）；超过该值将触发保护。

## 概述

`MaxPwrTemp` 是功率级（IPM）允许的最高温度，单位为 °C。当 [PwrTemp](PwrTemp.md) 接近或超过该限值时，过温保护动作以防止损坏。它保存至闪存，并可随时更改（范围 20…80 °C，默认 65 °C）——在 standalone 上为非轴范围（所有轴共用一个值），在 Central-i 上为按轴。

## 工作原理

### 过温故障

每毫秒一次，当电机使能且不在仿真模式时：

```text
if (PwrTemp > MaxPwrTemp)   →   disable axis, raise the power over-temperature fault, append to ErrLog
```

轴被禁用，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1018（IPM 温度过高），并记录该事件。故障在重新使能时清除。

### 分级告警分段（StatReg）

每当你写入 `MaxPwrTemp` 时，会按限值的 88 / 92 / 96 % 重新计算出三个推导的分段边界。它们送入 [StatReg](../../07-status-and-faults/StatReg.md) 中合并的功率/板温度告警字段（位 11–12）——报告的等级取 `PwrTemp` 与 [BoardTemp](BoardTemp.md) 两者贡献中的较高者：

| `PwrTemp` 分段 | StatReg 告警等级 | PCSuite LED |
|----------------|----------------------|-------------|
| < 0.88 × MaxPwrTemp | 0 — none | off |
| 0.88…0.92 × MaxPwrTemp | 1 — low | yellow |
| 0.92…0.96 × MaxPwrTemp | 2 — medium | orange |
| > 0.96 × MaxPwrTemp | 3 — high | red |
| > MaxPwrTemp | fault (`ConFlt = 1018`) | — |


> **注意：** 控制器板过温限值（[BoardTemp](BoardTemp.md)）是*固定的* 75 °C 常量——仅功率级限值可通过此关键字由用户设置。

### 边界情况

- **电机失能：** 故障检查以电机使能为门控条件（如上文文档所述），因此在电机失能时过温**不会**跳闸——热浸效应仅在下次重新使能时报错。
- **仿真模式：** 在仿真模式中跳过此跳闸。
- **模式依赖性：** 只要电机使能，无论何种运行模式，该跳闸均会运行。
- **范围溢出：** 超出 `20…80` 的写入会被拒绝（超范围错误），存储值保持不变；每当一次有效的 `MaxPwrTemp` 写入被接受时，告警分段边界都会重新计算。
- **清除故障：** ConFlt 码 1018 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 条目仍保留。
- **哪个轴跳闸：** 对应的 [ErrLog](../../07-status-and-faults/ErrLog.md) 条目会标记跳闸的轴——高 8 位中的来源标记承载基于 1 的轴号（轴 A = 1），与低位中的故障码 1018 一同记录——因此在多轴单元上你可以分辨出是哪个轴发生了故障。
- **共用告警字段：** [StatReg](../../07-status-and-faults/StatReg.md) 位 11–12 报告 [PwrTemp](PwrTemp.md) 与 [BoardTemp](BoardTemp.md) 告警等级中的较高者。
- **HWProtectBits / ProtectMask：** IPM 过温跳闸无法通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。独立的硬件 [HWProtectBits](../01-general-protection/HWProtectBits.md) IPM 故障位（ConFlt 码 1027）是不可屏蔽保护之一——无论 [ProtectMask](../01-general-protection/ProtectMask.md) 如何设置，它都保持有效。

## 示例

```text
AMaxPwrTemp[1]=65    ; trip axis A if the IPM exceeds 65 °C
AMaxPwrTemp          ; read the current limit
```

## 另请参阅

- [PwrTemp](PwrTemp.md) — 测得的功率级温度
- [BoardTemp](BoardTemp.md) — 控制器板温度（固定 75 °C 限值）
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 11–12 承载告警等级
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障码 1018（IPM 温度过高）
