---
keyword: BuffSlopes
summary: 在需要时施加于样条缓冲轨迹边缘的速度斜率。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 546
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# BuffSlopes

在需要时施加于样条缓冲轨迹边缘的速度斜率。

## 概述

当 [BuffEdgeMode](BuffEdgeMode.md) = 0（指定斜率边界）时，`BuffSlopes` 指定施加于样条缓冲轨迹边缘的速度斜率。它是一个三元素数组；边缘斜率取自索引 `[1]`。该值设置样条的进入/退出速度，而非由拟合自动确定。`BuffSlopes` 在 [BuffCalc](BuffCalc.md) 运行时从相关成员轴读取，保存至闪存，可随时修改，但修改只有在重新运行 [BuffCalc](BuffCalc.md) 后才会生效。

## 工作原理

### 单位与缩放

存储值是以**位置单位的千分之一每伺服采样**表示的斜率：控制器将 `BuffSlopes[1]` 除以 1000 以获得实际边缘导数。因此，存储值 `1000` 对应每采样一个位置单位的斜率，`500` 对应每采样半个位置单位。1000 的系数允许使用整数关键字设置小数斜率。

### 使用时机

仅当 **[BuffEdgeMode](BuffEdgeMode.md) = 0** 且曲线为抛物线或三次样条（[BuffSplineMod](BuffSplineMod.md) = 2 或 3）时，`BuffSlopes` 才影响拟合结果：

- 对于**抛物线**拟合，`BuffSlopes[1]` 设置轨迹起始处的初始速度（第一段的进入斜率）；其余边缘行为由逐段拟合确定。
- 对于**三次曲线**拟合，`BuffSlopes[1]` 约束末端导数，使样条以指定斜率进入和离开（钳位样条边界条件）。

当 [BuffEdgeMode](BuffEdgeMode.md) 为 1（自然）或 2（多周期）时，边缘导数由这些模式决定，忽略 `BuffSlopes`。线性插值（[BuffSplineMod](BuffSplineMod.md) = 1）同样忽略此设置。索引 `[2]` 保留；固件仅应用 `[1]`。

## 示例

```text
ABuffEdgeMode=0      ; 启用指定斜率边界
ABuffSlopes[1]=0     ; 以零速度进入/离开（从静止开始并在静止结束）
ABuffSlopes[1]=1000  ; 边缘斜率为每伺服采样 1.0 个位置单位
```

## 另请参阅

- [BuffEdgeMode](BuffEdgeMode.md) — 必须为 0 才能应用这些斜率
- [BuffSplineMod](BuffSplineMod.md) — 斜率仅适用于抛物线/三次曲线拟合
- [BuffPos](BuffPos.md) — 路径点位置
- [BuffCalc](BuffCalc.md) — 拟合样条时应用边缘斜率
