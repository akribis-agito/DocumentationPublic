---
keyword: MapType
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 320
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
summary: 选择误差映射维度（关闭、1D、2D 或 3D）。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MapType

选择误差映射维度（关闭、1D、2D 或 3D）。

## 概述

`MapType` 选择应用于轴位置反馈的误差映射修正模式。误差映射修正的是测得的反馈（[Pos](../10-motion/01-kinematics-status/Pos.md)）而非指令（[PosRef](../10-motion/01-kinematics-status/PosRef.md)），因此非零值会使用存储在 [MapTable](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) 数组中的修正值来启用位置误差补偿。有效范围为 `0` 到 `3`。

映射的几何由 [MapStartPos](MapStartPos.md)、[MapPosGap](MapPosGap.md) 和 [MapLength](MapLength.md) 定义；[MapEncoder](MapEncoder.md) 为每个维度选择编码器源；[MapStartIndex](MapStartIndex.md) 选择第一个活动表条目。未修正的位置可通过 [PosBeforeMap](PosBeforeMap.md) 获取以用于诊断。`MapType` 是轴相关的，不保存至闪存，且无法在轴运动中修改。

## 工作原理

`MapType` 在反馈流水线中每个控制周期读取一次，以选择修正分支。支持的取值为：

| `MapType` | 模式 | 查找维度 | 插值 |
|:---------:|------|-------------------|---------------|
| 0 | 关闭 | 无 —— `Pos = PosBeforeMap` | 无 |
| 1 | 1D | 仅第一编码器 | 线性（2 点） |
| 2 | 2D | 第一编码器 = 行，第二编码器 = 列 | 双线性（4 点） |
| 3 | 3D | 第一/第二/第三编码器 | 三线性（8 点） |

每个周期，控制器记录 `PosBeforeMap`（解码后的主编码器位置），然后——如果电机**不**处于仿真模式——运行所选分支以计算修正值，并构成 `Pos = PosBeforeMap + (经斜坡的修正值)`。`DeltaPos` 随后被重新计算，以使速度估计也反映修正后的位置。在**仿真**模式下完全跳过映射（`Pos = PosBeforeMap`），以避免在电机失能时形成闭环——在该情况下修正后的位置会反馈到指令位置。

### 内部类型与请求类型，以及接入/退出斜坡

写入 `MapType` **不会**突然开启或关闭修正。控制器保留一份活动类型的单独内部副本和一个 0..1 斜坡计数器：

- **接入**（将 `MapType` 由 0 写为 1/2/3）：内部类型立即被设置，斜坡计数器从 0 开始，以 [MapErrOnStep](MapErrOnStep.md) 设定的速率向 `16384` 的满刻度（在 16 kHz 基本采样率下为一秒）攀升。在达到满刻度之前，修正值按 `counter / 16384` 缩放，因此修正值（以及 [MapErrOffset](MapErrOffset.md) 分量）平滑淡入，没有位置阶跃。
- **退出**（将 `MapType` 写为 0）：用户值变为 0，但内部类型仍保持活动，修正值**向下**斜坡；只有当计数器达到 0 时，内部类型才恢复为关闭。当 [MapErrOnStep](MapErrOnStep.md) = 0 时，接入/退出转换是即时的（一个周期）。

此斜坡逻辑由 `MapType`、[MapErrOnStep](MapErrOnStep.md)、[MapErrOffset](MapErrOffset.md) 和 [MapErrOffRamp](MapErrOffRamp.md) 共享。接入也可在回零序列期间自动执行。

### 多轴映射要求源轴处于静止

映射本身无法在运动中启用（`ok_in_motion = false`），但写入 `MapType` 本身不会验证编码器选择。更严格的编码器/静止要求是单独强制执行的，即当在已映射的轴上运行**事件修正**时：第一维必须引用本轴自身的主编码器，对于 2D/3D，附加的源轴（由 [MapEncoder](MapEncoder.md) 选择）必须**电机使能且不运动**，并且必须使用其**主**编码器。

## 示例

```text
AMapType=1           ; enable 1D error mapping
AMapType=0           ; disable error mapping (ramps out per MapErrOnStep)
AMapType             ; read the active mapping mode
```

### 边界情况

- **运动进行中** —— `ok_in_motion = false`。运动期间的写入被拒绝；更改必须在轴静止时进行。
- **相位初始化完成** —— 映射在换相后的反馈路径上工作；实际上，轴必须已换相，映射才有意义。
- **仿真电机** —— 当 [MotorType](../02-motor-and-amplifier/MotorType.md) = 仿真时，映射被**完全跳过**，因为将修正后的位置反馈回仿真编码器会与位置参考形成闭环。在此情况下，无论 `MapType` 为何，`Pos = PosBeforeMap`。
- **维度错误** —— 超出 `0`–`3` 的值在参数表处被拒绝。
- **多维（`MapType` = 2 或 3）** —— 写入 `MapType` 不检查编码器选择，但在已映射的轴上运行**事件修正**时会检查：由 [MapEncoder](MapEncoder.md)`[2]`/`[3]` 引用的附加编码器轴必须电机使能、不运动，并指向**主**编码器，否则事件修正被拒绝并返回错误 `221`（其他轴未使能或运动中）或 `222`（其他轴未使用其主编码器）。
- **第一编码器约束** —— 对于事件修正，[MapEncoder](MapEncoder.md)`[1]` 必须指向本轴自身的主编码器，否则被拒绝并返回错误 `220`。事件修正还要求映射处于活动状态，否则返回错误 `219`。
- **`MapErrOnStep = 0`** —— 接入/退出是即时的；对测试有用，但会产生位置阶跃。
- **电机失能** —— 用户可见的 `MapType` 可以被写入（`ok_motor_on = true`）；斜坡计数器继续更新，因此重新使能电机时接入是平滑的。

## 另请参阅

- [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md) —— 映射所应用的修正值
- [MapEncoder](MapEncoder.md) —— 每个映射段所用的编码器源
- [MapStartIndex](MapStartIndex.md) —— 第一个活动映射段
- [PosBeforeMap](PosBeforeMap.md) —— 应用修正之前的反馈位置
- [Pos](../10-motion/01-kinematics-status/Pos.md) —— 映射所调整的修正后反馈位置
