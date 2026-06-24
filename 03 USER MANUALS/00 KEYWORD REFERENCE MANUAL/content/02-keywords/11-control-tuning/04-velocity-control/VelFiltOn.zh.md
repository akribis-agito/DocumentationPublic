---
keyword: VelFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 122
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
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
summary: 启用或旁路作用于速度 PI 输出的速度环滤波器。
---
# VelFiltOn

启用或旁路作用于速度 PI 输出的速度环滤波器。

## 概述

`VelFiltOn` 启用由 [VelFiltDef](VelFiltDef.md) 定义的速度环滤波器。这些滤波器串联应用于速度 PI 输出（[VelGain](VelGain.md) + [VelKi](VelKi.md) 结果），在位置模式下与前馈共同输出至环路侧电流参考（在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)），最终形成电机电流指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。每个已启用的滤波器对该信号进行整形——例如，用陷波器抑制机械谐振。

| 索引 | 滤波器 |
|-------|--------|
| 1 | 速度滤波器 1 |
| 2 | 速度滤波器 2 |

`VelFiltOn[Index] = 1` 启用对应滤波器；`VelFiltOn[Index] = 0` 旁路该滤波器（信号直通不变）。范围为 `0` 到 `1`，默认值 `0`（全部旁路）。

## 工作原理

速度 PI 输出依次通过已启用的滤波器，每个滤波器以其 [VelFiltDef](VelFiltDef.md) 参数实现为二阶（双二次）节。禁用的级将其输入直接传递至下一级。最后一级的输出（在位置模式下加上加速度/速度前馈）构成环路侧电流参考（在 central-i v5 上报告为 [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)）；经电流补偿和注入后，成为最终指令 [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)。

更改 `VelFiltOn` 本身不会重新计算滤波器；它仅标记系数已过期。更改 `VelFiltOn` 或 [VelFiltDef](VelFiltDef.md) 后，须运行 [CalcFilters](../01-general-keywords/CalcFilters.md)，使控制器重新计算内部滤波器系数。在 **v4** 中，在 `CalcFilters` 运行之前，受影响的轴无法使能——电机使能尝试将被拒绝（错误代码 `102`，"如果滤波器已修改但未执行 CalcFilters，则无法使能电机"）；若重新计算本身失败，电机使能将以错误代码 `87` 被拒绝。在 **v5（central-i）** 中，系数可动态重新计算，电机使能不受此约束。

## 示例

```text
AVelFiltOn[1]=1     ; 启用速度滤波器 1
AVelFiltOn[2]=0     ; 旁路速度滤波器 2
AVelFiltOn[1]       ; 读取速度滤波器 1 的使能状态
```

## 版本差异

在 **v4** 中，`VelFiltOn` 只能在电机关闭且不在运动中时更改。在 **v5（central-i）** 中，也可在电机使能和运动中时更改。

## 另请参阅

- [VelFiltDef](VelFiltDef.md) — 定义每个速度滤波器的类型和参数
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 更改后重新计算滤波器系数
- [VelGain](VelGain.md) / [VelKi](VelKi.md) — 产生这些滤波器所整形的 PI 输出
- [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — 滤波输出馈入的环路侧电流参考（central-i v5）
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — 经补偿/注入后的最终电机电流指令
- [PosFiltOn](../03-position-control/PosFiltOn.md) — 位置环滤波器使能
- 附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)
