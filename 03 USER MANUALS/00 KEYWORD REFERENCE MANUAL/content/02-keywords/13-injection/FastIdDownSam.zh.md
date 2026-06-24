---
keyword: FastIdDownSam
summary: 设置 PRBS 新值生成速率的降采样因子。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 541
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
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# FastIdDownSam

设置 PRBS 新值生成速率的降采样因子。

## 概述

`FastIdDownSam` 设置 PRBS（伪随机二进制序列）生成速率的降采样因子。仅当 [InjectType](InjectType.md) 选择 PRBS 注入（`InjectType = 6 or 7`）时有效。该值越大，相对于控制器周期速率，新二进制值的生成速率越慢。PRBS 序列索引可通过 [FastIdInit](FastIdInit.md) 复位。

## 工作原理

$$
\text{新二进制值的生成速率}\ [\text{Hz}] = \frac{\text{控制器周期速率}\ [\text{Hz}]}{2^{\text{FastIdDownSam}}}
$$

每个 PRBS 位在输出端保持 $2^{\text{FastIdDownSam}}$ 个控制周期后，才从序列中取出下一位，因此该因子在时间上拉伸序列而不改变其位模式。允许值对应的速率如下：

| 值 | 每个 PRBS 位的控制周期数 |
|-------|--------------------------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8（默认） |

例如，`FastIdDownSam = 1` 时，每 2 个控制周期产生一个新的二进制值。更改该因子对后续位立即生效；[FastIdInit](FastIdInit.md) 从第一位重启序列，但该因子保持不变。

## 示例

```text
AFastIdDownSam=1     ; new value every 2 controller cycles
AFastIdDownSam=3     ; new value every 8 controller cycles (default)
AFastIdDownSam      ; query the current downsampling factor
```

> **注意：** 该值不会被 PCSuite 复位。

## 另请参阅

- [InjectType](InjectType.md) — 选择 PRBS 波形
- [FastIdInit](FastIdInit.md) — 复位 PRBS 序列索引
