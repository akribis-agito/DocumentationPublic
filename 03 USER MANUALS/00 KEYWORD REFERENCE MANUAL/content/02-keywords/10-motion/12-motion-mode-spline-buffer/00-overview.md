# Motion mode – Spline buffer

Spline buffer motion mode produces smooth interpolated motion by fitting a spline through a set of user-supplied waypoints. The waypoint positions are loaded into [BuffPos](BuffPos.md) and their per-segment durations into [BuffTime](BuffTime.md), then [BuffCalc](BuffCalc.md) pre-computes the spline coefficients before a `Begin` command starts the motion.

![Spline buffer motion: buffered waypoints fitted to a spline, then streamed as the reference](spline-pipeline.svg)

The shape of the curve is controlled by [BuffSplineMod](BuffSplineMod.md) (interpolation mode), [BuffEdgeMode](BuffEdgeMode.md) (start/end boundary conditions), and [BuffSlopes](BuffSlopes.md) (edge velocity slopes). [BuffCycles](BuffCycles.md) sets how many times the trajectory repeats, and [BuffStatus](BuffStatus.md) reports the running state. A motion can be stopped with [StopBuff](../04-motion-command/StopBuff.md).
