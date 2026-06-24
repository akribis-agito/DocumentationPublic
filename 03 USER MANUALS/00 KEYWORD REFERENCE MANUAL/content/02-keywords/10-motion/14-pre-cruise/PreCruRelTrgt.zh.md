---
keyword: PreCruRelTrgt
summary: 以正弦点到点运动起始点为基准的预巡航目标距离（用户单位）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 842
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PreCruRelTrgt

以正弦点到点运动起始点为基准的预巡航目标距离（用户单位）。

该关键字从 **v5（仅限 central-i）** 起可用。

## 概述

`PreCruRelTrgt` 直接设置**预巡航行程**——以用户单位表示的有符号距离，从运动起始点到**预巡航目标点**。轴在该点之前以较快的 [PreCruiseSpd](PreCruiseSpd.md) 运行，之后降至正常巡航速度完成剩余行程。该关键字适用于正弦点到点模式（[MotionMode](../02-motion-configuration/MotionMode.md) `= 20` 和 `= 21`）；有关分段概念，请参阅[预巡航概述](00-overview.md)。

它是 [PreCruAbsTrgt](PreCruAbsTrgt.md) 的相对坐标对应量，后者以绝对位置表示同一目标点。运动的最终目标仍由 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) 设置。

## 工作原理

在正弦点到点模式下发出 [Begin](../04-motion-command/Begin.md) 时，控制器按如下规则解析预巡航目标：

- 若 `PreCruRelTrgt` 为**非零**，则预巡航目标为 `起始位置 + PreCruRelTrgt`，该次运动忽略 [PreCruAbsTrgt](PreCruAbsTrgt.md)。
- 若 `PreCruRelTrgt` 为 `0`，则改用绝对值 [PreCruAbsTrgt](PreCruAbsTrgt.md)。

由于非零相对值始终优先，当需要使用绝对预巡航目标时，应将 `PreCruRelTrgt` 设为 `0`。

仅当预巡航速度高于巡航速度且定义了预巡航行程时，才会执行预巡航阶段；否则运动退化为普通正弦点到点曲线。控制器在 `Begin` 时校验几何关系，若条件不满足则拒绝运动：

| 条件 | 不满足时的效果 |
|---|---|
| 预巡航行程方向指向最终目标 | 拒绝——总行程与预巡航行程必须同向（错误 381） |
| 最终目标超过预巡航目标 | 拒绝——总行程必须长于预巡航行程（错误 383） |
| 预巡航行程足以从静止加速至巡航速度 | 拒绝——预巡航行程不足（错误 384） |
| 预巡航目标之后的剩余行程足以从巡航速度减速至静止 | 拒绝——制动行程不足（错误 385） |

## 示例

总行程 500000 用户单位，其中前 200000 以较快的预巡航速度运行：

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed (used after pre-cruise)
APreCruiseSpd=800000   ; faster pre-cruise speed
APreCruRelTrgt=200000  ; run fast for the first 200000 units
ARelTrgt=500000        ; total move distance
ABegin                 ; start the move
APreCruRelTrgt         ; read back the pre-cruise distance
```

将已配置轴切换回绝对预巡航目标，清零此关键字即可：

```text
APreCruRelTrgt=0       ; fall back to PreCruAbsTrgt
```

## 另请参阅

- [PreCruAbsTrgt](PreCruAbsTrgt.md) — 以绝对位置表示的相同目标点
- [PreCruiseSpd](PreCruiseSpd.md) — 预巡航行程中保持的速度
- [预巡航概述](00-overview.md) — 各阶段的组合方式
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — 运动的最终目标
- [MotionMode](../02-motion-configuration/MotionMode.md) — 模式 20 和 21 选择正弦点到点运动
- [Begin](../04-motion-command/Begin.md) — 校验并启动运动
