---
keyword: AInFilt
summary: 每个模拟量输入的数字低通滤波器系数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 218
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 50000
  default: 10000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AInFilt

每个模拟量输入的数字低通滤波器系数。

## 概述

`AInFilt` 设置施加于模拟量输入的一阶数字低通滤波器的截止频率——它是[模拟量输入信号路径](00-overview.md)的第一个数字环节，在偏置、死区和增益之前作用于 ADC 读数。数组索引为模拟量输入编号（例如 `AInFilt[2]` 表示模拟量输入 2）。该值为以百分之一赫兹为单位的截止频率，因此其范围 1–50000 大致对应 **0.01 Hz 至 500 Hz**，默认值 10000 约为 **100 Hz** 截止频率。

## 工作原理

该滤波器为单极点指数低通滤波器。某个控制器周期的滤波输出（$y_{i}$）取决于当前输入（$u_{i}$）和上一次输出（$y_{i-1}$）：

$$
y_{i} = a\,u_{i} + (1 - a)\,y_{i - 1}
$$

系数 $a$ **并非** $\frac{\text{AInFilt}}{65536}$。每当写入 `AInFilt` 时都会重新计算该系数：

$$
a = 1 - e^{-2\pi\,T_s\,R\,\frac{\text{AInFilt}}{100}}
$$

其中 $T_s$ 为采样时间，$R$ 为模拟量输入更新速率（通常为 1——滤波器每个采样都运行）。$\frac{\text{AInFilt}}{100}$ 项为以赫兹为单位的有效截止频率：$a = 1 - e^{-2\pi f_c T_s}$，其中 $f_c = \frac{\text{AInFilt}}{100}$。两个系数（$a$ 和 $1-a$）被缓存并在每个周期复用，因此上述递推仅需两次乘法。

`AInFilt` **越大**意味着截止频率**越高**、滤波越弱；值越小则平滑越强。最低设置 `AInFilt = 1` 约为 0.01 Hz（极强的平滑）。

## 示例

```text
AAInFilt[1]=10000    ; ~100 Hz cutoff on analog input 1 (default)
AAInFilt[1]=50000    ; ~500 Hz cutoff (lightest filtering)
AAInFilt[1]=100      ; ~1 Hz cutoff (heavy smoothing)
```

### 边界情况

- **索引 0** — 无效；该数组为 1 起始索引（standalone/v4 上为 `AInFilt[1]`–`AInFilt[4]`）。`AInFilt[0]` 是保留的通信/内部槽位（用户不可访问），且 `AInFilt[5]` 不存在。
- **超出范围** — `AInFilt` 接受 `[1, 50000]` 范围内的值；超出该范围的写入会被以超出范围错误拒绝，且存储的值保持不变（不会被钳位）。
- **电机使能/失能** — 无论 `MotorOn` 如何，滤波器都持续运行；缓存的系数在每个周期都有效。
- **与模式无关** — 滤波器在任何特定于 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 的模拟量读数使用之前施加；在位置、速度、电流和力模式下该值的滤波方式相同。
- **运行中写入** — 写入 `AInFilt[i]` 时会重新计算缓存的 `a` 和 `1−a` 系数；运行中的输出历史**不会**被复位，因此响应会从旧截止频率平滑过渡到新截止频率。
- **强平滑陷阱** — 极小的值（例如 `AInFilt = 1` ≈ 0.01 Hz）需要数秒才能稳定；在滤波器跟上之前，读数看起来会是陈旧的。
- **保存** — `AInFilt` 可保存至闪存；滤波器系数在上电时根据存储的值重新计算。
- **平台** — central-i v5 将 `AInFilt` 存储为 `float32` 而非 `int32`；公式和单位相同。

## 另请参阅

- [AInPort](AInPort.md) — 得到的读数
- [AInOffset](AInOffset.md)、[AInGain](AInGain.md) — 信号链的后续环节
