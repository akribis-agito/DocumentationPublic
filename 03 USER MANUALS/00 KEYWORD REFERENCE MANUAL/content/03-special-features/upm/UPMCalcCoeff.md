# UPMCalcCoeff

**Definition:**

UPMCalcCoeff is a command that (re)calculates the UPM repetitive compensation coefficients from the current plant model (PlantModel) and the configured filter range (UPMRptRange). It validates the plant model, derives the inverse-plant filter chain and the range-shaping (Q) filter, and stores the resulting coefficients for use by UPMRptCalc when it builds the feedforward correction. Run UPMCalcCoeff once after setting the plant model and whenever you change PlantModel or UPMRptRange, since those changes mark the coefficients as needing recalculation and do not take effect until UPMCalcCoeff is issued.

The command requires a supported plant model: an integrator-type model (for example gain over s-squared, or gain over s times (s plus a)) with a single gain term and no high-frequency pole, optionally followed by resonance, anti-resonance, or second-order low-pass terms. If the plant model is missing or unsupported, the command returns an error and the coefficients are left invalid, so a subsequent UPMRptCalc will not run. On success the pending-recalculation indication is cleared. The command cannot be issued while the axis is in motion or with the motor on. It is an axis-related command and is not saved to flash.

This keyword is available from v5 (central-i).

**See also:**

[UPMRptRange](UPMRptRange.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptOn](UPMRptOn.md), [UPMRptState](UPMRptState.md)
