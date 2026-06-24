---
keyword: ForceMotorOn
summary: 在换相完成之前使能电机，仅用于电流环整定。
availability:
  standalone: []
  central-i:
  - v5
can_code: 829
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ForceMotorOn

在换相完成之前使能电机，仅用于电流环整定。

## 概述

`ForceMotorOn` **即使在轴尚未换相（定相）的情况下**也会使能电机。通常控制器会拒绝使能未定相的轴，并且一旦发现缺少定相，便会立即将已使能的轴跳闸关闭，因为驱动未定相的电机可能会向单个绕组注入直流电流。`ForceMotorOn` 是对该规则的刻意、受保护的例外：它用于**电流环整定**，在该场景下，你需要在执行定相之前、电机处于电流控制保持状态时使功率级带电。

由于它会覆盖一项安全互锁，因此该使能受到保护。写入 `ForceMotorOn` 仅在写入携带特定保留值 **`555851`** 时生效；任何其他值都会被以错误 `148` 拒绝，且电机不会被强制使能。读取 `ForceMotorOn` 会返回当前状态：处于强制使能（未定相）状态时为 `1`，否则为 `0`。

可用于 central-i（v5）。

## 工作原理

`ForceMotorOn` 不会替代正常的使能路径——它只从中移除一项特定的预条件。当你写入保留值时：

1. 如果轴尚未定相，则该轴的 `ForceMotorOn` 被置为 `1`，并且（如果该轴当前处于关闭状态）控制器会运行标准的 [MotorOn](MotorOn.md) 使能序列。其他所有 [MotorOn](MotorOn.md) 预条件以及使能后步骤仍照常完整执行——仅**换相完成**这一要求被豁免（与生产老化测试所用的豁免相同）。
2. 在 `ForceMotorOn = 1` 期间，禁用未定相轴的保护被抑制，因此该轴可在不进行定相的情况下保持电流控制下的使能状态。
3. 如果该轴属于龙门对且其中某个成员未换相，则会先放弃龙门控制，以便在单个轴上进行强制使能。

该豁免严格绑定于强制状态。一旦电机关闭（通过命令或任何故障），`ForceMotorOn` 即返回 `0`，正常互锁随即恢复生效：在 `ForceMotorOn = 0` 时被发现未定相的已使能轴会被自动禁用，并记录 [ConFlt](../../07-status-and-faults/ConFlt.md) = `1080`（未检测到定相）。要再次强制使能电机，你必须重新发出该保留值。

`ForceMotorOn` **不会**绕过任何其他使能检查——硬件健康状态、通信、浪涌旁路、母线放电及保护条件仍然适用，与 [MotorOn](MotorOn.md) 完全相同。它只允许你在定相之前操作电流环；它并非在未定相轴上运行位置或速度运动的途径。

## 示例

为电流环整定使未定相轴带电（电流控制模式）：

```text
AOperationMode=1     ; current control mode (writable only while disabled)
AForceMotorOn=555851 ; enable the motor without phasing (reserved value required)
AForceMotorOn        ; expect 1 = forced on (un-phased)
AMotorOn             ; expect 1 = servo on
                     ; ... perform current-loop tuning ...
AMotorOn=0           ; disable; ForceMotorOn returns to 0 automatically
```

### 边界情况

- **错误的写入值** —— 除 `555851` 以外的任何值都会被以错误 `148` 拒绝；电机不会被强制使能。
- **已定相** —— 如果轴已换相，则没有可豁免的项；适用正常的 [MotorOn](MotorOn.md) 路径。
- **其他预条件仍失败** —— 强制使能仍会运行完整的 [MotorOn](MotorOn.md) 预检查链（硬件、通信、浪涌、保护）；其中任何失败仍会拒绝使能。
- **电机关闭时自动清除** —— 关闭电机，或任何使其禁用的故障，都会将 `ForceMotorOn` 复位为 `0`；未定相保护随即重新置位。
- **未定相跳闸** —— 如果在 `ForceMotorOn = 0` 时发现某个已使能轴未定相，则该轴会被禁用，并记录 [ConFlt](../../07-status-and-faults/ConFlt.md) = `1080`（未检测到定相）。参见 [MotorReason](../../07-status-and-faults/MotorReason.md)。
- **龙门** —— 在强制使能进行之前，会为未定相的龙门对放弃龙门控制。
- **预期用途** —— 仅用于电流环整定。不要用它在未定相电机上尝试位置/速度运动。
- **平台** —— 仅限 v5 central-i。

## 另请参阅

- [MotorOn](MotorOn.md) —— 正常使能/禁用；`ForceMotorOn` 仅豁免其换相完成预条件
- [CanMotorOn](CanMotorOn.md) / [CanMotorOnRes](CanMotorOnRes.md) —— 预检查正常使能是否会成功
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 当未定相轴在未强制的情况下被使能时记录未定相故障
- [MotorReason](../../07-status-and-faults/MotorReason.md) —— 轴上次被禁用的原因
- [OperationMode](OperationMode.md) —— 为电流环整定选择电流控制模式
