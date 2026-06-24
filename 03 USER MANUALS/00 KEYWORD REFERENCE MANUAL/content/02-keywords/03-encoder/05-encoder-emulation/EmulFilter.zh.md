---
keyword: EmulFilter
summary: 应用于编码器仿真输出信号的数字滤波器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 403
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EmulFilter

应用于编码器仿真输出信号的数字滤波器。

## 概述

`EmulFilter` 设置应用于编码器仿真输出的数字滤波器。值越大，滤波越强，使仿真正交边沿更平滑。它与 [EmulRat](EmulRat.md)（输出比率）和 [EmulIndexType](EmulIndexType.md)（索引脉冲类型）配合使用，以配置仿真编码器接口。范围为 0 到 15（4 位字段），默认值为 3。它是轴相关参数，保存至闪存，并可在电机使能或运动中时更改。

## 工作原理

`EmulFilter` 和 [EmulIndexType](EmulIndexType.md) 共用一个每轴仿真设置寄存器。该寄存器的位组织如下：

| 位 | 字段 | 来源 |
|---|---|---|
| 0–3 | 输出滤波等级（0–15） | `EmulFilter` |
| 4–5 | 索引脉冲类型 | [EmulIndexType](EmulIndexType.md) |

`EmulFilter` 占用低 4 位，因此值被掩码至 0–15。写入任一关键字都会重新打包并重写整个寄存器，因此两项设置始终同时生效。

## 示例

```text
AEmulFilter=3        ; default filtering level
AEmulFilter=0        ; minimum filtering
AEmulFilter          ; query the configured filter level
```

## 另请参阅

- [EmulRat](EmulRat.md) —— 反馈计数与仿真正交输出之间的比率
- [EmulIndexType](EmulIndexType.md) —— 仿真输出上的索引脉冲类型
