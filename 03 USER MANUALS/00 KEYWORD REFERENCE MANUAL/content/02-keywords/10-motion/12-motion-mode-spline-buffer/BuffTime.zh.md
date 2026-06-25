---
keyword: BuffTime
summary: 样条缓冲区轨迹各段时长（伺服采样数）的数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 542
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 10001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BuffTime

样条缓冲区轨迹各段时长（伺服采样数）的数组。

## 概述

`BuffTime` 存储**每个航点的时间戳**，以从轨迹起点开始计算的伺服（控制）采样数表示。条目 `[i]` 是对应位置航点 [BuffPos](BuffPos.md)`[i]` 到达时的时刻，因此某段的持续时间为相邻条目之差。`BuffTime` 与 [BuffPos](BuffPos.md) 共同定义样条轨迹，两个数组由 [BuffCalc](BuffCalc.md) 展开为插值参考。`BuffTime` 不保存至闪存，可随时修改，但修改仅在再次运行 [BuffCalc](BuffCalc.md) 后生效。

> **产品限制。** `BuffTime` 的可用长度与 `BuffPos` 相同，取决于具体产品（参见[章节概述](00-overview.md#product-availability)）。最后（最大）时间戳还须在内部插值缓冲区的容量范围内，该容量因产品而异：独立型 AGD 驱动器最多 **34** 个采样，50 航点 Central-i AGM800 型最多 **1028** 个采样，10 000 航点 Central-i AGM800 型最多 **163 849** 个采样。

## 工作原理

### 累计时间戳，而非每段时长

尽管 `BuffTime` 常被描述为"每段时长"，其值实为**累计时间戳**。索引 `[1]` 为第一个航点的时刻，`[2]` 为第二个航点的时刻，依此类推，均以从 `t = 0` 起的伺服采样数计量。控制器在从航点 `i-1` 插值到航点 `i` 时花费 `BuffTime[i] − BuffTime[i-1]` 个采样。一个伺服采样等于一个控制周期，因此 100 个采样即 100 个控制周期的运动。

在 16 384 Hz 控制频率下，`BuffTime[1] = 1638` 对应 100 ms，`BuffTime[2] = 4915` 对应 300 ms，即第一段约持续 100 ms，第二段约持续 200 ms。整个预展开轨迹共包含 `BuffTime[last]` 个插值点，该值也由 `BuffStatus[6]` 上报。

### BuffCalc 执行的验证

[BuffCalc](BuffCalc.md) 运行时会检查 `BuffTime` 数组，若以下任意条件不满足则拒绝计算（返回错误）：

| 条件 | 要求 |
|---|---|
| 首条目 | `BuffTime[1]` 必须非零。 |
| 顺序 | 值必须**严格递增**（每个条目大于前一个）；相等或递减值将被拒绝。 |
| 终止符 | 列表必须以**零条目**结束：第一个零标志轨迹结束，其前的最后一个非零条目为最终航点。 |
| 长度 | 最后（最大）时间戳不得超过控制器内部插值缓冲区容量，因为 [BuffCalc](BuffCalc.md) 会为该时刻之前的每个采样展开一个点——独立型 AGD 驱动器最多 34 个，50 航点 AGM800 型最多 1028 个，10 000 航点 AGM800 型最多 163 849 个。 |

由于展开后的轨迹在 `t = 0` 到最后时间戳之间为每个伺服周期保存一个插值采样，最后的 `BuffTime` 值决定了轨迹消耗的内部存储量。

### 多轴共享时间基准

在多轴样条运动中，**主轴**的 `BuffTime` 提供所有成员轴共用的单一时间基准。每个成员轴提供各自的 [BuffPos](BuffPos.md) 航点，但均按照相同的时间戳推进，从而保持各轴同步。

## 示例

```text
ABuffTime[1]=100     ; first waypoint reached at sample 100
ABuffTime[2]=300     ; second waypoint at sample 300 (segment lasts 200 samples)
ABuffTime[3]=600     ; third waypoint at sample 600
ABuffTime[4]=0       ; zero terminates the list (3 waypoints used)
```

## 另请参阅

- [BuffPos](BuffPos.md) — 与这些时间戳配对的航点位置
- [BuffCalc](BuffCalc.md) — 验证这些时间戳并展开轨迹
- [BuffStatus](BuffStatus.md) — 上报最后时间戳及实时回放索引
- [BuffCycles](BuffCycles.md) — 时间基准的重放次数
