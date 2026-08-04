---
keyword: PVAJList
summary: PVAJ 轨迹表 —— 表头加最多 8192 行位置/速度/加速度/加加速度。
availability:
  standalone: []
  central-i:
  - v5
can_code: 880
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 32772
  data_type: double
  ok_in_motion: true
  ok_motor_on: true
  units: none
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
language: zh-CN
---
# PVAJList

由 PVAJ 运动模式（[MotionMode](../02-motion-configuration/MotionMode.md) = 22 或 23）执行的轨迹表。各模式之间的关系参见 [PVAJ 概述](00-overview.md)。

## 布局

与所有数组关键字一样，索引从 1 开始。

| 索引 | 内容 |
|---|---|
| `[1]` | **Len** —— 列表行数，`1`–`8192` |
| `[2]` | **Gap** —— 相邻两行之间的控制周期数，`1`–`32` |
| `[3]` | **Mode** —— `0` 绝对，`1` 相对于 `Begin` 时刻的位置 |
| `[4]`、`[5]`、`[6]`、`[7]` | 第 1 行：位置、速度、加速度、加加速度 |
| `[8]` … | 第 2 行，其后以 4 为步长依次类推 |

因此最后一个可用索引为 **32771** —— 第 8192 行的 `J`。

数值以 double 存储。位置单位为 counts，速度为 counts/秒，加速度为 counts/秒²，加加速度为 counts/秒³。

## 写入列表

写入**任一**元素都会使该轴回到*未校验*状态，因此任何修改之后都必须重新校验（[PVAJValidate](PVAJValidate.md)）并重新使能（[PVAJArm](PVAJArm.md)）。由于 [PVAJArm](PVAJArm.md) 对列表进行快照，因此在运动执行期间可以写入新列表 —— 正在运行的运动不受影响。

## 闪存

仅当产品的参数区足够大（14 MB）时，`PVAJList` 才保存至闪存；其他情况下**不**保存。若参数区较小，3 MB 的条目会使**每一次** `SaveFile` 都以闪存已满失败，而不仅仅是丢失 PVAJ 列表。

## 错误

列表的范围与连续性由 [PVAJValidate](PVAJValidate.md) 检查，而非在写入时检查；错误码参见该页面。
