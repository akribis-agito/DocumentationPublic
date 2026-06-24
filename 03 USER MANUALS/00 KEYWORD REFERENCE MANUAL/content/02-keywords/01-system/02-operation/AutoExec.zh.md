---
keyword: AutoExec
summary: 置位后，在上电或重启时自动运行用户程序。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 208
attributes:
  access: rw
  scope: non-axis
  flash: true
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# AutoExec

置位后，在上电或重启时自动运行用户程序。

## 概述

`AutoExec = 1` 使控制器在上电时或软件重启后自动开始执行用户程序。`AutoExec = 0`（默认）则保持程序处于停止状态，直到被显式启动。

由于 `AutoExec` 保存至闪存，请在复位前运行 [Save](Save.md)，以使该设置在重新上电后保留。

## 工作原理

`AutoExec` 是一个单一标志（范围 0–1），在启动期间于固件已从闪存加载参数并初始化所存储的用户程序之后被读取一次。此时控制器**仅当以下两项**条件均满足时才自动启动程序：

| 条件 | 要求 |
|-----------|-------------|
| `AutoExec` | 等于 1 |
| 存在用户程序 | 闪存中存储有有效的用户程序 |

当两者均为真时，程序将在用户程序执行线程上启动，从其第一条指令开始 —— 完全如同已发出 [ProgRun](../../17-user-program/02-program-execution/ProgRun.md) 一样。若未存储任何程序，`AutoExec = 1` 不产生任何效果。该标志仅在启动时被读取，因此在运行时更改它不会启动或停止程序，直至下次上电或 [Reset](Reset.md)。

与本节中的其他关键字不同，`AutoExec` 是一个存储参数而非命令：它可在任何时刻读取或写入，包括在电机使能或运动中时。

## 示例

```text
AAutoExec=1          ; run the user program automatically at startup
AAutoExec            ; read the current setting
ASave                ; persist to flash; then AReset to apply
```

## 另请参阅

- [Save](Save.md) —— 将此标志持久化至闪存，以使其在重新上电后保留
- [Reset](Reset.md) —— 软件重新上电，在重启时重新读取 `AutoExec`
- [ProgRun](../../17-user-program/02-program-execution/ProgRun.md) —— 手动启动用户程序
