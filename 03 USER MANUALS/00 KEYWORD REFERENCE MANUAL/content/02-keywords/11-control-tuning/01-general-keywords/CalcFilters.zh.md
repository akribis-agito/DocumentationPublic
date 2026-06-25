---
keyword: CalcFilters
summary: 重新计算可定制控制环滤波器内部系数的指令，系数由各定义关键字确定。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 360
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CalcFilters

根据定义关键字重新计算可自定义环路滤波器内部系数的命令。

## 概述

位置、速度、前馈和力路径中的可自定义滤波器通过定义关键字进行配置。更改定义关键字**不会**改变控制器正在运行的滤波器——它仅记录滤波器*定义*已更改且与当前使用的系数不同步。`CalcFilters` 是读取所有待处理定义、校验、计算新系数并一次性切换运行滤波器的命令。

`CalcFilters` 作用于被寻址的轴，并对该轴所有标记为已更改的滤波器生效。自上次计算以来定义未变更的滤波器不受影响。

需要通过 `CalcFilters` 使更改生效的关键字为：

1. `PosFiltDef` / `PosFiltOn` — 位置滤波器
2. `VelFiltDef` / `VelFiltOn` — 速度滤波器
3. `FFFiltDef` / `FFFiltOn` — 前馈滤波器
4. `ForceFiltDef` / `ForceFiltOn` — 力滤波器

## 工作原理

### 滤波器被标记为待重新计算的条件

在 central-i v5 上，每次写入上述定义关键字时，新值将与上次成功计算时生效的值进行比较。若不同，则对应滤波器在 [FilterStatus](FilterStatus.md) 中被标记为"待重新计算"（该滤波器字段的 bit `n+0` 被置位）。写入与当前已生效值相同的值不会标记该滤波器。在没有逐滤波器状态字的旧版固件上，任何对定义关键字的写入均会无条件置位 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 26（"滤波器已修改"）——不进行值比较。

### CalcFilters 对每个滤波器的处理

对于每个被标记为待处理的滤波器，控制器执行以下操作：

1. **校验定义。** 滤波器类型必须为已知类型；每个参数必须在允许范围内。结果写入 [FilterStatus](FilterStatus.md) 中对应滤波器字段：若滤波器类型未知，则置位 bit `n+1`；若参数超出范围，则按参数置位 bit `n+2`–`n+5`。
2. **校验成功时**，计算新系数，将运行滤波器切换为新系数，清除该滤波器的历史缓冲区（使新滤波器从干净状态启动），清除待重新计算标志，并将已接受的定义记录为未来变更检测的新基准。
3. **校验失败时**（类型未知或参数超出范围），控制器拒绝该滤波器的更改。整个定义恢复至上次接受的状态：滤波器开/关标志、滤波器类型及所有四个定义参数均恢复至上次成功计算时的值。滤波器继续以之前有效的系数运行，记录错误并返回。（此校验回滚行为仅在 central-i v5 上存在。）

处理完一个轴的所有滤波器后，控制器返回单个响应：若任何滤波器校验失败则返回错误，否则返回成功。

### 已清除的状态位

在旧版固件上，[StatReg](../../07-status-and-faults/StatReg.md) bit 26（"滤波器已修改"）和 bit 27（"计算滤波器失败"）跟踪计算结果：当 `CalcFilters` 完成且无失败时两个位均清零；若任何滤波器校验失败则置位 bit 27（"计算滤波器失败"）。该固件的使能序列检查这些位，因此 bit 26 或 bit 27 置位时轴无法使能——参见 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md)。在 central-i v5 上，逐滤波器结果通过 [FilterStatus](FilterStatus.md) 报告而非通过 `StatReg` 位，`CalcFilters` 允许在运动中及电机使能时执行，bit 26 和 bit 27 不再阻止使能。

### 消息顺序的重要性

由于 `CalcFilters` 校验的是执行时刻的当前定义，一个滤波器的所有参数必须在同一消息中**先于** `CalcFilters` 设置完毕。若 `CalcFilters` 在完整定义就位之前运行，则对不完整的定义进行校验。若该不完整定义无效，则被拒绝（开/关标志、类型及所有四个参数恢复至上次接受的定义），并保留之前运行的滤波器。在 `CalcFilters` 之后写入的参数不被本次计算所见，因此只有在后续 `CalcFilters` 校验时方可生效。

以下示例将速度滤波器 1 配置为 450 Hz、6 dB 深度、40 Hz 带宽的陷波滤波器。

| 参数 | 初始值 | 正确顺序（CalcFilters 后） | 错误顺序（CalcFilters 后） |
|---|---|---|---|
| `VelFiltOn[1]` | 1 | 1 | 1 |
| `VelFiltDef[1]` | 1 | 8 | 8 |
| `VelFiltDef[2]` | 20000 | 45000 | 45000 |
| `VelFiltDef[3]` | 0 | 6 | 0 |
| `VelFiltDef[4]` | 0 | 4000 | 0 |
| `VelFiltDef[5]` | 0 | 0 | 0 |
| 结果 | 速度滤波器 1 = 200 Hz 低通，已启用 | 450 Hz 陷波，6 dB，40 Hz 带宽，已启用。**已接受。** | 陷波定义不完整——陷波带宽仍为 0，低于允许最小值，滤波器被**拒绝为超出范围**。定义恢复至上次接受的状态（滤波器保持为低通）。随后写入 `VelFiltDef[3]` 和 `[4]`，但因在 `CalcFilters` 之后到达，不属于本次校验，需等到下一次 `CalcFilters` 才能生效。 |

- 正确顺序：`VelFiltDef[1]=8; VelFiltDef[2]=45000; VelFiltDef[3]=6; VelFiltDef[4]=4000; CalcFilters`
- 错误顺序：`VelFiltDef[1]=8; VelFiltDef[2]=45000; CalcFilters; VelFiltDef[3]=6; VelFiltDef[4]=4000`

## 示例

```text
AVelFiltDef[1]=8; AVelFiltDef[2]=45000; AVelFiltDef[3]=6; AVelFiltDef[4]=4000; ACalcFilters   ; define then calculate
ACalcFilters                                                                                  ; recalculate the axis filters now
```

## 另请参阅

- [FilterStatus](FilterStatus.md) — 逐滤波器的计算/校验结果
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 26（滤波器已修改）/ bit 27（计算滤波器失败）
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — 使能序列可能检查滤波器状态位
