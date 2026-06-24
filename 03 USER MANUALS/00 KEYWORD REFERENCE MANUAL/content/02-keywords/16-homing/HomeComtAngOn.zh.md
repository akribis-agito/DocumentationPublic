---
keyword: HomeComtAngOn
summary: 使能在回零过程中捕获原点位置处的换相角。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 408
attributes:
  access: rw
  scope: axis
  flash: false
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# HomeComtAngOn

使能在回零过程中捕获原点位置处的换相角。

## 概述

`HomeComtAngOn` 是换相角回零功能的主使能开关。换相角（[ComtAng](../15-commutation/ComtAng.md)）是控制器用于换相电机的电角度；该功能允许已知的机械原点位置重新建立该角度，而无需重新运行完整的定相/回零搜索。

`HomeComtAngOn` 控制两个相关操作：

- 在回零运行期间，当轴到达已记录的索引位置时，该处的换相角被捕获到 [HomeComtAngRd](HomeComtAngRd.md) 中——仅当 `HomeComtAngOn` 非零时——换相将被强制设为 [HomeComtAngWr](HomeComtAngWr.md) 中存储的值。
- 在 central-i v5 上，当用户直接写入 [HomeComtAngWr](HomeComtAngWr.md) 时，实时换相也会根据新值与 [HomeComtAngRd](HomeComtAngRd.md)`[1]` 中当前记录角度之间的差值进行调整——同样仅在 `HomeComtAngOn` 非零时有效。在 v4 上，直接写入 [HomeComtAngWr](HomeComtAngWr.md) 仅存储该值；在下次回零运行时生效。

该参数为轴作用域，不保存至闪存，可随时更改。

## 工作原理

捕获/应用操作在结束于索引位置的回零步骤（"移动至索引位置"，以及同样的"移动至锁定位置"）内执行。该步骤完成时：

1. 无论 `HomeComtAngOn` 的值如何，当前换相角均被复制到 [HomeComtAngRd](HomeComtAngRd.md)`[1]` 和 `[2]`。
2. 若 `HomeComtAngOn != 0`，控制器将 [ComtAng](../15-commutation/ComtAng.md) 设为 [HomeComtAngWr](HomeComtAngWr.md) 中的值，从中重新计算内部换相偏移，并将 [HomeComtAngRd](HomeComtAngRd.md)`[1]` 刷新为已应用的值。

若 `HomeComtAngOn` 为 `0`，索引处的角度仍会被捕获到 [HomeComtAngRd](HomeComtAngRd.md) 以供检查，但实时换相保持不变。

| HomeComtAngOn | 行为 |
|---|---|
| 0 | 仅捕获：[HomeComtAngRd](HomeComtAngRd.md) 在索引处更新，换相不改变。 |
| 1 | 捕获并应用：同上，然后将 [ComtAng](../15-commutation/ComtAng.md) 强制设为 [HomeComtAngWr](HomeComtAngWr.md)；在 central-i v5 上，直接写入 [HomeComtAngWr](HomeComtAngWr.md) 也会立即调整实时换相。 |

## 示例

```text
AHomeComtAngOn=1     ; enable capture-and-apply of the commutation angle at home
AHomeComtAngOn      ; 0 = disabled, 1 = enabled
```

## 另请参阅

- [HomeComtAngRd](HomeComtAngRd.md) — 保存已捕获角度的只读数组
- [HomeComtAngWr](HomeComtAngWr.md) — 使能时应用的角度
- [ComtAng](../15-commutation/ComtAng.md) — 该功能设置的实时换相角
