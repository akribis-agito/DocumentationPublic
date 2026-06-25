---
keyword: FrictionComp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 406
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 327680000.0
  default: 0
  scaling: 65536.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    scaling: 1.0
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 当用户变量 `FrictionComp` 非零时，摩擦补偿功能被激活；该参数始终取正值。
---
# FrictionComp

当用户变量 `FrictionComp` 非零时，摩擦补偿功能被激活。该参数始终取正值。

当运动通过 `Begin` 指令启动时，摩擦补偿标志被置位。运动一旦开始且该标志已置位，此值即用于对速度环积分项进行预设（设置），随后标志被清除。预设在每次运动中仅应用一次：标志在单次赋值后立即清除，因此在剩余运动期间，正常的速度环积分从预设值开始恢复。对于重复运动，标志在每次重复之前重新置位，因此积分项在每次重复的开始都会被重新预设。

预设值的符号跟随指令（规划器）速度的方向，以预设时刻规划器速度的严格边界为准：

- 当规划器速度严格大于零（正方向）时，施加正值（`+FrictionComp`）。
- 当规划器速度为零或负值时，施加负值（`-FrictionComp`）。

`FrictionComp` 的单位为毫安（mA），与产生的速度环电流贡献一一对应：将积分项预设为 `FrictionComp` 将产生 `FrictionComp` mA 的电流贡献。该关键字接受 0 至 5000 mA 的值，默认值为 0。

摩擦补偿仅在 `FrictionComp` 非零时生效。值为 0 时不会在运动开始时覆盖积分器，因此对于不平衡轴或重力负载轴，积分项中已有的静态（保持）电流会被保留，而不是被重置为零。

**注意：**

此功能仅在由速度规划器驱动的运动模式下有效。
