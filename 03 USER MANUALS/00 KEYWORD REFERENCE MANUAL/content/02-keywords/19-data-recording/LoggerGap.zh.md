---
keyword: LoggerGap
summary: 设置连续记录器的采样间隔（单位：伺服周期）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 531
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerGap

设置连续记录器的采样间隔（单位：伺服周期）。

## 概述

`LoggerGap` 设置连续数据记录器的采样间隔，控制 [LoggerParams](LoggerParams.md) 中各参数的捕获频率。数值越大，采样越稀疏，缓冲区覆盖的时间跨度越长。该参数为非轴参数，保存至闪存。与记录示波器不同，记录器实时读取间隔值，因此可在记录过程中随时修改 `LoggerGap`，新速率立即生效。它是 [RecGap](RecGap.md)（用于记录示波器）在连续记录器中的对应参数。

## 工作原理

记录器在固定内部节拍（约 1 ms，每 16 个伺服周期一次）上判断是否到达采样时刻。`LoggerGap` 表示相邻两次记录采样之间的节拍数，因此采样周期约为：

$$
\text{采样周期}\ [\text{ms}] \approx \text{LoggerGap}
$$

最小值 `1` 表示每个节拍均采样（约 1 kHz）。默认值 `10` 对应约每 10 ms 一次采样（约 100 Hz）。由于缓冲区可存储的采样数固定，较大的 `LoggerGap` 以牺牲时间分辨率为代价换取更长的总捕获窗口，直至 [LoggerFullMod](LoggerFullMod.md) 设定的缓冲区满处理行为生效。

## 示例

```text
ALoggerGap=10        ; 约每 10 ms 采样一次（默认，~100 Hz）
ALoggerGap=1         ; 每个节拍采样一次（~1 ms，~1 kHz）
ALoggerGap          ; 查询当前采样间隔
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerParams](LoggerParams.md) — 记录器记录的参数
- [LoggerFullMod](LoggerFullMod.md) — 缓冲区满时的处理行为
- [RecGap](RecGap.md) — 记录示波器的等效降采样参数
