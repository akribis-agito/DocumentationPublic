---
keyword: OneOverTOn
summary: 使能或禁用以 Vel[4] 报告的 1/T 速度测量。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 187
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# OneOverTOn

使能或禁用以 Vel[4] 报告的 1/T 速度测量。

## 概述

`OneOverTOn` 使能（`= 1`）或禁用（`= 0`）以 [Vel](Vel.md)`[4]` 报告的 1/T 速度测量。1/T 方法通过测量累积固定*编码器计数数量*所用的*时间*（而非统计在固定控制采样内发生了多少计数），在低速下给出高分辨率的速度估计。在低速下，每采样计数法较为粗糙（往往每采样仅 0 或 1 个计数），而以高频定时器对已知位移进行计时则仍然精确。

它在使用数字增量式编码器（[EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`）时适用。该测量还可通过 [OneOverTFreq](OneOverTFreq.md)（定时器频率）和 [OneOverTGap](OneOverTGap.md)（计数间隔）进一步整定。在独立产品上禁用时，`Vel[4]` 报告 `0`。

## 工作原理

在独立产品上，1/T 捕获由专用的正交编码器计时单元执行，该单元**始终运行**，与 `OneOverTOn` 无关——该单元持续锁存编码器事件之间的定时器计数。

`OneOverTOn` 仅对从该捕获值*计算* `Vel[4]` 进行门控，该计算在每个控制周期的后半段执行一次。速度计算涉及一次除法，因此当该功能关闭时，计算被跳过（以节省周期时间），`Vel[4]` 报告为 `0`。

实际速度由锁存的定时器周期推导而来；完整方程以及符号/溢出处理参见 [OneOverTFreq](OneOverTFreq.md) 和 [OneOverTGap](OneOverTGap.md)。

| 值 | 对独立产品的影响 |
|-------|----------------------|
| `0`（默认） | 跳过 1/T 速度计算；`Vel[4] = 0`。捕获计时单元仍在运行。 |
| `1` | 每次控制中断时从捕获的 1/T 定时器周期计算 `Vel[4]`。 |

## 示例

```text
AOneOverTOn=1        ; enable 1/T velocity measurement on axis A
AOneOverTOn=0        ; disable (Vel[4] reports 0 on standalone)
AOneOverTOn          ; read current value
```

使能后，用 `AVel[4]`（速度数组的 1/T 元素）读取结果。

## 版本间变更

在**独立产品（v4）**上，`OneOverTOn` 如上所述对基于计时单元的 `Vel[4]` 计算进行门控。

在 **Central-i（v5）**上，1/T 速度在远程驱动器中计算并通过同步报文传送至主机；主机将其直接复制到 `Vel[4]` 中。该 Central-i 路径**不受 `OneOverTOn` 门控**，因此在 Central-i 上，该关键字不会像在独立产品上那样关闭 `Vel[4]`。配套的整定关键字 [OneOverTFreq](OneOverTFreq.md)、[OneOverTGap](OneOverTGap.md) 和 [OneOverTAuto](OneOverTAuto.md) 仅适用于独立产品。

## 另请参阅

- [Vel](Vel.md) — 反馈速度数组（`Vel[4]` 为 1/T 方法）
- [OneOverTFreq](OneOverTFreq.md) — 1/T 定时器频率分频器（分辨率与溢出的权衡）
- [OneOverTGap](OneOverTGap.md) — 每个 1/T 采样测量的编码器计数间隔
- [OneOverTAuto](OneOverTAuto.md) — 预留的频率/间隔自整定（未实现）
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — 必须为数字增量式编码器
