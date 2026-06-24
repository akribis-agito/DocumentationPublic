---
keyword: VelFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 121
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
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
summary: 定义每个速度环滤波器的类型和参数。
---
# VelFiltDef

定义每个速度环滤波器的类型和参数。

## 概述

`VelFiltDef` 保存 [VelFiltOn](VelFiltOn.md) 所启用的两个速度环滤波器的定义。每个滤波器由最多 5 个连续数组元素描述（一个类型代码加最多四个参数），因此第 N 个滤波器占用 `VelFiltDef[N*5-4]` 至 `VelFiltDef[N*5]` 的元素：

| 滤波器（N） | 说明 | 数组元素 |
|---|---|---|
| 1 | 速度滤波器 1 | `VelFiltDef[1]` … `VelFiltDef[5]` |
| 2 | 速度滤波器 2 | `VelFiltDef[6]` … `VelFiltDef[10]` |

对于每个滤波器，第一个元素为**滤波器类型**，后四个为**参数 1 至 4**，其含义取决于类型。

## 工作原理

每个 5 元素块的布局如下：

| 偏移量 | 含义 |
|---|---|
| 第 1 个 | 滤波器类型（`0` = 无，`1` = 一阶低通，`2` = 二阶低通，`3` = 带一个零点的二阶低通，`4`/`5` = 一阶/二阶超前-滞后，`6`/`7` = 按相位的一阶/二阶超前-滞后，`8` = 陷波，`9` = 复数超前-滞后） |
| 第 2–5 个 | 参数 1 至 4（频率单位为 Hz/100，阻尼比单位为 %，相位单位为度，陷波深度单位为 dB——取决于类型） |

每个已启用的滤波器以二阶（双二次）节的形式串联应用于速度 PI 输出（[VelGain](VelGain.md) + [VelKi](VelKi.md) 结果），在位置模式下与前馈共同输出至环路侧电流参考（在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)），最终形成电机电流指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。类型代码为 `0`（无）时，该级为直通。

写入 `VelFiltDef` 本身不会重新计算滤波器；它仅标记系数已过期。写入 `VelFiltDef`（及对应的 [VelFiltOn](VelFiltOn.md)）后，须运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以重新计算系数。在 **v4** 中，在 `CalcFilters` 运行之前，受影响的轴无法使能——电机使能尝试将被拒绝（错误代码 `102`，"如果滤波器已修改但未执行 CalcFilters，则无法使能电机"）；若重新计算本身失败，电机使能将以错误代码 `87` 被拒绝。在 **v5（central-i）** 中，系数可动态重新计算，电机使能不受此约束。

完整的各类型参数定义、传递函数和单位见附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)。

## 示例

```text
; 将速度滤波器 1 设置为 450 Hz 陷波，深度 6 dB，宽度 40 Hz
AVelFiltDef[1]=8        ; 类型：陷波
AVelFiltDef[2]=45000    ; 陷波频率 450 Hz（Hz/100）
AVelFiltDef[3]=6        ; 陷波深度 6 dB
AVelFiltDef[4]=4000     ; 陷波宽度 40 Hz（Hz/100）
AVelFiltOn[1]=1         ; 启用速度滤波器 1
ACalcFilters            ; 重新计算滤波器系数
```

## 版本差异

在 **v4** 中，`VelFiltDef` 只能在电机关闭且不在运动中时更改。在 **v5（central-i）** 中，也可在电机使能和运动中时更改。

## 另请参阅

- [VelFiltOn](VelFiltOn.md) — 启用此处定义的每个速度滤波器
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 更改后重新计算滤波器系数
- [VelGain](VelGain.md) / [VelKi](VelKi.md) — 产生这些滤波器所整形的 PI 输出
- [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — 滤波输出馈入的环路侧电流参考（central-i v5）
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — 经补偿/注入后的最终电机电流指令
- [PosFiltDef](../03-position-control/PosFiltDef.md) — 位置环滤波器定义
- 附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)
