---
keyword: PwrTemp
summary: 只读的功率级温度（°C）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 38
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
  default: 25
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
# PwrTemp

只读的功率级温度（°C）。

## 概述

`PwrTemp` 报告功率级内部 IPM（智能功率模块）的温度，单位为 °C。它为只读且不保存至闪存——在 standalone 上为非轴范围（所有轴共用一个值），在 Central-i 上为按轴。保护限值为 [MaxPwrTemp](MaxPwrTemp.md)；功率级散热风扇也由该值驱动。

## 工作原理

### 测量流程（传感器 → °C）

IPM 温度以模拟电压感测，并通过查找校准曲线转换为 °C（IPM 热敏电阻是非线性的，因此不使用固定公式）。存在两种产品路径：

| 产品 | 方法 |
|---------|--------|
| AG100 类驱动器 | 每个周期将原始 IPM 电压换算为 mV，并通过**表搜索**沿校准曲线（索引 `−40…+119 °C`，每度一个条目）从上一估计值向上或向下查找，直到找到电压区间。 |
| Central-i（主站） | 对每个轴，将同步的 ADC 读数在按轴 10 点校准表中两个最近点之间进行**线性插值**。 |

读数被钳位到有效范围内（AG100 搜索在 −39 / +119 °C 处停止，在每端各保留一个保护点）。

### 无效读数处理

如果 STO2 或 IPM 故障硬件保护位被置位，则无法测量 IPM 电压。控制器随即将 `PwrTemp` 强制为 −40 °C 作为哨兵值（“无法测量”），并重新置位一次新的搜索以备保护清除后使用。在 STO2 插入后的最初几毫秒内，由于 IPM 行为，`PwrTemp` 可能读出虚高值——风扇逻辑已对此加以处理。

### 风扇控制

`PwrTemp` 以迟滞方式驱动功率级散热风扇：

| 产品 | 风扇开启于 | 风扇关闭于 |
|---------|-----------|-----------|
| AG100 | ≥ 50 °C（或上电后最初 5 秒内） | ≤ 45 °C |
| Central-i | ≥ 50 °C | ≤ 45 °C |

### 保护

当电机使能时，`PwrTemp > MaxPwrTemp` 会禁用轴并使 [ConFlt](../../07-status-and-faults/ConFlt.md) = 1018（IPM 温度过高）。分级告警出现在 [StatReg](../../07-status-and-faults/StatReg.md) 位 11–12 中——参见 [MaxPwrTemp](MaxPwrTemp.md)。

## 示例

```text
APwrTemp            ; power-stage (IPM) temperature (°C)
```

## 另请参见

- [MaxPwrTemp](MaxPwrTemp.md) — 功率级过温限值与告警分段
- [BoardTemp](BoardTemp.md) — 控制器板温度
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 11–12 承载功率/板温度告警
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 故障码 1018（IPM 温度过高）
