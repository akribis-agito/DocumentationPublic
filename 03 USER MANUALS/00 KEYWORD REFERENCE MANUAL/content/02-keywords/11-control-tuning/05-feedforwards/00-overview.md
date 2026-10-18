# Feedforwards

The following block diagram shows the typical feedforward control structure (including all the internal scaling).

![Feedforward structure: reference acceleration through AccFFW and reference velocity through VelFFW, summed and filtered into the current reference](feedforward-structure.svg)

Feedforward is the control effort that acts in advance, according to the motion profile to reduce position error during motion. This is different from reactive feedback control that forms control effort only when there is error.

Acceleration and velocity feedforwards will act on their counterparts, mass (inertia) and damping respectively. The summation of both feedforwards will pass through a programmable filter, before summing with velocity loop output to form loop’s current reference (CurrRefCtrl) for current control loop.

Acceleration and velocity feedforwards are applicable only when position operation mode (OperationMode = 3) is used. On AGM800 and AGM800-EC, the friction feedforward joins the same sum before the filter (see below). Velocity loop output, feedforward effort and current compensation from [TorqCompMode](../../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompMode.md) will add up to form [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md).

The following is the summary of feedforward keywords.

| No. | Keywords               | Summary                                  |
|-----|------------------------|------------------------------------------|
| 1   | [AccFFW](../../../02-keywords/11-control-tuning/05-feedforwards/AccFFW.md)      | Acceleration feedforward gain            |
| 2   | [FFFiltOn](../../../02-keywords/11-control-tuning/05-feedforwards/FFFiltOn.md) | Feedforward filter switch                |
| 3   | [FFFiltDef](../../../02-keywords/11-control-tuning/05-feedforwards/FFFiltDef.md)   | Feedforward filter definition parameters |
| 4   | [VelFFW](../../../02-keywords/11-control-tuning/05-feedforwards/VelFFW.md)      | Velocity feedforward gain                |

## Voltage feedforward (central-i v5)

A separate, model-based feedforward acts inside the current/voltage loop rather than on the position profile. From the motor's electrical model it estimates the terminal voltage needed to drive the commanded current and adds it ahead of the current PI controllers, improving current tracking at high speed and during fast current changes. These keywords are available from central-i v5.

| No. | Keywords | Summary |
|-----|----------|---------|
| 5   | [VoltageFFWOn](../../../02-keywords/11-control-tuning/05-feedforwards/VoltageFFWOn.md)   | Master enable for voltage feedforward |
| 6   | [RmFFWLevel](../../../02-keywords/11-control-tuning/05-feedforwards/RmFFWLevel.md)       | Level of the resistive (R·i) term |
| 7   | [LmFFWLevel](../../../02-keywords/11-control-tuning/05-feedforwards/LmFFWLevel.md)       | Level of the inductive (L·di/dt) term |
| 8   | [BEMFConst](../../../02-keywords/11-control-tuning/05-feedforwards/BEMFConst.md)         | Motor back-EMF constant |
| 9   | [BEMFFFWLevel](../../../02-keywords/11-control-tuning/05-feedforwards/BEMFFFWLevel.md)   | Level of the back-EMF term |
| 10  | [VqFFW](../../../02-keywords/11-control-tuning/05-feedforwards/VqFFW.md)                 | Q-axis voltage feedforward output (read-only) |
| 11  | [VdFFW](../../../02-keywords/11-control-tuning/05-feedforwards/VdFFW.md)                 | D-axis voltage feedforward output (read-only) |

## Friction feedforward (AGM800 and AGM800-EC)

The friction feedforward stage works out the current needed to overcome friction from the velocity and adds it to the feedforward sum, before the CNC skip and before the feedforward filter. So friction is zeroed with the rest of the feedforward at CNC segment transitions, and it is smoothed (and delayed at reversals) by [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) when the filter is on. Unlike acceleration and velocity feedforward, it also runs in velocity mode and in force mode with [ForcePIVOn](../../../02-keywords/11-control-tuning/07-force-control/ForcePIVOn.md) = 1; there the filter carries friction only. See [Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md) for the models, keywords and tuning order.

| No. | Keywords | Summary |
|-----|----------|---------|
| 12  | [Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md) | Friction models (`FricMethod` 0 to 5), levels, clamp and tuning |
| 13  | [CurrFFWValues](../../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) | Feedforward currents read-back: `[1]` filtered total (includes friction), `[6]` friction before the filter |
