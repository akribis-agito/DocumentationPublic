# Commutation

Commutation is the process of finding electrical angle offset (for DC brushless motor with at least 3 phases). This is to ensure when driver alternates the phase currents during motion, the electrical angle is always 90 degrees offset from the magnetic angle to produce force.

Commutation process is automatically performed following power on or reset (ComtMode\[5\]=1282).

To commutate a motor correctly, the controller must have information about the electrical angle of the motor. This information can be received from Hall sensors, for example.

In the absence of Hall sensors, the electrical angle of the motor must be derived from the encoder readings, which are generally not aligned with the motor electrical angle. As a result, an initialization process is required to align the encoder reading and the motor’s electrical phase.

Below is the summary table for commutation keywords:

| No. | Variables  | Summary                         |
|-----|------------|---------------------------------|
| 1   | ComtAng    | Instantaneous commutation angle |
| 2   | ComtMode   | Array of commutation settings   |
| 3   | ComtStatus | Commutation status              |
