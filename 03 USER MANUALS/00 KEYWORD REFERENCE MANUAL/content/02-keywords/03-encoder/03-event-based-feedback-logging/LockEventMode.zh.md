---
keyword: LockEventMode
summary: 选择锁存/事件偏移的传统、手动或自动学习模式。
availability:
  standalone: []
  central-i:
  - v5
can_code: 831
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -1
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-17'
doc_revision: '2026.10'
language: zh-CN
---
# LockEventMode

选择控制器如何学习控制器位置与远端捕获计数器之间的偏移。保存的默认值为 `0`。

| 值 | 行为 |
| --- | --- |
| `0` | 传统模式：每次 `LockEn` 或 `EventOn` 从 0 变为 1 时学习偏移。`LockEventStat` 报告 0。 |
| `1` | 手动模式：捕获源静止时执行 [LockEventInit](LockEventInit.md)，然后再使能锁存或事件。 |
| `2` | 自动模式：对于需要辅助计数器的捕获源，在锁存和事件均关闭时，进入模式 2、修改受跟踪的相关配置或重连后完成配置重放时，重新计算偏移。 |

数值范围保留 `-1` 以兼容旧配置，但它不是受支持的工作模式。请使用 0、1 或 2。

模式 2 下重复写入相同值不会强制重新测量。在模式 1 和模式 2 下，都可以执行 `LockEventInit` 显式刷新偏移。测量时捕获源必须静止。先设置 `LockEn=0`、`EventOn=0` 再配置捕获源；对于需要辅助计数器的源，使能前应检查 [LockEventStat](LockEventStat.md)。

模式 1 和 2 下，锁存或事件使能期间修改受跟踪的捕获源配置或方向，会被错误 403 拒绝。如果相关配置在使能后已使偏移发生变化，此时切换到模式 1 或 2 也会被拒绝。请先关闭两项功能再修改配置。未计算偏移时，使能被错误 335 拒绝；偏移过期时，使能被错误 404 拒绝。远端读取失败会使偏移保持无效，而不会将旧数据标记为有效。

模式 1 在偏移失效后需要显式初始化。模式 2 在未使能时以及重连后尝试自动重新计算；请确认状态，不要仅凭赋值命令成功就认为已完成测量。主绝对式编码器源不需要该辅助计数器偏移，状态可能保持不变。

请使用兼容的远端 FPGA，参见 [辅助寄存器兼容性要求](LockEventInit.md#remote-fpga-compatibility)。读取未映射寄存器得到零，不等于测得了偏移。

```text
ALockEn=0
AEventOn=0
ALockEventMode=2
; 在捕获源静止时配置它
ALockEventInit        ; 模式 2 下可选的显式刷新
ALockEventStat        ; 对需要辅助计数器的源，要求状态为 1
ALockEn=1
```

另见：[LockEventInit](LockEventInit.md)、[LockEventStat](LockEventStat.md)、[LockEn](LockEn-AuxLockEn.md)、[EventOn](../../18-event-generation/EventOn.md)。
