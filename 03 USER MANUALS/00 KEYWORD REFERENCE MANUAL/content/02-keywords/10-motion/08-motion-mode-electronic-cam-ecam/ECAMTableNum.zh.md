---
keyword: ECAMTableNum
summary: 选择活动 ECAM 凸轮曲线/查找表（1-10）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 311
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMTableNum

选择活动 ECAM 凸轮曲线/查找表（1-10）。

## 概述

`ECAMTableNum` 选择最多 10 条凸轮曲线（查找表）中的哪一条处于活动状态。每条凸轮曲线均有一套完整定义其的参数——[ECAMStart](ECAMStart.md)、[ECAMEnd](ECAMEnd.md)、[ECAMStartCyc](ECAMStartCyc.md)、[ECAMEndCyc](ECAMEndCyc.md)、[ECAMGap](ECAMGap.md)、[ECAMCycles](ECAMCycles.md)、[ECAMMaster](ECAMMaster.md) 和 [ECAMMasterIni](ECAMMasterIni.md)——以每曲线一个元素的数组形式保存。仅当轴不在运动中时才能更改所选曲线。

## 工作原理

控制器始终保存全部 10 条曲线的八个定义参数，但运动期间只有一条生效。ECAM 运动启动（[Begin](../04-motion-command/Begin.md)）时，控制器将 `ECAMTableNum` 所指定曲线的参数复制到活动工作集并进行校验。如果所选曲线存在以下情况，[Begin](../04-motion-command/Begin.md) 将被拒绝并返回特定的[指令错误代码](../../../04-error-codes/instruction-error-codes.md)：

- `ECAMStart`、`ECAMStartCyc`、`ECAMEndCyc` 或 `ECAMEnd` 中任意一个为 `0`——索引为零表示该曲线未使用（错误代码 73）；
- 索引不满足 `ECAMStart ≤ ECAMStartCyc < ECAMEndCyc ≤ ECAMEnd`（错误代码 74）；
- `ECAMGap` 为 `0`（错误代码 75），或 `ECAMCycles` 为 `0`（错误代码 76）；
- `ECAMMaster` 来源的复杂 CAN 编码超出范围（错误代码 77）、指定了无效轴（错误代码 78）、使用了错误的数组索引（错误代码 79），或指向函数而非参数（错误代码 80）；
- 回放该曲线所需的主值范围超过 ±2,000,000,000 主变量单位（错误代码 81）；
- 凸轮表中两个相邻条目差值过大（错误代码 82）；
- `ECAMMasterIni` 超出一个 ECAM 周期的主值范围（错误代码 323）。

由于参数在启动时锁存，运动中更改 `ECAMTableNum` 无效，因此在运动中对其写操作被禁止。当前周期计数器 [ECAMCycCount](ECAMCycCount.md) 也按曲线索引，因此每条曲线保有各自的周期计数。

## 示例

```text
AECAMTableNum=1      ; 选择凸轮曲线 1（默认）
AECAMTableNum        ; 读取活动凸轮曲线编号
```

### 操作示例：定义并运行一次 ECAM 周期

将一小段凸轮表加载到 [GenData](../../20-arrays/GenData.md) 的索引 1-5，将凸轮曲线 1 配置为使用这些条目，并跟随轴 B 的 [PosRef](../01-kinematics-status/PosRef.md) 运行单次周期。假设轴 A 已电机使能且不在运动中。

```text
; --- 1) 将凸轮曲线点加载到 GenData ---
AGenData[1]=0
AGenData[2]=2500
AGenData[3]=5000
AGenData[4]=2500
AGenData[5]=0

; --- 2) 将凸轮曲线 1 绑定到已加载的索引 ---
AECAMTableNum=1               ; 选择凸轮曲线 1（标量；曲线槽通过其他关键字的数组索引设置）
AECAMStart[1]=1               ; 曲线的第一个 GenData 索引
AECAMEnd[1]=5                 ; 曲线的最后一个 GenData 索引
AECAMStartCyc[1]=1            ; 重复段起始
AECAMEndCyc[1]=5              ; 重复段结束
AECAMGap[1]=1000              ; 相邻表索引间的主变量步进
AECAMCycles[1]=1              ; 运行一次周期
AECAMMaster[1]=...            ; 指向轴 B 的 PosRef 的复杂 CAN 编码
AECAMMasterIni[1]=0           ; Begin 时的凸轮对齐（参见 ECAMMasterIni）

; --- 3) 在轴 A 上启动 ECAM 运动 ---
AMotionMode=7                 ; 7 = ECAM
ABegin                        ; 控制器锁存表格后开始跟随主变量

; --- 4) 观察从动件 ---
AECAMCycCount[1]              ; 曲线 1 的当前周期索引（1..ECAMCycles）
APosRef                       ; 由凸轮查找表整形的从动件参考
```

如果曲线 1 的索引不满足 `ECAMStart <= ECAMStartCyc < ECAMEndCyc <= ECAMEnd`，或 `ECAMStart`、`ECAMEnd`、`ECAMStartCyc`、`ECAMEndCyc`、`ECAMGap`、`ECAMCycles` 中任意一个为 0，或 `ECAMMaster` 未指向有效变量，则 `Begin` 将被拒绝。

## 另请参阅

- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — 所选表格的曲线边界
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — 曲线内重复段边界
- [ECAMGap](ECAMGap.md) / [ECAMCycles](ECAMCycles.md) — 所选表格的主值间距和重复次数
- [ECAMMaster](ECAMMaster.md) / [ECAMMasterIni](ECAMMasterIni.md) — 主变量选择和初始对齐
- [ECAMCycCount](ECAMCycCount.md) — 活动曲线的当前周期索引
- [GenData](../../20-arrays/GenData.md) — 存储凸轮曲线点的数组
- [StopECAM](StopECAM.md) — 在保留压缩范围的同时退出 ECAM 运动
- [运动模式——电子凸轮（ECAM）](00-overview.md) — ECAM 运动概述
