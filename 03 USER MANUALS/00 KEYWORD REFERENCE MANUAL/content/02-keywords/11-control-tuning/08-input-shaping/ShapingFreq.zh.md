---
keyword: ShapingFreq
summary: 输入整形器所抑制的谐振频率。
availability:
- controller
- ci-master
can_code: 152
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 32768000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-11-23'
doc_revision: '2026.11'
language: zh-CN
---
# ShapingFreq

输入整形器所抑制的谐振频率。

## 概述

`ShapingFreq` 存储输入整形器所抑制振动模态的谐振频率。最多支持两个频率：`ShapingFreq[1]` 和 `ShapingFreq[2]`，各自与 [ShapingDamp](ShapingDamp.md) 中对应的阻尼比配对。整形器仅在 [ShapingOn](ShapingOn.md) 启用输入整形时有效。`ShapingFreq` 保存至闪存，不能在轴运动中或电机使能时修改。

第一个频率必须非零，整形器才会生效。第二个频率为可选项；将 `ShapingFreq[2] = 0` 则使用单谐振模式。

### 单位、缩放与值域

频率以 65536 为缩放因子存储——存储值等于频率（Hz）乘以 65536：

$$
\text{ShapingFreq} = f_{\text{Hz}} \cdot 65536
$$

| | 值 |
|---|---|
| 单位 | Hz × 65536 |
| 值域 | 0 至 32768000（0 至 500 Hz） |
| 默认值 | 0（整形器不激活） |

可用的最低频率取决于整形器历史缓冲区的长度，因产品而异。若配置的非零频率低于最小值或高于最大值，该轴的整形器将被禁用，并向 [ErrLog](../../07-status-and-faults/ErrLog.md) 记录一条告警。

在包含 [#2650](https://github.com/akribis-agito/Firmware-Main/pull/2650) 的 C2000 或 C28388 固件上，若控制环采样率为 16 kHz、历史缓冲区长度为 50 个采样点，则启用级的频率范围为 323.232330322265625 Hz（原始值 21183354）至 500 Hz。按整数 Hz 设置时，最低取 **324 Hz**。某一级设为 0 即停用该级。缓冲区可容纳的最大延迟为 49 个采样周期，而单级即使在 500 Hz 时也需要 32 个采样周期，因此该配置只能启用一级。其他采样率和缓冲区长度对应的频率限制不同。

## 工作原理

对于每个谐振，控制器根据频率计算半周期间距（脉冲分别位于 0、半个周期和一个完整周期处，周期为 1/`f`），并根据 [ShapingDamp](ShapingDamp.md) 中的阻尼比计算脉冲幅值。单个谐振的幅值为：

$$
A_0 = \frac{1}{1 + 2K + K^2}, \quad A_1 = \frac{2K}{1 + 2K + K^2}, \quad A_2 = \frac{K^2}{1 + 2K + K^2}
$$

$$
K = e^{\,-\zeta \pi / \sqrt{1 - \zeta^{2}}}
$$

其中 ζ 为 [ShapingDamp](ShapingDamp.md) 中的阻尼比。各幅值之和为 1。当定义了两个频率时，两组三脉冲序列将卷积为一组九脉冲序列；历史缓冲区必须足够长以容纳合并后的跨度，否则整形器将被禁用并向 [ErrLog](../../07-status-and-faults/ErrLog.md) 记录一条告警。

## 示例

```text
AShapingFreq[1]=26214400  ; first resonance at 400 Hz (400 x 65536)
AShapingFreq[2]=0         ; no second resonance
AShapingDamp[1]=3277      ; damping ratio 0.05
AShapingOn=1              ; enable input shaping
```

## 另请参阅

- [ShapingOn](ShapingOn.md) — 启用/禁用输入整形
- [ShapingDamp](ShapingDamp.md) — 与各频率配对的阻尼比
