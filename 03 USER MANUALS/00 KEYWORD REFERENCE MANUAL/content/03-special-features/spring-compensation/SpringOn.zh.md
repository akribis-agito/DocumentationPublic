---
keyword: SpringOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 592
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 使能弹簧补偿功能，向控制环注入与位置相关的前馈电流以抵消弹性恢复力。
---
# SpringOn

**定义：**

SpringOn 使能弹簧补偿功能，该功能向控制环注入与位置相关的前馈电流，以抵消作用于负载的弹性恢复力。该参数为轴相关参数，不保存至闪存，可随时更改。

SpringOn 接受 0 至 2 的值，默认为 0。补偿功能通过简单的非零测试进行门控，因此任意非零值（1 或 2）均以相同方式使能；两个使能值之间的行为没有区别。由于该参数不保存至闪存，上电时将恢复为 0（禁用），需重新设置以再次使能。轴运动中亦可更改该参数。

**参见：**

[SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)、[SpringTable](SpringTable.md)、[SpringPosFFW](SpringPosFFW.md)
