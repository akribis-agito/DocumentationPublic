# Status and Faults

Keywords that report the live status of an axis and record why and how it faulted. Every controller cycle the axis status is published as a bitfield in [StatReg](StatReg.md). When a disabling fault is detected, the controller acts in one atomic step: it turns the motor off and records the reason in [MotorReason](MotorReason.md), stores the fault code in [ConFlt](ConFlt.md), freezes a diagnostic snapshot in [ConFltSnapVal](ConFltSnapVal.md), and appends the event with its time to the controller log [ErrLog](ErrLog.md).

![The status and fault model: StatReg reports per-cycle status bits, and a disabling fault atomically turns the motor off (MotorReason), sets the fault code (ConFlt), freezes a snapshot (ConFltSnapVal) and appends an entry to ErrLog](status-fault-model.svg)

The category contains:

- **Live status** — [StatReg](StatReg.md), the 32-bit per-axis status word (warnings, limits, saturations, brake, homing and stall).
- **Fault code** — [ConFlt](ConFlt.md), the code that disabled the axis (`0` = no fault; codes are numbered from `1001`). See [Controller error codes](../../04-error-codes/controller-error-codes.md) for the full list.
- **Disable reason** — [MotorReason](MotorReason.md), distinguishing a fault from a deliberate disable command.
- **Fault snapshot** — [ConFltSnapSrc](ConFltSnapSrc.md) selects which parameters are captured, and [ConFltSnapVal](ConFltSnapVal.md) holds the values frozen at the moment of the fault.
- **Error log** — [ErrLog](ErrLog.md), the unit-wide circular log of recent errors and their times, cleared with [ClearErr](ClearErr.md).

`ConFlt` and `MotorReason` reflect the current fault state and are cleared when the axis is re-enabled; the snapshot and the log persist for later diagnosis.

## Walk-through: diagnose a fault occurrence

When an axis trips, four pieces of state are written in one atomic step: [MotorOn](../08-axis-operation/01-general-keywords/MotorOn.md) is forced off, [ConFlt](ConFlt.md) gets the fault code, [ConFltSnapVal](ConFltSnapVal.md) freezes a snapshot of selected parameters, and the event is appended to [ErrLog](ErrLog.md) with a timestamp. The standard diagnostic sequence reads them in that order.

1. **Configure the snapshot once, ahead of time.** Slots `[1]..[4]` of [ConFltSnapSrc](ConFltSnapSrc.md) name up to four parameters to capture (as [complex CAN codes](../../01-keyword-usage-and-syntax/complex-can-code.md)); slots `[5]..[14]` of [ConFltSnapVal](ConFltSnapVal.md) are fixed system parameters that are always captured automatically. Writing `ConFltSnapSrc` also clears the existing snapshot — reconfigure *before* the fault you want to diagnose, not after:

   ```text
   AConFltSnapSrc[1]=33                  ; capture StatReg (CAN code 33) into ConFltSnapVal[1]
   AConFltSnapSrc[2]=<complex code of AVel[1]>
   AConFltSnapSrc[3]=<complex code of ACurrent>
   AConFltSnapSrc[4]=0                   ; disable slot 4
   ```

2. **After a fault occurs, read the fault code.** [ConFlt](ConFlt.md) is `0` when no fault is present and a positive code (numbered from `1001`) when the axis was disabled by the controller. [MotorReason](MotorReason.md) reads `1` for a controller-fault disable, distinguishing it from a deliberate `MotorOn=0` command (`3` from a user program, `4` from communication) or a digital-input disable (`2`):

   ```text
   AConFlt                ; fault code (e.g. 1020 = position-error limit)
   AMotorReason           ; 1 = controller fault, 2 = DI, 3 = user program, 4 = comm
   ```

   See [Controller error codes](../../04-error-codes/controller-error-codes.md) for the meaning of each code.

3. **Inspect the snapshot.** The capture is frozen at the fault instant, so it reflects what the system *was* doing rather than what it is doing now. The fixed slots cover the most useful baseline (status word, position, velocity, current, the fault code itself in `[10]`, and the capture time in `[14]`); your user-selected parameters fill `[1]..[4]`:

   ```text
   AConFltSnapVal[5]      ; StatReg at fault — saturations, limits, brake state
   AConFltSnapVal[7]      ; Position
   AConFltSnapVal[8]      ; Velocity
   AConFltSnapVal[10]     ; same fault code as ConFlt
   AConFltSnapVal[14]     ; time of capture, in seconds since power-on
   AConFltSnapVal[1]      ; first user-selected parameter (here: StatReg, again)
   ```

4. **Reconstruct the timeline from [ErrLog](ErrLog.md).** The log is a 32-event ring of `(tagged code, time)` pairs (64 elements). The lower 24 bits of the code element are the error number; the upper 8 bits identify the source (`0` = non-axis, `1..8` = axis A..H, `16 + n` = user-program thread `n`). The companion element is the timestamp in seconds since power-on:

   ```text
   AErrLog[1]             ; tagged code of the first logged error
   AErrLog[2]             ; its timestamp
   AErrLog[3]             ; tagged code of the second logged error
   AErrLog[4]             ; its timestamp ...
   ```

   Decoding: `code = AErrLog[1] & 0xFFFFFF`, `source = (AErrLog[1] >> 24) & 0xFF`.

5. **Clear and re-enable.** Re-enabling the axis auto-clears `ConFlt` and resets `MotorReason`. Writing `0` to `ConFlt` clears the live fault state but does **not** wipe the snapshot or the log — those persist for later inspection. To wipe the log explicitly, use [ClearErr](ClearErr.md):

   ```text
   AConFlt=0              ; clear the live fault status (snapshot + log are untouched)
   AMotorOn=1             ; re-enable; ConFlt and MotorReason also auto-clear on enable
   AClearErr              ; wipe the unit-wide error log when you no longer need it
   ```

Live status (independent of faults) is reported every cycle by the 32-bit [StatReg](StatReg.md) — saturations, limits, warning levels, brake state and homing complete. The 2-bit severity fields (bus voltage, current, temperature, saturation, motor temperature) line up with the PCSuite status LEDs.
