---
keyword: MaxPWM
summary: 限制最大 PWM 占空比（从而限制施加给电机的最大电压）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 91
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1470
  default: null
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    scaling: 1.526
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxPWM

限制最大 PWM 占空比（从而限制施加给电机的最大电压）。

## 概述

对于 PWM 驱动器，`MaxPWM` 限制 PWM 驱动的最大占空比——从而限制施加给电机的最大电压。单位为 **0.1%**：`1000` 表示 100% 占空比，`0` 表示 0%。

## 工作原理

`MaxPWM` 在电流环内部作为输出电压的饱和限值施加，采用两种方式：

- **矢量幅值。** 对于无刷电机，固件限制输出电压矢量的幅值，使 $\sqrt{V_q^{2}+V_d^{2}} \le \text{MaxPWM}$（使用预先计算的 `MaxPWM²`）。若在 `ControlMode` 中启用了增强转速范围选项，平方预算将按 $\frac{4}{3}$ 缩放（空间矢量过调制）。
- **逐相钳位。** 每个相输出（`Va`、`Vb`、`Vc`）独立钳位至 ±`MaxPWM`。

每当输出电压被钳位时，固件会记录一个饱和因子并置位 [StatReg](../../07-status-and-faults/StatReg.md) 第 22 位（电压饱和）。`MaxPWM` 是*限值*，而非跳闸——超过需求只会使输出饱和，不会触发 [ConFlt](../../07-status-and-faults/ConFlt.md) 故障。

### 边界情形

- **电机失能：** 饱和不会主动钳位（没有相电压被驱动），但该限值在下次电机使能时立即生效。
- **模式依赖性：** 只要电流环产生相输出（伺服或步进内部驱动器），逐相钳位即生效。
- **外部驱动器：** 当驱动器配置为外部驱动器（模拟电流或模拟速度指令——相输出不由内部电流环驱动）时，`MaxPWM` 无效。
- **范围溢出：** 写入超出 `0…1470`（0.1 % 单位，即最高约 147 %）范围的值会被拒绝并返回越界错误；存储值保持不变。注意该关键字单位为 0.1 %，而非 %：`1000` = 100 %。
- **HWProtectBits / ProtectMask：** 电压饱和不是跳闸，也不可屏蔽。

## 示例

在 48 V 母线和默认 `MaxPWM = 900` 的情况下，要将输出限制为 30% 占空比（14.4 V），设置：

```text
AMaxPWM=300          ; limit to 30% duty cycle (~14.4 V on a 48 V bus)
```

## 参见

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — 母线电压限值
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 22 位标记电压饱和
