---
keyword: IdRef
summary: 只读的直轴电流参考，用于 dq0 域控制；目前始终为 0。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 29
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IdRef

只读的直轴电流参考，用于 dq0 域控制；目前始终为 0。

## 概述

`IdRef` 是直轴（d 轴）的参考电流，单位为毫安，用于 dq0 域（矢量）电流控制。它是相对于反馈值 [Id](Id.md) 进行调节的参考值，产生误差 [IdErr](IdErr.md)。d 轴为磁通/磁场轴；将 `IdRef` 保持为 0 可使所有指令电流均用于产生力矩（位于 q 轴上）。

## 工作原理

在三相电流环中，固件无条件地将直轴参考设为零：

$$
\text{IdRef}\ \lbrack mA\rbrack = 0
$$

因此 d 轴 PI 调节器将 [Id](Id.md) 驱动至零。当前固件不会产生非零的 `IdRef`（用于弱磁）。对于有刷电机和步进电机，d 轴不使用，`IdRef` 为 0。如需涉及非零 `IdRef` 的应用（例如弱磁），请联系 Agito。

## 示例

```text
AIdRef              ; read direct-axis current reference (mA)
```

## 另请参阅

- [Id](Id.md) — 相对于 IdRef 进行调节的直轴反馈电流
- [IdErr](IdErr.md) — 直轴电流误差（IdRef − Id）
- [IqRef](IqRef.md) — 交轴（力矩）电流参考
