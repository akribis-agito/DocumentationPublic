---
keyword: PStatParams
summary: 列出每次周期性统计发送所包含的参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 483
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# PStatParams

列出每次周期性统计发送所包含的参数。

## 概述

`PStatParams` 指定每次周期性程序状态发送所包含的控制器参数（最多 **20 个条目**，索引 `[1]`–`[20]`）。每个元素标识一个在 [PStatInterval](PStatInterval.md) 设定的间隔内采样并发送的参数，通过 [PStatPort](PStatPort.md) 选择的端口传输，当 [PStatOn](PStatOn.md) 启用流式传输时生效。它是非轴数组参数，保存至闪存（默认值 `0`）。

## 工作原理

每个元素保存一个[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)，用于指定要流式传输的确切参数——与快照和事件触发源所用的编码方式相同：

| 位 | 字段 |
|---|---|
| 0–9 | 参数的 CAN 代码 |
| 10–14 | 轴号（0 = A；非轴参数忽略） |
| 16–31 | 数组索引（数组参数使用；标量使用 0） |

对于 A 轴上的标量参数，复合代码即为普通 CAN 代码。值为 `0` 的条目将被跳过，未使用的槽位保持 `0` 即可。设置 `PStatParams` 时，控制器会验证每个非零条目；若任何条目所指定的参数无法解析，则拒绝该配置—— [PStatOn](PStatOn.md) 读回负值（错误值），问题条目被清除。每次发送按索引顺序传输每个有效条目的当前值。

## 示例

```text
APStatParams[1]=<complex CAN code of parameter to stream>    ; 第一个流式传输参数
APStatParams[2]=0    ; 将第二个槽位置为未使用
APStatParams         ; 读取完整的流式传输参数列表
```

## 另请参阅

- [PStatOn](PStatOn.md) — 启用/禁用周期性统计流式传输
- [PStatPort](PStatPort.md) — 用于流式传输的通信端口
- [PStatInterval](PStatInterval.md) — 发送间隔
