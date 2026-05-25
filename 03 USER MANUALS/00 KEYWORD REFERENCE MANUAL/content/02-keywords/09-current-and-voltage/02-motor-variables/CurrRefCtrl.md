# CurrRefCtrl

**Definition:**

CurrRefCtrl defines the loop’s current reference (instead of motor current reference). It is the value just before the decoupling matrix, current injection and current related compensation.

For position, velocity and force operation mode, CurrRefCtrl is the sum of current reference from the feedback loop, feedforwards and loop compensation. Please refer to [Control tuning – Velocity control](../../../02-keywords/11-control-tuning/04-velocity-control/00-overview.md), [Control tuning – Feedforwards](../../../02-keywords/11-control-tuning/05-feedforwards/00-overview.md) and [Control tuning – Force control](../../../02-keywords/06-protections/04-force-control/00-overview.md) for more information on CurrRefCtrl location.

For current operation mode, CurrRefCtrl is the current reference from the source defined by CurrCmdSrc (analog input, CurrCmdVal array, etc.).
