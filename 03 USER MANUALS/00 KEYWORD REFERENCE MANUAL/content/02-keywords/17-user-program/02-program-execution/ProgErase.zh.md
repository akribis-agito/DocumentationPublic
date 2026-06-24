---
keyword: ProgErase
summary: 从控制器内存中清除已存储的用户程序。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 299
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgErase

从控制器内存中清除已存储的用户程序。

## 概述

`ProgErase` 从控制器内存中清除已存储的用户程序，是通过 [DownloadUPBin](DownloadUPBin.md) 下载程序的逆操作。由于该命令会移除线程正在执行的程序，因此在电机使能或轴运动中时将被禁止执行，且在任意线程仍处于活动状态时也无法运行。它是一个非轴命令，不保存至闪存。

## 工作原理

`ProgErase` 首先检查所有线程；如果有任一线程仍在运行，则命令将被拒绝并返回错误，且不进行任何清除操作——请在清除前使用 [ProgHaltAll](ProgHaltAll.md) 停止所有线程（或将其复位）。当命令成功执行时，它将：

- 将控制器标记为没有已存储的程序，使 [ProgStat](ProgStat.md) 对每个线程读取为 `-1`，[ProgStatAll](ProgStatAll.md) 读取为 `-1`。
- 将每个线程的 [ProgPointer](ProgPointer.md) 设置为 `-1`（无程序）。
- 从控制器的非易失性程序内存中清除程序。

清除后，需要程序才能执行的命令——例如 [ProgRun](ProgRun.md)、[ProgReset](ProgReset.md) 和 [ProgInfo](ProgInfo.md)——将被拒绝，直到通过 [DownloadUPBin](DownloadUPBin.md) 下载新程序。注意，`ProgErase` 除了要求无线程运行外，还要求电机关闭且轴已停止。

## 示例

```text
AProgErase           ; erase the stored user program (motor off, not in motion)
```

## 另请参阅

- [DownloadUPBin](DownloadUPBin.md) — 向控制器下载已编译的用户程序
- [ProgHaltAll](ProgHaltAll.md) — 在清除前停止所有线程
- [ProgResetAll](ProgResetAll.md) — 停止所有线程并复位指针和栈
- [ProgInfo](ProgInfo.md) — 查询当前已存储程序的信息
