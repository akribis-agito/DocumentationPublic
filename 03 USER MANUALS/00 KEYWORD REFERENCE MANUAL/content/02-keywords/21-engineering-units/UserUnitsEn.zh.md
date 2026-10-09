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
last_updated: '2026-10-10'
doc_revision: '2026.06'
language: zh-CN
---
# UserUnitsEn

轴上全局工程单位功能的主使能开关。

## 概述

`UserUnitsEn` 用于开启或关闭某个轴上的全局工程单位功能。启用后，属于位置、速度、加速度和力单位组的关键字将以各量对应的系数和单位标签关键字所配置的工程单位进行显示和接受，而非控制器的内部单位。禁用时（默认），轴使用其普通的用户单位行为。

此功能仅在 central-i v5 版本可用。

## 工作原理

`UserUnitsEn` 是每轴的开/关开关：

| 值 | 含义 |
|---|---|
| 0 | 禁用（默认）。此轴的全局工程单位功能关闭。 |
| 1 | 启用。全局工程单位配置应用于此轴。 |

该设置存储于闪存，因此在重新上电后保持不变。

### 嵌入式缩放冲突

仅当访问的关键字使用嵌入式 `UsrUnits`、`AuxUsrUnits` 或 `PDUsrUnits` 缩放、属于相应的全局单位组，且该轴同时设置了 `UserUnitsEn = 1` 和非默认嵌入式比例时，才触发错误 `338`。在 AGM800-EC 上，`AuxVel` 和 `PDVel` 使用固定时间域缩放，不会触发此冲突。仍使用嵌入式缩放的位置关键字继续受此检查约束。完整换算列表见 [AGM800-EC 时间与单位](../01-system/03-timing/AGM800-EC-units.zh.md)。

出现冲突时，可将相应嵌入式比例恢复为默认值，或将 `UserUnitsEn` 设为 0。

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
- [UsrUnits/AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 嵌入式每轴缩放
