---
keyword: TorqCompMode
summary: 在速度/位置模式下选择环路电流（转矩）补偿的来源。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 391
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
  - -1
  - 5
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# TorqCompMode

在速度/位置模式下选择环路电流（转矩）补偿的来源。

## 概述

`TorqCompMode` 选择环路电流补偿的来源。仅当 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 2 或 3（速度或位置运行模式）时适用。当设置为某个固定来源时，它取自相应的 [TorqCompFix](TorqCompFix.md) 条目；当设置为 0 时，它使用一路模拟量输入。该补偿在框图中的位置参见 [Control tuning – Feedforwards](../../11-control-tuning/05-feedforwards/00-overview.md)。

## 工作原理

该补偿在位置/速度控制环中施加，紧接在电流参考由速度 PI 输出（以及任何力/前馈项）形成之后。所选补偿项被**加到**电流参考上。由于这发生在位置/速度环内而非电流环内，因此它仅在速度或位置运行模式下生效（在电流运行模式下，参考会在下游被覆盖，故此项无效）。

模式选择通过对 `TorqCompMode` 值进行开关切换来实现：

| TorqCompMode | 所加的电流补偿值 |
|----|----|
| -1 | 0（无补偿——默认值；任何超出范围的值也得到此结果） |
| 0 | 来自分配给转矩补偿的模拟量输入的值（经滤波的模拟量输入值；参见 [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md)，转矩补偿选择）。 |
| 1 | TorqCompFix[1] |
| 2 | TorqCompFix[2] |
| 3 | TorqCompFix[3] |
| 4 | TorqCompFix[4] |
| 5 | TorqCompFix[5] |

对于固定值模式，固件直接以模式编号索引 [TorqCompFix](TorqCompFix.md) 数组，因此模式 `N` 选择 `TorqCompFix[N]`。

该补偿项与电机电流参考（[CurrRef](../02-motor-variables/CurrRef.md)）采用相同单位。在 central-i v5 上，电流参考和固定值数组为浮点数；在 v4 上为整数。选择逻辑和值表在各版本间完全相同。

## 示例

```text
ATorqCompMode=-1     ; no compensation (default)
ATorqCompMode=1      ; use TorqCompFix[1]
ATorqCompMode=0      ; use analog-input torque compensation
```

### 操作演练：选择一个固定补偿值

固定来源模式（1-5）从 [TorqCompFix](TorqCompFix.md) 中按模式编号索引读取。下面的示例在位置运行模式下施加恒定的 200 mA 偏置，以平衡一个已知的稳态负载（例如垂直轴上的重力）。

1. **确保轴处于使用此补偿的模式。** 仅当 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 为 `2`（速度）或 `3`（位置）时才施加补偿：

   ```text
   AOperationMode=3
   ```

2. **将要使用的值存入所选的 [TorqCompFix](TorqCompFix.md) 槽位**（数组索引必须与 `TorqCompMode` 值匹配）：

   ```text
   ATorqCompFix[1]=200
   ```

3. **选择该槽位**：

   ```text
   ATorqCompMode=1
   ```

4. **验证其正在生效**，方法是在静止状态下读取环路侧电流参考 [CurrRefCtrl](../02-motor-variables/CurrRefCtrl.md)（v5）：它应在速度 PI 所产生的值之上带有 200 mA 偏置。

5. **在测试结束时切换回无补偿**：

   ```text
   ATorqCompMode=-1
   ```

> **环路侧与电机侧。** 此补偿加在位置/速度环*内部*（电流环之前）。若需电流侧偏置——即无论运行模式如何都直接加到最终电机电流参考上的偏置——请改用 [CurrRefOffset](CurrRefOffset.md)。

## 另请参阅

- [TorqCompFix](TorqCompFix.md) — 由此模式选择的固定补偿值
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — 须为 2 或 3 时本项才适用
- [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) — 模拟量输入转矩补偿源
- [CurrRefOffset](CurrRefOffset.md) — 电流侧偏置（不同的作用点）
- [CurrRefCtrl](../02-motor-variables/CurrRefCtrl.md) — 此补偿求和所在的环路侧电流参考
