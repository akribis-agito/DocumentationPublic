---
keyword: VLogic
summary: 只读的 5 V 逻辑电源电压；超出 4500–5500 mV 范围将禁用电机。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 37
attributes:
  access: ro
  scope: non-axis
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
  default: 5000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VLogic

只读的 5 V 逻辑电源电压；超出 4500–5500 mV 范围将禁用电机。

## 概述

`VLogic` 报告 5 V 逻辑电源电压测量值，单位为毫伏。它是一个带内置保护的只读状态量：如果 `VLogic` 离开 [4500, 5500] mV 范围，电机将因逻辑电压故障而被禁用。它作为母线电压读数 [VBus](VBus.md) 和 [DCDC](DCDC.md) 中逐轨逻辑测量值的补充。

## 工作原理

`VLogic` 每 16 个控制周期为一组采样一次，并使用逐型号的比例因子换算为毫伏（分压器和 ADC 参考因产品而异，故每种型号使用各自的乘数）。在没有 5 V 检测的型号上，以及在较旧的 central-i 远程单元上，会代入固定的 `5000` mV，使保护不会误触发。在 central-i 驱动器上，5 V 读数则通过驱动器同步报文到达，并按逐轴校准系数和偏置进行换算。

每个保护周期会将测量值与两个固定限值进行一次比较（这些是内置限值，**不可**由用户设置）：

| Condition | Fault | [ConFlt](../../07-status-and-faults/ConFlt.md) code |
|-----------|-------|------|
| `VLogic > 5500` mV | Logic voltage too high | 1010 |
| `VLogic < 4500` mV | Logic voltage too low | 1011 |

任一条件都会关闭电机并记录该故障。因此可接受的范围为：

$$
4500\ \text{mV} \le \text{VLogic} \le 5500\ \text{mV}
$$

> **注意：** 过压限值为开区间（`> 5500`），欠压限值为开区间（`< 4500`），因此边界值 4500 mV 和 5500 mV 仍可接受。

## 示例

```text
AVLogic             ; read the present 5 V logic voltage (mV)
```

## 另请参阅

- [DCDC](DCDC.md) — 逐轨内部逻辑电压测量值
- [VBus](VBus.md) — 驱动器直流母线电压读数
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 由逻辑电压保护触发的故障 1010 / 1011
