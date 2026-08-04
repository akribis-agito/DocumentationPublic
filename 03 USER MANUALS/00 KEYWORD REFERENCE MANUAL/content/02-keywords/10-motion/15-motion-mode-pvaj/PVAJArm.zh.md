---
keyword: PVAJArm
summary: 对已校验的 PVAJ 列表进行快照，使该轴可被 Begin 启动。
availability:
  standalone: []
  central-i:
  - v5
can_code: 882
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
last_updated: '2026-08-04'
doc_revision: '2026.08'
language: zh-CN
---
# PVAJArm

`PVAJArm = 1` **使能**该轴：已校验的 [PVAJList](PVAJList.md) 被复制到内部快照，该轴即可在 PVAJ 运动模式下被 `Begin` 启动。`PVAJArm = 0` 解除使能。

由于使能会进行快照，因此在运动执行期间可以上传并校验新的列表 —— 正在运行的运动继续使用其启动时的副本。

运动完成后该轴自动**解除使能**，故每次运行都需要重新执行 `PVAJArm = 1`。

## 错误

| 错误码 | 含义 |
|---|---|
| `398` | 列表尚未校验 —— 请先调用 [PVAJValidate](PVAJValidate.md) |
| `399` | 该轴正在执行 PVAJ 运动；在该运动结束前既不能使能也不能解除使能 |

对正在执行的轴解除使能会被拒绝而非被执行：否则插值器将继续运行在一份已不再归属于任何对象的快照之上。
