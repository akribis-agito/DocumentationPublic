---
summary: 选择编码器反馈类型（增量式、SIN/COS、绝对式或模拟量）。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EncType/AuxEncType

选择该轴的编码器反馈类型。

## 概述

`EncType` 定义编码器反馈类型。它告诉控制器如何读取和解码连接到该轴的位置反馈硬件，进而决定哪些附加配置关键字适用（增量式的子类型和滤波器、绝对式编码器参数，或 SIN/COS 设置）。`AuxEncType` 是辅助编码器的对应项，工作方式相同。

## 工作原理

| 值 | 编码器类型                            | 类别                    |
|-------|-----------------------------------------|-----------------------------|
| 0     | 保留                                | -                           |
| 1     | 增量式 – TTL                       | 数字增量式编码器 |
| 2     | 绝对式 – SSI（不支持）          | 绝对式编码器            |
| 3     | 绝对式 – EnDat 2.2                    | 绝对式编码器            |
| 4     | 增量式 – SINCOS                    | 模拟 SIN/COS 编码器      |
| 5     | 绝对式 – Nikon 17-bit（不支持） | 绝对式编码器            |
| 6     | 绝对式 – BiSS-C                       | 绝对式编码器            |
| 7     | 模拟量位置反馈                | 其他                      |
| 8     | 绝对式 – Tamagawa                    | 绝对式编码器            |

某一类型是否实际受支持取决于产品硬件；选择不支持的类型将被拒绝。

对于数字增量式编码器，另请参阅 [EncSubType](EncSubType-AuxEncSubType.md) 和 [EncFilt](EncFilt-AuxEncFilt.md)。`EncSubType` 选择增量式解码方案：A/B 正交（0）、脉冲/方向（1）、C0/C1（2）或加/减计数（3）。增量式类型（`EncType=1`）也是唯一适用 [EncDir](EncDir-AuxEncDir.md) 和 [EncFilt](EncFilt-AuxEncFilt.md) 的类型。

对于绝对式编码器，另请参阅 [EncAbsBits](EncAbsBits-AuxEncAbsBits.md)、[EncAbsMB](EncAbsMB-AuxEncAbsMB.md)、[EncAbsOff](EncAbsOff-AuxEncAbsOff.md) 和 [EncAbsVal](EncAbsVal-AuxEncAbsVal.md)。使用绝对式编码器时，反馈 [Pos](../../10-motion/01-kinematics-status/Pos.md) 在上电时由绝对读数初始化，而非从零开始。

### Tamagawa（值 8）

Tamagawa 编码器是一种单圈串行绝对式编码器，可用作主编码器（`EncType=8`），在硬件支持的产品上也可用作辅助编码器（`AuxEncType=8`）。它在一个识别字节（ENID）中报告自身的分辨率，[EncAbsBits](EncAbsBits-AuxEncAbsBits.md) / `AuxEncAbsBits` 的设置方式取决于产品：

- **独立式控制器（v4）：** 控制器从编码器读取分辨率，并将其存入 `EncAbsBits`（主编码器）或 `AuxEncAbsBits`（辅助编码器）。当 `EncType` 或 `AuxEncType` 为 8 时，写入这两个关键字中的任何一个都会被拒绝，并返回错误 331（“Tamagawa encoder resolution cannot be changed, it is learned”）。
- **Central-i：** 分辨率**不会**从编码器读取。请手动将 `EncAbsBits`（对于辅助 Tamagawa 编码器还需设置 `AuxEncAbsBits`）设置为编码器的单圈分辨率。错误的值不会被检测出来：回绕模数由它计算得出（参见 [EncAbsBits](EncAbsBits-AuxEncAbsBits.md)），因此位置会累积错误。在 **v4** 上，一旦任一类型为 8，位数写入即被拒绝，因此请在选择类型 8 之前写入 `EncAbsBits` / `AuxEncAbsBits`。在 **v5** 上，可以随时写入。

在独立式控制器上，可以使用 [EncAbsSendCmd](../07-absolute-encoder/EncAbsSendCmd.md) 读写编码器的板载存储器；该功能在 central-i 主控上不可用。

> [!caution]
> 在 **v4** central-i 主控上，`EncType=8` 会写入远程驱动器中一个无关的设置，并且只要 `EncType` 为 8，每次控制器启动或远程单元重新连接时都会再次写入。请勿在 v4 central-i 主控上将 Tamagawa 编码器用作主编码器。**v5** 不会写入该设置。`AuxEncType=8` 不受影响。

对于模拟 SIN/COS 编码器，另请参阅 [SinCosSetup](SinCosSetup-AuxSinCosSet.md) 和 [SinCosSignals](SinCosSignals-AuxSinCosSig.md)。对于 `EncType=4`，方向通过 `SinCosSetup` 设置，而非 [EncDir](EncDir-AuxEncDir.md)。

## 版本间的变化

| | v4（独立式与 central-i） | v5（central-i） |
|---|---|---|
| Tamagawa（值 8） | 在独立式控制器上支持。在 central-i 主控上，请勿将其用作主编码器：`EncType=8` 会反复更改一个无关的远程驱动器设置（见上文注意事项） | 支持（central-i） |
| central-i 上使用 Tamagawa 编码器时的 `EncAbsBits` / `AuxEncAbsBits` | 必须手动设置，且须在选择类型 8 之前设置（之后写入会被拒绝） | 必须手动设置；可随时写入 |

两个版本都将编码器类型枚举至值 8（Tamagawa）。与往常一样，受支持的类型最终由产品硬件决定。**v5 仅适用于 central-i。**

## 示例

```text
AEncType=1           ; incremental TTL encoder
AEncType=4           ; SIN/COS encoder
AEncType=6           ; BiSS-C absolute encoder
```

### 操作演示：在引导时设置绝对式编码器

典型的绝对式编码器调试投运序列。该示例使用 26 位 BiSS-C 设备，丢弃 4 个最低有效（精细/未使用）位，且无偏移；请根据您编码器的数据手册调整数值。

```text
AMotorOn=0                ; motor off — these keywords change the feedback pipeline
AEncType=6                ; absolute, BiSS-C (use 3 for EnDat 2.2; for Tamagawa see "Tamagawa (value 8)" above)
AEncAbsBits=26            ; total bit count of the absolute word
AEncAbsMB=4               ; discard the 4 least-significant (unused/fine) bits
AEncAbsOff=0              ; offset added to the masked reading at power-up
ASave                     ; persist the encoder configuration to flash
AReset                    ; software power cycle so the encoder is configured cleanly
                          ; ... then check the seeded position ...
AEncAbsVal                ; raw masked, direction-handled absolute reading
APos                      ; Pos seeded from (EncAbsVal + EncAbsOff) — no homing required
```

要将机械零点放置在选定的物理点：将轴停在该处，读取 `EncAbsVal`，然后将 `EncAbsOff` 设为该读数的相反数，并执行 `Save`/`Reset`。在无刷电机上，更改其中任何一项都会使换相失效，因此控制器会标记必须重新执行换相。

## 另请参阅

- [EncSubType](EncSubType-AuxEncSubType.md) — 增量式编码器子类型（`EncType=1`）
- [EncFilt](EncFilt-AuxEncFilt.md) — 增量式输入滤波器（`EncType=1`）
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) / [SinCosSignals](SinCosSignals-AuxSinCosSig.md) — SIN/COS 配置与状态（`EncType=4`）
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — 绝对式编码器位数（绝对式类型）
