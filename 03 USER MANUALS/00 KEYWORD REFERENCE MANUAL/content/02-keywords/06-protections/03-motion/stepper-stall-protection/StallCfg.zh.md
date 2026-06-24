---
keyword: StallCfg
summary: 配置步进失步（堵转）检测模式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 513
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StallCfg

配置步进失步（堵转）检测模式。

## 概述

`StallCfg` 用于使能步进失步（堵转）检测并选择堵转发生时的处理方式。它是整个步进失步保护组（[StallThPcnt](StallThPcnt.md)、[StallCnst](StallCnst.md)，以及只读的 [StallStat](StallStat.md)、[StallVal](StallVal.md)、[StallTh](StallTh.md)）的主开关。

## 工作原理

`StallCfg` 控制逐周期的堵转逻辑。当其为 `0` 时，完全跳过检测模块；否则会计算度量值/阈值，并在 `StallVal < StallTh` 时判定为堵转：

| 取值 | 行为 |
|-------|-----------|
| 0 | 检测禁用；不评估度量值与阈值 |
| 1 | 检测运行；堵转时设置 [StallStat](StallStat.md) 并设置 [StatReg](../../../07-status-and-faults/StatReg.md) 堵转位，但**不**关闭电机 |
| 2 | 检测运行；堵转时除设置上述状态外，**还**会关闭该轴，并记录 ConFlt 代码 1065 |

检测到堵转时，固件始终设置 [StallStat](StallStat.md) `= 1` 并设置 [StatReg](../../../07-status-and-faults/StatReg.md) 的堵转位（bit 31，`0x80000000`）。仅在模式 2 下，它才会额外关闭该轴，并将故障记录到 [ConFlt](../../../07-status-and-faults/ConFlt.md) 和 [ErrLog](../../../07-status-and-faults/ErrLog.md)。当度量值恢复时，堵转位被清除，`StallStat` 返回 `0`。

堵转检测仅作用于由内置驱动器驱动的步进电机。

### 边界情况

- **电机失能：** 检测模块不运行；电机失能时 [StallVal](StallVal.md)、[StallTh](StallTh.md) 和 [StallStat](StallStat.md) 全部复位为 `0`。
- **非步进电机 / 外部驱动器：** 完全不计算度量值（固件跳过整个步进电流环分支），因此无论 `StallCfg` 取值如何，检测均无效。
- **模式依赖：** 只要步进电流环运行（在内置驱动器上使用步进电机），检测就会运行——不存在按运行模式的旁路。
- **模式 1 下的恢复：** 当度量值恢复至 [StallTh](StallTh.md) 以上时，[StatReg](../../../07-status-and-faults/StatReg.md) 堵转位和 [StallStat](StallStat.md) 会自动清除；无需操作员干预。
- **模式 2 下的恢复：** 该轴以 ConFlt 代码 1065 被禁用。可通过重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 来清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目会保留。
- **整定前提：** 在针对您的电机/负载拟合 [StallCnst](StallCnst.md) 之前，计算得到的 [StallTh](StallTh.md) 不会随速度变化，检测可能不可靠。
- **HWProtectBits / ProtectMask：** 堵转跳闸不可通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

## 示例

```text
AStallCfg[1]=2        ; enable stall detection and turn motor off on stall
AStallCfg[1]=1        ; alert-only (set status, keep running)
AStallCfg[1]=0        ; disable
```

## 另请参阅

- [StallStat](StallStat.md) — 检测到堵转时设置的堵转状态标志
- [StallThPcnt](StallThPcnt.md) — 堵转灵敏度（百分比）
- [StallCnst](StallCnst.md) — 速度相关阈值系数
- [StatReg](../../../07-status-and-faults/StatReg.md) — 堵转时设置的堵转位（bit 31，`0x80000000`）
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 在模式 2 下记录堵转故障代码 1065
