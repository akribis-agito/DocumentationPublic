---
keyword: HomeComtAngWr
summary: 设置在原点位置应用的换相角，以跳过一次回零序列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 409
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
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# HomeComtAngWr

设置在原点位置应用的换相角，以跳过一次回零序列。

## 概述

`HomeComtAngWr` 保存换相角归零功能在原点/索引位置应用的换相角。该值为电角度，单位为 0.01°（范围 0–35999 = 0–359.99°）。将其设置为之前从 [HomeComtAngRd](HomeComtAngRd.md) 读取的角度，以便在回零完成后控制器以正确的电角度恢复换相。该参数为轴相关参数，保存至闪存，因此在重新上电后仍保持，且在轴运动中不可写入。

仅当 [HomeComtAngOn](HomeComtAngOn.md) 非零时，本关键字才生效。若该功能禁用，`HomeComtAngWr` 仅为一个存储值，在回零时既不会被应用，直接写入时也不会生效。

## 工作原理

`HomeComtAngWr` 在以下两种情况下被应用，均以 [HomeComtAngOn](HomeComtAngOn.md) 为门控条件：

- **回零过程中。** 当以索引结束的回零步骤完成且 [HomeComtAngOn](HomeComtAngOn.md) 非零时，控制器将当前换相角（[ComtAng](../15-commutation/ComtAng.md)）直接设为 `HomeComtAngWr`，并据此重新计算内部换相偏移。由于轴此时停在索引位置，这是一次直接赋值。

- **直接写入时。** 当在 [HomeComtAngOn](HomeComtAngOn.md) 非零的情况下写入 `HomeComtAngWr` 时，控制器计算新值与 [HomeComtAngRd](HomeComtAngRd.md)`[1]` 中当前值之间的差值，将该差值换算为编码器计数，并据此偏移换相偏移量（在一个电气周期内环绕）。随后 [HomeComtAngRd](HomeComtAngRd.md)`[1]` 更新为新值。写入仅在轴不处于运动中时允许，以确保调整期间角度定义明确。

换算使用轴的电气周期长度，因此同一个 0.01° 值无论极对数和编码器分辨率如何均能正确映射。

## 示例

```text
AHomeComtAngOn=1      ; 首先使能该功能
AHomeComtAngWr=12000  ; 将 120.00 电气度应用为原点换相角
AHomeComtAngWr       ; 读取已配置的换相角（单位：0.01°）
```

## 另请参阅

- [HomeComtAngRd](HomeComtAngRd.md) — 捕获角度的来源，写入本关键字
- [HomeComtAngOn](HomeComtAngOn.md) — 必须使能后本值才生效
- [ComtAng](../15-commutation/ComtAng.md) — 本值所设置的当前换相角
