---
keyword: SetPosition
summary: 在不移动电机的情况下将轴位置重新定义为给定值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 154
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# SetPosition

在不移动电机的情况下将轴位置重新定义为给定值。

## 概述

`SetPosition` 在不指令任何运动的情况下,立即将轴位置参考和反馈寄存器设置为指定值。它用于定义新的坐标原点或从位置偏差中恢复。由于它重写参考,因此不能在轴运动时发出。若要清除累积的位置误差而非重新定义坐标,参见 [ZeroPosErr](ZeroPosErr.md)。它是轴相关命令函数。

## 工作原理

`SetPosition` 在**同一原子步骤中将请求值写入反馈链与整个参考链**,因此重新定义坐标时跟随误差不会发生跳变：

- 反馈侧：编码器位置、[Pos](../01-kinematics-status/Pos.md) 及其上一采样值全部设置为该值。
- 参考侧：[PosRef](../01-kinematics-status/PosRef.md)、整形后及整形滤波后的参考及其所有 64 位历史/上一采样值均设置为该值,并据此重建高精度参考累加器。

由于 [Pos](../01-kinematics-status/Pos.md) 与 [PosRef](../01-kinematics-status/PosRef.md) 按**相同偏移量**移动,位置误差 [PosErr](../01-kinematics-status/PosErr.md)（`PosRef − Pos`）被**保留**而非置零——`SetPosition` 重新标定坐标,并不会将参考拉向反馈。（若要改为将参考贴合到反馈以置零误差,请使用 [ZeroPosErr](ZeroPosErr.md)。）

![SetPosition vs ZeroPosErr](setpos-vs-zeroerr.svg)

当电机**使能**时,平滑缓冲区也必须以新值重新填种；为在不扰乱控制环的情况下完成这一点,控制器临时将 [Jerk](Jerk.md) 强制为 `0`,以新值重新填充 `2^Jerk` 滑动平均历史,然后恢复 `Jerk`。当电机**失能**时则无需此操作,因为参考已跟踪反馈。

### 条件

如果满足以下任一情形,`SetPosition` 被拒绝（不做更改）：

- 编码器**误差映射**处于激活状态——请先将其禁用（[MapType](../../04-error-mapping/MapType.md)）。该拒绝（错误码 **83**,"assigning a value to position is not allowed while error mapping is activated"）取决于**内部**映射状态,而非用户写入的 [MapType](../../04-error-mapping/MapType.md)。在你写入 `MapType = 0` 之后,映射会在 [MapErrOnStep](../../04-error-mapping/MapErrOnStep.md) 个周期内斜坡退出,且 `SetPosition` 在整个斜坡退出期间持续被拒绝,直至内部类型完全恢复为关闭。当 [MapErrOnStep](../../04-error-mapping/MapErrOnStep.md) = 0 时,退出立即完成（一个周期）,因此 `SetPosition` 会立即被接受。
- **自动增益**已开启（它使用位置滤波器）——错误码 **84**。
- 请求值**超出软件位置限位** [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) … [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)——错误码 **163**。
- 电机**使能**且**输入整形**已开启（其缓冲区过大无法重新填种）——错误码 **85**。
- **（仅 central-i v5）** 该轴是**龙门对的 Yaw 轴**（龙门模式开启时该对中的奇数编号轴）——错误码 **329**。请改为对龙门的主轴（偶数编号轴）施加 `SetPosition`；在电机使能的龙门对上,该写入会以相同偏移量移动线性轴和 Yaw 轴,从而保留龙门反馈。

它在轴运动时也被阻止（`ok_in_motion: false`）。

### 边界情况

- **电机失能：** 允许；跳过平滑缓冲区的参考重新填种,因为缓冲区已在跟踪反馈。
- **电机使能：** 允许；控制器临时将 [Jerk](Jerk.md) 强制为 `0` 以新值重新填种滑动平均历史,然后恢复 `Jerk`。输入整形必须关闭（否则以错误拒绝）。
- **越界写入：** 若值落在 `[RevPLim, FwdPLim]` 之外则被拒绝（错误码 163）；超出数据类型范围的值同样被拒绝,而非钳位。
- **仿真模式（`MotorType` = 5）：** 允许；反馈跟随参考,因此偏移立即在二者中体现。
- **ModRev 环绕：** `SetPosition` 将原始值写入参考和反馈；对于连续旋转轴,该值可能需要位于 `[0, ModRev)` 内才有意义。写入该范围外的值将由控制器在下一个满足环绕条件的周期予以环绕。
- **激活故障：** 轴被禁用,但 `SetPosition` 仍被允许（运动中检查满足——没有运动）。新值在重新使能后保持。
- **其他运动模式：** 该关键字与模式无关；它直接作用于参考/反馈寄存器。
- **误差映射 / 自动增益 / 输入整形激活：** 被拒绝（参见上述条件）——先禁用,设置,再重新启用。

## 示例

```text
ASetPosition=0       ; redefine current position as zero
ASetPosition=50000   ; redefine current position as 50000
```

## 另请参阅

- [ZeroPosErr](ZeroPosErr.md) — 置零位置误差（将参考贴合到反馈）而非重新定义坐标
- [Pos](../01-kinematics-status/Pos.md) / [PosRef](../01-kinematics-status/PosRef.md) — 由 `SetPosition` 一并移动
- [PosErr](../01-kinematics-status/PosErr.md) — 由 `SetPosition` 保留（不置零）
- [MapType](../../04-error-mapping/MapType.md) — 误差映射必须关闭
- [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) / [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) — 值必须位于这两者之间
