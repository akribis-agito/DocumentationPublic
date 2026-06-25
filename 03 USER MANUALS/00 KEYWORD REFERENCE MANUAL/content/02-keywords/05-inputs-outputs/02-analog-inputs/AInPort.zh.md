---
keyword: AInPort
summary: 只读模拟量输入读数——处理后的值和原始 ADC 值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 35
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
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
    data_type: float32
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AInPort

只读模拟量输入读数——处理后的值和原始 ADC 值。

## 概述

`AInPort` 保存模拟量输入读数，单位为毫伏。其长度是模拟量输入数量的两倍：前半部分保存**处理后**的读数（经过滤波、偏置、第一级死区、增益和第二级死区），后半部分保存直接来自 ADC 的**原始**值。完整的处理链请参见[模拟量输入信号路径](00-overview.md)。

| 数据 | 模拟量输入 1 | 模拟量输入 2 | 模拟量输入 3 | 模拟量输入 4 |
|------|----------------|----------------|----------------|----------------|
| 处理后输入 | AInPort[1] | AInPort[2] | AInPort[3] | AInPort[4] |
| 原始输入 | AInPort[5] | AInPort[6] | AInPort[7] | AInPort[8] |

索引固定对应物理输入——`AInPort[1]` 始终为模拟量输入 1，`AInPort[2]` 为输入 2，依此类推。在 2 路输入产品上，仅存在输入 1–2（处理后）及其对应的原始条目；其余读作 0。

## 工作原理

每个控制周期，一路输入的 ADC 读数被取入一个工作值，原样存入原始条目（`AInPort[5]`–`AInPort[8]`），然后经过信号调理链处理并存入处理后条目（`AInPort[1]`–`AInPort[4]`）。调理各级请参见[模拟量输入信号路径](00-overview.md)。原始计数通过一个固定的硬件系数缩放为毫伏（例如 ±12500 mV 对应 ±32768 counts），因此 `AInPort` 的两半部分都以 mV 为单位。

更新速率取决于平台：

- **独立式（CONTROLLER）v4** — 全部四路输入在每个采样（16 384 Hz）都被调理。在 AG100 单轴变型上，仅存在输入 1–2。
- **Central-i v4 / v5** — 四路输入每 16 个采样槽调理一路，因此每路输入在每个已连接的远程单元上约以 1 024 Hz 刷新。

模拟量输入转换器为 16 位转换器，读数为有符号（二进制补码），因此原始条目跨越完整的 −32768…+32767 计数范围。在独立式产品上，每个控制周期转换器为每路输入取一个新采样：转换的时序安排使其在每个控制周期被读取时已就绪，且远在约 61 µs 的周期（16 384 Hz）之内，并且没有内部过采样或分块平均——`AInPort[5]`–`AInPort[8]` 是每个周期捕获的输入单点采样。（在 central-i 远程 I/O 上，四路输入如上所述轮流刷新，每路约 1 024 Hz，但每个值仍为单点采样，而非分块平均。）要平滑有噪声的输入，请使用数字滤波器 [AInFilt](AInFilt.md)，而不要依赖转换器平均。

处理后的值是控制功能在某路输入通过 [AInMode](AInMode.md) 路由后所使用的；原始值仅由模拟位置反馈功能（[AInMode](AInMode.md) 代码 10）直接使用。两者均为只读。

## 示例

```text
AAInPort[1]         ; processed reading of analog input 1
AAInPort[5]         ; raw (post-ADC) reading of analog input 1
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AInPort[1]`–`AInPort[8]`。`AInPort[0]` 不存在。
- **2 路输入产品（AG100）** — 仅填充 `AInPort[1]`、`AInPort[2]`、`AInPort[5]`、`AInPort[6]`；索引 3、4、7、8 读作 `0`。
- **与电机使能/失能及模式无关** — 无论 `MotorOn` 或 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 如何，采样和调理每个周期都会运行；即使轴被禁用，这些值也有效。
- **读取原始值** — `AInPort[5]`–`AInPort[8]` 是经毫伏缩放、未经任何滤波 / 偏置 / 死区 / 增益 / 静音的 ADC 值，在某个功能（例如 [AInMode](AInMode.md) 代码 10 位置反馈）需要未处理读数时很有用。
- **只读** — 对 `AInPort` 的写入会被拒绝；请通过 [AInGain](AInGain.md) / [AInOffset](AInOffset.md) / [AInDB](AInDB.md) / [AInMuteRange](AInMuteRange.md) / [AInFilt](AInFilt.md) 修改输入行为。
- **平台** — 在 central-i v5 上，这些值为 32 位浮点，采用相同的 mV 缩放。

## 另请参阅

- [AInFilt](AInFilt.md)、[AInOffset](AInOffset.md)、[AInDB](AInDB.md)、[AInGain](AInGain.md)、[AInMuteRange](AInMuteRange.md) — 产生 `AInPort[1]`–`AInPort[4]` 的处理链
- [AInMode](AInMode.md) — 为模拟量输入分配功能
