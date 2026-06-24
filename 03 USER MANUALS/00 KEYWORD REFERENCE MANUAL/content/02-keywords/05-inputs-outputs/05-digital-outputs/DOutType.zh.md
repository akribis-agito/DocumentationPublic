---
keyword: DOutType
summary: 单端数字量输出的按输出灌/拉电流模式（位域）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 209
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
  - 0
  - 65535
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
# DOutType

单端数字量输出的按输出灌/拉电流模式（位域）。

## 概述

`DOutType` 以位域形式（从 0 开始：位 0 = 输出 1）将每个数字量输出配置为灌电流或拉电流模式。各位：`0` = 灌电流，`1` = 拉电流。它仅适用于具有可配置灌/拉电流级的单端（开集电极）输出——参见各产品手册。差分输出以及没有可配置级的输出会忽略其 `DOutType` 位。

| 位值 | 模式 |
|-----------|------|
| 0 | 灌电流 |
| 1 | 拉电流 |

## 工作原理

`DOutType` 决定由哪个物理驱动器承载每个输出。最终输出字（`DOutPort XOR DOutLog`）首先构建，然后仅按类型路由开集电极位：

- **灌电流驱动器**获得 `DOutType = 0` 的位：`(~DOutType) & (final output word)`（按开集电极输出掩码）。
- **拉电流驱动器**获得 `DOutType = 1` 的位：`DOutType & (final output word)`（同一掩码）。

因此，一个输出位只通过其类型选定的驱动器驱动电流；另一个驱动器对该位看到的是 `0`。当你更改 `DOutType` 时，硬件输出级会立即更新（在独立式控制器上直接更新，或在 central-i 上通过向远程单元发送新的类型字更新），以使硬件级保持匹配。

`DOutType` 与[数字量输出概述](00-overview.md)中单端数字量输出信号路径上显示的灌/拉电流选择为同一设置。

## 示例

```text
ADOutType=9          ; binary …1001 — outputs 1 and 4 source mode; rest sink
ADOutType            ; read the present sink/source configuration
```

### 边界情况

- **差分输出**——这些引脚的 `DOutType` 位被忽略；输出字的高位直接馈入差分驱动器。
- **不可配置输出**——没有可配置灌/拉电流级的产品完全忽略 `DOutType`；类型在硬件中固定。
- **硬件功能输出**——若硬件路径使用开集电极级，则 [DOutSelect](DOutSelect.md) ≠ 0 的位仍遵循灌/拉电流划分；请查阅产品手册。
- **电机使能/失能**——与 `MotorOn` 无关。
- **保存**——可保存至闪存；启动时重新加载到硬件级。

## 参见

- [DOutPort](DOutPort.md) / [DOutLog](DOutLog.md)——产生按类型划分的输出字
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md)——输出功能分配
