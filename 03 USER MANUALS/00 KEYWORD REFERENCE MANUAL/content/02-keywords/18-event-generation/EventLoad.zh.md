---
keyword: EventLoad
summary: 准备所选硬件事件表，但不使能输出。
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
last_updated: '2026-10-28'
doc_revision: '2026.10'
language: zh-CN
---
# EventLoad

对于 AGM800 `EventType=3`，此无参数命令在后台分步预加载 `EventTableBeg..EventTableEnd`（包含首尾行），范围为 1–2048 行。它不使能输出，也不启动运动。

先配置位置、[EventTblMode](EventTblMode.md)、宽度、输出及位置源。使用校正源时，先运行 [EventCorrect](EventCorrect.md) 并检查 `EventTableCor`。加载前在静止时按正常流程建立锁存与事件的坐标对齐。加载器仅应用一次原有表偏移及硬件坐标转换。

读取 [EventStatus](EventStatus.md)：Loading 为位 0、Ready 为位 1、Fault 为位 4。只有完整加载达到 Ready 后，才接受 `EventOn=1`。失败、中断或结果不确定的传输不会自动使能。

`EventOn=0` 取消或停止并丢弃已准备的数据。每次运行都重新预加载所选范围。相关修改会使就绪数据失效，运行期间不允许修改。断线将丢弃任务，不会在重连后接管或恢复。失败通过原有命令及通信错误报告，无需 EventAbort/EventAckErr/EventError 确认流程。

若某所选输出的脉冲与恢复过程不能在下一事件前结束，本次运行报错。应停止、修正设置，再显式重新加载；不会延迟排队事件，也不会自动重试。

```text
AEventOn=0
AEventType=3
AEventTableBeg=5
AEventTableEnd=100
AEventTblMode=0
; 加载前写入行并配置位置源及设置。
AEventLoad
AEventStatus        ; 等待 Ready 并检查 Fault
AEventOn=1          ; 仅在 Ready 后使能
AEventOn=0          ; 停止并丢弃；再次运行前重新加载
```
