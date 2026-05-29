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

## Walk-through: initialize commutation with Hall + index

A typical setup for a brushless motor with Hall sensors and an encoder index is "rough then fine": start from the angle implied by the Hall state so the axis can move immediately, then refine to the exact electrical-angle zero at the next encoder index pulse. This is commutation method `3` (Hall + special-encoder switching).

1. **Select the method and when it runs.** With [ComtMode](ComtMode.md)`[19] = 0` (default) the controller runs the commutation automatically after power-on. The method is set in `[1]`:

   ```text
   AComtMode[1]=3       ; method 3: Hall + special-encoder switching (wait for index)
   AComtMode[19]=0      ; run automatically after power-on (default)
   ```

2. **Confirm the Hall mapping is sane.** Method `3` relies on [HallsValue](HallsValue.md) (the raw Hall state, expected to read `1..6`; values `0` and `7` are illegal) and on the [HallsAngle](HallsAngle.md) table that maps each legal Hall state to its electrical angle. With the motor stationary you should see `AHallsValue` in `1..6` and `AHallsAngle` configured for your motor.

3. **Enable the motor and let phasing run.** When commutation starts, [ComtStatus](ComtStatus.md)`[1]` advances through:

   | Value | Meaning |
   |---|---|
   | `1` | In progress |
   | `300` | Rough commutation done (from Halls); waiting for the index pulse |
   | `100` | Successfully finished — fine angle locked at the index |

   ```text
   AMotorOn=1               ; enable the motor; phasing begins
   AComtStatus[1]           ; 1, then 300 (rough done), then 100 (fine done)
   ```

   The axis can already produce torque while `AComtStatus[1]` is `300`, so a small motion is needed to bring the encoder index under the read head if it has not been crossed yet. When the index pulse arrives, the controller snaps the commutation angle to the index reference, sets [StatReg](../07-status-and-faults/StatReg.md) bit 0 (commutation complete), and `AComtStatus[1]` reads `100`.

4. **Verify and proceed.** Normal motion is blocked until `StatReg` bit 0 is set:

   ```text
   AComtAng                 ; the resulting electrical angle in use
   AStatReg                 ; bit 0 set = commutation complete
   ```

   If `AComtStatus[1]` reports a negative value, see the value table in [ComtStatus](ComtStatus.md) (for example `-7` for an illegal Hall sequence — usually a wiring problem).

5. **Re-trigger if needed.** To re-run commutation on demand without changing the method, write the special value `1282` into the `[5]` slot (the controller acts only with the motor off and clears the slot back to `0`):

   ```text
   AMotorOn=0
   AComtMode[5]=1282        ; re-run commutation now
   AMotorOn=1
   ```

For motors without an index pulse or where the Hall transitions are well-trusted, use method `4` (wait for the next Hall transition instead of the index) — the rough-done value is `400`. For motors without Hall sensors, the search-based methods (`0`, `5`) apply a small command and observe the response; for absolute encoders use method `2` (no motion required, reads a previously stored zero from `ComtMode[4]`). Hall-only continuous commutation is method `6`, optionally filtered by [HallOnlyFilt](HallOnlyFilt.md).
