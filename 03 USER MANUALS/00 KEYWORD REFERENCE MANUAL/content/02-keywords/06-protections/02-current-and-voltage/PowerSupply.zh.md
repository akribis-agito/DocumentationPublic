---
keyword: PowerSupply
summary: 声明驱动器的供电类型，使保护功能正确工作。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 401
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
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PowerSupply

声明驱动器的供电类型，使保护功能正确工作。

## 概述

`PowerSupply` 告诉驱动器为其供电的电源类型，以便 AC 缺相保护检查正确的输入引脚。请选择与你的硬件相匹配的值（通常通过 PCSuite 配置页面设置）。它无法在电机使能或运动中更改。

| 取值 | 供电类型 |
|-------|-------------|
| 1 | 单相 AC |
| 2 | DC —— 低压电源 |
| 3 | 三相 AC |

## 工作原理

`PowerSupply` 选择驱动器监测哪些电源输入相的“缺相”状态：

- **三相：** 同时检查 A&ndash;C 和 B&ndash;C 缺相标志。如果任一被置位，则禁用轴，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1054（AC 电源输入中至少有一个必需相被切断）。
- **单相：** 仅检查 B&ndash;C 缺相标志（引发相同的故障码 1054）。
- **DC：** 不施加 AC 缺相检查。

相同的供电相关相检查在轴使能时也会执行：如果在 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) 请求时刻所需的相缺失，则拒绝使能，并报告故障码 1054。

`PowerSupply` 还为保护掩码逻辑提供输入：当 [ProtectMask](../01-general-protection/ProtectMask.md)（或 `PowerSupply`）更改时，驱动器会重新推导硬件故障使能字，并根据所声明的供电类型对 AC 电源相位进行门控，使得该电源未使用的相不会被标记为缺失。（在独立 AG100 驱动器上，这通过专用的电源相位掩码位实现；在 Central-i 上，使能字被发送至远程驱动器。）

### 边界情况

- **电机失能 / 电机使能：** 该关键字被门控为 `ok_in_motion: false`、`ok_motor_on: false` —— 仅在电机禁用且非运动中时更改。保护使能字的重新推导发生在下一次写入时。
- **声明不匹配：** 在实际为 AC 接线的硬件上声明 `PowerSupply = 2`（DC）会抑制 AC 缺相故障 —— 你的保护实际上被禁用。请始终声明实际的供电类型。
- **对 [HWProtectBits](../01-general-protection/HWProtectBits.md) 的影响：** 无论所声明的供电类型如何，实时的 `HWProtectBits` 报告仍包含 AC 缺相位；`PowerSupply` 仅决定这些位是否引起跳闸。在 Central-i 上，相位位被排除在通用保护跳闸路径之外，而是由上述供电相关相检查评估。
- **三相引脚组：** 固件同时检查 A–C 和 B–C 相；任一缺失都会引发 [ConFlt](../../07-status-and-faults/ConFlt.md) 码 1054（一个或多个必需的 AC 相被切断）。
- **范围溢出：** 超出 `1…3` 的写入会被拒绝并报告超范围错误；存储值保持不变。

## 示例

```text
APowerSupply=3       ; three-phase AC supply
```

## 另请参阅

- [ProtectMask](../01-general-protection/ProtectMask.md) — 它所门控的电源相位保护
- [HWProtectBits](../01-general-protection/HWProtectBits.md) — 报告缺相位
- [ConFlt](../../07-status-and-faults/ConFlt.md) — AC 缺相时的故障 1054
- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — 母线电压限值
