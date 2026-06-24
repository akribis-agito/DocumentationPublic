---
summary: 选择 HallsAngle 表条目的解释方式（0 = 霍尔状态中点角度，1 = 霍尔状态切换角度）。
keyword: HallsAngleSw
availability:
  standalone: []
  central-i:
  - v5
can_code: 679
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# HallsAngleSw

选择 [HallsAngle](HallsAngle.md) 表条目的解释方式：霍尔状态中点角度或霍尔状态切换角度。

## 概述

`HallsAngleSw` 是一个模式选择器（范围 0–1，默认值 0），用于确定 [HallsAngle](HallsAngle.md) 中存储角度的解释方式，以及当 `HallsAngle` 未配置时控制器安装的默认角度映射。该参数为轴作用域、保存至闪存，仅在 central-i v5 上可用；在电机使能或运动中不可更改。

| 值 | 含义 |
|---|---|
| 0（默认值） | **中点角度**模式——每个 `HallsAngle` 条目为对应霍尔状态*中点*处的电角度。默认映射：状态 5 → 60°，1 → 120°，3 → 180°，2 → 240°，6 → 300°，4 → 360°。 |
| 1 | **切换角度**模式——每个条目为相邻霍尔状态之间*切换点*处的电角度。默认切换角度：30°、90°、150°、210°、270°、330°。 |

## 工作原理

当 [HallsAngle](HallsAngle.md) 表未配置（其六个条目中任意一个仍为默认值 `-1`，即"未配置"）时，控制器将根据 `HallsAngleSw` 安装上述两种默认映射之一。所选模式同时定义了在基于霍尔的换相方法（参见 [ComtMode](ComtMode.md)）从霍尔传感器导出换相角时，存储角度的应用方式。

将 `HallsAngleSw` 更改为与当前不同的值，还会重新推导现有的 [HallsAngle](HallsAngle.md) 条目：从中点切换到切换角度模式时，每个条目将被替换为相邻状态之间的中间角度；反向切换时则执行逆操作，因此已配置的表会在两种表示方式之间转换，而不是被丢弃。

> [!note]
> `HallsAngleSw` **不是**霍尔反馈与编码器反馈之间的切换角度阈值。它是 HallsAngle 表解释方式的 0/1 选择器，如上所述。

## 示例

```text
AHallsAngleSw=0      ; interpret HallsAngle as state mid-point angles (default)
AHallsAngleSw=1      ; interpret HallsAngle as state transition (switch) angles
AHallsAngleSw       ; query the current interpretation mode
```

## 另请参阅

- [HallsAngle](HallsAngle.md) — 映射到每个霍尔状态的电角度（按本选择器解释）
- [HallsValue](HallsValue.md) — 当前原始霍尔传感器状态
- [HallOnlyFilt](HallOnlyFilt.md) — 基于霍尔的换相角滤波器
- [ComtMode](ComtMode.md) — 选择换相方法
