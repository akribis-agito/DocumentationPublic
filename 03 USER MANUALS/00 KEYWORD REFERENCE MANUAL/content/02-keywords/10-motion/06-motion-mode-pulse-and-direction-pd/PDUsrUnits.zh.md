---
keyword: PDUsrUnits
summary: 用于将 PDPos 和 PDVel 查询结果转换为用户单位的每用户单位计数比例因子。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 66
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
  - 1
  - 2147483647
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PDUsrUnits

用于将 PDPos 和 PDVel 查询结果转换为用户单位的每用户单位计数比例因子。

## 概述

`PDUsrUnits` 对内部脉冲方向变量 [PDPos](PDPos.md) 和 [PDVel](PDVel.md) 进行缩放，在通过通信通道查询这些状态时，将控制器内部计数转换为用户单位。它与反馈侧的 [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 类似，但仅适用于 P/D 状态组。该参数仅影响报告值，不影响内部控制计算。默认值 `65536` 表示每用户单位对应一个计数。

## 工作原理

与 `UsrUnits` 类似，`PDUsrUnits` 是相对于基数 `65536` 的比值，有效比例为每用户单位 `PDUsrUnits / 65536` 个计数。读取 P/D 状态时，控制器将内部计数值除以此比值：

$$
\text{查询到的 PDPos [用户单位]} = \frac{\text{控制器 PDPos [计数]}}{\big(\text{PDUsrUnits} / 65536\big)} = \text{计数} \cdot \frac{65536}{\text{PDUsrUnits}}
$$

默认值 `65536` 对应因子 1（值直接以计数显示）。只有 `PDPos` 和 `PDVel` 属于 P/D 用户单位组，因此此缩放不影响其他关键字。

若要表示"*N* 个内部计数 = 1 用户单位"，请设置 `PDUsrUnits = N × 65536`。

## 示例

```text
APDUsrUnits=65536    ; 每用户单位 1 个计数（默认）
APDUsrUnits=327680   ; 每用户单位 5 个计数（比值 5 = 5 x 65536）
APDUsrUnits         ; 读取当前比例
```

## 另请参阅

- [PDPos](PDPos.md) — 以这些用户单位报告的经缩放 P/D 计数器
- [PDVel](PDVel.md) — 以这些用户单位报告的 P/D 速度
- [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 编码器反馈位置的等效比值
