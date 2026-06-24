---
keyword: MotorReason
summary: 只读代码，报告轴上次被禁用的原因。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 498
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
  - 0
  - 4
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MotorReason

只读代码，报告轴上次被禁用的原因。

## 概述

`MotorReason` 记录轴被禁用的原因，使你能够区分故障驱动的关闭与有意的禁用命令。它是一个轴级只读代码，不会保存至闪存。每当轴被使能（[MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md)=1）时，它会复位为 `0`（无）。

当 `MotorReason` 报告控制器故障（值 `1`）时，读取 [ConFlt](ConFlt.md) 获取具体故障码，读取 [ConFltSnapVal](ConFltSnapVal.md) 快照获取捕获的系统状态。


## 工作原理

`MotorReason` 保存**上一次**禁用的原因。它在轴从使能转为禁用的时刻被设置，并在轴被使能（[MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md)=1）时复位为 `0`（无），因此在轴运行期间它读取为 `0`。

| 值 | 描述 |
|---|---|
| 0 | **无** — 未记录禁用，或轴处于使能状态。 |
| 1 | **控制器故障** — 控制器故障禁用了轴。读取 [ConFlt](ConFlt.md) 获取具体代码。 |
| 2 | **数字量输入** — 配置为禁用轴的数字量输入被激活。 |
| 3 | **用户程序 (IDE+)** — `MotorOn=0` 命令来自用户程序。 |
| 4 | **通信** — `MotorOn=0` 命令来自通信通道。 |

故障原因（`1`）专门在轴于存在 [ConFlt](ConFlt.md) 时转为禁用的情况下设置，这将故障驱动的关闭与有意的禁用命令（原因 `2`–`4`）区分开来。

注意：参数表中报告的数组默认值为 `-1`，但在正常运行中，使能时的实时值为 `0`（无），且你只会看到 `0`–`4` 之间的值。

## 示例

```text
AMotorReason        ; 1 = controller fault, 2 = digital input, 3 = user program, 4 = communication
```

## 参见

- [ConFlt](ConFlt.md) — 当 MotorReason 为 1（控制器故障）时的具体故障码
- [ConFltSnapVal](ConFltSnapVal.md) — 故障时捕获的参数快照
- [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) — 使能轴会将 MotorReason 复位为 0
- [MotionReason](../10-motion/05-motion-status/MotionReason.md) — 值 8 标记被该禁用中断的运动
