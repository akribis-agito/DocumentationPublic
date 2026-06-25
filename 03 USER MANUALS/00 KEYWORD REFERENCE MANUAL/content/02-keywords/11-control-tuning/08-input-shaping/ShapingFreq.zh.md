---
keyword: ShapingFreq
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 输入整形器所抑制的谐振频率。
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
AShapingFreq[1]=3276800   ; first resonance at 50 Hz (50 x 65536)
AShapingFreq[2]=0         ; no second resonance
AShapingDamp[1]=3277      ; damping ratio 0.05
AShapingOn=1              ; enable input shaping
```

## 另请参阅

- [ShapingOn](ShapingOn.md) — 启用/禁用输入整形
- [ShapingDamp](ShapingDamp.md) — 与各频率配对的阻尼比
