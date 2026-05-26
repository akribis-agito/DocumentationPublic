---
keyword: AmpType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 226
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# AmpType

%%TO REVIEW FOR AMPTYPE = 8%%

**Definition:**

AmpType defines the amplifier mode in use by the axis. Depending on Agito product, an axis can use its internal PWM amplifier, or interface with external amplifier via analog/digital command. Please contact Agito for more information on amplifier functionality of each product.

The table below shows the AmpType value and its corresponding amplifier mode.

| AmpType | Descriptions |
|----|----|
| 0 | Built-in PWM amplifier |
| 1 | Reserved |
| 2 | External amplifier – analog current reference (CurrRef) command |
| 3 | External amplifier - digital command for pulse-direction (PD) mode |
| 4 | Reserved (built-in linear amplifier) |
| 5 | External amplifier - analog velocity reference (VelRef) command |
| 6 | External amplifier - digital command for pulse-direction (PD) mode with position feedback |
| 7 | External amplifier – analog phase current reference (IaRef/IbRef) command |
| 8 | External amplifier - digital SPI phase current reference (IaRef/IbRef) command |
