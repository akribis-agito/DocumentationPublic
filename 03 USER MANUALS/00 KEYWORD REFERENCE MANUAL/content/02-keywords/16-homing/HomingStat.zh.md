---
keyword: HomingStat
summary: 只读回零过程状态，包含步骤编号及错误码。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 342
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# HomingStat

只读回零过程状态，包含步骤编号及错误码。

## 概述

`HomingStat` 报告由 [HomingOn](HomingOn.md) 启动的回零过程的实时状态。回零运行期间，其值为当前正在处理的步骤编号；完成时报告成功（`100`）或描述过程中止原因的负错误码。当某回零步骤失败时，过程中止，`HomingOn` 被清除，`HomingStat` 被设为以下对应错误码。

读取 `HomingStat` 可等待回零完成并诊断失败原因。其值由 [HomingDef](HomingDef.md) 中的步骤定义驱动。过程激活期间，`HomingStat` 与 [HomingStep](HomingStep.md) 的值相同——均为当前步骤编号；两者仅在结束时有所不同：`HomingStat` 切换为 `100` 或负错误码，而 `HomingStep` 保留已到达的步骤编号。

## 工作原理

每个控制周期，回零引擎在执行步骤前将当前步骤编号写入 `HomingStat`。若步骤正常完成，引擎推进，下一步骤的编号随即出现。若步骤检测到错误条件，则将 [HomingOn](HomingOn.md) 清零并以对应条件的负码覆盖 `HomingStat`（见下表）。"结束回零"步骤将 `HomingStat` 设为 `100`。

各步骤的错误检查包括：步骤开始时轴意外处于运动中（`-6`）；步骤执行过程中电机被禁用，例如由故障触发（`-3`）；步骤超时（`-2`）；运动的结束原因与步骤要求不符（`-4`）；序列在没有"结束回零"指令的情况下运行至最后一步（`-7`）；以及以下列出的几个步骤特定条件。

## 状态值

| HomingStat | 说明 |
|----|-----|
| 0 | 上电或复位后尚未执行回零。 |
| 正值（非 100） | 回零进行中。该值为当前正在处理的步骤编号。 |
| -1 | 保留。当前固件不报告此通用"HomingDef 参数错误"中止码；无效步骤改由以下步骤特定中止处理（例如无法识别的步骤指令报告 `-5`）。 |
| -2 | 因某回零步骤超时中止（步骤的"最长时间"参数已耗尽）。 |
| -3 | 因电机意外失能中止。步骤执行过程中轴被禁用（例如由 ConFlt 中反映的故障导致），步骤无法完成。 |
| -4 | 因运动结束原因错误中止。某步骤期望特定的运动结束原因（RLS、FLS、索引、到达目标、原点变化等），但实际检测到不同的原因。 |
| -5 | 因步骤类型错误中止。序列到达某步骤，其指令值不是已识别的类型。 |
| -6 | 因新步骤开始时轴处于运动中而中止。 |
| -7 | 因步骤过多中止——序列在没有"结束回零"指令的情况下到达最后一个可能的步骤。 |
| -8 | 因意外限位中止。仅与"检查轴是否已离开限位"步骤相关。 |
| -9 | 因 SetPosition 的条件不满足而中止。与"设置位置"和两个"运动至机械硬限位"步骤相关。 |
| -10 | 因"写入 MotionMode"步骤请求了不允许的运动模式而中止。 |
| -11 | 因"写入 MapType"步骤请求了不允许的映射类型而中止。 |
| -12 | 因"使能（或禁用）电机"步骤运行时相位初始化（换相初始化）尚未完成而中止（无论请求为使能还是禁用均执行此检查：ComtStatus 必须已超过进行中状态）。 |
| 100 | 回零过程成功完成。 |

`-3` 错误反映步骤执行过程中的轴故障；原因由 [ConFlt](../07-status-and-faults/ConFlt.md) 报告。`-9` 错误指 [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) 的前置条件。

## 示例

```text
AHomingStat         ; 0 = 未回零，>0 = 步骤进行中，100 = 完成，<0 = 错误
```

## 另请参阅

- [HomingOn](HomingOn.md) — 启动本状态跟踪的回零过程
- [HomingStep](HomingStep.md) — 当前回零步骤编号
- [HomingDef](HomingDef.md) — 定义产生这些状态值的步骤
- [ConFlt](../07-status-and-faults/ConFlt.md) — `-3`（电机失能）中止背后的控制器故障
- [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) — `-9` 中止背后的前置条件
