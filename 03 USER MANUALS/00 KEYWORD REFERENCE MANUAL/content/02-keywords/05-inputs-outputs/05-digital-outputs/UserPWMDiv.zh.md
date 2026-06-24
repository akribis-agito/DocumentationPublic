---
keyword: UserPWMDiv
summary: 设置所有用户 PWM 通道 PWM 频率的周期分频值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 627
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 9
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# UserPWMDiv

设置所有用户 PWM 通道 PWM 频率的周期分频值。

## 概述

`UserPWMDiv` 设置用户 PWM 输出的周期分频值，由此固定 [UserPWM](UserPWM.md) 中定义的**两个**通道共享的 PWM 频率。较大的值会延长周期，产生**更低**的 PWM 频率；较小的值会缩短周期，从而获得更高的频率。范围为 `0`–`15`，默认值为 `9`。保存至闪存。

## 工作原理

PWM 时基在硬件中生成。当你写入 `UserPWMDiv`（或 [UserPWM](UserPWM.md)）时，新的分频值会被应用——在独立式控制器上直接应用，或在 central-i 上通过发送至远程单元应用。硬件将其基准时钟除以 `2^(UserPWMDiv+1)` 以推进一个 4096 计数的周期计数器，因此每个 PWM 周期跨越 `2^(UserPWMDiv+1) × 4096` 个基准时钟周期。因此该分频值按 2 的幂单调地缩放周期：分频值越大 → 周期越长 → 频率越低。12 位周期计数器还将占空比分辨率固定为 4096 步，与分频值无关。

在 PWM 时基由 50 MHz 硬件时钟运行的产品上，所得频率为：

```text
PWM frequency = 50 MHz / (2^(UserPWMDiv + 1) × 4096)
```

| `UserPWMDiv` | 近似频率（50 MHz 时基） |
|--------------|------------------------------------------|
| 0            | ≈ 6.10 kHz |
| 9（默认）  | ≈ 11.9 Hz |
| 15（最大）     | ≈ 0.19 Hz |

确切频率因产品而异；请使用上述公式并代入你的产品的时基时钟。

由于该分频值设置共享时基，它一次性应用于两个 UserPWM 通道——你无法为两个通道设置不同的频率，只能设置不同的占空比。更改分频值不会改变占空*比例*（`0`–`4095` 的 [UserPWM](UserPWM.md) 值），只会改变测量该比例所基于的周期。

## 示例

```text
AUserPWMDiv=9        ; default period divisor
AUserPWMDiv=4        ; smaller divisor → shorter period → higher PWM frequency
AUserPWMDiv          ; read the present divisor
```

### 边界情况

- **超出范围**——`0`–`15` 之外的值会被拒绝。
- **共享时基**——一次性应用于两个 [UserPWM](UserPWM.md) 通道；无按通道频率。
- **保留占空比**——更改分频值会保留 `0–4095` 的占空比例，但相应地重新缩放导通时间。
- **电机使能/失能**——与 `MotorOn` 无关。
- **保存**——可保存至闪存；启动时重新应用。

## 参见

- [UserPWM](UserPWM.md)——按通道的占空比（本周期所适用的比例）
- [DOutSelect](DOutSelect.md)——将 PWM 通道路由到输出
