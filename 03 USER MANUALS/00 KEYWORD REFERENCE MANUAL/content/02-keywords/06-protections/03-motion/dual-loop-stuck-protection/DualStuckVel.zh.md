---
keyword: DualStuckVel
summary: 双环两路反馈之间容许的最大速度差。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 157
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# DualStuckVel

双环两路反馈之间容许的最大速度差。

## 概述

`DualStuckVel` 是双环配置中两路反馈之间容许的最大绝对速度差，单位为 count/s（count 指主反馈 / 位置环反馈）。如果该差值在连续 [DualStuckTime](DualStuckTime.md) 个周期内超过此值，则禁用轴——以捕捉两个编码器之间打滑或断裂的耦合。

## 工作原理

该检测在每个控制采样运行，但**仅当启用双环时**（`DualLoopOn` 非零）：

```text
if dual-loop is enabled
    if |Vel[2] - dual-loop speed| > DualStuckVel
        increment the dual-stuck counter
        if the dual-stuck counter has reached DualStuckTime
            turn the axis off and log the fault
    else
        reset the dual-stuck counter to 0
```

- 被比较的量是位置环反馈速度 `Vel[2]` 与内部计算的双环速度（以相同单位表示的速度环反馈）之间的绝对差。健康的耦合会使两个速度保持接近；打滑、断裂或标定错误的耦合会使它们偏离。
- 当该差值超过 `DualStuckVel` 时，内部计数器递增；任何处于容差内的采样都会将其复位为 `0`。该故障仅在连续运行 [DualStuckTime](DualStuckTime.md) 个采样时触发。
- 跳闸时轴被关闭，并由 [ConFlt](../../../07-status-and-faults/ConFlt.md) 记录 ConFlt 码 1049（双环堵转）。

默认值为 `40000` count/s。由于该保护受 `DualLoopOn` 控制，因此对单环轴无效。

### 边界情况

- **电机失能：** 双环检测不运行；该环路代码块仅在电机使能时运行，因此电机失能时内部计数器被保持（不清零）；它在上电时以及运行期间任何处于容差内的采样时被清零。
- **`DualLoopOn = 0`：** 整个双环堵转路径被跳过——无论取值如何，单环轴都不会被此保护跳闸。
- **模式相关性：** 只要 `DualLoopOn` 非零，双环堵转在所有运行模式下都会运行（它不会被那些会绕过[电机堵转](../motor-stuck-protection/00-overview.md)的电流/力/自动定相模式所旁路）。
- **伪双环（[DualEncSwapOn](../../../11-control-tuning/02-dual-loop-control/DualEncSwapOn.md) = 1）：** 该检测仅在真正双环实际接入期间运行——即 [DualLoopStat](../../../11-control-tuning/02-dual-loop-control/DualLoopStat.md) = 2 期间。在伪双环中两个环路使用单一反馈源，因此不存在双反馈失配可供检测，保护被挂起。当 `DualEncSwapOn = 0` 时，只要 `DualLoopOn` 非零保护就始终激活。在范围受限切换（[DualEncMode](../../../11-control-tuning/02-dual-loop-control/DualEncMode.md) = 1）下也适用相同条件：检测仅在真正双环范围内激活。
- **范围溢出：** 超出 `0…1300000000` 的写入会以超范围错误被拒绝；存储值保持不变。
- **清除故障：** ConFlt 码 1049 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍保留。
- **HWProtectBits / ProtectMask：** 双环堵转跳闸不可通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

## 示例

```text
ADualStuckVel[1]=40000   ; max tolerated feedback velocity mismatch (count/s)
ADualStuckVel[1]         ; read back the threshold
```

## 另请参阅

- [DualStuckTime](DualStuckTime.md) — 失配可持续的时长
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1049（双环堵转）
