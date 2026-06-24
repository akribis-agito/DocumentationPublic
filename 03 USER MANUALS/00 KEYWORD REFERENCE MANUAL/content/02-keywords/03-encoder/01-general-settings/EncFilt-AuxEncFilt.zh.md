---
summary: 应用于增量式编码器 A/B/Z 输入通道的数字滤波器。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EncFilt/AuxEncFilt

应用于增量式编码器 A/B/Z 输入通道的数字滤波器。

## 概述

`EncFilt` 指定应用于编码器输入通道 A、B 和 Z 的数字滤波器。该滤波器在硬件中实现，其定义因产品而异。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为 1（数字增量式编码器）时才使用；SIN/COS 编码器的滤波器请参阅 [SinCosSetup](SinCosSetup-AuxSinCosSet.md)。该滤波器仅在某个逻辑电平连续多个采样值相同后才予以确认，从而抑制正交输入上的噪声，代价是降低最大输入频率（因而降低最大支持的轴速度）。`AuxEncFilt` 是辅助编码器的对应项，其工作方式相同。

## 工作原理

`EncFilt` 写入解码硬件中的编码器输入确认滤波器。在**独立控制器**上，它设置 DSP 输入确认分频器（固件默认值 10，最大值 255）。在 **Central-i 远程单元**上，它是打包到远程编码器配置字中并发送给远程单元的一个 3 位字段（固件默认值 2，最大值 7）。与 [EncDir](EncDir-AuxEncDir.md) 和 [EncSubType](EncSubType-AuxEncSubType.md) 一样，它仅对增量式编码器路径（`EncType=1`）生效。

对于**独立控制器**，该滤波器的特性如下：

1. A、B 和 Z 输入由滤波机制采样。仅在连续 6 个采样值相同后才确认输入电平。这意味着信号的“1”逻辑至少需被采样 6 次，“0”逻辑同样如此，总计 (2*6) = 12 个采样。

2. 滤波频率（采样频率）由 `EncFilt` 参数决定。

   - 若 `EncFilt` 为 0：

     $$\text{Filter frequency} = \text{DSP clock frequency} = 300\ [\text{MHz}]$$

   - 若 `EncFilt` 不为 0：

     $$\text{Filter frequency} = \frac{300}{2 \cdot \text{EncFilt}}\ [\text{MHz}]$$

3. 最大理论输入频率（无噪声时）如下。

   - 若 `EncFilt` 为 0：

     $$\text{Max input frequency} = \frac{300}{12}\ [\text{MHz}]$$

   - 若 `EncFilt` 不为 0：

     $$\text{Max input frequency} = \frac{300}{2 \cdot 12 \cdot \text{EncFilt}}\ [\text{MHz}]$$

4. 最大理论支持速度（无噪声时）如下。

   - 若 `EncFilt` 为 0：

     $$\text{Max theoretical supported speed} = \frac{4 \cdot 3 \cdot 10^{8}}{12}\ [\text{count/s}] = 1.0 \cdot 10^{8}\ [\text{count/s}]$$

   - 若 `EncFilt` 不为 0：

     $$\text{Max theoretical supported speed} = \frac{4 \cdot 3 \cdot 10^{8}}{2 \cdot 12 \cdot \text{EncFilt}}\ \left[\frac{\text{count}}{\text{s}}\right] = \frac{5 \cdot 10^{7}}{\text{EncFilt}}\ [\text{count/s}]$$

5. 从滤波器的角度出发并忽略硬件限制，最高滤波频率为 300 MHz，当 `EncFilt=0` 时最高输入频率为 25 MHz（假设无噪声）。

对于 **Central-i 远程单元**，该滤波器的特性如下：

1. 输入由滤波机制采样。仅在连续 4 个采样值相同后才确认输入电平，总计 (2*4) = 8 个采样。

2. 滤波频率（采样频率）由 `EncFilt` 参数决定。

   $$\text{Filter frequency} = \frac{100}{2^{\,\text{EncFilt} + 1}}\ [\text{MHz}]$$

3. 最大理论输入频率（无噪声时）如下。

   $$\text{Max input frequency} = \frac{100}{8 \cdot 2^{\,\text{EncFilt} + 1}}\ [\text{MHz}]$$

4. 最大理论支持速度（无噪声时）如下。

   $$\text{Max theoretical supported speed} = \frac{4 \cdot 10^{8}}{8 \cdot 2^{\,\text{EncFilt} + 1}}\ [\text{count/s}]$$

5. 下表汇总了各自的频率和支持速度。

| EncFilt value | Filter frequency [MHz] | Max input frequency [MHz] | Max theoretical supported speed [*1E6 count/s] |
|----|----|----|----|
| 0 | 50 | 6.25 | 25 |
| 1 | 25 | 3.125 | 12.5 |
| 2 | 12.5 | 1.5625 | 6.25 |
| 3 | 6.25 | 0.78125 | 3.125 |
| 4 | 3.125 | 0.390625 | 1.5625 |
| 5 | 1.5625 | 0.1953125 | 0.78125 |
| 6 | 0.78125 | 0.09765625 | 0.390625 |
| 7 | 0.390625 | 0.048828125 | 0.1953125 |

6. 从滤波器的角度出发并忽略硬件限制，最高滤波频率为 50 MHz，当 `EncFilt=0` 时最高输入频率为 6.25 MHz（假设无噪声）。

> **Note:**
> 1. 由 `EncFilt` 设定的“Max input frequency”（或最大轴速度）是理论上限，其假设为理想方波信号（无限大变化速率）和理想电子器件（接收芯片无延迟）。实际最大输入频率会更小，取决于信号质量。
> 2. 信号上的噪声可能使滤波器无法计满某给定逻辑电平所需的连续采样数。因此建议不要将 `EncFilt` 设得过高。
> 3. 建议将 `EncFilt` 设置为使最大理论支持速度为系统中实际预期最大速度的两倍。
> 4. `EncFilt` 的初始值可根据上述公式设定，但最终值须在仔细考虑编码器信号质量（例如噪声）的前提下设定。
> 5. 若需要更快的输入，请咨询 Agito。

## 示例

```text
AEncFilt=0           ; no filtering (highest input frequency)
AEncFilt=3           ; apply filtering to reject noise
```

## 参见

- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncFilt` 适用于 `EncType=1`
- [EncSubType](EncSubType-AuxEncSubType.md) — 数字增量式编码器子类型
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — SIN/COS 编码器的滤波器配置
