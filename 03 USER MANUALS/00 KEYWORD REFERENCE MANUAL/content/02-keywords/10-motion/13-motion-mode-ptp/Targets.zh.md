---
keyword: Targets
summary: 多目标点到点运动的目标位置数组（用户单位）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 376
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Targets

闪存存储的目标位置数组（用户单位），可供用户程序使用。

## 概述

`Targets` 是一个小型、闪存存储、轴作用域的位置值数组，以用户单位表示。其用途是为[用户程序](../../../01-keyword-usage-and-syntax/syntax.md)提供便捷的持久化存储，存放一组命名目的地，程序可读取后加载至 [AbsTrgt](AbsTrgt.md)（或转换为 [RelTrgt](RelTrgt.md)），再在每次 [Begin](../04-motion-command/Begin.md) 前使用。该参数可读写并保存至闪存，因此目的地在重新上电后仍会保留。

## 工作原理

`Targets` 是一个**存储数组，而非自动运动队列。** 它是闪存存储参数，但没有任何运动引擎、规划器或解释器逻辑会读取它——它仅是持久化存储。轨迹规划器始终驱向单一目标 [AbsTrgt](AbsTrgt.md)；若要依次经过多个位置，需在运动间自行将 `Targets[n]` 读入 `AbsTrgt`。

### 数组大小与索引

该数组包含**三个可用条目**。与所有关键字数组一样，索引 `0` 保留，指令索引从 `1` 开始，有效索引为 `Targets[1]`、`Targets[2]`、`Targets[3]`。每个条目与 `AbsTrgt` 具有相同的完整位置范围。

## 示例

```text
ATargets[1]=10000    ; store destination 1 in flash
ATargets[2]=20000    ; store destination 2
ATargets[3]=30000    ; store destination 3
AAbsTrgt=10000       ; later: load a stored destination into the active target
ABegin               ; and move there
```

若要在用户程序中依次经过所有三个目标，则依次将每个条目复制至 `AbsTrgt` 并执行 `Begin`，在运动间等待到位信号。

### 边界情况

- **电机关闭：** 值保存在闪存中；读写不受影响。
- **超范围写入：** 超出数据类型范围（v4 为 ±2³¹−1，v5 为 ±2⁵¹−1）的值将被拒绝并报错，存储条目保持不变；不进行钳位处理。
- **索引 `[0]` / `[4]`：** 该关键字有 3 个可用条目 `[1]` … `[3]`，超出此范围的索引将返回错误。
- **仿真模式（`MotorType` = 5）：** 无变化——`Targets` 为纯存储。
- **ModRev 环绕：** 值以原始用户单位存储；将超出 `[0, ModRev)` 的值加载至 `AbsTrgt` 是有效的，但控制器的环绕行为会在运动过程中调整参考帧。
- **有效故障：** 值被保留（闪存存储）。
- **其他运动模式：** 该数组与模式无关。预期用途为 PTP，但用户可将条目复制至任何有符号整数位置关键字。
- **运动中实时修改：** 允许；修改仅作用于存储条目，不影响当前运动（因为规划器不读取 `Targets`）。

## 版本间变更

在 **v5（central-i）** 中，条目为 64 位整数，范围如 frontmatter 所示，与 64 位位置流水线匹配。**v5 仅适用于 central-i**，因此在独立型设备上 `Targets` 仍为 v4 的 32 位数组。

## 另请参阅

- [AbsTrgt](AbsTrgt.md) — 存储值加载至的单一有效目标
- [RelTrgt](RelTrgt.md) — 单一相对目标距离
- [Begin](../04-motion-command/Begin.md) — 向已加载目标启动运动
