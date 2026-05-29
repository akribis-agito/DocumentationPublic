---
keyword: DInMode
summary: Assigns a software function to each digital input, with per-axis targeting.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 225
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# DInMode

Assigns a software function to each digital input, with per-axis targeting.

## Overview

`DInMode` assigns a software function to a digital input. The array **index** selects the input (1-based: `DInMode[1]` is input 1, `DInMode[2]` is input 2, …).

## How it works

- The **lower 16 bits** of the value select the function (a numeric functionality code — see the table below).
- **Bits 16–27** select which axes the function applies to; each bit is one axis (A–L), and multiple bits may be set.

| Axis | A | B | C | D | E | F | G | H | I | J | K | L |
|------|---|---|---|---|---|---|---|---|---|---|---|---|
| Value, Bit# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |

**Example:** `CDInMode[2] = 131081` (binary `…0010 0000 0000 0000 1001`):
- Index → 2 (digital input 2)
- Lower 16 bits → 9 (reverse limit switch)
- Bit 17 set → axis B

…so digital input 2 (of axis C) acts as the reverse-limit-switch input for axis B. (To target axis A instead, set bit 16 — value `65545` — or leave the upper 16 bits at 0; both forms select axis A.)

### Dispatch mechanism

When `DInMode[]` is written, an internal table of active functionalities is built — each entry holds the function code, the input bit mask, and the target axis. Each control cycle this table is walked, comparing the current input word against the previous one ([DInPort](DInPort-DInPortHigh.md)) to detect **rising** and **falling** edges, then running the function's action. Inputs used for these functions are sampled in groups once every 16 interrupts.

![DInMode dispatch: edge-detected DInPort drives the active functions table, which fans out to per-function actions](dinmode-dispatch.svg)

### Functionality codes

The lower 16 bits select one of the following functions. The "Edge / level" and "Action" columns summarize what the dispatch does.

| Code | Name | Edge / level | Action |
|------|------|--------------|--------|
| 0 | User input (general purpose) | — | No function; the input is read only via [DInPort](DInPort-DInPortHigh.md). May be assigned to multiple inputs. |
| 1 | Dedicated HW function | — | Routed to dedicated hardware; no software action in the dispatch. |
| 2 | Motor-on input | rising / falling | Rising edge (when off and no fault) requests servo-on; falling edge disables the motor and sets [MotorReason](../../07-status-and-faults/MotorReason.md) = I/O. See [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md). |
| 3 | Begin motion | rising | Releases a move armed with [BeginDInOn](../../10-motion/04-motion-command/BeginDInOn.md): sets a per-axis flag the profiler uses to start the move. |
| 4 | Stop motion | rising | Issues a controlled [Stop](../../10-motion/04-motion-command/Stop.md) on the axis (and along the CNC / vector path if it is a member). |
| 5 | Clear input pulses | rising / falling | With servo on: rising edge aborts the current move; falling edge re-begins motion from the present reference. |
| 6 | Abort-resume motion | — | Reserved — defined but not implemented in firmware. |
| 7 | Alarm reset | level + falling | Held on for ≥20 ms then released clears the fault ([ConFlt](../../07-status-and-faults/ConFlt.md) → none). |
| 8 | Abort motion | level (on) | Aborts motion immediately ([Abort](../../10-motion/04-motion-command/Abort.md)); for CNC/vector members aborts the whole group. |
| 9 | Reverse limit switch (RLS) | level | Sets/clears the RLS bit in [LimitsStat](../../06-protections/03-motion/position-limit-protection/LimitsStat.md) and [StatReg](../../07-status-and-faults/StatReg.md) bit 17; the limit handler decelerates the axis. |
| 10 | Forward limit switch (FLS) | level | Sets/clears the FLS bit in [LimitsStat](../../06-protections/03-motion/position-limit-protection/LimitsStat.md) and [StatReg](../../07-status-and-faults/StatReg.md) bit 18; the limit handler decelerates the axis. |
| 11 | Torque limit on | level | Enables/disables the current (torque) limit (gates `CurrLimMode`). |
| 12 | Activate dynamic brake | level | Turns the dynamic brake on/off. |
| 13 | Lock static brake | level | Locks/releases the static brake (only when brake mode is "automatic by discrete input"). See [Static brake](../../06-protections/06-brake/Staticbrake.md). |
| 14 | Control-set change | level | Selects the active gain set when schedule mode is manual/DInPort. |
| 15 | Add filter | level | Enables/disables the second velocity bi-quad filter. |
| 16 | Mode switch VEL ↔ POS | level (motor off) | While the motor is off, selects velocity vs position [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md). |
| 17 | Mode switch VEL ↔ CUR | level (motor off) | While the motor is off, selects velocity vs current mode. |
| 18 | Mode switch POS ↔ CUR | rising / falling | Rising edge switches to position **only if currently in current mode**; falling edge switches to current **only if currently in position mode and the axis is not a CNC or vector member**. Has no effect from velocity or force mode. |
| 19 | Clear absolute encoder | — | Defined; no action in the dispatch (empty case). |
| 20 | Change speed | rising | Applies the queued new speed (`SpeedChgNew` → `Speed`). |
| 21 | Home | level | Sets/clears the home state and [StatReg](../../07-status-and-faults/StatReg.md) home bit; toggling raises a home-change pulse. |
| 22 | Mode switch POS ↔ FORCE | rising / falling | Rising edge switches to position **only if currently in force mode**; falling edge switches to force **only if currently in position mode and the axis is not a CNC or vector member**. Has no effect from velocity or current mode. |
| 23 | Hall A | — | Marks this input as Hall A (Hall B/C assumed on the next inputs); HW routing, no dispatch action. |
| 24 | Fault input | level (on) | While on and the motor is on (and not a simulated motor), disables the motor with fault [ConFlt](../../07-status-and-faults/ConFlt.md) = 1050 (external fault input activated). Ignored on simulation motors. |
| 25 | Homing on input | rising | Triggers `HomingOn = 1` to start a homing sequence. |
| 26 | Fault input — controlled stop | level (on) | While on, performs a controlled stop and disables the motor at the end. |

## Notes

1. After changing `DInMode[]`, [Save](../../01-system/02-operation/Save.md) and [Reset](../../01-system/02-operation/Reset.md) — some special functions only start (or stop) working after a power cycle.
2. At most **20** special functions may be assigned across the digital inputs; beyond that, only the first 20 are operational. A function applied to two axes counts as two.
3. Functions are evaluated in ascending index order; a duplicate functionality on a later input is ignored (except general-purpose input). No error is raised, but PCSuite shows a warning.

## Examples

### Walk-through: wire and use a home switch on digital input 3

Configure DI 3 as the home-state input for axis A: pick the port, assign the function, set fail-safe polarity, and add debounce. After the wiring is in place, the input's level drives the home bit and `Pos`-based homing logic.

```text
AMotorOn=0                ; configure with the motor off
ADInMode[3]=21            ; function 21 = home (level); applies to this axis (upper bits 0 = axis A)
ADInLog=4                 ; bit 2 set — invert DI 3 so a disconnected switch (low) is treated as "not home"
ADInFilt=3                ; 3-sample hardware debounce (raise if the switch is electrically noisy)
ASave                     ; persist (DInMode and DInLog are flash-saveable; DInFilt too)
AReset                    ; some DInMode functions only attach on power-up — restart the controller
                          ; ... then verify ...
ADInPort                  ; read the live input word; bit 2 reflects DI 3 after filter and inversion
AStatReg                  ; the home bit in StatReg tracks the input level
```

Use the same pattern for limit switches (function 9 = RLS, 10 = FLS) — these feed [LimitsStat](../../06-protections/03-motion/position-limit-protection/LimitsStat.md), and when the axis is moving into an active limit the limit handler decelerates it.

### Walk-through: drive a motion start from a digital input

Pair `DInMode = 3` (begin motion) with [BeginDInOn](../../10-motion/04-motion-command/BeginDInOn.md) so a button press launches an armed move.

```text
ADInMode[4]=3             ; DI 4 = begin motion (rising edge)
ABeginDInOn=1             ; arm: the next rising edge of DI 4 releases the queued move
                          ; ... rising edge on DI 4 ...
AMotionStat               ; motion has started — non-zero
```

### Edge cases

- **Motor off** — input-driven mode switches in codes 16 (VEL↔POS) and 17 (VEL↔CUR) **only act while the motor is off**; an edge while the motor is on is silently ignored. Codes 18 (POS↔CUR) and 22 (POS↔FORCE) act on edge regardless of motor state but only if the axis is already in one of the two participating modes.
- **CNC / vector member** — codes 18 and 22 will not fall through to current or force while the axis is a member of a CNC or vector group; the dispatch silently skips the transition.
- **Simulation motor** — code 24 (fault input) is ignored on simulated motors; the motor stays on even with the fault input asserted.
- **Out-of-range function code** — values not listed in the table are ignored at dispatch (no error, no action).
- **More than 20 active functions** — only the first 20 dispatch entries are operational; later assignments are silently inactive at dispatch time.
- **Duplicate function on another input** — only the lower-index input is acted on; the later duplicate is dropped (except function 0 = general-purpose). PCSuite issues a configuration warning.
- **Save / Reset** — some codes only attach (or release) on power-up; after editing `DInMode` you must [Save](../../01-system/02-operation/Save.md) and [Reset](../../01-system/02-operation/Reset.md).
- **Platform** — code 27 (Heidenhain limits) is central-i v5 only; codes 0–26 are common to all platforms.

## Changes between versions

Central-i v5 adds one functionality code: **27 — Heidenhain limits**. It is not present in v4 / standalone (where the highest code is 26). All codes 0–26 above are unchanged.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — input states this dispatch reads
- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — logic inversion applied before the state is read
- [BeginDInOn](../../10-motion/04-motion-command/BeginDInOn.md) — per-axis enable for the begin-motion function (code 3)
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — enabled/disabled by the motor-on (code 2) and fault (codes 24/26) functions
- [LimitsStat](../../06-protections/03-motion/position-limit-protection/LimitsStat.md) — RLS/FLS bits driven by codes 9/10
