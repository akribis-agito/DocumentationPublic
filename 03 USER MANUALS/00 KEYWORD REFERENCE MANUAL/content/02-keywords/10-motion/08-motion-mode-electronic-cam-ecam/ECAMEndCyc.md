# ECAMEndCyc

**Definition:**

ECAMEndCyc defines the GenData index where the cyclical/repeating cam pattern ends. It is an array of size 10, where each element corresponds to a cam pattern.

ECAMEndCyc must match the following order where the overall cam pattern is derived.

$$
ECAMStart \leq ECAMStartCyc < ECAMEndCyc \leq ECAMEnd
$$
