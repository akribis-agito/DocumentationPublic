---
keyword: CompFiltFreq
summary: 补偿滤波器一阶低通级的截止频率，单位为赫兹。
availability:
  standalone: []
  central-i:
  - v5
can_code: 835
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1.0
  - 1000.0
  default: 200.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CompFiltFreq

补偿滤波器一阶低通级的截止频率，单位为赫兹。

## 概述

当使用 [CompFiltOn](CompFiltOn.md) 启用补偿滤波器时，测量力与补偿表预测力之差会先经过一阶低通滤波器，再叠加回预测力。`CompFiltFreq` 设置该滤波器的截止频率，单位为赫兹。

低通滤波器作用于测量力与表预测力之差。截止频率较高时，输出能在更宽（更快）的频带内跟随力传感器；截止频率较低时，传感器仅能提供最慢速的修正，平滑的表预测力主导快速变化。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

该值以赫兹为单位解释为频率，内部使用控制器采样周期将其转换为单极低通系数；所得滤波器在指定频率处的 -3 dB 点即为该截止频率。每次频率更改时系数均重新计算，因此更新无需禁用滤波器即可生效。

固件接受 1 至 1000 Hz 的范围，默认值为 200 Hz。

### 滤波器数学

截止频率 $f_c$ 映射为指数平滑系数
$$\alpha = e^{-2\pi f_c\,T_s}$$
其中 $T_s$ 为控制器采样周期。测量力 $F_m$ 与表预测力 $F_t$ 之差 $d_k = F_{m,k} - F_{t,k}$ 经过单极递推
$$d_{\text{filt},k} = \alpha\,d_{\text{filt},k-1} + (1-\alpha)\,d_k$$
力控制的输出为 $d_{\text{filt},k} + F_{t,k}$。$f_c$ 越高，$\alpha$ 越小，滤波后的差值响应越快（传感器的更宽频带得以通过）；$f_c$ 越低，$\alpha$ 越接近 1，差值平滑越重，只有最慢速的传感器修正才能保留。

## 示例

将轴的补偿滤波器截止频率设置为 150 Hz：

```
ACompFiltFreq[1]=150
```

读回已配置的截止频率：

```
ACompFiltFreq[1]
```

## 另请参阅

- [CompFiltOn](CompFiltOn.md)
- [CompFiltTble](CompFiltTble.md)
- [00-overview](00-overview.md)
