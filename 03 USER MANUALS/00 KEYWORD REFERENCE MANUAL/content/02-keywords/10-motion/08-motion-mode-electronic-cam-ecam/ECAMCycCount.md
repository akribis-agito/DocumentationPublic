# ECAMCycCount

**Definition:**

ECAMCycCount tracks the index of the cam pattern repetition cycle. It is an array of size 10, where each element corresponds to a cam pattern.

Its value always starts with 1 upon beginning of ECAM motion, and will increment/decrement according to the value of master variable and the sign of ECAMGap.

Please refer to the figures in [Motion mode – Electronic cam (ECAM)](../../../02-keywords/10-motion/08-motion-mode-electronic-cam-ecam/00-overview.md) for more information.
