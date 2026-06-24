---
summary: 数字量输入经消抖和逻辑反转后的位打包状态（DInPort = 输入 1–32，DInPortHigh = 33–64）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DInPort / DInPortHigh

数字量输入经消抖和逻辑反转后的位打包状态。

## 概述

`DInPort` 反映数字量输入 1–32 的状态；`DInPortHigh` 在拥有超过 32 个输入的产品上覆盖输入 33–64。每个输入对应一**位**（位位置从 0 开始：位 0 = 输入 1），所显示的值是经过 [DInFilt](DInFilt.md) 消抖和任何 [DInLog](DInLog-DInLogHigh.md) 反转之后的结果。两者均为只读且不保存至闪存。见[数字量输入信号路径](00-overview.md)。

| Bit value | State |
|-----------|-------|
| 0 | Off |
| 1 | On |

## 工作原理

每个控制周期都会从硬件读取消抖后的输入字，并在结果被存储之前 XOR 进 [DInLog](DInLog-DInLogHigh.md) 反转掩码，因此你读取的值已经同时反映了消抖和极性设置：

$$
\text{DInPort} = (\text{debounced inputs}) \oplus \text{DInLog}
$$
$$
\text{DInPortHigh} = (\text{debounced inputs 33–64}) \oplus \text{DInLogHigh}
$$

为检测上升沿和下降沿，函数分派（见 [DInMode](DInMode.md)）每 16 个中断分组采样一次输入，并将每个快照与上一个比较。在 Central-i 主站上，这些字改为来自远程单元的同步 I/O 镜像，但与 `DInLog` 进行 XOR 的步骤完全相同。

`DInPort` 以控制器的环路速率每个控制周期刷新；底层原始信号在硬件中以快得多的速度采样和消抖（见 [DInFilt](DInFilt.md)）。

## 示例

```text
ADInPort              ; read inputs 1–32 as a bitfield
ADInPortHigh          ; read inputs 33–64
```

若 `DInPortHigh = 18`（二进制 `…0001 0010`），则位 1 和位 4 被置位——因此数字量输入 **34** 和 **37** 为开启。

## 注意事项

对于配置为输出的双向 I/O（见 [BiDirConfig](../01-general-keywords/BiDirConfig.md)），可回读 `DInPort`/`DInPortHigh` 以检查输出的状态。

### 边界情况

- **只读** — 写入被拒绝。请通过 [DInLog](DInLog-DInLogHigh.md)、[DInFilt](DInFilt.md)、[DInMode](DInMode.md) 修改输入行为。
- **未连接的输入** — 读取由输入上拉/下拉强制的值；结合 [DInLog](DInLog-DInLogHigh.md)，反转掩码可将"开路"翻转为逻辑"开启"。
- **小型平台上的 `DInPortHigh`** — 没有输入 33–64 的产品在 `DInPortHigh` 上始终返回 `0`；该关键字存在是为了软件可移植性。
- **电机使能/失能** — 无论 `MotorOn` 如何，采样和消抖都持续运行。
- **模式无关性** — 这些值在每种 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 下均有效；由 [DInMode](DInMode.md) 配置的函数仅在其适用的模式下查询这些位。
- **边沿检测** — [DInMode](DInMode.md) 中的分派比较当前与上一个输入快照，这些快照每 16 个中断分组采集一次（而非连续的控制周期）；短于该 16 中断采样窗口的跳变可能被漏掉。
- **Central-i 镜像延迟** — 在 central-i 主站上，输入字来自同步 I/O 镜像；相对于远程引脚，预期会有一个镜像周期的延迟。

## 另请参阅

- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — 逐输入逻辑反转
- [DInFilt](DInFilt.md) — 消抖滤波器
- [DInMode](DInMode.md) — 为输入分配函数
