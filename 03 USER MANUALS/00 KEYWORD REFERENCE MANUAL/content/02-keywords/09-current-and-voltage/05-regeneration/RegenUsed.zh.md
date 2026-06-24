---
keyword: RegenUsed
summary: 选择使用外部还是内部再生电阻。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 378
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 1
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
# RegenUsed

选择使用外部还是内部再生电阻。

## 概述

`RegenUsed` 配置是否使用再生（制动电阻）电路，使控制器与所连接的硬件相匹配。它是一个 0/1 设置（默认 1）。由于它是硬件配置设置，因此在轴运动中或电机使能时不能更改，并且会保存至闪存。阈值 [RegenOn](RegenOn.md) / [RegenOff](RegenOff.md) 仅在 `RegenUsed` 为非零时才生效。

## 工作原理

`RegenUsed` 是整个再生机制的使能门控。在再生步骤中（在 central-i 上为按轴，在独立控制器上为控制器范围），控制器**仅当 `RegenUsed` ≠ 0 时**才评估 [RegenOn](RegenOn.md) / [RegenOff](RegenOff.md) 阈值：

| `RegenUsed` | 行为 |
|-------------|-----------|
| 0 | 再生禁用。制动斩波器指令和 [StatReg](../../07-status-and-faults/StatReg.md) 位 1 被强制清除，阈值比较被跳过，且“regeneration active”数字量输出始终读为非激活。 |
| 1（默认） | 再生使能。斩波器按照围绕 [VBus](../01-system-variables/VBus.md) 的 `RegenOn` / `RegenOff` 迟滞进行切换。 |

写入 `RegenUsed = 0` 立即生效：斩波器指令和再生状态位（在独立控制器上为每个轴）在写入该值的瞬间即被清除，因此已经激活的电阻会被切断，而无需等待下一个再生步骤。

在 central-i 上，阈值比较还要求该轴的端口处于激活状态，且所连接的设备是带有母线电压读数的驱动器。如果端口上未绑定驱动器（或该设备不报告母线电压），则即使 `RegenUsed` 为非零，也不会对该轴评估再生。

> **注意：** 禁用再生会移除母线电压的耗散通路。在没有再生电阻的情况下，急剧减速可能将 [VBus](../01-system-variables/VBus.md) 推入过压保护（[MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../../06-protections/02-current-and-voltage/MaxVBusAbs.md)）并使轴跳闸。

## 示例

```text
ARegenUsed=1         ; enable the regen circuit (default)
ARegenUsed=0         ; disable regeneration (chopper forced off)
ARegenUsed           ; read the present setting
```

## 另请参阅

- [RegenOn](RegenOn.md)、[RegenOff](RegenOff.md) — 再生激活/停用阈值（仅在此项为非零时有效）
- [RegenCurr](RegenCurr.md) — 测得的再生电阻电流
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 1 报告再生处于激活状态
