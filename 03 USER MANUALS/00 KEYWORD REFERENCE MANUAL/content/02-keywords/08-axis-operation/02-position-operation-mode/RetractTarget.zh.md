---
keyword: RetractTarget
summary: 进入位置模式时点到点运动的绝对目标。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 609
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RetractTarget

进入位置模式时点到点运动的绝对目标。

## 概述

`RetractTarget` 是以用户单位表示的**绝对**目标位置，对应于进入位置运行模式时运行的点到点运动（前提是 [BeginOnToPos](BeginOnToPos.md) 已置位）。当 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) 非零时，它会被覆盖：此时目标将改为相对于进入时刻的位置参考来取值。该运动以 [RetractSpeed](RetractSpeed.md) 运行。它是闪存存储设置，因此可在重新上电后保持。

## 工作原理

启动进入运动时，PTP 目标按如下方式选择：

```text
if RelTrgt != 0:  target = entry reference + RelTrgt   ; relative to the entry reference
else:             target = RetractTarget               ; absolute target
```

因此 `RetractTarget` **仅在 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) 为 0 时**才被使用；否则它将被忽略，由相对目标占优。所得目标即标准的点到点目标，因此该运动与其他任何运动一样遵守软件位置限位（[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)）。默认值为 0。

## 版本间差异

在 **v5（central-i）** 中，运动管线为 64 位，因此 `RetractTarget` 是 64 位值，取值范围扩大（见 frontmatter）；目标选择逻辑保持不变。**v5 仅适用于 central-i**，因此在 standalone 上 `RetractTarget` 仍为 v4 的 32 位值。

## 示例

```text
ARetractTarget=50000 ; absolute entry-move target (user units)
ARetractSpeed=20000  ; entry-move speed
ABeginOnToPos=1      ; arm the move
AGoToPosMode         ; switch and start the move
```

### 边界情况

- **`RelTrgt ≠ 0`** —— `RetractTarget` 被忽略；运动相对于进入时的参考取值。
- **未置位则不使用** —— 仅当 [BeginOnToPos](BeginOnToPos.md) 已设置且发生进入模式切换时才会被查询。
- **位置限位裁剪** —— 超出 [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) 时，运动会被裁剪到限位处。
- **超出范围** —— 超出平台范围的值会被拒绝。
- **保存** —— 可保存至闪存。
- **平台** —— v5 扩展为 64 位；v4 为 32 位。

## 另请参阅

- [BeginOnToPos](BeginOnToPos.md) —— 置位进入运动
- [RetractSpeed](RetractSpeed.md) —— 进入运动的速度
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) —— 相对目标覆盖（非零时优先）
- [GoToPosMode](GoToPosMode.md) —— 触发该运动的命令之一
