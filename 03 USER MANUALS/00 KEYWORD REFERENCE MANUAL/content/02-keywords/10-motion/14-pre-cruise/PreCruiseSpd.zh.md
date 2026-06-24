---
keyword: PreCruiseSpd
summary: 正弦点到点运动预巡航阶段所保持的速度（用户单位）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 843
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PreCruiseSpd

正弦点到点运动预巡航阶段所保持的速度（用户单位）。

该关键字从 **v5（仅限 central-i）** 起可用。

## 概述

`PreCruiseSpd` 是轴在**预巡航阶段**的运行速度——即正弦点到点运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 20` 和 `= 21`）较快的起始段速度。轴完成预巡航行程（至 [PreCruAbsTrgt](PreCruAbsTrgt.md) 或 [PreCruRelTrgt](PreCruRelTrgt.md) 设定的目标点）后，降至普通巡航速度 [Speed](../03-kinematics-configuration/Speed.md) 完成剩余行程。有关分段概念，请参阅[预巡航概述](00-overview.md)。

该值始终为零或正数；运动方向由目标点决定，而非此关键字的符号。

## 工作原理

仅当 `PreCruiseSpd` **大于**巡航速度 [Speed](../03-kinematics-configuration/Speed.md) **且**定义了预巡航行程时，才会插入预巡航阶段。原理如下：

- 若 `PreCruiseSpd` &gt; `Speed`，运动以较快速度执行起始行程，然后**降**至巡航速度完成剩余段——先加速至预巡航速度，保持，降至巡航速度，保持巡航速度，再减速至目标点。
- 若 `PreCruiseSpd` **小于或等于** `Speed`（包括默认值 `0`），则无需先运行较快阶段，预巡航速度被有效截限，运动退化为以巡航速度运行的普通正弦点到点曲线。

各阶段的加速度、减速度和急动整形与普通正弦点到点运动相同，均使用 [Accel](../03-kinematics-configuration/Accel.md)、[Decel](../03-kinematics-configuration/Decel.md) 及急动设置。`Begin` 时，控制器检查预巡航行程是否足以从静止加速至巡航速度；若不足，则拒绝运动（预巡航行程不足，[指令错误代码](../../../04-error-codes/instruction-error-codes.md) 384）。同时检查预巡航目标之后的剩余行程是否足以从巡航速度减速至静止；若不足，则拒绝运动（制动行程不足，错误 385）。

## 示例

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed
APreCruiseSpd=800000   ; faster pre-cruise speed (> Speed, so a pre-cruise stage runs)
APreCruRelTrgt=200000  ; pre-cruise stroke
ARelTrgt=500000        ; total move distance
ABegin                 ; start the move
APreCruiseSpd          ; read back the pre-cruise speed
```

在已配置的轴上禁用预巡航阶段，将预巡航速度设置为不高于巡航速度即可：

```text
APreCruiseSpd=0        ; no pre-cruise; plain sine point-to-point at Speed
```

## 另请参阅

- [Speed](../03-kinematics-configuration/Speed.md) — 预巡航阶段结束后使用的巡航速度
- [PreCruAbsTrgt](PreCruAbsTrgt.md) / [PreCruRelTrgt](PreCruRelTrgt.md) — 预巡航阶段的终点
- [预巡航概述](00-overview.md) — 各阶段的组合方式
- [MotionMode](../02-motion-configuration/MotionMode.md) — 模式 20 和 21 选择正弦点到点运动
- [Begin](../04-motion-command/Begin.md) — 校验并启动运动
