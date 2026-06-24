---
keyword: LoggerAbout
summary: 报告当前连续记录器会话的元数据。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 535
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 44
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerAbout

报告当前连续记录器会话的元数据。

## 概述

`LoggerAbout` 是一个只读数组，报告当前记录器会话的元数据：生效的缓冲区满模式、记录开始时间以及已记录参数列表的快照。它允许上位机应用程序在解读 [LoggerUpload](LoggerUpload.md) 返回的数据时，无需单独重新查询配置。该快照在记录器启用时刻获取，因此即使事后修改了 [LoggerParams](LoggerParams.md) 或 [LoggerFullMod](LoggerFullMod.md)，它仍反映实际记录数据时所使用的配置。该变量为非轴状态变量，不保存至闪存。

## 工作原理

该数组以 1 为起始索引，布局如下：

| 索引 | 报告内容 | 含义 |
|---|---|---|
| 1 | （保留） | 本固件版本中不使用；采样间隔从 [LoggerGap](LoggerGap.md) 实时获取，因此可即时更改。读回值为未初始化的标记值。 |
| 2 | 缓冲区满模式 | 记录启动时 [LoggerFullMod](LoggerFullMod.md) 的快照：`0` 表示满时停止，`1` 表示覆盖最旧数据。 |
| 3 | 开始时间 | 会话启动时捕获的控制器时间戳。 |
| 4 及以上 | 已记录参数 | [LoggerParams](LoggerParams.md) 的快照：索引 `4` 对应 `LoggerParams[1]`，索引 `5` 对应 `LoggerParams[2]`，依此类推。 |

每次记录器通过 [LoggerOn](LoggerOn.md) 从关闭切换到开启时，快照（索引 2 及以上）均会刷新。

## 示例

```text
ALoggerAbout[2]     ; 查询会话所使用的缓冲区满模式
ALoggerAbout[3]     ; 查询会话开始时间戳
ALoggerAbout[4]     ; 查询会话的第一个已记录参数
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerParams](LoggerParams.md) — 记录器记录的参数
- [LoggerStatus](LoggerStatus.md) — 记录器运行状态
- [LoggerUpload](LoggerUpload.md) — 检索已记录的数据
