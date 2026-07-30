---
keyword: DTCompGain
summary: 死区补偿增益；设为 0 则禁用该功能。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 867
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: [0, 10]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# DTCompGain

死区补偿增益；设为 0 则禁用该功能。

## 概述

功率桥臂的两个晶体管绝不允许同时导通，因此驱动器在每个开关沿插入一段短暂的封锁时间——即**死区时间**。在此期间两个器件均不导通，相绕组得不到电压。该损失是每个 PWM 周期内固定的伏秒量，因此无论指令电流大小，它消耗的电流基本恒定，所以在低电流时造成的相对影响最大。

`DTCompGain` 用于缩放沿各相指令电流方向叠加的补偿电压。设为 `0` 时补偿完全不起作用。

## 工作原理

每个控制周期，驱动器按 `DTCompGain` 比例向各相叠加一个电压，其符号取自该相的指令电流。在零电流附近 ±[DTCompLvl](DTCompLvl.md) 的区间内，符号采用线性插值而非直接切换，以避免电流过零时补偿产生抖振。

> **重要：** `DTCompGain` 是**逐驱动器标定**的参数，而非通用设置。正确值取决于所用驱动器的封锁时间，而该时间在产品系列间并不相同——AGD155 的死区时间是 AGD301 的四倍。默认值 1.0 对两者都不是最优值。

> **示例演算：** 以 800 mA 方波电流注入测量电流环相对参考值的平均跟踪误差。在 0.5 µs 死区下，增益 1.0 消除 43% 的误差，增益 2.0 消除 86%。在 2.0 µs 死区下，增益 1.0 仅消除 18%，而 5.2 可消除 97%——将误差从 165.6 mA 降至 5.2 mA。请注意最优值与死区时间并非线性关系，因此必须实测而不能计算得出。

### 确定合适的取值

1. 使用 [InjectType](../../13-injection/InjectType.md) 在电流参考处设置方波注入。
2. 记录 [CurrRef](../02-motor-variables/CurrRef.md) 与实测电流之间的跟踪误差。
3. 逐步提高 `DTCompGain`，保留使该误差最小的取值。

> **注意：** 误差曲线存在明确的极小值。超过最优点后驱动器将**过度**补偿，误差会对称地重新增大——取值过高与过低同样错误。

### 边界情况

- **闭环与开环：** 闭环电流环的积分器最终会自行补回大部分缺失的伏秒，因此两种情况下的稳态电流都接近正确值。死区时间对闭环造成的损失体现在每次过零附近的瞬态精度上。在电压模式或开环运行时，该损失直接体现在输出电流中。
- **低电流：** 这正是该功能的价值所在。指令较小时，固定的伏秒损失占指令的比例很大。
- **范围：** 超出 `0…10` 的写入将被钳位。

## 示例

```text
ADTCompGain=5.2      ; 针对 2.0 us 死区标定（AGD155）
ADTCompGain=2.0      ; 针对 0.5 us 死区标定（AGD301）
ADTCompGain=0        ; 禁用功能（默认）
```

## 另请参阅

- [DTCompLvl](DTCompLvl.md) — 过零插值区间
- [CurrRef](../02-motor-variables/CurrRef.md) — 补偿帮助电流环跟踪的参考值
