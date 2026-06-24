---
keyword: DCDC
summary: 内部逻辑电源轨电压测量值的只读数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 42
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 8
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
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
# DCDC

内部逻辑电源轨电压测量值的只读数组。

## 概述

`DCDC` 以数组形式报告驱动器的内部逻辑电源电压测量值，每个逻辑轨对应一个条目，单位为毫伏。它是一个只读诊断量，作为 [VLogic](VLogic.md) 中单一 5 V 读数的补充。并非每个产品都会填充所有条目；如需特定产品适用的读数，请联系 Agito。

## 工作原理

该数组有 8 个元素（索引 0 未使用，使通信索引从 1 开始）。每个索引按下表映射到一个逻辑轨。

| Index | Description                                        |
|-------|----------------------------------------------------|
| 1     | 3.3 V logic                                        |
| 2     | 15 V logic                                         |
| 3     | -15 V logic                                        |
| 4     | 1.2 V logic                                        |
| 5     | 1.8 V logic                                        |
| 6     | Backup or logic supply                             |
| 7     | 4.7 V logic                                        |

这些逻辑轨在两个控制子周期内采样（3.3 V / ±15 V 一组在一个步骤中采样，1.2 V / 1.8 V 一组在下一个步骤中采样），每个原始读数都通过固定的逐轨乘数换算为毫伏。实际采样哪些逻辑轨取决于产品：

- 在不检测某一逻辑轨的产品上，会代入标称值（例如 3.3 V 轨代入 3300 mV，±15 V 轨代入 ±15000 mV，1.2 V / 1.8 V 轨代入 1200 / 1800 mV），使读数仍然合理而不为零。
- 在某些产品上，−15 V 读数针对 3.3 V 负载进行了修正，因此它是计算值而非直接读取的值。
- 在 **central-i** 远程轴上，索引 6（备用 / 逻辑）和索引 1（3.3 V）由驱动器同步报文填充，各自按逐轴校准系数和偏置进行换算；而该同一报文中的 5 V 读数则存储在 [VLogic](VLogic.md) 中。

因此，某一逻辑轨上恒定的标称读数并不一定意味着该逻辑轨正常——可能只是该产品未对其进行检测。

## 示例

```text
ADCDC[1]            ; read the 3.3 V logic rail
ADCDC[2]            ; read the 15 V logic rail
ADCDC[6]            ; read the backup / logic rail
```

## 另请参阅

- [VLogic](VLogic.md) — 5 V 逻辑电源电压读数
- [VBus](VBus.md) — 驱动器直流母线电压读数
