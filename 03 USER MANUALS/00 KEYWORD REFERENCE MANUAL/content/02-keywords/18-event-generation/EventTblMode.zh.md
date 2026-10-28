---
keyword: EventTblMode
summary: 选择预加载硬件事件表使用公共设置还是逐行设置。
availability:
  standalone: []
  central-i:
  - v5
can_code: 975
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-29'
doc_revision: '2026.10'
language: zh-CN
---
# EventTblMode

在实现原有引擎预加载的 AGM800 固件中（`EventType=3`），在 [EventLoad](EventLoad.md) 前选择脉冲宽度与输出设置的解析方式。

| 值 | 设置 |
|----|------|
| 0（默认） | 从首个所选行 `EventTableBeg` 解析设置，并用于整个运行。 |
| 1 | 按原有软件表的宽度继承规则解析每行设置；仅当解析后的设置字改变时，才传送新的设置字。 |

首行决定全局宽度或翻转模式、以及宽度继承的规则，见 [EventTableWid](EventTableWid.md)；输出选择见 [EventTableSel](EventTableSel.md)。所选范围可以从任一有效索引开始，不必为 1。两种模式使用相同的位置、`EventTableSrc`、表偏移及原有校正和坐标转换。

加载前设置此参数。该参数不保存到闪存，准备或运行期间不可修改。先用 `EventOn=0` 停止，再修改并重新加载。每次运行都预加载所选范围，最多 2048 行，不提供保留窗口模式。

对于此硬件预加载路径，首个所选行决定整个运行是否采用翻转模式：该行宽度为 0，或为 -1 且 `EventPulseWid=0` 时，两种模式均使每次事件翻转输出。后续行的宽度不会将脉冲运行改为翻转模式。 输出极性同样在整个运行期间保持不变：首个解析后宽度的符号适用于所有行，模式 1 只改变脉冲时长和输出选择。在脉冲模式下，转换为零个硬件单位的宽度会使 EventLoad 在使能前失败；继承和量化规则参见 EventTableWid。

```text
AEventOn=0
AEventType=3
AEventTblMode=0
; 配置并写入所选位置、宽度和输出行。
AEventLoad
AEventStatus        ; 等待 Ready（位 1），且 Fault（位 4）为 0
AEventOn=1
```

此参数不改变其他事件类型的行为。
