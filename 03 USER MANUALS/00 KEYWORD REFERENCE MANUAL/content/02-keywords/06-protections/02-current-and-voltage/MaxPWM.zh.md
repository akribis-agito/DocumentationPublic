---
keyword: MaxPWM
summary: 限制 PWM 电压指令幅值；AGD101 最大值为 900（90%），其他产品使用其报告的范围。
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
  range: null
  default: null
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    scaling: 1.526
last_updated: '2026-10-21'
doc_revision: '2026.10'
language: zh-CN
---
# MaxPWM

限制 PWM 电压指令幅值。

## 概述

`MaxPWM` 限制电流环输出的电压指令。单位为 **PWM 指令范围的 0.1%**：`900` 表示该范围的 90%。这是双极性调制幅值限制，并非高侧开关占空比的直接百分比。在 AGD101 的中心对齐上下计数 PWM 中，正向 90% 相电压指令对应的理想高侧占空比为 95%（未计死区）；零相电压指令对应 50% 占空比。

自动生成的 Quick Facts 按旧版 standalone/central-i 版本单元区分，并不区分各 AGD101 型号，因此通用数值范围保留为未解析。旧 standalone 缩放系数 1.144 不适用于正常 AGD101 C28388 配置（每个关键字单位为 3.125 个时钟计数）。请使用下述产品限制及控制器报告的元数据。

### AGD101 限制

AGD101 允许的最大设置为 **900（90%）**，保留原有 90% 默认值。更高的设置会被拒绝，已存储的值不变。加载旧固件保存的参数映像时，超过新内部上限的 AGD101 设置会通过正常的加载范围检查恢复为原有默认值。

此限制为低侧电流采样验证预留调制余量。它不会启用过采样，也不代表电流检测的稳定时间、噪声或时序已通过验证。内部值以整数 PWM 计数器时钟为单位，因此缩放和读回会存在正常的计数量化。此变更适用于 AGD101 的各电流规格型号；其他产品保留各自与产品相关的上限。

## 工作原理

无刷矢量控制使用预先计算的 `MaxPWM²` 限制输出电压矢量。[ControlMode](../../09-current-and-voltage/02-motor-variables/ControlMode.zh.md) 中的扩展速度范围选项会改变该矢量预算。直接将各相钳位至 ±`MaxPWM` 的处理适用于电流控制或矢量控制旁路模式。可配置的死区补偿也可能改变最终相电压指令，因此仅凭此关键字不能保证物理低侧导通窗口。

电压饱和通过 [StatReg](../../07-status-and-faults/StatReg.zh.md) 第 22 位报告。`MaxPWM` 限制请求的输出；饱和本身不会触发 [ConFlt](../../07-status-and-faults/ConFlt.zh.md) 故障。

## 示例

```text
AMaxPWM=900          ; AGD101 最大值：PWM 电压指令范围的 90%
AMaxPWM=300          ; 将限制降低为指令范围的 30%
```

`AMaxPWM=901` 超出 AGD101 的允许范围，会被拒绝。其他产品请使用控制器报告的关键字范围。

## 另请参阅

- [MaxVBus](MaxVBus.zh.md) / [MinVBus](MinVBus.zh.md) — 母线电压限制
- [StatReg](../../07-status-and-faults/StatReg.zh.md) — 第 22 位表示电压饱和
