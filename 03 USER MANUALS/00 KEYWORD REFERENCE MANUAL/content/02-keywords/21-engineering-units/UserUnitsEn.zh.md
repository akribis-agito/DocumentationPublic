---
keyword: UserUnitsEn
summary: 轴上全局工程单位功能的主使能开关。
availability:
  standalone: []
  central-i:
  - v5
can_code: 826
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
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
# UserUnitsEn

轴上全局工程单位功能的主使能开关。

## 概述

`UserUnitsEn` 用于开启或关闭某个轴上的全局工程单位功能。启用后，属于位置、速度、加速度和力单位组的关键字将以各量对应的系数和单位标签关键字所配置的工程单位进行显示和接受，而非控制器的内部单位。禁用时（默认），轴使用其普通的用户单位行为。

此功能仅在 central-i v5 及以上版本可用。

## 工作原理

`UserUnitsEn` 是每轴的开/关开关：

| 值 | 含义 |
|---|---|
| 0 | 禁用（默认）。此轴的全局工程单位功能关闭。 |
| 1 | 启用。全局工程单位配置应用于此轴。 |

该设置存储于闪存，因此在重新上电后保持不变。

### 与嵌入式 UsrUnits 缩放的互斥性

全局工程单位功能与嵌入式每轴 [UsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) / `AuxUsrUnits` 缩放在同一轴上**互斥**。两者均将关键字值表示为原始内部单位以外的形式，因此同一时刻只能激活其中一个。

每当访问受影响的关键字时，控制器均会执行此检查。若对某轴同时满足以下两个条件，则对属于任一全局单位组的关键字进行读取或写入将被拒绝，并返回错误码 `338`：

- `UserUnitsEn` 设置为 1，且
- 对应的嵌入式缩放（主反馈关键字对应 `UsrUnits`，或辅助/脉冲方向变体对应其各自关键字）设置为非默认值。

错误 `338` 提示："Global User Units feature is mutually exclusive with embedded controller user units. Please disable one of the scaling factors."（全局用户单位功能与嵌入式控制器用户单位互斥，请禁用其中一个缩放系数。）要解决冲突，请将嵌入式缩放保留为默认值，或将 `UserUnitsEn` 设回 0。

如果嵌入式缩放处于默认值，启用 `UserUnitsEn` 不会引发此冲突。

## 示例

```text
AUserUnitsEn[1]=1      ; 在轴上启用全局工程单位功能
AUserUnitsEn[1]=0      ; 禁用（默认）
AUserUnitsEn[1]        ; 读取当前使能状态
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [PosUnitGrp](PosUnitGrp.md) — 位置相关的受影响关键字
- [PosUnitFct](PosUnitFct.md) — 位置比例系数
- [UsrUnits/AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 与本功能互斥的嵌入式缩放
