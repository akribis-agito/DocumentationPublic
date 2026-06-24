---
keyword: HomeComtAngRd
summary: 只读数组，保存在原点位置捕获的换相角。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 410
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# HomeComtAngRd

只读数组，保存在原点位置捕获的换相角。

## 概述

`HomeComtAngRd` 是一个只读数组，保存在回零过程中于索引位置记录的换相角。每个值均为电角度，单位为 0.01°，因此范围 0–35999 覆盖完整的电气旋转一周（0–359.99°）。使用元素 `[1]` 和 `[2]`；元素 `[0]` 不存在（数组为 1-indexed）。无论 [HomeComtAngOn](HomeComtAngOn.md) 是否使能，捕获均会发生，因此可通过读取该数组来获取对应机械原点的换相角，再将其保存至 [HomeComtAngWr](HomeComtAngWr.md)。该参数为轴相关只读数组，不保存至闪存。

## 工作原理

当以索引位置结束的回零步骤完成后，控制器将当前换相角同时复制到 `HomeComtAngRd[1]` 和 `HomeComtAngRd[2]`。若 [HomeComtAngOn](HomeComtAngOn.md) 非零，控制器随即将当前换相强制设为 [HomeComtAngWr](HomeComtAngWr.md) 中的值，并将 `HomeComtAngRd[1]` 刷新为该已应用值。结果如下：

| 元素 | 索引步骤完成后的内容 |
|---|---|
| `HomeComtAngRd[1]` | 当前生效的换相角：在索引处测量的角度，或——若 [HomeComtAngOn](HomeComtAngOn.md) 已使能——所应用的 [HomeComtAngWr](HomeComtAngWr.md) 值。 |
| `HomeComtAngRd[2]` | 在索引处测量的换相角，在任何应用操作之前。 |

当 [HomeComtAngOn](HomeComtAngOn.md) 为 `0` 时，两个元素均保存在索引处测量的角度。若要获取某原点对应的存储角度，可执行一次回零序列后读取 `HomeComtAngRd[2]`。

## 示例

```text
AHomeComtAngRd[1]   ; 当前生效的换相角（单位：0.01°）
AHomeComtAngRd[2]   ; 在索引处测量的换相角
AHomeComtAngRd      ; 读取完整的捕获角度数组
```

## 另请参阅

- [HomeComtAngOn](HomeComtAngOn.md) — 使能捕获并应用至本数组
- [HomeComtAngWr](HomeComtAngWr.md) — 使能时所应用的存储角度
- [ComtAng](../15-commutation/ComtAng.md) — 当前换相角，单位同为 0.01°
