---
keyword: AInMode
summary: 为每个模拟量输入分配控制功能，并支持按轴定向。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 257
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
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
# AInMode

为每个模拟量输入分配控制功能，并支持按轴定向。

## 概述

`AInMode` 为模拟量输入分配功能——它将某个输入的*经调理*读数（[信号调理链](00-overview.md)的结果：滤波、偏置、死区、增益、静音）路由至特定的控制功能，例如速度指令、电流指令或力反馈。数组**索引**选择输入（例如 `AInMode[2]` 配置模拟量输入 2）。该值为一个 32 位字段：低 16 位选择功能，高 16 位选择由哪些轴使用它。

`AInMode` 会保存至闪存。更改它不会每个周期搬移数据；而是在每次写入该关键字时重建一个内部路由表（见下文）。

## 工作原理

写入 `AInMode` 时，会重新解析每个输入并重建一个内部路由表。每个功能都持有对所分配输入的经调理读数（[AInPort](AInPort.md)`[1]`–`[4]`）和原始读数（[AInPort](AInPort.md)`[5]`–`[8]`）的引用，外加一个已定义/未定义标志。未被分配的功能读取常量零，因此未配置的功能读取 `0` 而非陈旧数据。该表以原子方式更新，因此控制周期绝不会看到更新到一半的路由。

**低 16 位**选择功能（有效范围 0–10）：

| 低 16 位值 | 功能 | 使用方 |
|--------------------|---------------|-------------|
| 0 | 通用输入 – 无控制功能 | 仅通过 `AInPort` 读取 |
| 1 | 速度指令 | 速度控制模式从该输入设置速度参考 |
| 2 | 电流指令 | 电流模式的电流参考 |
| 3 | 力反馈 | 力反馈 `Force`；同时也是由 [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md) 和 [ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) 测试的值 |
| 4 | 力指令 | 力模式的力参考 |
| 5 | 操纵杆输入 | 规划器中的点动 / 位置目标 |
| 6 | 转矩补偿 | 叠加到电流参考 |
| 7 | 反向（负）电流限制 | 钳位电流参考 |
| 8 | 正向（正）电流限制 | 钳位电流参考 |
| 9 | 测速机反馈 | 用于双环的速度反馈 |
| 10 | 位置反馈 | 来自*原始*读数的主/辅编码器位置 |

写入大于 10 的功能值将被拒绝：该 `AInMode` 条目被置零并记录一个超出范围的状况。

**高 16 位**选择由哪些轴使用该功能——每一位对应一个轴，可设置多个位，因此一个物理输入可驱动多个轴：

| 值, 位号 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|-------------|----|----|----|----|----|----|----|----|
| 轴 | A | B | C | D | E | F | G | H |

若高 16 位**全为零**，则该功能被分配给轴 A——为向后兼容而保留。

> 注意：位置反馈（功能 10）使用**原始**读数（[AInPort](AInPort.md)`[5]`–`[8]`），而非经调理的读数；滤波/偏置/增益环节对其不适用。

## 示例

将轴 C 的模拟量输入 2 用作轴 A 的力反馈：

$$
\text{CAInMode}[2] = 3 + 2^{16} = 65539
$$

```text
AAInMode[1]=1        ; analog input 1 -> velocity command of axis A
AAInMode[1]=3        ; analog input 1 -> force feedback of axis A
AAInMode               ; read the current AInMode assignments
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AInMode[1]`–`AInMode[4]`。`AInMode[0]` 不存在。
- **超出范围的功能** — 低 16 位 > 10 的值将被拒绝：该条目被置零并记录故障 2013（分配给 AInMode 的功能超出允许范围）。
- **未分配的功能** — 没有任何输入映射到的功能读取常量 `0` 而非陈旧数据，因此缺失的路由会安全失效。
- **多个输入映射到一个功能** — 路由表按升序逐个输入重建；若两个输入将同一功能分配给同一目标轴，则较后输入的指针胜出。
- **多轴广播** — 设置多个高位会将一个输入扇出到多个轴；每个目标轴读取相同的经调理值。
- **错误模式下使用** — 分配功能 1（速度指令）本身并不会将轴切换至速度控制 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md)；仅在使用该值的模式处于活动状态时才使用所路由的值。该路由在其他模式下无害。
- **位置反馈（代码 10）** — 使用**原始**的 [AInPort](AInPort.md)`[5]`–`[8]` 读数；滤波、偏置、死区和增益环节对其不适用。
- **电机使能/失能** — 路由在写入时重建；现有路由不受 `MotorOn` 状态切换影响。
- **保存 / 复位** — `AInMode` 可保存至闪存。持久化的路由在引导时通过同一解析器重新应用。
- **平台** — 代码列表 0–10 在 standalone、central-i v4 和 central-i v5 上完全相同。

## 另请参阅

- [AInPort](AInPort.md) — 模拟量输入读数（由 `AInMode` 路由的值）
- [AInGain](AInGain.md)、[AInOffset](AInOffset.md)、[AInFilt](AInFilt.md)、[AInDB](AInDB.md)、[AInMuteRange](AInMuteRange.md) — 路由之前施加的信号调理链
- [CurrAInTh](../../08-axis-operation/03-current-operation-mode/CurrAInTh.md)、[ForceAInTh](../../08-axis-operation/04-force-operation-mode/ForceAInTh.md) — 作用于力反馈功能的阈值
