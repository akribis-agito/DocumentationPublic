---
keyword: EmulIndexType
summary: 选择在编码器仿真输出上生成的索引脉冲类型。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 402
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EmulIndexType

选择在编码器仿真输出上生成的索引脉冲类型。

## 概述

`EmulIndexType` 选择在编码器仿真输出上生成的索引（Z）脉冲类型。值范围为 0 到 1，默认值为 0。它与 [EmulRat](EmulRat.md)（输出比率）和 [EmulFilter](EmulFilter.md)（输出滤波）配合使用，以配置仿真编码器接口。它是轴相关参数，保存至闪存，并可在电机使能或运动中时更改。

## 工作原理

`EmulIndexType` 和 [EmulFilter](EmulFilter.md) 共用一个每轴仿真设置寄存器。该寄存器的位组织如下：

| 位 | 字段 | 来源 |
|---|---|---|
| 0–3 | 输出滤波等级 | [EmulFilter](EmulFilter.md) |
| 4–5 | 索引脉冲类型 | `EmulIndexType` |

`EmulIndexType` 写入寄存器的第 4–5 位（掩码至 2 位）；向用户公开的关键字值范围为 0–1。写入任一关键字都会重新打包并重写整个寄存器，因此两项设置同时生效。该位字段选择仿真 Z 脉冲的生成方式：

| 值 | 仿真索引（Z）行为 |
|---|---|
| 0 | 直通。传入的索引脉冲不经更改，直接在仿真索引输出上发出。 |
| 1 | 重新生成并对齐。索引脉冲根据仿真 A/B 正交边沿重新导出，并在一个固定的窄区间（宽度为几个仿真边沿）内保持有效，使其边沿与仿真正交输出对齐，而非与原始传入索引对齐。 |

## 示例

```text
AEmulIndexType=0     ; default index pulse type
AEmulIndexType       ; query the configured index pulse type
```

## 另请参阅

- [EmulRat](EmulRat.md) —— 反馈计数与仿真正交输出之间的比率
- [EmulFilter](EmulFilter.md) —— 应用于仿真输出的滤波器
