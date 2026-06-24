---
keyword: RecLength
summary: 每个示波器每个参数捕获的数据点数（记录时长）。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 241
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
  - 0
  - 30500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# RecLength

每个示波器每个参数捕获的数据点数（记录时长）。

## 概述

`RecLength` 是一个数组，定义每个参数捕获的数据点数，从而确定记录时长。与降采样因子 [RecGap](RecGap.md) 结合，决定示波器的记录持续时间。每个数组索引对应一个示波器。

| 索引 | 说明                        |
|------|-----------------------------|
| 1    | 第一个示波器                |
| 2    | 第二个示波器（如适用）      |

## 工作原理

记录时长为：

$$
\text{示波器 } x \text{ 的记录时长}\ [\text{s}] = \frac{\text{RecLength}[x] \cdot \text{RecGap}[x]}{\text{控制器周期速率}\ [\text{Hz}]}
$$

`RecLength` 设置的是*每个参数*捕获的点数。示波器缓冲区在所有已记录通道间共享，因此约束条件为总采样数：[RecParamA/RecParamB](RecParamA-RecParamB.md) 中所选通道数与 `RecLength` 的乘积必须在缓冲区容量之内。否则 [RecStart](RecStart.md) 将被拒绝。记录通道越多，可用的最大 `RecLength` 越小。最大缓冲区大小因产品而异（各产品的点数限制请参见[数据记录](00-overview.md)概述）。

在 [RecStart](RecStart.md) 执行前，该示波器的 `RecLength` 必须大于 0；以默认值 0 或任何不大于 0 的值启动将被拒绝。

[RecTrigPos](RecTrigPos.md) 将这些点划分为触发前和触发后两部分：触发前部分作为滚动缓冲区首先填充，示波器在此等待触发；触发后部分在触发发生后捕获。

计算示例：在 `RecLength[1] = 16384`、`RecGap[1] = 1`、周期速率为 16384 Hz 时，记录时长为 `16384 / 16384 = 1.0` s（每个参数）。将降采样因子增大至 `RecGap[1] = 2` 可在相同点数下将时长延长至 2.0 s，但时间分辨率减半。若通过 [RecParamA/RecParamB](RecParamA-RecParamB.md) 选择了 4 个通道，缓冲区需容纳 `4 x 16384 = 65 536` 个采样——请确保该乘积在产品缓冲区限值以内。

## 示例

```text
ARecLength[1]=16384  ; 第一个示波器每个参数捕获 16384 个数据点
ARecLength[1]       ; 查询第一个示波器的记录长度
```

## 另请参阅

- [RecGap](RecGap.md) — 降采样因子（设置频率）
- [RecTrigPos](RecTrigPos.md) — RecLength 的触发前比例
- [RecStart](RecStart.md) — 设置完成后启动记录
