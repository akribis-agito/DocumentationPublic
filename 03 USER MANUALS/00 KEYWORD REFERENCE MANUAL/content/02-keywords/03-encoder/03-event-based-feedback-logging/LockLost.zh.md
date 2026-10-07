---
keyword: LockLost
summary: 统计在 Central-i 主站上未能单独成为一次捕获的锁存采样。
availability:
  standalone: []
  central-i:
  - v5
can_code: 918
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-07'
doc_revision: '2026.09'
language: zh-CN
---
# LockLost

统计在 Central-i 主站上未能单独成为一次捕获的锁存采样。

## 概述

`LockLost` 是与 [LockCntr](LockCntr-AuxLockCntr.md) 配套的只读计数器。`LockCntr` 统计已捕获的位置；`LockLost` 统计其位置无法被单独捕获的触发采样，原因是远程单元仅保留最近一个边沿的位置。在一连串触发边沿之后，请同时读取两者：`LockLost` 不为零，表示即使 `LockCntr` 已前进，[LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) 中仍缺少部分边沿。

当记录（[LockEn](LockEn-AuxLockEn.md)）从禁用状态被启用时，`LockLost` 与 `LockCntr` 一同复位为 `0`。它按轴设置，为 32 位，不保存至闪存，仅在 Central-i 主站上可用。

## 工作原理

远程单元每个控制周期（约 61 µs）对触发采样一次。它锁存该周期内最后一个边沿的位置，不保留其他信息，因此同一周期内较早边沿的位置无法恢复。包含两个或更多边沿的周期会作为错误采样上报给主站。主站通过离线邮箱读取所保留的位置，这需要若干个控制周期才能得到应答，而在此期间到达的边沿会替换下一次读取将返回的位置。

遇到下列任一采样时，`LockLost` 前进一个：

| 情形 | `LockCntr` | `LockLost` |
|---|---|---|
| 一个控制周期内有一个边沿 | +1 | 0 |
| 一个控制周期内有两个或更多边沿 | +1，位置为最后一个边沿的位置 | +1 |
| 上一个边沿的读取尚未完成时到达一个边沿 | 该读取得到应答后 +1（该边沿在之后被读取，并作为独立条目记录） | 0 |
| 后续读取仍在等待时又出现一个边沿 | 该边沿本身不使其变化，它与后续读取共用一次捕获 | +1 |
| 读取尚未完成时出现包含多个边沿的控制周期 | 后续读取得到应答后 +1 | +1 |
| 远程未返回位置，或未在规定时间内应答 | 0 | +1 |
| 绝对式或 SinCos 主编码器，一个控制周期内有两个或更多边沿 | +1，位置为该周期读取到的位置 | +1 |

`LockLost` 统计的是控制周期而非边沿：包含四个边沿的周期使 `LockCntr` 加一、`LockLost` 加一。该周期捕获的位置是最后一个边沿的位置。

[LockTimeTable](LockTimeTable-LockTimeTabB.md) 记录的是读取到该位置的控制周期，因此在上一次应答之后才被读取的边沿记录的是那个较晚的周期，而不是该边沿本身所在的周期。

要将每个边沿作为独立条目记录，请使触发边沿之间保持足够间隔。在以固定间隔触发四个事件的台架测量中，间隔不小于 200 µs 时每个边沿都被记录。

## 示例

```text
ALockLost            ; read the number of lock samples that were not captured on their own
ALockEn=0
ALockEn=1            ; LockCntr and LockLost both return to 0
```

## 另请参阅

- [LockCntr](LockCntr-AuxLockCntr.md) — 统计已捕获的位置，并作为历史数组的索引
- [LockEn](LockEn-AuxLockEn.md) — 启用记录；将 `LockLost` 复位为 0
- [LockSrc](LockSrc-AuxLockSrc.md) — 定义触发事件
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — 历史数组
