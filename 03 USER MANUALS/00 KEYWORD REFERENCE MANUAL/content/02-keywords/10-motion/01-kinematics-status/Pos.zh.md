---
keyword: Pos
summary: 以用户单位表示的主位置反馈；位置环反馈信号。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 2
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Pos

以用户单位表示的主位置反馈；位置环反馈信号。

## 概述

`Pos` 是主位置反馈，且在正常（非龙门）运行下是**位置环反馈信号**——因此它是位置误差 [PosErr](PosErr.md) 的依据（`PosErr = PosRef − Pos`）。它以用户单位（由 [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 设置）报告；内部流水线（映射、取模）以主编码器计数运行。

`Pos` 为只读，但并不简单等同于“编码器”。它是**反馈流水线的输出**，并由以下所述的若干机制（仿真、误差映射、取模、双环、龙门）重新整形。它在上电时复位为 `0`，并可用 [SetPosition](../03-kinematics-configuration/SetPosition.md) **预置**（不要直接写入 `Pos`）；使用绝对式编码器时，它在启动时由绝对读数初始化。

## 工作原理

### 反馈流水线

每个控制周期，`Pos` 由解码后的主编码器读数分阶段产生：

```text
main encoder ─► (decode) ─► PosBeforeMap ─► [error mapping] ─► [modulo ModRev] ─► Pos
```

[PosBeforeMap](../../04-error-mapping/PosBeforeMap.md) 保存校正**之前**的值（用于诊断）。在无误差映射且无取模时，`Pos` 等于解码后的编码器读数。

### 仿真模式

当轴运行于**仿真**（`MotorType` = simulation）时不存在物理编码器：控制器将反馈设置为等于参考值，因此 **`Pos` 精确跟随 `PosRef`**。仿真中误差映射被有意跳过，以避免与强制 `PosRef = Pos` 的电机失能行为构成反馈回路。这使您可以在没有硬件的情况下空运行运动程序。

### 电机失能行为

电机失能时，控制器强制 `PosRef = Pos`，因此参考值跟踪实时反馈。这保证了电机使能瞬间位置误差为零，防止跳变。

### 误差映射

当编码器误差映射处于激活状态（[MapType](../../04-error-mapping/MapType.md) = 1D/2D/3D）时，`Pos = PosBeforeMap + correction`，其中修正值由映射表插值得到。修正值会**渐进接入/退出**，使接入或更改映射不会产生位置阶跃。

### 取模（连续旋转）— ModRev

如果 [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0，`Pos` 被保持在 `[0, ModRev)` 范围内。当读数将跨越边界（正向时 `Pos ≥ ModRev`，或负向时 `Pos < 0`）时，控制器从 `Pos` 中减去/加上 `ModRev`，**并将整个参考坐标系移动相同的量**——`PosRef`、整形/滤波后的参考值、[AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md)、`PDPos` 以及齿轮主轴位置一起移动——因此跟随误差在环绕期间得以保持，轴可以连续旋转。仅当加加速度缓冲区中没有环绕前的值时才执行环绕，并且它假定每个控制周期的运动不超过半个模数距离。对于步进开环电机，环绕边沿在参考值而非 `Pos` 上检测（无闭环反馈可供比较）。最短路径目标设定另请参阅 [ModShort](../../03-encoder/04-modulo-mode/ModShort.md)。

### 边界情形

- **电机失能：** `Pos` 继续跟踪编码器读数（因此外部推动会移动 `Pos`）；控制器强制 `PosRef = Pos`，使 [PosErr](PosErr.md) 保持为零。
- **仿真模式（`MotorType` = 5）：** `Pos` 被强制等于 `PosRef`（无物理编码器）。
- **激活故障：** 编码器流水线持续更新 `Pos`；控制环被关闭，但反馈仍然有效，可用于检查停止位置。
- **越界写入：** `Pos` 为只读——写入尝试被参数系统拒绝。请使用 [SetPosition](../03-kinematics-configuration/SetPosition.md) 进行预置。
- **加加速度缓冲移动期间的 ModRev 环绕：** 仅当加加速度缓冲区中没有环绕前的值时才执行环绕，因此在环绕边沿附近的往返运动可能会暂时跳过一次环绕；这是无害的。
- **双环：** 在伪双环中，`Pos` 是缩放后的 [AuxPos](AuxPos.md)；在真双环和龙门中，位置环使用 `Pos`/[GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md)，而 `Pos` 仍读取主编码器。

### 双环与龙门

`Pos` 所代表的含义还取决于环路配置：

| 配置 | `Pos` 定义 |
|---------------|------------------|
| 默认、双环或龙门（除伪双环外的所有情形） | 解码后的主编码器读数（映射/取模之后）。 |
| 伪双环（非龙门） | 辅助编码器，缩放至主编码器单位：$$\text{Pos} = \text{AuxPos} \cdot \frac{\text{DualLoopFact}}{65536}$$ |

在龙门模式下，位置环使用 [GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md)（共模位置）而非单轴 `Pos`。

## 版本间变更

| | v4（独立与 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位整数（`long`） | **64 位整数（`long long`）** |
| 范围 | ±2,147,483,647 | ±2,251,799,813,685,247（2⁵¹−1） |

在 **v5** 中，位置流水线改为**64 位**计算，因此 `Pos` 是一个范围大得多的 64 位值（上限为 2⁵¹−1，因为 PCSuite 以 `double` 记录数据），允许在不环绕的情况下累积远多的行程。**v5 仅适用于 central-i**——独立产品不在 v5 上受支持，因此在独立产品上 `Pos` 仍为 v4 的 32 位值。

## 示例

```text
APos                ; read axis A's main position feedback
```

## 另请参阅

- [PosRef](PosRef.md) — 位置参考；[PosErr](PosErr.md) — `PosRef − Pos`
- [PosBeforeMap](../../04-error-mapping/PosBeforeMap.md) — 误差映射校正之前的反馈
- [AuxPos](AuxPos.md) — 辅助反馈（用于伪双环）
- [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) / [ModShort](../../03-encoder/04-modulo-mode/ModShort.md) — 取模（连续旋转）模式
- [MapType](../../04-error-mapping/MapType.md) — 编码器误差映射
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — 预置反馈
- [GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md) — 龙门共模位置
- [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 用户单位缩放
