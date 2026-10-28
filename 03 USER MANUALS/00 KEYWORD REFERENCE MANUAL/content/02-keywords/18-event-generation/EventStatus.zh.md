---
keyword: EventStatus
summary: 报告硬件表加载与运行的精简状态标志。
availability:
  standalone: []
  central-i:
  - v5
can_code: 973
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-28'
doc_revision: '2026.10'
language: zh-CN
---
# EventStatus

此只读标量标志用于 AGM800 原有引擎预加载（`EventType=3`）。它是精简状态字，不是旧验证引擎的状态数组。

| 位 | 掩码 | 含义 |
|----|------|------|
| 0 | 1 | Loading：固件正在准备或传输行。 |
| 1 | 2 | Ready：完整的所选表已通过最终准入检查。 |
| 2 | 4 | Enabled：硬件表运行已使能。 |
| 3 | 8 | Complete：本次运行已完成。 |
| 4 | 16 | Fault：加载或运行失败；停止后须显式重新加载。 |

Loading 是固件本地状态。Ready/Fault 及运行状态使用正常的硬件周期状态，无需为每个事件自动离线读取计数或下一位置。`EventCntr` 在完成后刷新一次；需要中间计数时可显式查询。

配置完成后执行 [EventLoad](EventLoad.md)，等待 Ready 为 1 且 Fault 为 0，再用 `EventOn=1` 使能。`EventOn=0` 停止或取消并丢弃任务。重连不会恢复运行。相关修改会使就绪状态失效，运行期间不允许修改。无需错误确认命令。

硬件表模式不能使用 1/T，因此 `Vel[4]=0`。其他事件类型保持原有状态含义。

```text
AEventStatus
AEventCntr
```
