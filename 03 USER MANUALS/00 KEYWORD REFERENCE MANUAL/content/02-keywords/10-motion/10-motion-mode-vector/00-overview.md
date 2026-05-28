# Motion mode – Vector motion

This section extends from vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). All the keywords in this section are only applicable under these motion modes.

Vector motion moves a group of axes together along a geometric path. A line or arc target ([VecType](VecType.md)) is run through a single path-velocity profile (set by [VecSpeed](VecSpeed.md), [VecAccel](VecAccel.md) and [VecDecel](VecDecel.md)), and the resulting path position is split across the member axes ([VecMemberAxes](VecMemberAxes.md)) so they stay coordinated on the path.

![Vector motion: a path target through one path-velocity profile, split across the member axes](vec-pipeline.svg)

Regardless, the standard motion keywords still apply and refer to the individual axis, instead of the vector.
