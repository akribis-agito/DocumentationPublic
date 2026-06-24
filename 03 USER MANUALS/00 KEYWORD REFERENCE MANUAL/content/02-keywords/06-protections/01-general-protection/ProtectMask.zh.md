---
keyword: ProtectMask
summary: 位域，启用哪些硬件保护条件触发故障。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 97
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 65535
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProtectMask

位域，用于屏蔽（禁用）选定的硬件保护条件。

## 概述

`ProtectMask` 选择哪些硬件保护条件被*抑制*。它使用与 [HWProtectBits](HWProtectBits.md) 相同的位位置，但它是一个**排除掩码**：

- `ProtectMask` 位 = **1** &rarr; 该保护被**禁用**（屏蔽——它不会禁用轴）。
- `ProtectMask` 位 = **0** &rarr; 该保护被**启用**（默认值——该条件会禁用轴）。

因此默认的 `ProtectMask = 0` 使每一项（可屏蔽的）保护都保持激活。置位某一位会关闭一项保护。它是轴作用域的，保存至闪存，并且可在任何时刻更改（运动中或电机使能时）。

> **注意：** 屏蔽某项硬件保护会移除一个安全限值。只有在你了解它为何触发以及它所防护的对象时，才应禁用某项保护。

## 工作原理

`ProtectMask` 不直接用于控制环；相反，每当它（或 [PowerSupply](../02-current-and-voltage/PowerSupply.md)）发生变化时，驱动器都会据此重新计算硬件故障使能设置。实际应用于硬件的使能在效果上为：

```text
hardware_enable = (all maskable protections & ~ProtectMask) | non-maskable protections
```

也就是：从“所有保护开启”开始，清除你在 `ProtectMask` 中置位的位，然后将不可屏蔽保护强制重新开启。这就是为何 `ProtectMask` 中的 `1` 会*移除*一项保护，以及为何某些关键保护（不可屏蔽集合）无论你写入什么都无法被禁用。

在 standalone 驱动器上，结果在本地应用；在 **Central-i (v5)** 上，等效的使能字被发送至远程驱动器。电源相保护还额外受 [PowerSupply](../02-current-and-voltage/PowerSupply.md) 控制，使得未使用的 AC 相不被保护。

当 [HWProtectBits](HWProtectBits.md) 中出现已启用的保护条件时，轴被禁用，并触发对应的 [ConFlt](../../07-status-and-faults/ConFlt.md) ConFlt 码。

### 边界情况

- **电机失能：** 写入立即生效（该关键字为 `ok_in_motion: true`、`ok_motor_on: true`）。每当 `ProtectMask`（或 [PowerSupply](../02-current-and-voltage/PowerSupply.md)）变化时，硬件会重新推导使能字。
- **模式相关性：** 该掩码无条件地应用于所有可屏蔽的硬件保护位。
- **不可屏蔽保护：** STO1（位 0）、STO2/VCC（位 6）、过流（位 4 和 5）、5 V 电源故障（位 10）、IPM 故障（AG100 上的位 12）、硬件看门狗（位 7）以及其他安全关键条件，无论 `ProtectMask` 如何都会被强制重新开启。只有主编码器（位 2）和辅助编码器（位 3）错误保护是可屏蔽的；置位任何其他位均无效——那些保护无法被禁用。
- **软件保护不在范围内：** `ProtectMask` **不**屏蔽软件级跳闸（跟随误差 / 超速 / 过温 / I²t / 电机堵转 / 双环堵转 / 失步 / 力误差 / 位置限位）。它们独立运行，无法用该掩码禁用。
- **范围：** 可用范围为 `0..65535`（`0x0000..0xFFFF`）——只有低 16 位有意义，且该值作为 16 位掩码应用。映射到不存在保护的位会被静默忽略。
- **故障时的快照：** 故障发生时刻 [HWProtectBits](HWProtectBits.md) 的值被捕获在 [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md)`[11]` 中。

## 示例

```text
AProtectMask         ; read the current protection mask
AProtectMask=0       ; default: every maskable protection enabled
```

要仅禁用辅助编码器错误保护（standalone 位 3），同时保持其余全部启用，请置位对应的位：`AProtectMask=0x0008`。

## 另请参阅

- [HWProtectBits](HWProtectBits.md) — 报告这些保护的实时状态（相同的位位置）
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 已启用的保护触发的故障
- [PowerSupply](../02-current-and-voltage/PowerSupply.md) — 额外控制电源相保护
