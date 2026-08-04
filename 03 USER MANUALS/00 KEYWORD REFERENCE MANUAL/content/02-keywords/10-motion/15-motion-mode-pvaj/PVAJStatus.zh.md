---
keyword: PVAJStatus
summary: PVAJ 状态、当前行与剩余行数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 883
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 4
  data_type: int32
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
# PVAJStatus

只读报告，反映本轴在 PVAJ 流程中所处的位置。

| 索引 | 内容 |
|---|---|
| `[1]` | **状态** —— 见下表 |
| `[2]` | 执行期间的**当前行**，从 1 开始 |
| `[3]` | 列表完成前的**剩余行数** |

## 状态

| 取值 | 状态 | 达成方式 |
|---|---|---|
| `0` | 未校验 | 上电，或对 [PVAJList](PVAJList.md) 的任何写入 |
| `1` | 已校验 | [PVAJValidate](PVAJValidate.md) 成功 |
| `2` | 已使能 | [PVAJArm](PVAJArm.md) `= 1` |
| `3` | 执行中 | 在 [MotionMode](../02-motion-configuration/MotionMode.md) `22` 或 `23` 下执行 `Begin` |

运动完成后该轴回到*未校验*状态，因为完成即解除使能，若要再次运行则必须重新校验列表。
