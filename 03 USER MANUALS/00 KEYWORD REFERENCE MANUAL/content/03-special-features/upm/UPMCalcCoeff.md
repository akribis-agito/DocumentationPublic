---
keyword: UPMCalcCoeff
availability:
  standalone: []
  central-i:
  - v5
can_code: 649
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# UPMCalcCoeff

**Definition:**

UPMCalcCoeff is a command that (re)calculates the UPM repetitive compensation coefficients from the current plant model (PlantModel) and the configured filter range (UPMRptRange). It validates the plant model, derives the inverse-plant filter chain and the range-shaping (Q) filter, and stores the resulting coefficients for use by UPMRptCalc when it builds the feedforward correction. Run UPMCalcCoeff once after setting the plant model and whenever you change PlantModel or UPMRptRange, since those changes mark the coefficients as needing recalculation and do not take effect until UPMCalcCoeff is issued.

The command requires a supported plant model: an integrator-type model (for example gain over s-squared, or gain over s times (s plus a)) with a single gain term and no high-frequency pole, optionally followed by resonance, anti-resonance, or second-order low-pass terms. The model must ALSO contain exactly one delay term (the system/feedback delay) in addition to the single gain term and the integrator(s). Having zero or more than one delay term, zero or more than one gain term, the wrong number of integrator components, or any high-frequency pole makes the model unsupported. Note that the delay's value itself is not used by the UPM repetitive calculation; only the presence of exactly one delay term is required for the model to be accepted.

If the plant model is missing or unsupported, the command returns error 234 (at least one plant model entry is illegal) and the coefficients are left invalid, so a subsequent UPMRptCalc will not run (it then returns error 236, no valid plant model). A failed UPMCalcCoeff also sets a distinct "calculation failed" indication (separate from the needs-recalculation indication); this indication persists until a later successful UPMCalcCoeff clears it, and it does not block enabling the motor. The command itself replies OK or error so you can observe the outcome directly; the two indications are reflected in the axis status register (the needs-recalculation indication on bit 26, the calculation-failed indication on bit 27). On success the pending-recalculation indication is cleared. The command cannot be issued while the axis is in motion or with the motor on. It is an axis-related command and is not saved to flash.

This keyword is available from v5 (central-i).

**See also:**

[UPMRptRange](UPMRptRange.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptOn](UPMRptOn.md), [UPMRptState](UPMRptState.md)
