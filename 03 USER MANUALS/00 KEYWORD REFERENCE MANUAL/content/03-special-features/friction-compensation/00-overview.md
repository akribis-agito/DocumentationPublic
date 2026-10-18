# Friction feedforward

AGM800 and AGM800-EC (central-i v5) have one friction feedforward stage. It looks at the velocity, works out the current the axis needs to overcome friction, and adds that current to the feedforward path, so the velocity loop does not have to discover the friction through following error first.

This is not [FrictionComp](FrictionComp.md). `FrictionComp` seeds the velocity-loop integrator once at the start of a move; the friction feedforward stage acts on every control cycle.

## The stage in one picture

$$
\text{FricMethod model} \;+\; \text{quadrant-switching kick} \;\longrightarrow\; \boxed{\pm\,\text{FricLim}} \;\longrightarrow\; \text{feedforward sum} \;\longrightarrow\; \text{CNC skip} \;\longrightarrow\; \boxed{\text{FFFiltOn / FFFiltDef}} \;\longrightarrow\; \text{CurrRef}
$$

1. **Model.** [FricMethod](FricMethod.md) picks the friction model (0 = off, 1 to 5).
2. **Quadrant-switching kick (optional).** With [FricQSCOn](FricQSCOn.md) = 1, a short breakaway kick is added at starts and reversals (methods 0 to 3 only).
3. **One clamp.** [FricLim](FricLim.md) limits the total to ±`FricLim` % of [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md).
4. **Feedforward path.** The clamped friction current is added to the feedforward sum *before* the CNC skip and *before* the feedforward filter:
   - At CNC segment transitions the firmware zeroes all feedforward for two control cycles. Friction is zeroed with the rest — one rule for all feedforward.
   - With [FFFiltOn](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltOn.md) = 1, friction passes through the same filter ([FFFiltDef](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltDef.md)) as the acceleration and velocity feedforward.
5. **When it runs.** Whenever the velocity loop forms the current reference: position mode, velocity mode, and force mode with [ForcePIVOn](../../02-keywords/11-control-tuning/07-force-control/ForcePIVOn.md) = 1. In velocity and force mode the filter carries friction only, because [AccFFW](../../02-keywords/11-control-tuning/05-feedforwards/AccFFW.md) and [VelFFW](../../02-keywords/11-control-tuning/05-feedforwards/VelFFW.md) act in position mode only. In other modes the stage is off and its internal state is cleared.

**Reading it back.** [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md)`[6]` is the friction current *before* the filter. `CurrFFWValues[1]` is the filtered total that goes into the current reference, and it now includes friction.

**Filter delay.** With `FFFiltOn` = 1 the friction step at a reversal is smoothed and delayed by the filter. If you need sharp compensation at reversals, tune with `FFFiltOn` = 0, or choose a filter with little delay.

## Models

| `FricMethod` | Model | Keywords it uses |
|---|---|---|
| 0 | Off | — |
| 1 | Linear ramp through zero | FricIPos/Neg, FricVBandPos/Neg, FricViscous |
| 2 | Hysteresis (switch with memory) | FricIPos/Neg, FricVBandPos/Neg, FricViscous |
| 3 | Play (hysteresis with a ramp) | FricIPos/Neg, FricVBandPos/Neg, FricViscous |
| 4 | LuGre (bristle model) | FricIPos/Neg, FricIStatPos/Neg, FricVStribPos/Neg, FricBrstlStf, FricBrstlDmp, FricViscous |
| 5 | Stribeck | FricIPos/Neg, FricIStatPos/Neg, FricVBandPos/Neg, FricVStribPos/Neg, FricViscous |

Method 5, for velocity $v$ (from [FricVelSrc](FricVelSrc.md)) and velocity feedback $v_{fb}$, per direction of travel:

$$
I = \operatorname{sign}(v)\cdot\tanh\!\left(\frac{|v|}{\text{FricVBand}}\right)\cdot\left(\text{FricI} + (\text{FricIStat} - \text{FricI})\,e^{-(v/\text{FricVStrib})^2}\right) + \text{FricViscous}\cdot v_{fb}
$$

The levels are used as magnitudes; the sign comes from the direction of travel.

## Keywords

| CAN | Keyword | What it sets |
|---|---|---|
| 921 | [FricVStribPos](FricVStribPos.md) | Stribeck velocity, positive direction (counts/s) |
| 922 | [FricVStribNeg](FricVStribNeg.md) | Stribeck velocity, negative direction (counts/s) |
| 925 | [FricLim](FricLim.md) | Clamp on the whole stage (% of PeakCL) |
| 926 | [FricMethod](FricMethod.md) | Model: 0 off, 1 linear, 2 hysteresis, 3 play, 4 LuGre, 5 Stribeck |
| 927 | [FricVelSrc](FricVelSrc.md) | Velocity source: 0 dPosRef, 1 VelRef, 2 feedback |
| 928 | [FricIPos](FricIPos.md) | Coulomb level, positive direction (mA) |
| 929 | [FricINeg](FricINeg.md) | Coulomb level, negative direction (mA) |
| 930 | [FricVBandPos](FricVBandPos.md) | Zero-crossing band, positive side (counts/s) |
| 931 | [FricVBandNeg](FricVBandNeg.md) | Zero-crossing band, negative side (counts/s) |
| 932 | [FricViscous](FricViscous.md) | Viscous slope (mA per count/s) |
| 933 | [FricIStatPos](FricIStatPos.md) | Breakaway level, positive direction (mA) |
| 934 | [FricIStatNeg](FricIStatNeg.md) | Breakaway level, negative direction (mA) |
| 935 | [FricBrstlStf](FricBrstlStf.md) | LuGre bristle stiffness σ0 |
| 936 | [FricBrstlDmp](FricBrstlDmp.md) | LuGre bristle damping σ1 |
| 938 | [FricQSCOn](FricQSCOn.md) | Quadrant-switching kick on/off |
| 939 | [FricQSCTime](FricQSCTime.md) | Kick decay time constant (µs) |
| 940 | [FricQSCHold](FricQSCHold.md) | Hold-off before the kick (µs) |

## FricLim

`FricLim` is kept as it is for now: one clamp on the whole stage, default 40 % of `PeakCL`. The firmware does not report when it is limiting. Whether the friction stage needs its own clamp at all is an open question (Firmware-Main #1423).

## Gravity and constant offsets

Friction levels are for friction only. Put gravity on a vertical axis, spring preload or any other constant current in [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md) (selected with [TorqCompMode](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompMode.md)), not in `FricIPos`/`FricINeg`.

## Tuning order

Tune with `FFFiltOn` = 0 so the filter does not hide what friction is doing.

1. **Null the offset.** Select a fixed compensation entry with [TorqCompMode](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompMode.md) (for example `TorqCompMode` = 1) and set that entry of [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md) (here `TorqCompFix[1]`) so the axis holds still and moves at low speed with the same current in both directions. Do this with `FricMethod` = 0.
2. **Per-direction levels.** Move slowly at constant speed in each direction and set `FricIPos` and `FricINeg` to the current the velocity loop still needs. For methods 4 and 5, then set the breakaway levels `FricIStatPos`/`FricIStatNeg` and the Stribeck velocities `FricVStribPos`/`FricVStribNeg`. Set the bands `FricVBandPos`/`FricVBandNeg` just above the velocity noise.
3. **Slope.** Last, run at a few higher speeds and set `FricViscous` so the remaining current no longer grows with speed.

Then turn `FFFiltOn` back on if you use the feedforward filter, and check the reversals.

## Changes from 5.3.0-rc4

5.3.0 merges the rc4 Stribeck feedforward into this stage as `FricMethod` = 5 and renames several keywords. **There is no compatibility layer**: values saved under rc4 are not converted. After upgrading, re-enter the friction settings.

| rc4 keyword (CAN) | 5.3.0 | Note |
|---|---|---|
| StribOn (920) | `FricMethod` = 5 | Code 920 is now unused. |
| StribVs (921) | [FricVStribPos](FricVStribPos.md) / [FricVStribNeg](FricVStribNeg.md) | Now per direction; 921 is `FricVStribPos`. |
| StribEps (922) | [FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md) | The tanh width is the band; 922 is now `FricVStribNeg`. |
| StribFc (923) | [FricIPos](FricIPos.md) / [FricINeg](FricINeg.md) | Code 923 is now unused. |
| StribFsEx (924) | [FricIStatPos](FricIStatPos.md) / [FricIStatNeg](FricIStatNeg.md) | Now an absolute level: rc4 StribFc + StribFsEx. Code 924 is now unused. |
| StribLim (925) | [FricLim](FricLim.md) | Same code; now clamps the whole stage. |
| FricVBlindPos / FricVBlindNeg (930/931) | [FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md) | Renamed, same codes. |
| FricSigma0 / FricSigma1 (935/936) | [FricBrstlStf](FricBrstlStf.md) / [FricBrstlDmp](FricBrstlDmp.md) | Renamed, same codes. |
| FricCurr (937) | [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md)`[6]` | Code 937 is now unused. |
| FricQSCDelay (940) | [FricQSCHold](FricQSCHold.md) | Same code; now in µs instead of control cycles. |

LuGre (method 4) now reads the Stribeck velocity from `FricVStribPos`/`FricVStribNeg`; in rc4 it read the band.

To set up the rc4 Stribeck behaviour in 5.3.0: `FricMethod` = 5, `FricIPos` = StribFc, `FricINeg` = −StribFc, `FricIStatPos` = StribFc + StribFsEx, `FricIStatNeg` = −(StribFc + StribFsEx), `FricVBandPos` = `FricVBandNeg` = StribEps, `FricVStribPos` = `FricVStribNeg` = StribVs, `FricLim` = StribLim, `FricViscous` = 0, `FricVelSrc` = 0.

## See also

- [FrictionComp](FrictionComp.md) — one-time integrator seed at the start of a move (a different mechanism)
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — feedforward read-back
- [Feedforwards](../../02-keywords/11-control-tuning/05-feedforwards/00-overview.md)
