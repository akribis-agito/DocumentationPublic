# Gantry control

Keywords for configuring and tuning gantry (dual-motor) axes, where two parallel drive motors move a single mechanism under coordinated MIMO control.

This category is organised into:

- [General variables](01-general-variables/00-overview.md) — enabling gantry mode and the map/yaw correction variables
- [Gantry kinematic feedback](02-gantry-kinematic-feedback/00-overview.md) — feedback, offset, and auxiliary-encoder readings
- [Gantry tuning](03-gantry-tuning/00-overview.md) — yaw position/velocity gains and feedforward terms
- [Dual-loop gantry control](04-dual-loop-gantry-control/00-overview.md) — feedback sourcing for dual-loop and pseudo dual-loop modes

## How gantry control works

A gantry has two parallel drive motors moving the two ends of one beam. Instead of controlling each motor independently, the controller transforms the two motor measurements into two virtual axes — a **common (linear) mode** that is the mean of the two ends (what the stage actually translates, commanded by the master axis), and a **differential (yaw) mode** that is the difference between the two ends (the squareness of the beam, normally held at zero or at the offset set by [GantryYawRef](01-general-variables/GantryYawRef.md)). Each virtual axis runs its own position and velocity loops, and the two loop outputs are recombined into per-motor current commands: one motor receives linear + yaw and the other linear − yaw. This decoupling means a translation command does not induce yaw and a yaw correction does not induce translation.

The common/differential transform and recombination are illustrated in the diagram under [General variables / GantryOn](01-general-variables/GantryOn.md).

## Walk-through: engage gantry control

The two motors must be powered, phased, and the yaw axis must not be commanded independently before `GantryOn` is set. The full engagement sequence on a master `A` / yaw `B` pair is:

1. **Bring both motors up.** Both `A` and `B` must have completed commutation (`AComtStatus[1]` and `BComtStatus[1]` both `100`) and have their motors enabled. Until then, [GantryOn](01-general-variables/GantryOn.md) is rejected and will not stay set:

   ```text
   AMotorOn=1           ; enable the master motor
   BMotorOn=1           ; enable the yaw motor (same pair)
   ```

2. **Engage gantry mode on the master axis.** On the `0` → `1` transition the controller captures the current difference between the two ends into [GantryOffset](02-gantry-kinematic-feedback/GantryOffset.md) and folds it into the feedbacks so the differential (yaw) reading starts from clean zero without forcing the beam square. The control scheme switches to the gantry MIMO topology:

   ```text
   AGantryOn=1          ; engage MIMO gantry control on the master axis
   AGantryOffset        ; read back the captured A/B offset (set at the 0->1 transition)
   ```

3. **Verify the feedbacks.** The master value of [GantryFdbk](02-gantry-kinematic-feedback/GantryFdbk.md) is the common (mean) gantry position the linear loop follows; the yaw-axis value is the differential reading the yaw loop drives to [GantryYawRef](01-general-variables/GantryYawRef.md). The feedbacks are recomputed every cycle **only while gantry is on**; before the first engagement they read `0`, and after disengagement they hold their last value until the next engagement.

   ```text
   AGantryFdbk          ; mean (common) gantry position
   BGantryFdbk          ; differential (yaw) reading
   AGantryYawRef        ; commanded yaw target (default 0)
   ```

4. **Move the stage by commanding the master axis only** (gantry motion is commanded through `A`'s normal motion keywords). The yaw loop quietly holds the beam square. If either motor of the pair turns off mid-run — for example because of a fault — the controller deliberately turns the other one off too and records [ConFlt](../07-status-and-faults/ConFlt.md) code `1061` on the side that was forced down; `AGantryOn` is then cleared back to `0` and engagement must be repeated after the fault is resolved.

5. **Disengage** by writing `AGantryOn=0`. Each axis returns to independent control. Cycling gantry mode off and on recaptures `GantryOffset`, so do not toggle it casually while the beam is loaded.

For load-side control where the linear loop closes on a separate measurement (e.g. a ruler under the workpiece), see [GantryDLoopOn](01-general-variables/GantryDLoopOn.md) and [GantryFdbkSrc](02-gantry-kinematic-feedback/GantryFdbkSrc.md) in [Dual-loop gantry control](04-dual-loop-gantry-control/00-overview.md). For a position-dependent 50/50 split along the beam, see [GantryMapType](01-general-variables/GantryMapType.md) (central-i v5).
