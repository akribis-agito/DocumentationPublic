---
keyword: EventLoad
summary: 在使能前预加载并验证有限的硬件位置事件表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 970
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
# EventLoad

在使能前预加载并验证有限的硬件位置事件表。

## 可用性

Central-i 主控制器必须通过 [Identity](../01-system/01-status/Identity.zh.md) 宣告已验证事件表 API；连接的远程设备还必须独立宣告兼容的表引擎。[EventStatus](EventStatus.zh.md) 报告当前能力。仅有 API 能力位不代表远程硬件支持，也不代表事件速率已通过验证。

## 配置与加载

1. 保持所选位置源静止。配置位置源、EventType=3、位置表、脉宽及输出选择。设置 [LockEventMode](../03-encoder/03-event-based-feedback-logging/LockEventMode.zh.md)=1，执行 [LockEventInit](../03-encoder/03-event-based-feedback-logging/LockEventInit.zh.md)，确认 LockEventStat=1。EventLoad 不会自动学习源坐标偏移。
2. EventTableBeg..EventTableEnd 为包含两端的索引范围，共 **1–2048 项**。EventTableSrc 选择 EventTable 或 EventTableCor。原始控制器坐标及修正后的远程有符号 32 位计数器坐标均须按同一方向严格排序；不支持回绕及越界目标。
3. 若 EventTableSrc=1，上传所选输入后执行无参数的 [EventCorrect](EventCorrect.zh.md)，并确认成功完成；写入 EventTable 不会重新生成 EventTableCor。软件须在修正及回读前读取代次，回读全部三个所选输入列和设置，仅允许修正命令使位置源/表代次各增加一次（按32位回绕）。Source0 回读不允许代次变化。Ready 必须匹配最终代次。
4. 执行 EventLoad。命令被接受只表示异步加载开始，并不表示 Ready。控制器保留私有副本，写入所有记录，再由远程硬件对实际 RAM 内容验证 CRC。接受新的加载时清零 EventCntr 和 EventNextPos。
5. 按一致性读取规则轮询 EventStatus，确认目标会话的 Ready 状态及 Ready-valid 标志，再在位置源尚未到达首目标时写入 [EventOn](EventOn.zh.md)=1。恰好位于或已经越过首目标均被拒绝。只有获得新鲜的远程 Armed/Running 确认后，EventOn 才读回 1。

立即拒绝返回错误 151；异步失败保留于 [EventError](EventError.zh.md)。修正配置并在允许的状态下确认错误后才能重试。其他任务已占用引擎时，拒绝新加载并保留原任务。

## 执行与失效

此模式只执行有限突发，不进行运行时补表、隐式重复或 EventAlwaysOn 连续运行。硬件自主消耗已验证的表，不需要主机逐事件写入。所有目标退出且最终脉冲尾段结束后才 Complete；翻转模式可能保持最终输出电平，直到显式 Abort。EventCntr 是已退出目标数；EventNextPos 使用保留的原始控制器坐标，而非远程修正坐标。

更改已捕获的表、位置源、原点或脉冲配置会使会话失效并禁止后续事件，必须重新加载验证。控制器与远程设备链路重置后也必须重新加载。仅 PC 断开连接不保证健康的自主序列停止；应显式执行 [EventAbort](EventAbort.zh.md) 并确认结果。

现场验收目标是在 AGM800 + AGA101 和增量电机上支持 500 kHz–1 MHz 的目标事件。这是待验证要求，并非已测得额定值。2048 项按目标周期计算，在 500 kHz 为 4.096 ms，在 1 MHz 为 2.048 ms，不构成无限流。每秒一百万次翻转形成 500 kHz 方波。
