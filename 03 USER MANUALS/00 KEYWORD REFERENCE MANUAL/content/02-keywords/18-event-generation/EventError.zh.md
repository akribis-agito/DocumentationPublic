---
keyword: EventError
summary: 读取首个保留的硬件事件表错误及其原始原因。
availability:
  standalone: []
  central-i:
  - v5
can_code: 974
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 13
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
language: zh-CN
---
# EventError

读取首个保留的硬件事件表错误及其原始原因。

可用索引为 **1–12**，索引 0 保留。适用字段以 LONG32 携带无符号 32 位模式。必须在 [EventStatus](EventStatus.zh.md) 发布序号括号内读取；分散读取可能混入不同发布版本。

| Index | Meaning |
|---|---|
| 1 | 归一化错误码 |
| 2 | 失败阶段 |
| 3 | 原始外部表索引；不适用为 0 |
| 4 | 命令操作码 |
| 5 | 原始 CiQStatus 传输结果 |
| 6 | 命令序号 |
| 7 | 会话令牌低 32 位 |
| 8 | 会话令牌高 32 位 |
| 9 | 发生时间（ms） |
| 10 | 远程原始 RESULT/FAULT 字 |
| 11 | Central-i 端口（从 1 开始） |
| 12 | 错误发生序号 |

## 编码

0 无；1 项数无效；2 位置/范围/排序；3 设置/坐标偏移未初始化；4 忙/所有权；5 不支持；6 超时；7 CRC；8 回复格式或身份不符；9 远程拒绝；10 实际存储表验证不符；11 主动中止（通常仅为最近结果）；12 端口断开；13 重置；14 位置源或配置变化；15 漏过目标；16 输出忙；17 过期；18 内部错误。

阶段：0 无，1 校验，2 BEGIN，3 APPEND，4 VERIFY，5 ARM，6 运行，7 快照，8 中止，9 恢复，10 错误确认。操作码：1 BEGIN，2 APPEND，3 VERIFY，4 ARM，5 ABORT，6 ACK_ERROR，7 SNAP。尚未提交匹配远程命令的本地拒绝，其命令序号为 0。[5] 保留原始传输结果，[10] 保留应用层结果/故障，两者不得互相替代。

首个可见错误元组保持不变，直至允许的 [EventAckErr](EventAckErr.zh.md) 完成。之后的 Busy 拒绝或 Abort 请求不会擦除它。EventStatus[21] 独立报告最近操作结果。准入错误之后被遮挡的核心故障，在准入错误确认后可成为新的错误发生项。无法映射或属于其他会话的远程行索引报告 0，不会错误地指向新表选择。
