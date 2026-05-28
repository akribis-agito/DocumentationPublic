# Commutation

Commutation is the process of finding the electrical-angle offset of a DC brushless motor (with at least 3 phases). It ensures that, as the controller alternates the phase currents during motion, the applied current vector stays 90 electrical degrees from the magnetic field so that force/torque is produced efficiently.

![Establishing the electrical angle: ComtMode selects the method (search, Hall, absolute encoder or minimal-jumps search); when commutation completes ComtStatus reads 100 and StatReg bit 0 is set, which allows normal motion; ComtAng reports the angle in effect](commutation-overview.svg)

To commutate correctly the controller must know the motor electrical angle. This can come directly from Hall sensors, from a previously stored absolute-encoder reference, or be found by a search that applies a small command and observes the response. In the absence of Hall sensors the angle must be derived from the encoder, which is generally not aligned with the motor electrical phase, so an initialization (phasing) process is needed to align the two.

When commutation runs is configured by [ComtMode](ComtMode.md) (after power-on, on motor-on, both, or manual only); the process can also be re-triggered on request. Until commutation completes, the commutation-complete bit of [StatReg](../07-status-and-faults/StatReg.md) (bit 0) stays cleared and normal motion is blocked.

The category contains:

| No. | Keyword | Summary |
|-----|---------|---------|
| 1 | [ComtAng](ComtAng.md) | Instantaneous commutation (electrical) angle |
| 2 | [ComtMode](ComtMode.md) | Array of commutation settings (method and mode) |
| 3 | [ComtStatus](ComtStatus.md) | Commutation process status |
| 4 | [HallsValue](HallsValue.md) | Raw Hall-sensor state |
| 5 | [HallsAngle](HallsAngle.md) | Electrical angle mapped to each Hall state |
| 6 | [HallsAngleSw](HallsAngleSw.md) | How the HallsAngle entries are interpreted (central-i v5) |
| 7 | [HallOnlyFilt](HallOnlyFilt.md) | Filter for the Hall-only commutation angle |
