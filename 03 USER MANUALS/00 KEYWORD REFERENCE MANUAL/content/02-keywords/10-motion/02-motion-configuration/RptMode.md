# RptMode

**Condition:**

RptMode is used only when MotionMode = 2 (repetitive point-to-point (PTP) motion).

**Definition:**

RptMode is used to define whether the repetitive motion is unidirectional or bidirectional. This is useful for applications where repeated step motion is needed.

| RptMode | Descriptions |
|---|---|
| 0 | **Bidirectional motion** Axis will move to AbsTrgt (or relative location defined by RelTrgt) and then back to initial location. 1 repetition number equals to 1 motion to AbsTrgt (or relative location defined by RelTrgt), or 1 motion back to initial position This means RptCycles = 2 equals to one set of to-and-fro motion. |
| 1 | **Unidirectional motion** Axis will always move at the position delta of (AbsTrgt – initial position) or RelTrgt, where axis will move further and further away. 1 repetition number equals 1 delta motion. |
