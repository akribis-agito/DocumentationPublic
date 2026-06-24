---
keyword: RecTrigsMode
summary: 为每个示波器选择并行（逻辑）或串行触发检测模式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 564
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigsMode

为每个示波器选择并行（逻辑）或串行触发检测模式。

## 概述

`RecTrigsMode` 定义触发检测模式，每个示波器最多支持 3 个触发器。在并行模式下，触发器通过 [RecTrigsLogic](RecTrigsLogic.md) 进行逻辑组合；在串行模式下，触发器必须按顺序依次发生。每个数组索引选择一个示波器。

| 索引 | 描述                   |
|-------|------------------------------|
| 1     | 第一示波器                   |
| 2     | 第二示波器（如适用）         |

## 工作原理

各值定义如下所示。请参阅[数据记录](00-overview.md)中的流程图。

| 值 | 检测模式               |
|-------|------------------------------|
| 1     | 并行（逻辑）检测 |
| 2     | 串行检测             |

在**并行**模式下，所有已配置的触发器在每个记录采样时（即每 [RecGap](RecGap.md) 个控制器周期一次，而非每个控制器周期）进行评估，并使用 [RecTrigsLogic](RecTrigsLogic.md) 中设置的运算符组合为单一布尔表达式；一旦该组合表达式为真，记录触发器即触发。由于触发器仅在采样周期内进行检测，较大的 [RecGap](RecGap.md) 值会降低触发条件检测的时间分辨率。

在**串行**模式下，触发器必须按顺序依次触发：先是触发器 1，然后是触发器 2，再是触发器 3。示波器等待触发器 1 激活后，再等待触发器 2，依此类推；整体记录触发器仅在最后一个已定义触发器激活后才触发。在串行模式下，[RecTrigsLogic](RecTrigsLogic.md) 不起作用。

在串行触发模式（`RecTrigsMode` = 2）下，由 [RecTrigForce](RecTrigForce.md) 设置的强制触发标志将保持置位，直至下一次 [RecStart](RecStart.md)，且示波器每记录一个采样就推进串行序列中的一个触发器。因此，单次 `RecTrigForce` 将依次满足序列中所有剩余触发器，在若干记录采样内完成整个串行链，而不仅仅满足当前等待的触发器。

对于单触发器配置，仅配置触发器 1，并将未使用的触发器设置为非活动类型（请参阅 [RecTrigTyp](RecTrigTyp.md) 中的说明）。

## 示例

```text
ARecTrigsMode[1]=1   ; 第一示波器使用并行（逻辑）检测
ARecTrigsMode[1]=2   ; 第一示波器使用串行检测
```

## 另请参阅

- [RecTrigsLogic](RecTrigsLogic.md) — 并行模式下连接触发器的逻辑运算符
- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
