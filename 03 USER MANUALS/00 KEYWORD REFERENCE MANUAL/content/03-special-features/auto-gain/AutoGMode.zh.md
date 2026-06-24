---
keyword: AutoGMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 367
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 选择自整定算法的运行模式。
---
# AutoGMode

**定义：**

AutoGMode 选择自整定算法的运行模式。该模式控制算法是自行计算惯量比，还是使用您在 AutoGJratUs 中提供的值；以及计算所得增益是自动应用（全自动），还是留待您之后通过 AutoGCopy 手动应用（半自动）。范围 0 至 5；默认值 1。该参数为轴相关参数，保存至闪存，可随时修改。

| 值 | 含义 |
|-------|---------|
| 0 | 手动：算法运行，但不计算任何参数。 |
| 1 | 计算惯量比与增益，并自动应用（全自动）。 |
| 2 | 计算惯量比与增益，但不自动应用；之后通过 AutoGCopy 手动应用（半自动）。 |
| 3 | 使用 AutoGJratUs 中用户提供的惯量比，并自动应用增益（全自动）。 |
| 4 | 使用 AutoGJratUs 中用户提供的惯量比，但不自动应用增益；之后通过 AutoGCopy 手动应用（半自动）。 |
| 5 | 计算估算惯量与用户提供惯量之间的增益比（估算总惯量除以用户提供的总惯量，以百分比表示）并进行校验。 |

在模式 3、4 和 5 中，仅当 AutoGJratUs 的值在 AutoGMinRat 至 AutoGMaxRat 范围内时，该值才会被采用；超出该范围时，增益不会被计算，也不会有任何应用操作。当增益被应用时（全自动模式 1 和 3，或在半自动模式 2 和 4 中通过 AutoGCopy 应用），只有在 AutoGMask 中启用的参数才会被写入，且写入目标为 AutoGNumSet 所选的控制组。

**另见：**

[AutoGOn](AutoGOn.md)、[AutoGStatus](AutoGStatus.md)、[AutoGNumSet](AutoGNumSet.md)
