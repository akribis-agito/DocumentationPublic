---
keyword: CommitMotion
summary: 提交对正在运行的正弦点到点运动的暂存式实时更改的命令。
availability:
  standalone: []
  central-i:
  - v5
can_code: 844
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# CommitMotion

提交对正在运行的正弦点到点运动的暂存式实时更改的命令。

## 概述

`CommitMotion` 在一次正弦点到点运动**已经处于运行中**时对其应用更改，而无需停止并重新发出该运动。你在该轴仍处于运动中时暂存新的运动参数，然后调用 `CommitMotion` 请求控制器重新计算曲线并无缝过渡到新目标。它是一个轴相关的命令函数，不携带任何值。

它仅在正弦点到点模式（[MotionMode](../02-motion-configuration/MotionMode.md) = 20，正弦 PTP；以及 21，正弦 PTP repetitive）下且该轴处于运动中时才有意义。在任何其他模式下，或当该轴不处于运动中时，该命令会被拒绝。

可用于 central-i（v5）。

## 工作原理

当发出 `CommitMotion` 时，控制器将暂存的更改交给规划器，并等待其判定该更改能否在运动的当前点上被应用：

1. **资格检查。** 除非该轴处于运动中（[MotionStat](../05-motion-status/MotionStat.md) bit 0 被置位）**且**处于正弦点到点模式（[MotionMode](../02-motion-configuration/MotionMode.md) = 20 或 21），否则该命令会被立即拒绝。否则它会返回“必须为有效的运动模式”错误。
2. **规划器评估。** 规划器检查正在运行的运动，要么接受该更改（剩余的运动量足以干净地重新设定目标），要么拒绝它（例如运动距离结束太近，来不及重新计算）。每个握手步骤都有一秒超时；超时会被报告为错误。
3. **重新计算与过渡。** 如果被接受，则计算新的正弦曲线，规划器实时过渡到该曲线。控制器可以**在实际曲线过渡之前确认本次提交**——该确认告知你更改已被接受，并将在运动中的适当点上被应用，而不必等待过渡本身完成。这使提交保持响应迅速，并让重复运动得以不间断地继续。

### 重新计算窗口

新曲线并非瞬时计算完成；控制器为后台重新计算保留一个**固定的 16 个控制环周期的窗口**（在默认控制速率下为 1&nbsp;ms），步骤 2 中的接受/拒绝判定即针对该固定窗口做出。由于该窗口是一个常量，因此它**与运动长度无关**——只有该窗口前方剩余多少正在运行的运动才有影响。由此会产生两种不同的错误：

- **窗口放不下（错误 387）。** 在初始检查时即提前抛出，因为运动原本会结束之前所剩的时间短于该 16 周期窗口，所以即便重新计算立即开始也无法及时完成。对于重复运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 21），剩余时间预算还包含重复间隔停留（[RptWait](../02-motion-configuration/RptWait.md)），因此在一次重复中较晚发出的提交，只要后面跟随足够的停留时间，仍然可以放得下。
- **重新计算未在窗口内完成（错误 388）。** 当 16 周期倒计时归零而后台重新计算尚未完成时抛出。在这种情况下，本次提交被放弃，原始运动保持不变继续进行。

387 和 388 都适用于正弦 PTP（模式 20）和正弦 PTP repetitive（模式 21）。

如果任何步骤失败或超时，`CommitMotion` 会返回一个错误，运动保持其原始曲线不变继续进行。

## 示例

在不停止的情况下为正在运行的正弦 PTP 运动重新设定目标：

```text
AMotionMode=20       ; sine point-to-point
AAbsTrgt=100000      ; initial target
ABegin               ; start the sine PTP move
                     ; ... while it is running, stage a new target ...
AAbsTrgt=150000      ; new target
ACommitMotion        ; apply the new target on the fly; OK = accepted, error = rejected/timed out
```

### 边界情况

- **不处于运动中** — 拒绝；没有正在运行的运动可供提交更改。
- **错误的运动模式** — 除非激活模式为正弦 PTP（20）或正弦 PTP repetitive（21），否则拒绝。
- **运动中太晚** — 当剩余的运动量不足以重新计算并过渡时，规划器可能会拒绝该更改（错误 387，16 周期窗口在剩余时间内放不下）；原始运动保持不变完成。
- **重新计算超出窗口** — 如果后台重新计算未在 16 周期窗口内完成，则放弃本次提交（错误 388），原始运动保持不变继续进行。
- **超时** — 如果规划器在任何握手步骤中约一秒内未响应，该命令返回错误。
- **只读 / 函数** — `CommitMotion` 是一个命令（发出它以触发它）；它不携带任何要写入的值。
- **平台** — 仅 v5 central-i。

## 另请参阅

- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择本命令所操作的正弦点到点模式（20 / 21）
- [Begin](Begin.md) — 启动 `CommitMotion` 随后重新设定目标的运动
- [MotionStat](../05-motion-status/MotionStat.md) — 该命令被接受所必须置位的运动中位
- [RptWait](../02-motion-configuration/RptWait.md) — 重复间隔停留，为重复（模式 21）运动延长提交预算
- [Stop](Stop.md) — 受控停止，当更改无法实时提交时的替代方案
