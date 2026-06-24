---
keyword: GantryMapGap
summary: 龙门解耦映射表中相邻条目之间的源位置单位间距。
availability:
  standalone: []
  central-i:
  - v5
can_code: 751
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMapGap

龙门解耦映射表中相邻条目之间的源位置单位间距。

## 概述

`GantryMapGap` 设置位置相关龙门解耦映射表的**步长**：即在 [GantryMapSrc](GantryMapSrc.md) 所选源的单位中，相邻两个 [GantryMap](GantryMap.md) 条目之间的距离。结合 [GantryMapInit](GantryMapInit.md)（第一个条目的位置），它确定每个表条目在横梁上的位置：

```text
第 n 个条目的位置  =  GantryMapInit + GantryMapGap × (n − 1)
```

因此，条目 1 位于 [GantryMapInit](GantryMapInit.md)，条目 2 在此基础上再向前一个间距，以此类推。间距乘以已填写条目数即为映射表覆盖的总行程。

该参数为龙门主轴上的轴范围值，可保存至闪存，可在电机使能时设置但不能在运动中设置。最小值为 `1`（间距为零不允许，因为控制器通过 `1 ÷ 间距` 计算单位插值斜率）。默认值为 `1`。仅适用于 central-i（v5）。

## 工作原理

当位置相关映射表激活时（[GantryMapType](GantryMapType.md) = 1），每个控制周期控制器从 [GantryMapSrc](GantryMapSrc.md) 获取实时源位置，减去 [GantryMapInit](GantryMapInit.md)，再除以 `GantryMapGap` 得到分数表索引。然后在两个相邻的 [GantryMap](GantryMap.md) 条目之间进行线性插值，并将结果报告为 [GantryMapVal](GantryMapVal.md)。写入 `GantryMapGap` 会重新计算插值所用的倒数，因此新间距在下次查找时立即生效。

根据映射条目数量选择合适的间距，使映射表覆盖龙门的工作行程：较小的间距提供更精细的位置分辨率，但在给定条目数量下覆盖范围较小；较大的间距覆盖范围更大但分辨率较粗。超出第一个或最后一个条目的位置将钳位至端部条目。

## 示例

```text
AGantryMapGap=1000   ; 映射条目之间间隔 1000 个源位置单位
AGantryMapGap        ; 读取已配置的间距
```

### 边界情况

- **运动中写入**——被拒绝（`NOMOTN`）；可在电机使能时更改。
- **间距为零**——不允许；最小值为 `1`。
- **映射类型关闭**（[GantryMapType](GantryMapType.md) = 0）——已存储但**不被查询**；龙门使用固定的 50/50 对称分配。
- **间距对行程而言过大或过小**——若工作范围超过 `GantryMapInit + GantryMapGap × (条目数 − 1)`，超过最后一个条目的位置将钳位至最后一个条目；请减小间距或增加条目以覆盖全部范围。
- **设置在错误轴上**——仅在龙门主轴上读取；其他轴的写入虽被存储，但将被忽略。
- **保存**——可保存至闪存；启动时重新加载。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryMap](GantryMap.md) — 此间距所决定条目位置的解耦比值表
- [GantryMapInit](GantryMapInit.md) — 第一个条目的源位置
- [GantryMapSrc](GantryMapSrc.md) — 此间距所对应单位的源
- [GantryMapType](GantryMapType.md) — 启用映射表的使用
- [GantryMapVal](GantryMapVal.md) — 在索引位置处的实时插值比值
