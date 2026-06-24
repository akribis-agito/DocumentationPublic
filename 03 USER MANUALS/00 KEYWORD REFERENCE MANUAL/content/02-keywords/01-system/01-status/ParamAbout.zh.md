---
keyword: ParamAbout
summary: 函数，返回由 CAN 代码选定的单个参数的最小值、最大值与默认值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 499
attributes:
  access: rw
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
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ParamAbout

函数，返回由 CAN 代码选定的单个参数的最小值、最大值与默认值。

## 概述

`ParamAbout` 是一个函数，返回单个参数的**有效范围与默认值**——其最小值、最大值和默认值——并附带一个标识所连接控制器的代码。它让上位机软件和诊断工具能够在运行时发现参数的限值，而无需将其硬编码。与转储每个参数的 [About](About.md) 不同，`ParamAbout` 仅针对一个参数。

## 工作原理

要检查的参数通过将其 **CAN 代码**作为函数参数传入来选定，采用赋值形式 `AParamAbout=<CAN code>`（有效范围 0–1023 与控制器的 CAN 代码空间相匹配）。该实参为必需项：这是一个需要参数的函数，因此不带实参调用它将以错误被拒绝，而超出 0–1023 的 CAN 代码将以超范围被拒绝。回复由提供实参的同一次调用产生——没有单独的读取步骤。固件在其关键字表中查找该代码，并构建一个包含以下内容的回复：

- 一个固定标签，
- 一个标识所连接控制器类型的字（对于直接连接的独立单元，或通过 Central-i 访问时的 Central-i 主控 / 远程驱动器），
- 参数的**最小值**、**最大值**和**默认值**。

若所选关键字为非轴对象，则请求上的任何轴前缀将被忽略。回复对以太网采用字节分段、对 CAN/RS-232 采用字分段，因此相同的值会以各传输方式所期望的编码交付。对于限值因端口而异而非固定的 Central-i 参数，回复在可用时使用端口的参数属性，否则使用常量表限值。

## 示例

```text
AParamAbout=100     ; inspect CAN code 100: returns its min / max / default descriptor
```

## 另请参阅

- [About](About.md) — 完整参数转储（Agito PCSuite 内部使用）
- [ParamCS](ParamCS.md) — 参数集的校验和
- [Identity](Identity.md) — 控制器识别信息与功能
