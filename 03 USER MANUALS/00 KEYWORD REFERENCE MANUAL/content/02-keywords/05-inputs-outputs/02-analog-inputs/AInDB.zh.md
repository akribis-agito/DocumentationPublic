---
keyword: AInDB
summary: 每个输入的第一级模拟量输入死区（mV）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 215
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AInDB

每个输入的第一级模拟量输入死区（mV）。

## 概述

`AInDB` 设置施加于模拟量输入的**第一级**死区，单位为毫伏——它是[模拟量输入信号路径](00-overview.md)中位于偏置（[AInOffset](AInOffset.md)）与增益（[AInGain](AInGain.md)）之间的死区环节。数组索引为模拟量输入编号（例如 `AInDB[3]` 表示模拟量输入 3）。位于死区内的输入被强制为零，从而抑制 0 mV 附近的噪声；超出死区时，经偏置修正的值会**减去死区宽度**，使输出在死区边缘连续（无跳变）。

## 工作原理

死区施加于经偏置修正的值 `u`：

| 输入 `u` | 输出 |
|-----------|--------|
| `u > AInDB` | `u − AInDB` |
| `u < −AInDB` | `u + AInDB` |
| 其他情况（位于死区内） | `0` |

因此死区会**平移**信号而非将其截断：恰好位于边缘处输出为 0，并在死区外线性增长，从而给出连续的特性。由于该环节在增益之前运行，死区宽度以输入侧（偏置之后）的 mV 指定。

例如，对于 20 mV 死区，输出（mV）作为输入（mV）的函数为：

```desmos-graph
left=-120; right=120; bottom=-90; top=90
height=300;
xAxisLabel=Input (mV)
yAxisLabel=Output (mV)
---
y=\{x>20:x-20,x<-20:x+20,0\}|blue
x=20|black|dashed
x=-20|black|dashed

```

## 示例

```text
AAInDB[1]=20         ; ±20 mV deadband on analog input 1
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AInDB[1]`–`AInDB[4]`。`AInDB[0]` 是保留的通信/内部槽位（用户不可访问），且 `AInDB[5]` 不存在。
- **超出范围** — 不接受负值（范围从 `0` 起始）；`AInDB` 为零将完全禁用该环节。
- **位于死区边缘** — 上界比较为严格大于（`u > AInDB`），下界为严格小于（`u < −AInDB`），因此恰好位于 `±AInDB` 的值被强制为 `0`（死区在其边界上为闭区间）。
- **与 [AInOffset](AInOffset.md) 的交互** — 死区以经偏置修正的零点为中心；请先整定 `AInOffset` 以消除任何直流偏置。
- **与 [AInGain](AInGain.md) 的交互** — 死区宽度以输入侧（偏置之后）的 mV 指定，处于增益之前；增益之后，在 `AInPort` 上看到的等效阈值为 `AInDB × AInGain / 65536`。
- **与电机使能/失能及模式无关** — 无论 `MotorOn` 或 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 如何，每个周期都运行。
- **保存** — `AInDB` 可保存至闪存。
- **平台** — central-i v5 将该值存储为 `float32`；行为不变。

## 另请参阅

- [AInMuteRange](AInMuteRange.md) — 第二级死区（增益之后）
- [AInGain](AInGain.md) — 增益环节
