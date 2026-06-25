---
keyword: ShapingOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 151
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 启用或禁用轴上的输入整形。
---
# ShapingOn

启用或禁用轴上的输入整形。

## 概述

`ShapingOn` 启用轴上的输入整形（指令滤波）。启用后，位置参考与脉冲序列进行卷积，使一个或两个谐振频率处的能量相互抵消，从而在轴稳定时抑制残余振动。谐振频率及其阻尼比由 [ShapingFreq](ShapingFreq.md) 和 [ShapingDamp](ShapingDamp.md) 设置。

| `ShapingOn` | 行为 |
|---|---|
| 0 | 输入整形禁用（默认）。 |
| 1 | 输入整形启用——参考信号由 [ShapingFreq](ShapingFreq.md) 和 [ShapingDamp](ShapingDamp.md) 所构建的脉冲序列进行整形。 |

`ShapingOn` 保存至闪存，不能在轴运动中或电机使能时修改。输入整形仅在位置或速度运行模式下有效（不适用于电流或力控制模式），且不能与主编码器的取模（连续旋转）模式同时使用。若在主编码器取模模式激活时启用整形，尝试使能电机将被拒绝；若该组合在电机使能时变为激活状态，轴将以故障码 1032 跳闸关断。

在输入整形启用且电机使能期间，向轴位置赋值将被拒绝并返回错误 85，因为整形器的历史缓冲区无法与突然的位置变化相协调。请在赋值位置前禁用整形（或关闭电机）。

## 工作原理

整形器是对规划器后位置参考执行的有限脉冲响应（FIR）运算。针对单个谐振，它施加三个脉冲，间距分别为 0、半个谐振周期和一个完整周期：

$$
\text{shaped}_k = A_0 \cdot \text{ref}_k + A_1 \cdot \text{ref}_{k-N} + A_2 \cdot \text{ref}_{k-2N}
$$

其中半周期间距 $N$ 对应谐振频率的半个周期。脉冲幅值由阻尼比导出（参见 [ShapingFreq](ShapingFreq.md) 和 [ShapingDamp](ShapingDamp.md)），各幅值之和始终为 1，因此稳定的参考信号可原样通过，仅动态瞬态部分被整形。当定义了两个谐振频率时，两组三脉冲序列将卷积为一组九脉冲序列。

整形器的历史缓冲区在电机使能时初始化为当前参考值，确保运动起始干净。

## 示例

```text
AShapingFreq[1]=3276800   ; resonance at 50 Hz (value = Hz x 65536)
AShapingDamp[1]=3277      ; damping ratio 0.05
AShapingOn=1              ; enable input shaping
```

### 计算示例：50 Hz / 阻尼比 0.05 模态的脉冲时序与幅值

对于 `ShapingFreq[1]` = 50 Hz、`ShapingDamp[1]` = 0.05（ζ = 0.05）：

- 周期 T = 1 / 50 Hz = 20 ms
- 脉冲位置：0 ms、T/2 = 10 ms、T = 20 ms
- K = exp(-0.05 x π / √(1 - 0.05²)) ≈ 0.855
- 1 + 2K + K² ≈ 3.441
- A₀ ≈ 1 / 3.441 ≈ 0.291
- A₁ ≈ 2 x 0.855 / 3.441 ≈ 0.497
- A₂ ≈ 0.855² / 3.441 ≈ 0.213
- 合计：A₀ + A₁ + A₂ ≈ 1.001（四舍五入）；在控制器定点运算中恰好为 1。

因此，整形器叠加原始参考（权重 0.291）、延迟 10 ms 的相同参考（权重 0.497）以及延迟 20 ms 的参考（权重 0.213）。从 0 到目标值的阶跃在 20 ms 后到达目标值，但 50 Hz 处的残余振荡被抵消。

## 另请参阅

- [ShapingFreq](ShapingFreq.md) — 待抑制的谐振频率
- [ShapingDamp](ShapingDamp.md) — 各谐振的阻尼比
