---
keyword: StallThPcnt
summary: 步进失步阈值（以百分比表示，10–90%，默认 50%）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 512
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
  - 10
  - 90
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# StallThPcnt

步进失步阈值（以百分比表示，10–90%，默认 50%）。

## 概述

`StallThPcnt` 以百分比形式（有效范围 10–90，默认 50）设定预期健康度量的多大比例被视为失步。它是步进失步检测面向用户的灵敏度旋钮：它直接缩放所计算的阈值 [StallTh](StallTh.md)，实时度量 [StallVal](StallVal.md) 会与该阈值比较。

## 工作原理

在每个控制周期，固件在构建 [StallTh](StallTh.md) 时将与速度相关的预期度量拟合乘以 `StallThPcnt/100`：

```text
threshold input = (StallThPcnt * speed) * 0.01 * 0.001
                  * (StallCnst[1]*speed + StallCnst[2]) - 10000;
```

`* 0.01` 项即将百分比转换为分数的 `/100`。随后当 `StallVal < StallTh` 时即判定为失步。

由于 `StallTh` 随 `StallThPcnt` 升高：

- **`StallThPcnt` 越高**会提高阈值，因此 `StallVal` 更容易低于它 → **灵敏度更高**（也更容易误触发）。
- **`StallThPcnt` 越低**会降低阈值 → **灵敏度更低**（度量必须进一步崩落才会标记为失步）。

有效范围为 10–90 %，默认 50 %。

## 示例

```text
AStallThPcnt[1]=50    ; threshold at 50% of the expected healthy metric
AStallThPcnt[1]       ; read back
```

## 另请参阅

- [StallTh](StallTh.md) — 此百分比所缩放的最终（只读）阈值
- [StallCnst](StallCnst.md) — 此百分比所缩放的速度相关拟合
- [StallVal](StallVal.md) — 与 `StallTh` 比较的度量
- [StallCfg](StallCfg.md) — 失步检测模式（启用此保护）
