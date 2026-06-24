---
keyword: InjectFreq
summary: 注入正弦波或方波的频率，单位为 Hz/100。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 117
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
  - 800000
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# InjectFreq

注入正弦波或方波的频率，单位为 Hz/100。

## 概述

`InjectFreq` 设定注入正弦波或方波的频率，以 Hz/100 为单位（即存储值为频率 Hz 值乘以 100）。仅当 [InjectType](InjectType.md) 选择正弦或方波波形时（`InjectType = 1、2、3 或 4`）生效。波形幅值由与所选 [InjectPoint](InjectPoint.md) 对应的幅值参数确定。

## 工作原理

频率的 Hz 值为 `InjectFreq / 100`。例如，11.2 Hz 的波形需将 `InjectFreq` 设为 `1120`。

控制器内部在每个控制周期按与 `InjectFreq` 成比例的量推进相位角，满一整圈后归零。对于**正弦**波形，相位在内部正弦表中进行索引（并在表项之间插值），从而以设定频率输出平滑的正弦波；对于**方波**波形，在每个相位周期的前半段输出 +幅值，后半段输出 −幅值。因此同一频率同时控制两种波形。由于每个控制周期只推进一步，频率很高时每个周期内采样点数较少；chirp 波形（[InjectChirpF](InjectChirpF.md)）采用独立机制，保证每个正弦周期内的最小采样点数。

## 示例

```text
AInjectFreq=1120     ; 11.2 Hz 正弦/方波
AInjectFreq=200      ; 2 Hz
AInjectFreq         ; 查询当前注入频率
```

## 另请参见

- [InjectType](InjectType.md) — 选择使用此频率的正弦/方波波形
- [InjectChirpF](InjectChirpF.md) — chirp 注入的起始/结束频率
- [InjectPoint](InjectPoint.md) — 选择注入位置
