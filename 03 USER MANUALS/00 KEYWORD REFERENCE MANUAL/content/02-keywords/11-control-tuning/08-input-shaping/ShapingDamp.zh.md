---
keyword: ShapingDamp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 153
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
  - 1
  - 65535
  default: 32768
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 输入整形器所抑制各谐振的阻尼比。
---
# ShapingDamp

输入整形器所抑制各谐振的阻尼比。

## 概述

`ShapingDamp` 存储 [ShapingFreq](ShapingFreq.md) 中所定义各谐振模态的阻尼比。元素 `ShapingDamp[1]` 与 `ShapingFreq[1]` 配对，`ShapingDamp[2]` 与 `ShapingFreq[2]` 配对。阻尼比决定整形器脉冲的相对幅值，频率决定脉冲的时序。整形器仅在 [ShapingOn](ShapingOn.md) 启用输入整形时有效。`ShapingDamp` 保存至闪存，不能在轴运动中或电机使能时修改。

### 单位、缩放与值域

阻尼比以 65536 为缩放因子存储——存储值等于阻尼比乘以 65536：

$$
\text{ShapingDamp} = \zeta \cdot 65536
$$

| | 值 |
|---|---|
| 单位 | 阻尼比 × 65536 |
| 值域 | 1 至 65535（ζ 略大于 0 至略小于 1） |
| 默认值 | 32768（ζ = 0.5） |

阻尼比必须为小于 1 的正分数。

## 工作原理

阻尼比 ζ 转换为整形器幅值项：

$$
K = e^{\,-\zeta \pi / \sqrt{1 - \zeta^{2}}}
$$

对应谐振的三个脉冲幅值由 $K$ 导出：

$$
A_0 = \frac{1}{1 + 2K + K^2}, \quad A_1 = \frac{2K}{1 + 2K + K^2}, \quad A_2 = \frac{K^2}{1 + 2K + K^2}
$$

各幅值之和始终为 1，因此稳定的参考信号不受影响。当定义了两个谐振时，两组幅值将进行卷积（参见 [ShapingFreq](ShapingFreq.md)）。

## 示例

```text
AShapingFreq[1]=3276800   ; resonance at 50 Hz (50 x 65536)
AShapingDamp[1]=6554      ; damping ratio 0.10 (0.10 x 65536)
AShapingOn=1              ; enable input shaping
```

## 另请参阅

- [ShapingOn](ShapingOn.md) — 启用/禁用输入整形
- [ShapingFreq](ShapingFreq.md) — 与各阻尼比配对的谐振频率
