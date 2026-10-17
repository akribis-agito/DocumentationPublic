---
keyword: LockEventStat
summary: 报告锁存/事件偏移的传统、有效、未计算或过期状态。
availability:
  standalone: []
  central-i:
  - v5
can_code: 833
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-17'
doc_revision: '2026.10'
language: zh-CN
---
# LockEventStat

报告 [LockEventMode](LockEventMode.md) 使用的偏移状态，是只读的轴级值。

| 值 | 含义 |
| --- | --- |
| `0` | 传统模式 0，在使能时学习偏移；此状态本身不证明已经完成测量。 |
| `1` | 适用的偏移有效。 |
| `-1` | 尚未计算偏移。 |
| `-2` | 以前计算的偏移已过期。 |

模式 1 在偏移失效后，需要在捕获源静止时执行 [LockEventInit](LockEventInit.md)。模式 2 在锁存和事件均关闭、相关配置变化或远端重连后，尝试自动重新计算。对于需要辅助计数器的捕获源，应在使能前检查结果状态。重复赋值模式 2 不会强制重新测量；`LockEventInit` 可以。

适用偏移尚未计算时，使能被错误 335 拒绝；偏移过期时，被错误 404 拒绝。辅助读取失败会使偏移保持无效。主绝对式编码器源不需要该偏移，状态可能保持不变。

状态 1 以远端 FPGA 兼容为前提。历史版本 v4.3.6 对未映射的辅助读取返回零，不能证明完成了该测量。参见 [远端 FPGA 兼容性](LockEventInit.md#remote-fpga-compatibility)。

另见：[LockEventInit](LockEventInit.md)、[LockEventMode](LockEventMode.md)、[LockEn](LockEn-AuxLockEn.md)、[EventOn](../../18-event-generation/EventOn.md)。
