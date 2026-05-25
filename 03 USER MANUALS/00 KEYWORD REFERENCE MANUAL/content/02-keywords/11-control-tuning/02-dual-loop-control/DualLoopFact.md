# DualLoopFact

**Definition:**

DualEncFact is used to scale the position loop output and true velocity reference, from position/load unit to velocity/motor unit, so that all inputs to the velocity loop are of the same unit.

The scaling factor in use, k will be

$$
k = \frac{65536}{DualLoopFact}
$$

$k$ is defined as follows.

$$
k = \frac{Motor\ feedback\ count\ per\ physical\ unit}{Load\ feedback\ count\ per\ physical\ unit} = \frac{Load\ feedback\ physical\ unit\ per\ count\ }{Motor\ feedback\ physical\ unit\ per\ count\ }
$$

DualLoopFact is therefore

$$
DualLoopFact = \frac{65536\  \bullet Motor\ feedback\ physical\ unit\ per\ count\ }{Load\ feedback\ physical\ unit\ per\ count\ }
$$

**Example:**

The motor feedback uses 4µm SINCOS encoder at 4096x interpolation factor (0.97656nm per count).

The load feedback uses 200nm SINCOS encoder at 8192x interpolation factor (24.41pm per count).

Then,

$$
DualLoopFact = \frac{65536\  \bullet 0.97656\ }{24.41*0.001\ } = 2621440
$$
