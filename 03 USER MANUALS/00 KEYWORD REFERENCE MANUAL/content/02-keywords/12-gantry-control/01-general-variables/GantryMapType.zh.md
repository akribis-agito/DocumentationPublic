---
summary: 选择应用于偏摆轴的龙门映射修正类型。
keyword: GantryMapType
availability:
  standalone: []
  central-i:
  - v5
can_code: 749
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMapType

启用位置相关的龙门解耦映射。

## 概述

`GantryMapType` 选择控制器如何在两台电机之间分配龙门驱动。默认值 `0` 时，龙门采用固定的对称分配（每台电机位于线性指令和偏摆指令的中点）。值为 `1` 时，控制器改用**位置相关解耦映射**：通过 [GantryMapSrc](GantryMapSrc.md) 提供的位置查询比率表，沿横梁移动龙门的有效中点。这可补偿非对称机构——例如刚度或几何形状关于中心不对称的横梁——使线性轴和偏摆轴在整个行程范围内保持解耦。

| `GantryMapType` | 模式 | 效果 |
|:---------------:|------|------|
| 0 | 关闭（对称） | 固定 50/50 分配：线性反馈为两台电机的均值；偏摆电流平均分配。 |
| 1 | 映射（central-i v5） | 映射表中的解耦比率同时作用于反馈合成和电机电流分配。 |

该参数为轴范围，保存至闪存，可在电机使能时修改，但不可在运动中修改。用于索引映射的位置由 [GantryMapSrc](GantryMapSrc.md) 选择，当前插值比率由 [GantryMapVal](GantryMapVal.md) 报告，比率表存储于 [GantryMap](GantryMap.md)。值 `1` 仅在 central-i（v5）上可用；独立产品仅支持 `0`。

## 工作原理

`GantryMapType` = 0 时，龙门共模位置简单取两台电机位置的均值，偏摆修正电流等量叠加到一台电机并从另一台电机中减去。`GantryMapType` = 1 时，控制器在当前源位置（实时报告为 [GantryMapVal](GantryMapVal.md)）处查询 [GantryMap](GantryMap.md) 表中的比率 *r*（介于 0 和 1 之间），并将其同时用于对两台电机位置合成线性反馈的加权，以及对线性和偏摆电流指令分配到两台电机的加权。比率为 0.5 时还原为对称行为；偏离 0.5 则将受控中点移向横梁的一侧。映射表几何结构参见 [GantryMap](GantryMap.md)，查找索引参见 [GantryMapSrc](GantryMapSrc.md)。

## 示例

```text
AGantryMapType=1     ; 启用位置相关解耦映射（central-i v5）
AGantryMapType=0     ; 使用固定对称分配
AGantryMapType       ; 读取当前映射模式
```

### 边界情况

- **运动中写入** — 被拒绝（`NOMOTN`）；可在电机使能时修改。
- **`GantryMapType = 1` 但未配置表** — 每个条目均为默认值 `0.5`，未配置的表与对称 50/50 分配效果相同；请在依赖位置相关分配之前配置 [GantryMap](GantryMap.md)、[GantryMapSrc](GantryMapSrc.md)、[GantryMapInit](GantryMapInit.md) 及映射间距。
- **龙门使能期间更改映射类型** — 更改在下一控制周期生效，无平滑过渡；线性-偏摆分配的阶跃指令可能短暂扰动横梁。建议在 [GantryOn](GantryOn.md) = 0 时更改映射类型。
- **超出范围** — 超出平台支持范围的值将被拒绝。值 `1` 仅在 central-i 主站型上被接受；其他型号仅接受 `0`。
- **写入错误轴** — 仅在主轴上读取；写入其他轴时虽被存储但被忽略。
- **保存** — 可保存至闪存。
- **平台** — `GantryMapType = 1` 仅适用于 v5 central-i。

## 另请参阅

- [GantryMap](GantryMap.md) — 解耦比率表
- [GantryMapSrc](GantryMapSrc.md) — 用于索引映射的位置源
- [GantryMapVal](GantryMapVal.md) — 从映射中读取的实时插值比率
- [GantryMapInit](GantryMapInit.md) — 第一个映射条目对应的位置
