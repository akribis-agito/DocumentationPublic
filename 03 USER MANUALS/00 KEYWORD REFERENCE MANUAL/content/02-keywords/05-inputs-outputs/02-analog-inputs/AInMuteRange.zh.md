---
keyword: AInMuteRange
summary: 每路模拟量输入的第二级死区（mV），在增益之后施加。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 377
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AInMuteRange

每路模拟量输入的第二级死区（mV），在增益之后施加。

## 概述

`AInMuteRange` 设置施加于模拟量输入的**第二级**死区，单位为毫伏，是[模拟量输入信号路径](00-overview.md)的最后一级，位于增益（[AInGain](AInGain.md)）之后。与第一级死区（[AInDB](AInDB.md)）不同，落在该区间之外的值**原样**通过（不做减法）：它是纯粹的静音，而非偏移。数组索引为模拟量输入编号（例如 `AInMuteRange[2]` 表示模拟量输入 2）。由于它在增益之后运行，因此阈值是基于输出（增益后）值以 mV 指定的。

## 工作原理

静音施加于增益后的值 `y`。比较在两个边沿上均为**闭区间**，因此恰好等于阈值的值也会被静音：

| 输出 `y` | 结果 |
|------------|--------|
| `−AInMuteRange ≤ y ≤ AInMuteRange` | `0` |
| 其他 | `y`（不变） |

这会在区间边缘留下一个阶跃不连续点（值从 0 跳变到 ±`AInMuteRange`），这与连续的 [AInDB](AInDB.md) 形成对比。其结果存入 `AInPort[1]`–`AInPort[4]`，并由 [AInMode](AInMode.md) 路由至控制功能。

## 示例

```text
AAInMuteRange[1]=10  ; mute analog input 1 within ±10 mV of zero
AAInMuteRange[1]=0   ; no mute (default)
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AInMuteRange[1]`–`AInMuteRange[4]`。`AInMuteRange[0]` 是保留的通信/内部槽位（用户不可访问），`AInMuteRange[5]` 不存在。
- **超出范围** — 不接受负值（范围从 `0` 开始）；`AInMuteRange` 为零会完全禁用此级。
- **静音位于增益后侧** — 阈值以 `AInPort` 的 mV 指定（在 [AInGain](AInGain.md) 之后）。在增益后的噪声底之上设置静音很直接；将增益前的 mV 值乘以 `AInGain / 65536` 即可换算为其增益后的等效值（增益级按 `AInGain / 65536` 进行缩放）。
- **阶跃不连续** — 刚好落在区间之外的值会以全幅值通过，因此 `0 → ±AInMuteRange` 的过渡是陡峭的；如果连续性很重要，请改用 [AInDB](AInDB.md)。
- **负 [AInGain](AInGain.md)** — 静音关于 `0` 对称，因此 `AInGain` 中的反向无需对 `AInMuteRange` 做任何更改。
- **与电机使能/失能及模式无关** — 无论 `MotorOn` 或 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 如何，每个周期都会运行。
- **保存** — `AInMuteRange` 可保存至闪存。
- **平台** — central-i v5 将该值存储为 `float32`；行为不变。

## 另请参阅

- [AInDB](AInDB.md) — 第一级死区，位于增益之前（连续、减法式）
- [AInGain](AInGain.md) — 在此静音之前施加的增益级
- [AInPort](AInPort.md) — 由此得到的读数
