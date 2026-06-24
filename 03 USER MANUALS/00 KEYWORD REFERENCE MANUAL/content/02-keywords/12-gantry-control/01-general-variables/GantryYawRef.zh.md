---
keyword: GantryYawRef
summary: 偏摆修正参考，指令两台龙门电机之间的差模偏置。
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 679
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
  - -20000
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryYawRef

偏摆修正参考，指令两台龙门电机之间的差模偏置。

## 概述

`GantryYawRef` 是龙门**差模（偏摆）环**的位置参考——该虚拟轴控制横梁两端的差值（参见 [GantryOn](GantryOn.md) 中的共模/差模说明）。设为 `0` 指令横梁保持对齐；非零值（以用户单位表示）指令两端之间的有意偏斜，用于补偿机械偏差使负载运行准确。该参数为轴范围，不保存至闪存，可随时修改，包括在运动中。允许范围为 -20000 到 20000。

偏摆环将该参考与差模反馈（[GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) 的偏摆轴值）进行比较，向两台电机驱入差模电流——一台加，一台减——以消除误差。其响应由偏摆轴增益 [GantryPosGain](../03-gantry-tuning/GantryPosGain.md)、[GantryVelGain](../03-gantry-tuning/GantryVelGain.md) 及相关前馈/积分项设置；产生的差模电流由 [GantryCurrRef](GantryCurrRef.md) 报告。该参考仅在龙门模式激活时（[GantryOn](GantryOn.md) = 1）生效。

## 工作原理

每个控制周期，偏摆环由 `GantryYawRef` 与差模反馈形成误差，运行偏摆位置环和速度环，并产生偏摆电流指令。该指令随后在控制器将两个虚拟轴输出重新合成为两台物理电机电流时与共模（线性）电流指令合并：一台电机接收线性 + 偏摆，另一台接收线性 − 偏摆。由于两个环已解耦，指令偏摆偏置不会平移台。

## 示例

```text
AGantryYawRef=500   ; 指令偏摆修正偏置（用户单位）
AGantryYawRef=0     ; 取消偏摆修正
AGantryYawRef      ; 读取当前偏摆参考
```

### 边界情况

- **龙门关闭**（[GantryOn](GantryOn.md) = 0）— 偏摆环未激活；写入被接受但参考对电机无影响。在 `0 → 1` 跳变时，固件将**偏摆轴的 `GantryYawRef` 复位为 `0`** 以与捕获的偏置对齐，因此接合前的任何预设值均会丢失。
- **写入错误轴** — 偏摆环读取的是**偏摆轴**（`B` 轴）上的 `GantryYawRef`；写入主轴或非龙门轴虽被接受但从不被读取。
- **电机关闭** — 被接受；值保留至两台电机均使能且龙门接合后生效。
- **超出范围** — -20000 到 20000 范围之外的写入被拒绝；值不会被钳位。
- **龙门关闭跳变时** — 固件在重新合成时将 `GantryYawRef` 展开到各电机的位置参考（一端偏移 +YawRef/2，另一端偏移 -YawRef/2），因此解除接合时非零偏摆将使两台电机保持对应的机械偏置。
- **平台** — 仅适用于 v4。在 v5 上不存在 `GantryYawRef`；偏摆参考由规划器生成——参见 [v5 双环/龙门概述](../04-dual-loop-gantry-control/00-overview.md)。

## 另请参阅

- [GantryOn](GantryOn.md) — 必须使能才能应用偏摆修正；解释共模与差模模式
- [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) — 该参考所比较的差模（偏摆）反馈
- [GantryCurrRef](GantryCurrRef.md) — 偏摆环产生的差模电流
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — 偏摆位置环的比例增益
- [GantryVelGain](../03-gantry-tuning/GantryVelGain.md) — 偏摆速度环的比例增益
