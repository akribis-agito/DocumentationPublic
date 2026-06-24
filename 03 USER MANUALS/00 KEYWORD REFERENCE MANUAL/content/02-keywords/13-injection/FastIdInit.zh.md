---
keyword: FastIdInit
summary: 将 PRBS 序列索引复位至第一个预定义二进制值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 540
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# FastIdInit

将 PRBS 序列索引复位至第一个预定义二进制值。

## 概述

`FastIdInit` 将 PRBS（伪随机二进制序列）索引复位至第一个预定义二进制值，使注入从序列起始处重新开始。仅当 [InjectType](InjectType.md) 选择 PRBS 注入（`InjectType = 6 or 7`）时有效。它不会复位 PRBS 降采样因子 [FastIdDownSam](FastIdDownSam.md)。

## 工作原理

PRBS 波形从一个包含 8192 位的固定表（最大长度序列）中读取。控制器逐位遍历该表，先取当前 16 位字的最高有效位，依次向最低有效位推进，然后移至下一个字。`FastIdInit` 将读取位置恢复至最开始（第一个字的最高有效位），并清除降采样计数器，使下一次 PRBS 注入从起始处产生完全相同的位模式。发出该指令后，重复辨识运行可使用相同的激励，这在需要比较或平均其结果时是必要的。设置读取速率的降采样因子 [FastIdDownSam](FastIdDownSam.md) 保持不变。

## 示例

```text
AFastIdInit          ; reset the PRBS sequence index
```

## 另请参阅

- [InjectType](InjectType.md) — 选择 PRBS 波形
- [FastIdDownSam](FastIdDownSam.md) — PRBS 生成降采样因子（不被 FastIdInit 复位）
