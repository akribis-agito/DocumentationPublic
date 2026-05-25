# DualStuckVel

**Definition:**

DualStuckVel is the maximum absolute velocity difference between the two feedback in dual-loop tolerable by the controller. It is in count/s where the count refers to the main (or position-loop) feedback count.

**Formula:**

$$
Absolute\ velocity\ difference = abs\left( Vel\lbrack 2\rbrack - \frac{AuxVel \bullet DualLoopFact}{65536} \right)
$$
