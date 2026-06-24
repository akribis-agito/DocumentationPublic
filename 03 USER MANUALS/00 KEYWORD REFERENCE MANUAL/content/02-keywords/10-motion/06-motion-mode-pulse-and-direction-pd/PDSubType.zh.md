---
keyword: PDSubType
summary: 选择脉冲方向输入信号格式（例如步进/方向与正转/反转脉冲）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 421
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PDSubType

选择脉冲方向输入信号格式（例如步进/方向与正转/反转脉冲）。

## 概述

`PDSubType` 选择控制器解释两路输入线的方式，使 [PDPos](PDPos.md) 能针对所连接的主站正确累积。共有两种格式：经典脉冲方向（一路脉冲线 + 一路方向线）和 A-quad-B 增量式（两路正交线）。这是一个保存至闪存的轴相关参数，在轴运动中或电机使能时不能更改。

## 工作原理

`PDSubType` 设置控制器用于将两路输入线解码为每周期脉冲计数的输入格式（见 [PDPos](PDPos.md)）。

| 值 | 输入格式 | 说明 |
|---|---|---|
| 0 | **脉冲方向**（默认） | 一路线携带步进脉冲，另一路携带方向电平。每个脉冲使计数器步进；方向线设置符号。 |
| 1 | **AqB 增量式** | 两路相位相差 90° 的正交通道（A 和 B），如增量式编码器所输出。解码器从相位关系推导计数和方向。 |

取值范围为 0–1；未定义其他格式。格式按轴配置。无论选择哪种格式，两路输入线都首先经过由 [DInFilt](../../05-inputs-outputs/04-digital-inputs/DInFilt.md) 设置的每轴硬件消抖——详见下方*输入滤波与最大速率*。该消抖是调理原始输入边沿的唯一设置；[PDFiltFact](PDFiltFact.md)（由 [PDPosFilt](PDPosFilt.md) 推导）是随后单独应用于位置参考的直接模式低通滤波器，不涉及输入边沿。

### 各格式解码方式

- **脉冲 + 方向（0）：** 计数器在（经滤波的）脉冲线每个**上升沿**时变化一次；方向线被采样并决定该变化为 +1 还是 -1。仅计数上升沿。
- **A-quad-B（1）：** 两路通道按相位关系解码；A/B 的每次跳变都使计数器步进，A 相对于 B 的超前/滞后顺序决定符号，因此一个正交周期（编码器的一条完整线）产生四个计数。

### 输入滤波与最大速率

两路输入线均经过同一硬件消抖，其强度由 [DInFilt](../../05-inputs-outputs/04-digital-inputs/DInFilt.md)（0-15）按轴设置。任一输入线上的电平变化只有在连续 `DInFilt + 1` 个滤波时钟周期内保持稳定后才被接受，因此 `DInFilt` 越大，稳定时间越长，输入能分辨的最高脉冲速率越低。精确的稳定时间和速率上限取决于产品内部滤波时钟频率；为留有余量，应使输入脉冲速率远低于脉冲每半个高/低周期短于消抖稳定时间的临界点，并在仍能抑制噪声的前提下使用尽可能小的 `DInFilt`。

## 示例

```text
APDSubType=0         ; pulse + direction input (default)
APDSubType=1         ; A-quad-B (quadrature) input
```

## 另请参阅

- [PDPos](PDPos.md) — 根据所选解码格式填充的计数器
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — 解码后应用的输入缩放系数
- [SetPDPos](SetPDPos.md) — 预置/重新清零 P/D 计数器
