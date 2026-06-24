---
keyword: ScopeGap
summary: 设置 Central-i 示波器的采样间隔。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 743
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
  - 1
  - 1000000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeGap

设置 Central-i 示波器的采样间隔。

## 概述

`ScopeGap` 设置 Central-i 示波器的采样间隔，控制 [ScopeParams](ScopeParams.md) 中信号的捕获频率。较大的值采样频率较低，从而在固定缓冲区内覆盖更长的时间跨度。该参数为非轴参数，保存至闪存。示波器实时读取该间隔，因此 `ScopeGap` 可在示波器运行期间修改，新速率立即生效。它是 [LoggerGap](LoggerGap.md) 和 [RecGap](RecGap.md) 在 Central-i 示波器中的对应项。

## 工作原理

示波器以约 1 ms 的固定内部节拍（每 16 个伺服周期一个节拍）判断是否到达采样时刻。`ScopeGap` 为连续捕获采样之间的节拍数，因此采样周期约为：

$$
\text{采样周期}\ [\text{ms}] \approx \text{ScopeGap}
$$

值为 `1` 时，每个节拍捕获一次（约 1 kHz）。由于缓冲区存储固定数量的采样，较大的 `ScopeGap` 以牺牲时间分辨率换取更长的总捕获窗口，在缓冲区填满且示波器暂停前（参见 [ScopeStatus](ScopeStatus.md)）。允许范围和默认值请参阅关键字属性。

## 示例

```text
AScopeGap=1          ; 每个节拍捕获一次（~1 ms，~1 kHz）
AScopeGap=10         ; 约每 10 ms 捕获一次（~100 Hz）
AScopeGap           ; 查询当前采样间隔
```

## 另请参阅

- [ScopeOn](ScopeOn.md) — 启动/停止示波器
- [ScopeParams](ScopeParams.md) — 示波器捕获的信号
- [ScopeStatus](ScopeStatus.md) — 示波器运行状态及缓冲区填充情况
- [LoggerGap](LoggerGap.md) — 连续记录器的等效间隔
