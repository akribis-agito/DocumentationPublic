---
keyword: EventAbort
summary: 请求解除硬件事件表使能并执行有界远程清理。
availability:
  standalone: []
  central-i:
  - v5
can_code: 971
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
# EventAbort

请求解除硬件事件表使能并执行有界远程清理。

EventType=3 时，EventAbort 与 EventOn=0 请求相同清理。EventOn 立即清零，取消待发布的使能状态，并请求远程禁止事件及清理。按一致性规则轮询 [EventStatus](EventStatus.zh.md)，确认 Aborted 且无待处理清理。命令回复、本地超时或 Fault 状态本身均不能证明远程输出已空闲。

最近操作结果变为 11（主动中止），但不创建或替换已保留的首个 [EventError](EventError.zh.md)；若此前没有错误，清理失败可建立错误。远程状态不确定时保留所有权并禁止配置写入，直至恢复确认。重复 Abort 请求恢复，不重放结果不确定的 APPEND。确认清理后用 [EventAckErr](EventAckErr.zh.md) 确认错误，再以 [EventLoad](EventLoad.zh.md) 创建新会话。

正常 Complete 后，脉冲和翻转任务都须显式 Abort 并确认 Aborted，再由 EventAckErr 释放至 Empty。PC 重连不能证明旧连接中的命令已经退出。若旧写操作仍可能到达，SDK 须保持 RecoveryRequired，直到证明确已退出；仅重新读取实时状态不能授权替代连接恢复或使能。
