---
keyword: EventAckErr
summary: 在允许的状态下确认保留的硬件事件表错误，不会隐式重新使能。
availability:
  standalone: []
  central-i:
  - v5
can_code: 972
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
language: zh-CN
---
# EventAckErr

在允许的状态下确认保留的硬件事件表错误，不会隐式重新使能。

[EventError](EventError.zh.md) 保留首个可见错误，直至确认成功。需要远程确认或恢复时，EventAckErr 异步执行。按一致性规则轮询 [EventStatus](EventStatus.zh.md) 和 EventError；命令被接受不代表错误确认已完成。EventAckErr 不会加载或使能表。

正常 Complete 后，脉冲和翻转任务都须显式执行 EventAbort → 确认 Aborted → EventAckErr → 确认 Empty 才释放占用。主动 Abort 可能没有保留的首个错误，但确认命令仍用于释放 Aborted 占用。Complete 本身不允许直接确认。

已知引擎未使能时可清除本地准入错误，包括尚未开始使能的有效 Ready 会话；这种确认保留原 Ready 会话。如果首个准入错误之后又发生核心故障，清除准入错误会立即以新的发生序号发布该核心故障，不会短暂发布健康状态，因此可能还需再次确认。

正在确认、清理状态不确定、使能进行中或序列运行中时可能拒绝确认（立即错误 151，保留原诊断）。必要时先完成 [EventAbort](EventAbort.zh.md) 恢复。确认失败后，可先 Abort 并获得清理确认，再次请求确认。应检查错误发生序号和待处理标志，不能仅凭命令回复判断错误已清除。
