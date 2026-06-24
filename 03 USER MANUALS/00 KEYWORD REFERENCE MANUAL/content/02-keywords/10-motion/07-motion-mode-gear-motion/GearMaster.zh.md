---
keyword: GearMaster
summary: 复合 CAN 代码，用于选择电子齿轮运动的主变量。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 489
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GearMaster

复合 CAN 代码，用于选择电子齿轮运动的主变量。

## 概述

`GearMaster` 选择轴在电子齿轮运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 5` 直接或 `= 6` 间接）中所跟随的变量。它不是固定的枚举值，而是一个[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)——任意关键字（包括其轴字母和数组索引）的编码引用——因此主变量可以是另一轴的位置、编码器、计数器、模拟量输入等。每个控制器周期，控制器读取该变量，将其变化量按 [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) 缩放，并将结果累加到 [MasterPos](MasterPos.md) 中，从而驱动从动件的位置参考 [PosRef](../01-kinematics-status/PosRef.md)。

**特殊情况（自动选择）：** 当从动件以 1:1 齿轮比跟随（在 v5/central-i 上 [MasterFact](MasterFact.md) 和 [MasterFactDen](MasterFactDen.md) 化简为 1；在 v4 上 [MasterFact](MasterFact.md) `= 65536`），无滤波器（[MasterFilt](MasterFilt.md) `= 64`），处于直接电子齿轮运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 5`），且 `GearMaster` 指向另一轴的 [PosRef](../01-kinematics-status/PosRef.md) 时，控制器将直接跟随该轴的全分辨率（亚计数）位置参考，而非以计数分辨率重新读取。这使得 1:1 无滤波器的 `PosRef` 从动件完全精确，没有每计数量化误差。任何其他主变量、非单位比值或任何滤波均会恢复为通过 [MasterPos](MasterPos.md) 的标准计数分辨率累加。

## 工作原理

### 主变量的解析

写入 `GearMaster` 时，复合 CAN 代码标识主变量（其关键字、轴及数组索引），控制器解析指向它的指针。此后控制器每周期读取该变量，无需重新解析代码。同时，控制器将变量的当前值捕获为"前一个"值，使第一个周期产生零变化量。

每当写入 [GearMaster](GearMaster.md)、[MasterFact](MasterFact.md)、[MasterFilt](MasterFilt.md) 或 [MotionMode](../02-motion-configuration/MotionMode.md) 时（在 v5/central-i 上还包括 [MasterFactDen](MasterFactDen.md)），主指针将（重新）解析，主变量当前值将（重新）捕获为"前一个"值——不仅限于写入 `GearMaster` 本身时。由于在每次上述写入时均刷新前一个值，在配置轴期间更改比值或滤波器不会向 [MasterPos](MasterPos.md) 注入虚假的单周期跳变。

写入 `GearMaster` 在接受前会经过验证，被拒绝的写入将保留之前的主变量选择。以下情况将以明确的指令错误拒绝写入：

- CAN 代码超出范围，
- 轴字母超出范围，
- 数组索引对目标关键字不正确（为非数组关键字提供了索引，或为数组关键字省略了索引——数组关键字需要 1 或更大的索引），或
- 目标不是参数（例如，指定的是函数而非可设置的关键字）。

![从 GearMaster 到 PosRef 的电子齿轮运动信号路径](gear-signal-path.svg)

### 另存在一种独立的"直接从轴"运动模式

`GearMaster`、`MasterFact`/`MasterFactDen`、`MasterFilt` 和 `MasterPos` 均属于电子齿轮运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 5` 和 `= 6`）。控制器还实现了一种独立的、更窄的运动模式——直接从轴（[MotionMode](../02-motion-configuration/MotionMode.md) `= 10`，参见 [MotionMode10](MotionMode10.md)）——该模式直接基于另一轴的参考构建从动件参考，无需经过 `GearMaster`、`MasterPos` 或 `MasterFilt`。它与电子齿轮运动机制不同，且不使用本关键字。

### 与其他齿轮关键字的关系

- 经缩放的累加主变量变化量由 [MasterPos](MasterPos.md) 报告。
- 如果所选主变量本身存在环绕（其 `ModRev` 非零——例如旋转 [Pos](../01-kinematics-status/Pos.md) 或另一轴的 [PosRef](../01-kinematics-status/PosRef.md)），则必须将 [MasterModRev](MasterModRev.md) 设置为该环绕值，以保持累加的连续性。

### 轨迹计算（v5/central-i）

在 v5（central-i）上，向 [MasterPos](MasterPos.md) 的每周期累加精确且无漂移。每个周期，主变量变化量 Δ（当前主变量值与捕获的前一个值之差）被 [MasterFactDen](MasterFactDen.md) 除，得到整数商和余数。整数部分使定点累加器按商 × [MasterFact](MasterFact.md) 推进；余数被加入保留的小数累加器中，该累加器始终小于 [MasterFactDen](MasterFactDen.md)，产生的整数倍折回整数累加器。由于保留的小数始终进位而非四舍五入，不存在累积舍入漂移，[MasterPos](MasterPos.md) 等于整数累加量加上进位小数 × [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md)。应用前，比值会化简为正分母的最简分数形式（参见 [MasterFactDen](MasterFactDen.md)）。

`GearMaster` 可在电机使能时修改，但**不能**在轴运动时修改：请仅在轴未处于电子齿轮运动状态时更改主变量选择。

## 示例

```text
AGearMaster=...      ; 设置为所需主变量的复合 CAN 代码
AGearMaster          ; 读取当前主变量复合 CAN 代码
```

该值为复合 CAN 代码；请按照[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)规则，根据要跟随的关键字、轴和索引进行构建。

### 操作示例：在主编码器上运行电子齿轮

将轴 A 配置为使用直接电子齿轮运动以 1:1 跟随某主变量。以下示例使用单位分子和直通滤波器，但任意比值和任意滤波器系数均有效；非单位比值在 v4 上仅使用 `MasterFact`，在 v5（central-i）上使用 `MasterFact / MasterFactDen`。假设两轴均处于电机使能但未运动状态；按照[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)规则编码主变量选择。

```text
; --- 1) 在从动件（轴 A）上选择主变量 ---
AGearMaster[1]=...   ; 标识主变量的复合 CAN 代码

; --- 2) 设置齿轮比分子（v5 上还需设置分母）---
AMasterFact[1]=65536    ; 65536 = 单位分子（1:1）
AMasterFactDen[1]=65536 ; 仅 v5 (central-i) -- 精确有理分母，默认 65536
AMasterFilt[1]=64       ; 64 = 直通（无平滑）；减小以增加平滑

; --- 3) （可选）如果主变量存在环绕，告知控制器 ---
AMasterModRev[1]=0      ; 若主变量存在环绕，设置为主变量的环绕值

; --- 4) 使能直接电子齿轮运动 ---
AMotionMode[1]=5        ; 5 = 直接齿轮，6 = 间接齿轮
ABegin                  ; 在启动时锁存 MasterPos；从动件开始跟随主变量增量

; --- 5) 在主变量运动时观察从动件 ---
AMasterPos[1]           ; 自 Begin 以来经缩放的累加主位置
APosRef[1]              ; 从动件参考——应镜像滤波后的 MasterPos
```

从动件在 `Stop`、`Abort` 或电机被禁用时退出电子齿轮运动。若要更改主变量选择，请先退出电子齿轮运动；轴在运动中时，`GearMaster` 的写入将被拒绝。

## 参见

- [MasterPos](MasterPos.md) — 经累加、缩放的主位置
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — 齿轮比分子 / 分母
- [MasterFilt](MasterFilt.md) — 齿轮参考的低通滤波器（直接模式）
- [MasterModRev](MasterModRev.md) — 主变量的取模除数
- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择电子齿轮运动（`= 5` 或 `6`）
- [MotionMode10](MotionMode10.md) — 独立的直接从轴运动模式（`MotionMode = 10`），不使用 `GearMaster`
- [复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md) — 主变量的编码方式
