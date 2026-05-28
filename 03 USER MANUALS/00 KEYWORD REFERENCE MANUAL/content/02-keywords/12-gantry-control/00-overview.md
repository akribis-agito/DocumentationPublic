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
