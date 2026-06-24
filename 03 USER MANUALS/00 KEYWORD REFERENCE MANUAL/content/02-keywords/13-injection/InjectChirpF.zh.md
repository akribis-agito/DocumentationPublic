---
summary: 扫频注入的初始和终止频率，单位为 Hz/100。
keyword: InjectChirpF
availability:
  standalone: []
  central-i:
  - v5
can_code: 716
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 10
  - 100000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# InjectChirpF

扫频注入的初始和终止频率，单位为 Hz/100。

## 概述

`InjectChirpF` 是一个数组，定义扫频信号的起始和终止频率，以 Hz/100 为单位。仅当 [InjectType](InjectType.md) 选择扫频波形（`InjectType = 8 or 9`）时有效。扫频从初始频率扫至终止频率后重复；扫频周期由终止频率推导（参见 [InjectType](InjectType.md)）。

## 工作原理

| 索引 | 定义 |
|-------|-------------------|
| 1 | 初始频率 |
| 2 | 终止频率 |

实际频率（Hz）= 存储值 ÷ 100。例如，初始扫频频率为 5 Hz，则需设置 `InjectChirpF[1] = 500`。

每当写入该数组时，控制器预先计算扫频，使瞬时频率在一个扫频周期内从初始频率**线性**上升至终止频率，然后跳回初始频率并重复。扫频周期由终止频率推导，确保扫频范围内每个单独正弦波至少有 16 个采样点（周期计算公式参见 [InjectType](InjectType.md)）。由于扫频仅在写入该数组时重新计算，而非在设置 [InjectType](InjectType.md) 时，因此应在启动扫频前写入（或重新写入）两个数组元素；终止频率同时决定扫频所需的时间。

两个频率均须在关键字范围内（0.1 Hz 至 1000 Hz，即存储值 10 至 100000）。波形幅值来自与所选 [InjectPoint](InjectPoint.md) 绑定的幅值关键字。

## 示例

```text
AInjectChirpF[1]=100     ; start at 1 Hz
AInjectChirpF[2]=20000   ; end at 200 Hz
AInjectChirpF[1]        ; query the initial frequency
```

## 另请参阅

- [InjectType](InjectType.md) — 选择扫频波形并定义扫频周期
- [InjectFreq](InjectFreq.md) — 正弦波/方波注入的固定频率
- [InjectPoint](InjectPoint.md) — 选择注入位置
