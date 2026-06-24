---
keyword: EventSuppress
summary: 暂时抑制远程驱动器比较硬件中事件脉冲生成的命令。
availability:
  standalone: []
  central-i:
  - v4
can_code: 188
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EventSuppress

暂时抑制远程驱动器比较硬件中事件脉冲生成的命令。

## 概述

`EventSuppress` 是一条命令，用于通知远程驱动器中的位置比较引擎抑制事件输出生成。它与事件生成功能的其余部分（[EventOn](EventOn.md)、[EventType](EventType.md)、[EventPulseWid](EventPulseWid.md)）配合使用：上述关键字负责使能并整形轴经过配置的比较位置时触发的输出脉冲，而 `EventSuppress` 是向硬件发出抑制控制的命令，从而阻止脉冲输出。

该功能属于 Central-i 特性：命令被转发至远程驱动器的比较硬件。对于不具备该远程比较硬件的产品，该命令无效。它不携带数值，也不存储持久状态——发出后即在远程驱动器上生效，并报告执行完成。

此关键字存在于 **central-i v4** 上，不属于 v5 关键字集。

## 工作原理

发出 `EventSuppress` 时，控制器以瞬时动作向远程驱动器的比较硬件发送抑制控制——即先置位抑制控制，再释放。命令在远程消息排队后即报告成功；该命令没有可读的开/关状态（读取该关键字不是状态查询，而是一条命令）。

将 `EventSuppress` 与事件生成配置配合使用：通过 [EventOn](EventOn.md) 使能生成，通过 [EventPulseWid](EventPulseWid.md) 整形脉冲，然后在需要中止当前正在输出的脉冲时发出 `EventSuppress`。

抑制动作为边沿触发，作用于当前正在输出的脉冲：若命令到达时脉冲处于激活状态，比较硬件将立即结束该脉冲，将输出恢复到空闲电平，并清除剩余宽度计数。由于它仅作用于进行中的脉冲，`EventSuppress` 是对当前输出的瞬时中止，而非对未来事件的阻断；下一个配置的位置交叉点将正常触发。若命令发出时没有脉冲处于激活状态，则该命令无可见效果。

## 示例

```text
AEventSuppress       ; suppress event-pulse generation in the remote drive
```

## 另请参阅

- [EventOn](EventOn.md) — 使能事件生成
- [EventType](EventType.md) — 选择比较方案（单事件 / 按间距 / 按表格）
- [EventPulseWid](EventPulseWid.md) — 事件输出脉冲的波形
- [EventSelect](EventSelect.md) — 事件输出的路由
