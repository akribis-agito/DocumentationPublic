---
summary: 对数字量输入进行逐输入逻辑反转（XOR）（DInLog = 输入 1–32，DInLogHigh = 33–64）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DInLog / DInLogHigh

对数字量输入进行逐输入逻辑反转（XOR）。

## 概述

`DInLog` 反转所选数字量输入 1–32 的逻辑；`DInLogHigh` 对输入 33–64 执行相同操作。每个输入对应一位；置位的位会在状态被存入 [DInPort](DInPort-DInPortHigh.md) 之前通过 XOR 反转该输入。

| Bit value | Logic |
|-----------|-------|
| 0 | Default |
| 1 | Inverted |

## 工作原理

反转在每个控制周期从硬件读取原始输入字的时刻进行——消抖后的硬件字会在被存储之前与 `DInLog` 掩码进行 XOR，因此 [DInPort](DInPort-DInPortHigh.md)（以及每个读取它的函数）所看到的已经是反转后的极性：

$$
\text{DInPort} = (\text{debounced inputs}) \oplus \text{DInLog}
$$
$$
\text{DInPortHigh} = (\text{debounced inputs 33–64}) \oplus \text{DInLogHigh}
$$

**示例：** 当消抖后的输入读数为 `15`（`…00001111`）且 `DInLog = 6`（`…00000110`）时，结果为 `DInPort = 9`（`…00001001`）——位 1 和位 2 被反转（数字量输入 2 和 3）。

由于反转发生在边沿检测和 [DInMode](DInMode.md) 函数分派之前，反转限位开关或故障输入也会翻转该函数的有效逻辑方向。在 Central-i 主站上，每个 `DInLog` 的有效范围被限制为与远程设备实际数字量输入数量对应的位，因此只有这些位可写。

## 注意事项

出于失效安全（fail-safe）原因，通常用于限位开关：配置成在开关断开（输入为低）时触发故障。

### 边界情况

- **Central-i 远程位数** — 只有与远程设备实际数字量输入数量对应的位可写；多余的位被屏蔽。
- **小型平台上的 `DInLogHigh`** — 没有输入 33–64 的产品会忽略 `DInLogHigh`；该关键字存在是为了软件可移植性。
- **在边沿检测之前应用** — 反转限位/故障输入会翻转对应 [DInMode](DInMode.md) 函数的有效逻辑方向。
- **电机使能/失能** — 与 `MotorOn` 无关；反转每个周期都运行。
- **保存** — 可保存至闪存；重启后持久保留。

## 另请参阅

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — 经此 XOR 后得到的输入状态
- [DInFilt](DInFilt.md) — 消抖滤波器（在硬件中应用，在此反转之前）
- [DInMode](DInMode.md) — 为输入分配函数（这些函数看到的是反转后的极性）
