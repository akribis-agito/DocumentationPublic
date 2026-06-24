---
keyword: RelTrgt
summary: 下一次点到点运动的相对目标距离（用户单位）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 135
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RelTrgt

下一次点到点运动的相对目标距离（用户单位）。

## 概述

`RelTrgt` 请求相对于*当前位置参考*的运动。它是 [AbsTrgt](AbsTrgt.md) 的相对对应量：在 [Begin](../04-motion-command/Begin.md) 时，非零的 `RelTrgt` 被转换为绝对目标，运动随后与绝对 PTP 运动完全相同。该参数不保存至闪存，可随时修改。

![AbsTrgt 与 RelTrgt 几何关系](abstrgt-vs-reltrgt.svg)

## 工作原理

### RelTrgt 在 Begin 时被消耗，而非保持

规划器从不直接读取 `RelTrgt`。`Begin` 运行时，控制器执行：

```text
if (RelTrgt != 0)
    AbsTrgt = PosRef + RelTrgt
```

即将相对距离加到**参考位置 [PosRef](../01-kinematics-status/PosRef.md)**（而非反馈 [Pos](../01-kinematics-status/Pos.md)）上，形成新的 [AbsTrgt](AbsTrgt.md)。此转换适用于所有接受相对目标的模式：

- PTP `Begin`
- 重复 PTP `Begin`
- 矢量运动 `Begin`（每个成员轴）
- 切换至位置模式时的快速 begin

此设计有两个推论：

- **`RelTrgt = 0` 表示"使用 `AbsTrgt`"。** 零相对目标意味着保持 `AbsTrgt` 不变并运动至绝对目标。若要命令一个相对移动量为零的运动，不能使用 `RelTrgt = 0`，否则轴将驶向 `AbsTrgt` 当前值。请注意，写入 [AbsTrgt](AbsTrgt.md) 会自动将 `RelTrgt` 重置为 0，因此设置绝对目标始终会取消任何待处理的相对目标。
- **以参考为基准，可重复执行。** 由于基准为 `PosRef`，再次发出相同的 `RelTrgt` 将从上次运动结束处步进相同距离，不会累积跟随误差。

转换后，得到的 `AbsTrgt` 将与绝对运动完全相同地进行软件限位和限位开关范围检查（参见 [AbsTrgt](AbsTrgt.md) — *Begin 时的验证*）；因此超出范围的相对目标会导致 `Begin` 被拒绝，而非截断处理。

## 示例

```text
ARelTrgt=5000        ; next Begin moves +5000 user units from the reference
ABegin               ; perform the relative move
ARelTrgt=-5000       ; next Begin moves 5000 user units in the negative direction
ARelTrgt             ; read the current relative target
```

### 边界情况

- **电机关闭：** 值保持不变；不执行验证。
- **超范围写入：** 参数系统钳位至数据类型范围；验证在 `Begin` 时转换为 `AbsTrgt` 后进行。
- **仿真模式（`MotorType` = 5）：** 无变化。
- **ModRev 环绕：** `Begin` 时的转换使用当前 `PosRef`（若取模有效则已在 `[0, ModRev)` 内）；得到的 `AbsTrgt` 可能超过 `ModRev`，但随运动进行，环绕逻辑会将所有内容一起偏移。
- **有效故障：** 值被保留。
- **其他运动模式：** 转换仅在使用 `AbsTrgt` 的模式（PTP、重复 PTP、矢量）中执行。其他模式忽略 `RelTrgt`。
- **`RelTrgt = 0`：** 下一次 `Begin` 原样使用 `AbsTrgt`（将 0 视为"使用绝对目标"）。若要明确原地不动，请改为设置 `AbsTrgt = PosRef`。
- **运动中实时修改：** 行为取决于 [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md)。`PTPKeepMoving = 0` 时，新值等待下一次 `Begin`，当前运动继续驶向原目标。`PTPKeepMoving = 1` 时，运动中写入 `RelTrgt` 会立即将其加到有效 [AbsTrgt](AbsTrgt.md) 上（`AbsTrgt = AbsTrgt + RelTrgt`），实时重新定向当前运动。

## 版本间变更

在 **v5（central-i）** 中，`RelTrgt` 为 64 位整数，范围如 frontmatter 所示，与 64 位位置流水线匹配；转换为 `AbsTrgt` 的方式不变。**v5 仅适用于 central-i**，因此在独立型设备上 `RelTrgt` 仍为 v4 的 32 位值。

## 另请参阅

- [AbsTrgt](AbsTrgt.md) — 相对距离转换成的绝对目标
- [Targets](Targets.md) — 用户程序使用的闪存存储目标数组
- [Begin](../04-motion-command/Begin.md) — 将 `RelTrgt` 转换为 `AbsTrgt` 并启动运动
- [PosRef](../01-kinematics-status/PosRef.md) — 相对距离叠加的基准
