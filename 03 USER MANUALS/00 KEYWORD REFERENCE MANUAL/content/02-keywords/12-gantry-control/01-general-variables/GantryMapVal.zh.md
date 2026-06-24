---
summary: 在当前索引位置从龙门映射表读取的修正值。
keyword: GantryMapVal
availability:
  standalone: []
  central-i:
  - v5
can_code: 750
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1.0
  default: 0.5
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMapVal

在当前位置从龙门映射插值得到的实时解耦比率。

## 概述

`GantryMapVal` 是控制器当前正在应用的只读解耦比率，由控制器在 [GantryMapSrc](GantryMapSrc.md) 所取位置处从 [GantryMap](GantryMap.md) 表插值得到。该比率范围为 **0.0 到 1.0**（在映射建立之前读取为 **0.5**，即对称分配）。它在龙门轴对的两个轴上均有报告（主轴值驱动反馈合成，偏摆轴值驱动电流分配），且不保存至闪存。仅当启用了位置相关映射（[GantryMapType](GantryMapType.md) = 1）时该值才有意义。适用于 central-i（v5）。

`GantryMapVal` 是确认映射被正确索引和插值的诊断量：随着龙门移动，该值应平滑扫过您存储在 [GantryMap](GantryMap.md) 中的各比率。

## 工作原理

每个控制周期，当映射激活时，控制器从 [GantryMapSrc](GantryMapSrc.md) 读取源位置，在 [GantryMap](GantryMap.md) 中找到相邻条目（以 [GantryMapInit](GantryMapInit.md) 为起点，按映射间距排列），并在其间线性插值，结果即为 `GantryMapVal`。龙门两个轴各自插值一个独立比率：主轴（偶数轴）读取的比率用于加权龙门反馈合成，偏摆轴（奇数轴）读取的比率用于加权电机电流分配（参见 [GantryMapType](GantryMapType.md)）。两个比率来自映射的不同列，因此两轴的读数可以不同。超出映射范围时，钳位至第一个或最后一个表条目。

## 示例

```text
AGantryMapVal        ; 读取当前位置的实时解耦比率
```

### 边界情况

- **映射类型关闭**（[GantryMapType](GantryMapType.md) = 0）— `GantryMapVal` 不由查找更新；保持表插值最后产生的值（通常为 `0.5`）。
- **源未配置**（[GantryMapSrc](GantryMapSrc.md) = 0）— 查找从空指针读取并产生第一个表条目；读取结果需谨慎使用。
- **超出表范围** — 超过最后一个条目的值钳位至最后一个条目；低于第一个条目的值钳位至第一个条目。当龙门离开映射范围时，诊断值将趋于平稳。
- **只读** — 写入操作将被拒绝。
- **各轴独立值** — 活跃龙门轴对的两个轴各自携带其插值比率：主轴（偶数轴）值驱动反馈合成，偏摆轴（奇数轴）值驱动电流分配。不属于活跃龙门轴对的轴不会由查找更新，保持默认值或最后值。
- **平台** — 仅适用于 v5 central-i。

## 另请参阅

- [GantryMap](GantryMap.md) — 该值插值所依据的表
- [GantryMapSrc](GantryMapSrc.md) — 用于索引表的位置源
- [GantryMapType](GantryMapType.md) — 启用映射
- [GantryMapInit](GantryMapInit.md) — 对应第一个表条目的位置
