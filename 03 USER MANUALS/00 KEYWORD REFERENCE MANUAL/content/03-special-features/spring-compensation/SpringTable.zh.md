---
keyword: SpringTable
summary: 保留的、尚未实现的数组关键字（大小为 41，可用索引为 1 至 40）。
availability:
- controller
- ci-master
can_code: 597
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 41
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -16000
  - 16000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000
    - 64000
  agc300-et:
    range:
    - -4000
    - 4000
  agc301-et:
    range:
    - -4000
    - 4000
  agc301-et-bioxtreme:
    range:
    - -4000
    - 4000
  agd200-et-2d01:
    range:
    - -4000
    - 4000
  agd200-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d01:
    range:
    - -4000
    - 4000
  agd301-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d09:
    range:
    - -25500
    - 25500
  agd155-af-2a06:
    range:
    - -25500
    - 25500
  agd155-af-2a10:
    range:
    - -28500
    - 28500
  agd155-ec:
    range:
    - -25500
    - 25500
  agd155-ec-var34:
    range:
    - -28500
    - 28500
  agd155-ec-var34-3:
    range:
    - -42500
    - 42500
  agd156-ec:
    range:
    - -12726
    - 12726
  agd101-ec-34a:
    range:
    - -28280
    - 28280
  agd101-ec-17a:
    range:
    - -14140
    - 14140
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# SpringTable

**定义：**

SpringTable 是一个保留的、尚未实现的数组关键字（大小为 41，可用索引为 1 至 40），当前对弹簧补偿无任何效果。有效的补偿为由 [SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)、[SpringPosFFW](SpringPosFFW.md) 和 [SpringCurrFFW](SpringCurrFFW.md) 定义的线性模型。实现后，其各元素将以 1 为起始索引保存每段的电流修正值。该参数为轴相关数组参数，保存至闪存，可随时更改。

**另请参阅：**

[SpringOn](SpringOn.md)、[SpringTableGp](SpringTableGp.md)、[SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)
