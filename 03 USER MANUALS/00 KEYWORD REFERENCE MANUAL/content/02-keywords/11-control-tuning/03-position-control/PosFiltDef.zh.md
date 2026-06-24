---
keyword: PosFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 123
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
    array_size: 11
    ok_in_motion: true
    ok_motor_on: true
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 定义每个位置环滤波器的类型和参数。
---
# PosFiltDef

定义每个位置环滤波器的类型和参数。

## 概述

`PosFiltDef` 保存由 [PosFiltOn](PosFiltOn.md) 启用的位置环滤波器定义。每个滤波器由 5 个连续数组元素描述（一个类型码加上最多四个参数）。v4 仅支持单个滤波器，数组占元素 `[1]`–`[5]`；Central-i v5 支持两个滤波器，占元素 `[1]`–`[10]`：

| 滤波器（N） | 说明 | 数组元素 |
|---|---|---|
| 1 | 规划器后滤波器 | `PosFiltDef[1]` … `PosFiltDef[5]` |
| 2 | 位置误差滤波器 | `PosFiltDef[6]` … `PosFiltDef[10]` |

对于每个滤波器，第一个元素为**滤波器类型**，后四个为**参数 1 到 4**，其含义取决于类型。

## 工作原理

每个 5 元素块的布局如下：

| 偏移 | 含义 |
|---|---|
| 第 1 个 | 滤波器类型（`0` = 无，`1` = 一阶低通，`2` = 二阶低通，`3` = 带一个零点的二阶低通，`4`/`5` = 一阶/二阶超前-滞后，`6`/`7` = 按相位的一阶/二阶超前-滞后，`8` = 陷波，`9` = 复合超前-滞后） |
| 第 2–5 个 | 参数 1 到 4（频率单位 Hz/100，阻尼比单位 %，相位单位度，陷波深度单位 dB——取决于类型） |

所选滤波器在位置环中以二阶（双二阶）节实现，位置由 [PosFiltOn](PosFiltOn.md) 设定：索引 1 对规划器输出（最终的 [PosRef](../../10-motion/01-kinematics-status/PosRef.md)）进行整形，索引 2 在 [PosGain](PosGain.md) 之前对位置误差 [PosErr](../../10-motion/01-kinematics-status/PosErr.md) 进行整形。写入 `PosFiltDef`（及对应的 [PosFiltOn](PosFiltOn.md)）后，执行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以重新计算系数。

完整的按类型参数定义、传递函数和单位详见附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)。

## 示例

```text
; Position-error filter (index 2) as a second-order low-pass at 850 Hz, damping 0.71
APosFiltDef[6]=2        ; type: second-order low-pass
APosFiltDef[7]=85000    ; cutoff 850 Hz (Hz/100)
APosFiltDef[8]=71       ; damping ratio 0.71 (%)
APosFiltOn[2]=1         ; enable the position-error filter
ACalcFilters            ; recompute filter coefficients
```

## 版本间变更

在 **v4** 上，仅支持规划器后滤波器（滤波器 1，元素 `[1]`–`[5]`）；位置误差滤波器（滤波器 2，元素 `[6]`–`[10]`）**仅限 Central-i v5**。v4 上 `PosFiltDef` 只能在电机关闭且不在运动时更改。在 **v5（Central-i）** 上，两个滤波器均可用，且 `PosFiltDef` 也可在电机使能和运动中更改。

## 另请参阅

- [PosFiltOn](PosFiltOn.md) — 启用此处定义的各位置滤波器
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 更改后重新计算滤波器系数
- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — 索引 2 处被滤波的信号
- [PosRef](../../10-motion/01-kinematics-status/PosRef.md) — 索引 1 处被整形的参考
- [VelFiltDef](../04-velocity-control/VelFiltDef.md) — 速度环滤波器定义
- 附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)
