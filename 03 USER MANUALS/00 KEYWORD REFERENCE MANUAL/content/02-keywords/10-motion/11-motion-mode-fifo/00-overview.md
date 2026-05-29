# Motion mode – First in first out (FIFO)

FIFO motion mode lets the user push a sequence of motion segments into a queue, which the controller then executes in order. Segments can be pushed before or during the motion, and the queue holds up to 128 entries.

![FIFO motion: the host fills a point queue that the controller drains each cycle time into the reference](fifo-pipeline.svg)

Two related subsystems are documented in this section:

- **FIFO segment motion** ([MotionMode](../02-motion-configuration/MotionMode.md) = 9) — sequences of linear (constant-velocity) and parabolic (constant-acceleration) segments. See [FIFOType](FIFOType.md) for the full description, with [FIFOValue](FIFOValue.md), [FIFOStatus](FIFOStatus.md), [FIFOCycleTime](FIFOCycleTime.md), the `FIFOPush*` functions ([FIFOPushCycle](FIFOPushCycle.md), [FIFOPushLinP](FIFOPushLinP.md), [FIFOPushLinV](FIFOPushLinV.md), [FIFOPushParP](FIFOPushParP.md), [FIFOPushParA](FIFOPushParA.md)), [FIFORemove](FIFORemove.md), [FIFOClear](FIFOClear.md), and [StopFIFO](StopFIFO.md).
- **FIFO position tracking** ([MotionMode](../02-motion-configuration/MotionMode.md) = 19) — a reference trajectory streamed from a position queue. See [FIFOPosType](FIFOPosType.md), [FIFOPosFIFOEn](FIFOPosFIFOEn.md), [FIFOPosCycle](FIFOPosCycle.md), [FIFOPosPush](FIFOPosPush.md), [FIFOPosTrgt](FIFOPosTrgt.md), [FIFOPosPosOf](FIFOPosPosOf.md), [FIFOPosVelOf](FIFOPosVelOf.md), [FIFOPosCurrOf](FIFOPosCurrOf.md), [FIFOPosStatus](FIFOPosStatus.md), and [FIFOPosClear](FIFOPosClear.md).

## Underrun behaviour by subsystem

The two subsystems behave differently when the queue empties — this is a frequently missed detail:

| Subsystem | When the queue empties... |
|---|---|
| FIFO segment motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 9) | The motion **ends** automatically on the last consumed segment (underrun). Use [StopFIFO](StopFIFO.md) for a graceful end or [Stop](../04-motion-command/Stop.md) to decelerate to zero. |
| FIFO position tracking ([MotionMode](../02-motion-configuration/MotionMode.md) = 19) | The motion does **not** end. The axis holds the last working target [FIFOPosTrgt](FIFOPosTrgt.md) and waits. Use [Stop](../04-motion-command/Stop.md) to bring it to rest. |
