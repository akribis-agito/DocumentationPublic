---
keyword: MotorType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 50
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
  implemented: final
overrides: {}
---
# MotorType

**Definition:**

MotorType defines the type of the motor connected to the built-in/external amplifier.

This variable determines how currents and voltages are calculated and applied to the motor. It also defines how a motor will be protected against overcurrent. Selecting the wrong MotorType may result in severe damage.

The following table shows the MotorType values and their descriptions.

**Note:**

MotorType Descriptions 0 Unknown This is the default value of a new controller. No voltage outputs will be applied. 1 DC brush The motor requires only two motor output terminals and does not require commutation (physically commutated). 2 Voice coil The motor only has 1 magnet pole pair and 1 actuator coil. It requires only two motor output terminals and does not require commutation. Its operation is identical to DC brush motor. 3 Linear DC brushless The motor has 3 phases (containing 3 sets of actuator coils separated by 120 electrical degrees). It requires 3 motor output terminals. Commutation is needed to determine the current or voltage outputs through Park/inverse Park transformation. Axis will be treated in linear configuration. EncRes will be the number of encoder count per pole pair. Motor pole pair (PolePrs) will be automatically set to 1. 4 Rotary DC brushless The motor has 3 phases (containing 3 sets of actuator coils separated by 120 electrical degrees). It requires 3 motor output terminals. Commutation is needed to determine the current or voltage outputs through inverse Park transformation. Axis will be treated in rotary configuration. EncRes will be the number of encoder count per revolution. Motor pole pair (PolePrs) will define the number of pole pairs per revolution. 5 Simulation This motor type is used for simulation during development. It allows generation of simulated motion profile, input and output behaviors without a physical motor. 6 Stepper in open loop The motor used is 2-phase stepper motor, requiring 3 pins (phase A, phase B and phase A/B returns (joined)). In 1 electrical cycle (1 set of full-step excitation sequence), there are total of 4 full steps. Normally, stepper motor manufacturers specify the resolution in terms of physical angle per one full step. For Agito controller, the number of steps per electrical cycle is defined by StepBits variable. The minimum value of StepBits is 2, corresponding to 4 full steps. The number of position count (for PosRef, AbsTrgt, etc.) per electrical cycle is C o u n t s p e r e l e c t r i c a l c y c l e = 2 S t e p B i t s The physical resolution will be $$Resolution\ \left\lbrack \frac{physical\ deg}{count} \right\rbrack = \ \frac{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}{2^{StepBits}}$$ Number of counts per revolution will be $$Counts\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \bullet 2^{StepBits}}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}$$ For open-loop steeper control, no position feedback is used (Pos = 0 and PosErr = 0). User commands motion where position reference (PosRef) will be changed and used to determine the stepping currents for phase A and B. PosRef is used to track location of stepper motor. 7 Stepper in closed loop The motor used is 2-phase stepper motor, requiring 3 pins (phase A, phase B and phase A/B returns (joined)). In 1 electrical cycle (1 set of full-step excitation sequence), there are total of 4 full steps. Normally, stepper motor manufacturers specify the resolution in terms of physical angle per one full step. For Agito controller, the number of steps per electrical cycle is defined by StepBits variable. The minimum value of StepBits is 2, corresponding to 4 full steps. The number of steps per electrical cycle is S t e p s p e r e l e c t r i c a l c y c l e = 2 S t e p B i t s [ s t e p c o u n t ] The physical resolution will be $$Resolution\ \left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack = \ \frac{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}{2^{StepBits}}$$ Number of steps per revolution will be $$Steps\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \bullet 2^{StepBits}}{4 \bullet Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$ For closed-loop steeper control, encoder feedback is used, and position is defined in terms of encoder count (not step count). This means the number of pole pairs per revolution ( PolePrs ) and encoder count per revolution ( EncRes ) has to be provided. Only the position closed loop is used, as shown below. VelRef is the sum of position loop output and position derivative. VelRef will be converted from encoder count term to step count term, before integration to form stepper position reference. Finally, it goes through the stepper current loop control logic (same as open-loop stepper) before forming the required stepping currents. 8 Stepper in closed loop (brushless motor) This is a reserved option for internal use.

See the product manual to find out which terminals to use for each type of motor.
