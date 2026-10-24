---
keyword: EventStatus
summary: 读取硬件事件表能力、进度和状态的一致 RAM 发布映像。
availability:
  standalone: []
  central-i:
  - v5
can_code: 973
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 25
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
# EventStatus

读取硬件事件表能力、进度和状态的一致 RAM 发布映像。

可用索引为 **1–24**，索引 0 保留。每项为 LONG32。位域、CRC、令牌和序号按无符号 32 位模式解释，即使传输显示为有符号负数。读取的是 RAM 发布映像，不会为每项读取触发远程命令。

## 一致性读取

依次读取首序号 [1]、载荷 [2]..[23]、[EventError](EventError.zh.md)[1]..[12]、尾序号 [24]，再读一次首序号 [1]。仅当三次序号相同且为偶数时接受。客户端须有界重试；不完整回复、奇数、序号变化或超时均不构成有效快照。配置失效可立即将发布序号标为奇数。处于稳定且无待处理操作的 Empty、Ready、Complete、Aborted 或 Fault 时，仅遥测值（包括命令序号及年龄）变化导致的发布间隔至少为五秒。其他占用活动按 100 ms 合并，未占用空闲遥测按 1 s 合并。状态、新鲜/Ready-valid 标志、会话/配置、错误及重连失效立即发布。读取不会锁存数据或推迟发布。

一次完整尝试恰好使用 37 个实时请求。若每次尝试在两秒内完成，应在有界总期限内立即重试一次被打断的读取；单次周期性终态遥测发布不会打断这两次尝试。安全状态变化仍可能阻止成功，此时须返回不可用，不能使用缓存 Ready。Running 的变化可能快于慢速串口的观察速度，可在之后读取终态 Complete。SDK 须验证实际传输延迟；上述间隔不是波特率保证。

年龄保守地从远程 SNAP 请求开始计算**至发布时刻**，并非至读取完成时刻或当前时间。保留的较小年龄值不能证明快照持续新鲜。使能仍须获取新的匹配远程快照，Complete 仍须来自新鲜的最终查询。

| Index | Meaning |
|---|---|
| 1 | 发布序号（首） |
| 2 | 状态 |
| 3 | 标志 |
| 4 | 支持容量；不可用时为 0 |
| 5 | 请求项数 |
| 6 | 已接受项数 |
| 7 | 已提交项数 |
| 8 | 已退出目标数 |
| 9 | 剩余目标数 |
| 10 | 占用项数 |
| 11 | 会话令牌低 32 位 |
| 12 | 会话令牌高 32 位 |
| 13 | 预期 CRC |
| 14 | RAM 实际存储 CRC |
| 15 | 远程命令序号 |
| 16 | 快照年龄（ms）；缺失为 0xFFFFFFFF |
| 17 | 远程时钟（Hz）；不支持时为 0 |
| 18 | 所选位置源 |
| 19 | 配置代次 |
| 20 | 主坐标代次 |
| 21 | 最近操作的归一化结果 |
| 22 | 忙输出掩码 |
| 23 | 远程原始 CAPS |
| 24 | 发布序号（尾） |

状态：0 Empty，1 Loading，2 Verifying，3 Ready，4 Armed，5 Running，6 Complete，7 Aborted，8 Fault。标志：位 0 支持，位 1 有新鲜远程快照，位 2 Ready-valid，位 3 保留错误，位 4 操作待完成。支持不等于 Ready-valid。接受 Armed/Running 或 Complete 前须确认新鲜且匹配会话的快照。Complete 需要全部目标退出且末脉冲结束；Fault 不等于已确认 Abort。[21] 使用 EventError 的归一化编码；11 表示主动中止请求，不一定产生新的保留错误。

加载与使能流程见 [EventLoad](EventLoad.zh.md)，恢复见 [EventAbort](EventAbort.zh.md)。
