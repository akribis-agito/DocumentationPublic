---
keyword: RecGap
summary: 每个示波器的降采样因子，用于设置记录频率。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 242
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
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# RecGap

每个示波器的降采样因子，用于设置记录频率。

## 概述

`RecGap` 是一个数组，定义应用于控制器周期频率的降采样因子，从而设置每个示波器的数据记录频率。值越大，记录越稀疏，对于给定的 [RecLength](RecLength.md) 可延长所捕获的时间跨度。每个数组索引对应一个示波器。

| 索引 | 说明                        |
|------|-----------------------------|
| 1    | 第一个示波器                |
| 2    | 第二个示波器（如适用）      |

## 工作原理

数据记录频率为：

$$
\text{示波器 } x \text{ 的数据记录频率}\ [\text{Hz}] = \frac{\text{控制器周期速率}\ [\text{Hz}]}{\text{RecGap}[x]}
$$

在内部，示波器维护一个减计数器，以 `RecGap` 值重载，并在每个控制器周期递减一次；仅当计数器归零时才对所有已记录通道采集一次样本，随后重载。因此 `RecGap[x]=1` 表示每个周期均记录，`RecGap[x]=10` 表示每十个周期记录一次，以此类推。`RecGap` 在 [RecStart](RecStart.md) 执行时读取一次，并在该次记录期间保持固定。

`RecGap` 与 [RecLength](RecLength.md) 共同决定总记录时长。

## 示例

```text
ARecGap[1]=1         ; 第一个示波器以完整控制器周期速率记录
ARecGap[2]=10        ; 第二个示波器以 1/10 周期速率记录
ARecGap[1]          ; 查询第一个示波器的降采样因子
```

## 另请参阅

- [RecLength](RecLength.md) — 每个参数的数据点数（设置时长）
- [RecStart](RecStart.md) — 设置完成后启动记录
- [LoggerGap](LoggerGap.md) — 连续记录器对应的降采样参数
