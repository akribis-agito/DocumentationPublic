---
summary: 期望用户单位与编码器计数之间的比率，用于读取位置及其各阶导数。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# UsrUnits/AuxUsrUnits

期望用户单位与编码器计数之间的比率，用于读取位置及其各阶导数。

## 概述

`UsrUnits` 允许用户以编码器计数以外的单位读写位置及其各阶导数。它对与上位机交换的数值（位置、速度、加速度）进行缩放，使其能够以便于工程使用的单位（例如 mm）而非原始计数来表示。内部控制环始终以计数工作；`UsrUnits` 仅在通信/显示层应用。`AuxUsrUnits` 是辅助编码器的对应项，以相同方式作用于辅助反馈位置及其各阶导数。

> **注意（central-i v5）** —— `UsrUnits`/`AuxUsrUnits` 是嵌入式的逐轴缩放。central-i v5 还提供一种替代的*全局工程单位特性*，通过 [UserUnitsEn](../../21-engineering-units/UserUnitsEn.md) 逐轴启用，它以可配置的工程单位表示关键字数值。这两套系统在同一轴上互斥：当 `UserUnitsEn = 1` 且 `UsrUnits`/`AuxUsrUnits` 保持为非默认值时，访问受影响的关键字将被拒绝并返回错误 `338`。将嵌入式缩放保持为默认值，或将 `UserUnitsEn` 重新设回 0，即可解决该冲突。

## 工作原理

`UsrUnits` 以 **16.16 定点比率**存储：有效缩放因子为 `UsrUnits / 65536`（定点缩放为 65536，即 16 个小数位）。因此默认值 `UsrUnits = 65536` 表示因子为 1（数值直接以计数显示）。

$$\text{user value} = \frac{\text{counts}}{\bigl(\text{UsrUnits} / 65536\bigr)} = \text{counts} \cdot \frac{65536}{\text{UsrUnits}}$$

当 `UsrUnits` 是 65536 的精确整数倍时，固件采用快速精确路径，将计数值除以 `UsrUnits >> 16` 并取整；否则使用完整的定点比率。写入（例如设置目标值）按相反方式缩放（乘以该比率）。同一因子适用于所有导数，因此速度以 用户单位/s 报告，加速度以 用户单位/s² 报告。

若要表示“*N* 个编码器计数 = 1 个用户单位”，则设置 `UsrUnits = N × 65536`。

## 示例

若要在 5 个编码器计数等于 1 mm 时以 mm 读取位置，则将比率设为 5 —— 即 `UsrUnits = 5 × 65536 = 327680`。此时位置以 mm 报告，速度以 mm/s 报告，加速度以 mm/s² 报告。

第二个实例：一台 `EncRes = 10000` 计数/转的旋转电机，你希望以度数读取。一度对应 `10000 / 360 ≈ 27.78` 个计数，因此设置 `UsrUnits = 27.78 × 65536 ≈ 1820445`。此后上位机看到的位置以度数表示，速度以 deg/s 表示，加速度以 deg/s² 表示。

```text
AUsrUnits=327680     ; 5 counts per user unit (ratio 5 = 5 x 65536) — mm with 5 counts/mm
AUsrUnits=1820445    ; degrees on a rotary motor with EncRes = 10000
AUsrUnits=65536      ; factor 1 — report directly in encoder counts (default)
```

## 参见

- [EncRes](EncRes.md) —— 原始编码器分辨率，以每节距或每转的计数表示
- [Pos](../../10-motion/01-kinematics-status/Pos.md) —— 反馈位置，按 `UsrUnits` 缩放后报告
- [UserUnitsEn](../../21-engineering-units/UserUnitsEn.md) —— central-i v5 全局工程单位特性，与本嵌入式缩放互斥（错误 `338`）
- [Engineering Units overview](../../21-engineering-units/00-overview.md) —— 全局 Group / Factor / Unit 模型
