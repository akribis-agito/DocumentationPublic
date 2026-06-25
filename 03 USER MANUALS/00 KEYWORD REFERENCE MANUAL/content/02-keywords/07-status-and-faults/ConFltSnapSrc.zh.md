---
keyword: ConFltSnapSrc
summary: 配置在发生故障时哪些参数被捕获到 ConFltSnapVal。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 528
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
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
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# ConFltSnapSrc

配置在发生故障时哪些参数被捕获到 ConFltSnapVal。

## 概述

`ConFltSnapSrc` 选择当控制器故障发生时，哪些参数被捕获（抓拍）到 [ConFltSnapVal](ConFltSnapVal.md)。这让你能够在轴故障的确切瞬间冻结最相关的诊断数据，从而事后检查系统状态，而不必去读取此后已经发生变化的参数。

它是一个轴范围数组，可读写并保存至闪存，因此你的快照配置可在重新上电后保持。它提供 **4 个用户可配置槽位**，索引为 `[1]` 至 `[4]`（索引 `[0]` 未使用，以便索引从 1 开始）。这四个槽位填充 `ConFltSnapVal[1]…[4]`；`ConFltSnapVal` 其余的槽位由一组固定的系统参数自动填充，这些参数不在此处配置（参见 [ConFltSnapVal](ConFltSnapVal.md)）。

## 工作原理

每个槽位保存一个**复合 CAN 代码**，用以指定要捕获的参数，而不仅仅是一个裸 CAN 代码。该复合值编码了三个字段：

| Bits | 字段 |
|---|---|
| 0–9 | 参数的 CAN 代码 |
| 10–14 | 轴号（0 = A；对非轴参数忽略） |
| 16–31 | 数组索引（用于数组参数；标量使用 0） |

对于当前轴上的标量轴参数，复合代码就是纯 CAN 代码本身，因此 `AConFltSnapSrc[1]=33` 选择 [StatReg](StatReg.md)（CAN 代码 33）。向某个槽位写入 `0` 会禁用它（其 `ConFltSnapVal` 条目保持为 `-1`）。

当你设置 `ConFltSnapSrc` 时，固件会：

- 校验复合代码（CAN 代码必须存在、必须是参数而非命令，且轴/数组索引必须在范围内；否则写入会因快照配置错误而被拒绝）。
- 为每个槽位解析并存储一个内部指针外加一个缩放因子，使故障时的捕获能够快速完成。如果所选参数带有缩放，捕获的值以原始（内部）单位存储。
- **将所有 [ConFltSnapVal](ConFltSnapVal.md) 条目重置为 `-1`**，丢弃任何先前捕获的快照。请在你想诊断的故障之前配置好源，而不是在故障之后。

## 示例

```text
AConFltSnapSrc[1]=33     ; capture StatReg (CAN code 33) into ConFltSnapVal[1] at the next fault
AConFltSnapSrc[2]=0      ; disable the second slot
AConFltSnapSrc[1]       ; query which parameter the first slot will capture
AConFltSnapSrc          ; query the whole snapshot source list
```

## 另请参阅

- [ConFltSnapVal](ConFltSnapVal.md) — 捕获的值（此处的槽位 1–4，外加固定的系统参数）
- [ConFlt](ConFlt.md) — 触发快照的故障码
- [StatReg](StatReg.md) — 常见的捕获目标（CAN 代码 33）
