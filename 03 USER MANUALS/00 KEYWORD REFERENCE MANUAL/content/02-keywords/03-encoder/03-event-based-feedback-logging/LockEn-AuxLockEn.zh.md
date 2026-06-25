---
summary: 启用或禁用基于事件的反馈记录。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockEn/AuxLockEn

启用或禁用基于事件的反馈记录。

## 概述

`LockEn` 武装（`LockEn=1`）或解除武装（`LockEn=0`）基于事件的反馈记录（“位置锁存” / “捕获”）功能。武装后，由 [LockSrc](LockSrc-AuxLockSrc.md) 选定的硬件/固件触发会在触发事件发生的瞬间锁存编码器反馈位置。每个事件将锁存的位置记录到 [LockVal](LockVal-AuxLockVal.md)（并存入 [LockValTable](LockValTable-LockValTabB.md)），将已逝时间记录到 [LockTimeTable](LockTimeTable-LockTimeTabB.md)，并使事件计数器 [LockCntr](LockCntr-AuxLockCntr.md) 递增。

`AuxLockEn` 是其辅助编码器对应项。在当前固件中，捕获机制接入主编码器；如需辅助编码器捕获，请联系供应商。

## 工作原理

| LockEn | 状态 |
|---|---|
| 0 | 基于事件的反馈记录已禁用 |
| 1 | 基于事件的反馈记录已启用 |

### 武装序列（从禁用状态启用）

当 `LockEn` 由 `0 → 1` 转变时，固件将：

1. 将事件计数器 [LockCntr](LockCntr-AuxLockCntr.md) 复位为 `0`。
2. 将内部已逝周期计时器（[LockTimeTable](LockTimeTable-LockTimeTabB.md) 的来源）复位为 `0`。随后在记录启用期间，每个控制周期递增一。
3. 为 [LockSrc](LockSrc-AuxLockSrc.md) 选定的源和边沿配置触发硬件，并清除任何待处理的触发标志。

在 `LockEn` 已为 `1` 时再写入 `LockEn=1` **不会**重新武装或复位计数器/计时器——复位仅在禁用 → 启用的转变时发生。

### 捕获流水线

启用期间，固件在每个控制周期推进计时器并检查触发：

- **数字增量式 / SIN-COS 编码器**——位置在触发边沿的瞬间由硬件锁存（真正的硬件捕获），因此记录的值精确到触发时刻。
- **绝对式 / 其他非增量式编码器**——硬件捕获不可用；固件记录最近一次轮询的反馈位置。触发必须持续足够长的时间以便在控制周期速率下被检测到，所记录的值是轮询瞬间的位置（相对于真正的触发瞬间略有延迟）。

当检测到触发时：锁存位置 → 存入 `LockVal` → 递增 `LockCntr` → 将位置和时间追加到历史表。

### 与事件生成的互斥（仅 Standalone）

在非 Central-i 产品上，捕获触发与事件生成输出共用同一硬件引脚，因此这两个功能不能同时激活。武装 `LockEn=1` 会自动清除事件生成（`EventOn=0`），而武装事件生成会自动清除 `LockEn`。此限制不适用于 Central-i 产品。

### 捕获与事件生成共用一个通道（Central-i）

在 Central-i 上，捕获与事件生成可同时激活，但主控通过一个共享的通信通道从远程驱动器读取每个捕获位置，该通道同时也承载事件输出更新。因此这两个功能在该通道上轮流使用：当两者都繁忙时，处理其中一个可能使另一个延迟一个或多个控制周期。与单独运行任一功能相比，当捕获与事件生成一起运行时，这会降低最大持续捕获/事件速率。

## 示例

```text
ALockEn=1            ; enable event-based feedback logging (resets LockCntr and the timer)
ALockEn=0            ; disable logging
```

### 操作演练：为打标配置 Lock 捕获

在数字量输入 1（上升沿）上设置一个打标，武装捕获，然后观察每个标记的反馈位置。本示例使用 Standalone 产品——对于 Central-i，请参见 [LockSrc](LockSrc-AuxLockSrc.md) 中的源表。

```text
AMotorOn=0           ; on standalone products, LockEn takes the capture pin from event generation
ALockSrc=1           ; trigger source = digital input 1, rising edge
ALockEn=1            ; arm capture; LockCntr and the elapsed-cycle timer reset to 0
                     ; ... drive the axis past the marks ...
ALockCntr            ; count of marks captured so far
ALockVal             ; feedback position of the most recent mark
ALockValTable[1]     ; position of the first mark
ALockValTable[2]     ; position of the second mark
ALockTimeTable[1]    ; control cycles elapsed at the first mark
ALockEn=0            ; disarm when done (LockVal and LockCntr keep their last values)
```

对于数字增量式和 SIN/COS 编码器，位置在精确的触发边沿由硬件锁存，因此 `LockVal` 精确到触发瞬间——非常适合产品打标。对于绝对式编码器，所记录的值是最近一次轮询的 `Pos`，因此应使轴速度足够低，以免触发在两个控制周期之间经过。

## 边界情况

- **电机失能。** 只要正在读取编码器，捕获即可工作；即使轴被手动移动，`LockEn=1` 也会锁存事件。
- **运动中。** 允许在运动时写入 `LockEn`；捕获将在下一周期武装，且不会扰动正在进行的运动。
- **已武装。** 在 `LockEn` 已为 `1` 时再写入 `LockEn=1` 是空操作——计数器和已逝周期计时器*仅*在禁用 → 启用的转变时复位。
- **事件生成冲突（仅 Standalone）。** 在非 Central-i 产品上，捕获引脚与事件生成共用。武装 `LockEn=1` 会强制 [EventOn](../../18-event-generation/EventOn.md)=0（反之亦然）。Central-i 远程驱动器具有独立硬件，因此这两个功能可以共存。
- **表已满。** 一旦 [LockValTable](LockValTable-LockValTabB.md) 和 `LockValTabB` 都已存满，历史记录停止，但 `LockCntr` 和 [LockVal](LockVal-AuxLockVal.md) 在此后每个事件时仍继续更新。解除武装后再重新武装即可重新开始。
- **辅助编码器。** 提供 `AuxLockEn` 以保持对称性，但当前固件仅将捕获机制接入主编码器。
- **Central-i 断连。** 在断连的端口上，远程驱动器不会馈送锁存配置寄存器，也不会有捕获位置返回主控。

## 另请参阅

- [LockSrc](LockSrc-AuxLockSrc.md) — 选择触发源和边沿
- [LockCntr](LockCntr-AuxLockCntr.md) — 事件计数器，启用时复位为 0
- [LockVal](LockVal-AuxLockVal.md) — 最后锁存的反馈位置
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — 位置和时间戳历史表
