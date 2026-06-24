---
keyword: ProgInfo
summary: 报告已加载用户程序中嵌入的信息字符串。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 297
attributes:
  access: ro
  scope: non-axis
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgInfo

报告已加载用户程序中嵌入的信息字符串。

## 概述

`ProgInfo` 返回已加载用户程序中存储的信息字符串：CRC 值、日期、CUP 文件名，以及通过 `#information` 编译器指令提供的自由文本信息。用于识别控制器上当前驻留的程序（与 [ProgErase](ProgErase.md) 和 [DownloadUPBin](DownloadUPBin.md) 对应，后两者分别用于删除和加载程序）。该命令为非轴状态命令，不保存至闪存。

## 工作原理

程序下载时，程序代码之前会存储一个包含标识信息的头部——包括 CRC、构建日期、源文件名、`#information` 文本，以及任务、函数、全局变量和事件的内部表。`ProgInfo` 将该头部流式返回给请求接口（程序运行时使用的自由文本打印字符串不包含在报告中）。该命令需要已加载的用户程序；若未加载程序，则命令被拒绝。报告的 CRC 是控制器用于验证程序完整性的值，因此可作为在运行前确认预期程序已正确驻留的可靠方式。

## 示例

```text
AProgInfo           ; report CRC, date, CUP file name and #information text
```

## 另请参阅

- [DownloadUPBin](DownloadUPBin.md) — 下载已编译的用户程序
- [ProgErase](ProgErase.md) — 擦除已存储的用户程序
- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
