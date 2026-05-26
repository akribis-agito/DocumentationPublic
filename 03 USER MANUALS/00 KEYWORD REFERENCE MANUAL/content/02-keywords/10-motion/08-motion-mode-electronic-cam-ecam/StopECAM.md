---
keyword: StopECAM
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 310
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopECAM

**Definition:**

StopECAM is used to exit ECAM motion.

However, upon receipt of such command, the axis does not quit the ECAM motion outright. Rather, the master range shrinks, where the beginning and ending pattern segments are appended to the existing cycle pattern. Only if the master value exits this new range that ECAM motion will stop.

For the example below (ECAMGap \> 0 and ECAMCycles = 3), the axis receives StopECAM command while the master position is in the middle of second cycle. The master range will shrink where $R > P$ and $S < Q$. Now, only when the master becomes lower than or equal to R /higher than or equal to S that the ECAM motion will end. Note that the slave position reference at R does not necessarily equal to that at P, since the cam pattern has shrunk. This is also true for S when compared to Q.

![image51.png](../../../assets/image51.png)

The following picture shows the same stopping logic of StopECAM command for condition when ECAMCycles \< 0.

![image52.png](../../../assets/image52.png)
<span class="anchor" id="_ECAMCycCount"></span>If user wants to stop the ECAM motion immediately, [Stop](../../../02-keywords/10-motion/04-motion-command/Stop.md) command can be used, so that slave position reference will be unchanged regardless of the master value.
