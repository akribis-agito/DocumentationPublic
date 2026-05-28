# Motion mode – Computer numerical control (CNC)

CNC mode supports two parallel motion engines, **CNCA** and **CNCB**. Each
keyword exists as a CNCA / CNCB pair; the keyword files in this folder
document both variants together.

The host streams a queue of path segments (lines and arcs) into an engine. The engine executes the segments in order, building a single path-velocity profile that respects the configured speed, acceleration and jerk, and splits the resulting path position across the member axes so they stay coordinated on the path.

![CNC motion: from the streamed segment queue through the path profiler to the member-axis references](cnc-path-pipeline.svg)
