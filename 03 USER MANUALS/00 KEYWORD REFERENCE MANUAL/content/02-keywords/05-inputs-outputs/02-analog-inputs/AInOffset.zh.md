---
keyword: AInOffset
summary: 加到每路模拟量输入上的偏置（mV）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 216
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
  - -2147483648
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
# AInOffset

加到每路模拟量输入上的偏置（mV）。

## 概述

`AInOffset` 为模拟量输入加上一个固定偏置，单位为毫伏，是[模拟量输入信号路径](00-overview.md)的偏置级，施加于滤波后（[AInFilt](AInFilt.md)）的值上、并在第一级死区（[AInDB](AInDB.md)）之前。数组索引为模拟量输入编号（例如 `AInOffset[3]` 表示模拟量输入 3）。可用它来抵消传感器的偏置，使端子上的 0 mV 读作 0。

## 工作原理

在每个周期的调理过程中，偏置在任何死区或增益之前加到滤波后的读数上：

$$
y = u + \text{AInOffset}
$$

由于偏置是在第一级死区*之前*加入的，因此死区围绕修正后的零点施加，而非原始零点——所以用 `AInOffset` 抵消传感器偏置时，也会正确地使死区居中。

## 示例

```text
AAInOffset[1]=-50    ; subtract 50 mV of bias from analog input 1
AAInOffset[1]=0      ; no offset
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AInOffset[1]`–`AInOffset[4]`。`AInOffset[0]` 是保留的通信/内部槽位（用户不可访问），`AInOffset[5]` 不存在。
- **大偏置** — 此级不做限幅；偏置后的值以完整的浮点分辨率流入死区级和增益级。
- **符号约定** — 为加（而非减）；使用负的 `AInOffset` 来消除正向偏置。
- **与电机使能/失能及模式无关** — 无论 `MotorOn` 或 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 如何，偏置每个周期都会运行；所有使用者都看到修正后的值。
- **与 [AInDB](AInDB.md) 的交互** — 由于偏置先施加，死区窗口以偏置修正后的零点居中，而非原始传感器零点。
- **保存** — `AInOffset` 可保存至闪存。
- **平台** — central-i v5 将该值存储为 `float32`；公式和单位不变。

## 另请参阅

- [AInFilt](AInFilt.md) — 在偏置之前施加的滤波级
- [AInDB](AInDB.md) — 第一级死区，紧接在偏置之后施加
- [AInGain](AInGain.md) — 在死区之后施加的增益级
- [AInPort](AInPort.md) — 由此得到的读数
