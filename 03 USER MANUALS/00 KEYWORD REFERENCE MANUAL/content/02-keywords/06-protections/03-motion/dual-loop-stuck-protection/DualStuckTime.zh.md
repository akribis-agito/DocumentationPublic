---
keyword: DualStuckTime
summary: 双环反馈失配在触发跳闸前可持续的连续控制周期数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 158
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
  - 2147483647
  default: 4096
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# DualStuckTime

双环反馈失配在触发跳闸前可持续的连续控制周期数。

## 概述

`DualStuckTime` 表示双环反馈失配在双环堵转故障触发前可持续的时长。你以毫秒为单位设置；该关键字带有采样数到毫秒的换算，内部将其与采样计数器比较（在标准 16 kHz 控制速率下，1 个控制采样 ≈ 61.0 µs；你以 ms 设置的值在内部以 value·16.384 个采样存储）。默认值为 `4096`。

## 工作原理

启用双环时，固件在每个控制采样检测两路反馈的速度差是否超过 [DualStuckVel](DualStuckVel.md)：

```text
increment the dual-stuck counter
if the dual-stuck counter has reached DualStuckTime
    turn the axis off and log the fault
```

- 只要失配超过 `DualStuckVel`，内部计数器每个采样递增一次；任何处于容差内的采样都会将其复位为 `0`。该故障要求出现一段不间断的 `DualStuckTime` 连续运行。
- 达到阈值时，轴被关闭，并由 [ConFlt](../../../07-status-and-faults/ConFlt.md) 记录 ConFlt 码 1049（双环堵转）。
- 整个检测受 `DualLoopOn` 控制，因此在单环轴上该计数器从不运行。

较大的 `DualStuckTime` 可容忍更长的瞬态偏离（例如在两路反馈瞬间不一致的剧烈瞬态过程中）；较小的值则对真正打滑或断裂的耦合反应更快。

### 边界情况

- **电机失能：** 双环检测停止运行，其内部计数器保持（冻结）上一个值。该计数器仅在上电时，以及在电机使能期间某个采样回到容差范围内时被清零，而不会在电机失能时清零。
- **`DualLoopOn = 0`：** 整个双环堵转路径被跳过——计数器从不运行。
- **伪双环（[DualEncSwapOn](../../../11-control-tuning/02-dual-loop-control/DualEncSwapOn.md) = 1）：** 在伪双环激活期间检测被挂起，仅在真正双环接入期间运行（[DualLoopStat](../../../11-control-tuning/02-dual-loop-control/DualLoopStat.md) = 2）；因此在范围受限切换（[DualEncMode](../../../11-control-tuning/02-dual-loop-control/DualEncMode.md) = 1）下，它仅在真正双环范围内激活。当 `DualEncSwapOn = 0` 时，只要 `DualLoopOn` 非零它就始终激活。
- **`DualStuckTime = 0`：** 计数器在第一个超出容差的采样即达到限值，因此保护立即跳闸（无消抖）。
- **范围溢出：** 超出 `0…2147483647` 的写入会以超范围错误被拒绝；存储值保持不变。
- **清除故障：** ConFlt 码 1049 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍保留。
- **HWProtectBits / ProtectMask：** 双环堵转跳闸不可通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

## 示例

```text
ADualStuckTime[1]=4096   ; how long the feedback mismatch may persist before tripping
ADualStuckTime[1]        ; read back
```

## 参见

- [DualStuckVel](DualStuckVel.md) — 容许的速度差阈值
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1049（双环堵转）
