# MasterFactDen

**Definition:**

MasterFactDen is the denominator used in the scaling ratio applied onto the delta of master variable. Once the gear motion is started, the final change in profiler position reference (if [MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 5) or target position (if [MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 6) is as shown.

$$
\mathrm{\Delta}_{ProfilerPosRef/AbsTrgt} = \mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}\ 
$$
