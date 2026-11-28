---
keyword: GantryOffset
summary: 龙门轴的偏置；其采集或写入方式由 GantryMode 决定。
availability:
- controller
- ci-master
can_code: 653
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-11-24'
doc_revision: '2026.11'
language: zh-CN
---
# GantryOffset

`GantryMode=0` 时，龙门启用时根据两轴经过整形和滤波的位置参考之差捕获主轴偏置。该值只读，下次启用时重新计算。

`GantryMode` 为 1 或 2 时，主轴和偏摆轴分别使用各自的偏置。在龙门已关闭且切换已完成时可写入两个值。启用龙门或切换尚未完成时会拒绝写入。读数使用位置单位；偏置不保存至闪存。

例如，`AGantryOffset` 读取 A/B 轴对的主轴偏置，`BGantryOffset` 读取偏摆偏置。[GantryMode](../01-general-variables/GantryMode.zh.md)
