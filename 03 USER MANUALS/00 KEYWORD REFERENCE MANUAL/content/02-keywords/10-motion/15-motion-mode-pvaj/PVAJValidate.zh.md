---
keyword: PVAJValidate
summary: 在允许使能之前校验 PVAJ 列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 881
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
  - 1
  - 3
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
language: zh-CN
---
# PVAJValidate

校验本轴的 [PVAJList](PVAJList.md)。列表必须通过校验，[PVAJArm](PVAJArm.md) 才会接受它。

| 取值 | 执行的检查 |
|---|---|
| `1` | **完整** —— 表头、范围**及**连续性 |
| `2` | **不检查** —— 不作检查直接置为有效。轨迹的正确性由用户自行负责 |
| `3` | **部分** —— 仅表头与范围；不检查连续性 |

成功后该轴进入*已校验*状态，可在 [PVAJStatus](PVAJStatus.md)`[1]` 中查看。

## 检查内容

**表头** —— `Len` 在 `1`–`8192` 之间，`Gap` 在 `1`–`32` 之间，`Mode` 为 `0` 或 `1`。

**范围** —— 每一行的位置在位置限制之内，速度在 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) 之内，加速度在 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) 之内。

**连续性** —— 相邻两行与其间五次多项式所隐含的结果一致，位置误差在 [PVAJPosTol](PVAJPosTol.md) 之内，速度误差在 [PVAJVelTol](PVAJVelTol.md) 之内。

## 错误

| 错误码 | 含义 |
|---|---|
| `390` | 列表长度（`Len`）超出范围 |
| `391` | 间隔（Gap）超出范围 |
| `392` | 模式既非 `0` 也非 `1` |
| `393` | 某个位置超出位置限制 |
| `394` | 某个速度超过 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) |
| `395` | 某个加速度超过 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) |
| `396` | 位置连续性检查未通过 —— 请检查 [PVAJPosTol](PVAJPosTol.md) |
| `397` | 速度连续性检查未通过 —— 请检查 [PVAJVelTol](PVAJVelTol.md) |

范围失败优先于更早出现的连续性失败被报告，且报告的行号即为失败所在的行。
