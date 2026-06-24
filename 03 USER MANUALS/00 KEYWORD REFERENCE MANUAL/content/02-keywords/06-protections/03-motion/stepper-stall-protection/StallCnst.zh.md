---
keyword: StallCnst
summary: 步进失步（堵转）检测的整定常数（3 元素数组）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 515
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
# StallCnst

步进失步（堵转）检测的整定常数。

## 概述

`StallCnst` 是一个数组，保存着**期望堵转度量值相对指令速度的线性拟合**的系数。堵转阈值计算使用这些系数来预测当前速度下健康的 [StallVal](StallVal.md)，从而能将真正的坍塌（堵转）与该度量值正常的速度依赖性区分开。

## 工作原理

在每个周期构建阈值 [StallTh](StallTh.md) 时，固件会计算拟合 `slope·speed + intercept`：

```text
fit = StallCnst[1] * speed + StallCnst[2]    ; slope*speed + intercept
```

其中 `speed` 是（经位移的）指令速度绝对值。

| 元素 | 作用 |
|---------|------|
| `StallCnst[1]` | **斜率**——期望度量值随速度增长的快慢 |
| `StallCnst[2]` | **截距**——（接近）零速度时的期望度量值 |

得到的拟合结果随后由 [StallThPcnt](StallThPcnt.md) 缩放并加上偏移，形成 [StallTh](StallTh.md)。该数组大小为 3；只有上述斜率和截距条目参与阈值公式。

这些系数是针对特定电机/负载，通过在若干速度下表征健康的 `StallVal` 并拟合一条直线来确定的。两者均默认为 `0`；在默认系数下，拟合结果为 `0`，因此阈值输入仅剩固定的 `−10000` 偏移，[StallTh](StallTh.md) 变为负值。由于 [StallVal](StallVal.md) 为非负值，在针对应用恰当设置这些系数之前，永远不会标记任何堵转。

## 示例

```text
AStallCnst[1]=...     ; slope of the expected-metric-vs-speed fit
AStallCnst[2]=...     ; intercept of the fit
AStallCnst[1]         ; read back the slope
```

## 另请参阅

- [StallTh](StallTh.md) — 使用这些系数的阈值
- [StallThPcnt](StallThPcnt.md) — 缩放拟合结果的百分比
- [StallVal](StallVal.md) — 这些系数所建模的度量值
- [StallCfg](StallCfg.md) — 堵转检测模式
