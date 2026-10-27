---
keyword: DOutSelect
summary: Selects the hardware function (or software control) routed to each digital output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 314
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-10-27'
doc_revision: '2026.10'
---
# DOutSelect

Selects the hardware function (or software control) routed to each digital output.

## Overview

`DOutSelect` assigns a hardware function to a digital output through a multiplexer. The array **index** is the output number (1-based: `DOutSelect[1]` is output 1). Setting it to `0` hands the output back to software control via [DOutMode](DOutMode.md). Hardware functions (events, P/D signals, UserPWM) run on the hardware layer for high-frequency signals; when a hardware function is selected, `DOutMode` and `DOutPort` are irrelevant for that output. The available functions differ by product:

| Value | Standalone | Central-i slaves |
|-------|------------|------------------|
| 0 | Software (using DOutMode) | Software (using DOutMode) |
| 1 | Encoder emulation | Reserved |
| 2 | A event #1 | Main event #1 |
| 3 | A event #2 | Main event #2 |
| 4 | A event #3 | Main event #3 |
| 5 | B event #1 | Aux. event #1 (not implemented) |
| 6 | B event #2 | Aux. event #2 (not implemented) |
| 7 | B event #3 | Aux. event #3 (not implemented) |
| 8 | C event #1 | Pulse (P/D control) |
| 9 | C event #2 | Direction (P/D control) |
| 10 | C event #3 | Main encoder raw index (capability required) |
| 11 | UserPWM 1 | Auxiliary encoder raw index (capability required) |
| 12 | UserPWM 2 | UserPWM 1 |
| 13 | Reserved | UserPWM 2 |
| 14 | Reserved | Reserved |
| 15 | Reserved | Central-i remote signal |

## How it works

`DOutSelect` programs a per-output multiplexer in hardware that chooses what feeds each physical output pin. When you write `DOutSelect`, the per-output codes — **4 bits per output** — are packed into the hardware output-routing registers (on a standalone controller) or sent to the remote unit (on central-i). Because each output gets a 4-bit selector, the value range is `0`–`15`.

- Code `0` connects the output to the **software layer** — the `DOutPort` bit (with [DOutLog](DOutLog.md) / [DOutType](DOutType.md) applied), optionally driven by a [DOutMode](DOutMode.md) function. This is the path the software updates each control cycle at the loop rate.
- Any non-zero code connects the output to a **hardware function** generated directly in hardware (position events, encoder/pulse-direction signals, UserPWM). These run at the hardware clock rate, far faster than the control loop, so the software `DOutPort`/`DOutMode` value is irrelevant for that output while a hardware function is selected.

The selector is a routing MUX only; it does not change the signal's polarity or stage — [DOutLog](DOutLog.md) and [DOutType](DOutType.md) still apply to the software path, and the [UserPWM](UserPWM.md) duty/divider still govern a PWM output.

## Examples

```text
ADOutSelect[3]=0     ; output 3 is software-controlled (uses DOutMode[3])
ADOutSelect[4]=2     ; output 4 = Main Event #1 (Central-i) / A event #1 (standalone)
```

### Edge cases

- **Index 0** — invalid; valid indices are `DOutSelect[1]`–`DOutSelect[16]`. `DOutSelect[0]` does not exist.
- **Out of range** — values outside `0`–`15` are rejected by the parameter table.
- **Non-zero `DOutSelect`** — overrides [DOutMode](DOutMode.md) and [DOutPort](DOutPort.md) for that output; the hardware function drives the pin directly at the FPGA clock rate.
- **Unimplemented function** — codes marked "not implemented" or "reserved" produce no useful output on the addressed pin.
- **Software-only path** — `DOutSelect = 0` is required for [DOutPort](DOutPort.md) bit manipulation and [DOutMode](DOutMode.md) function dispatch.
- **Save** — flash-saveable; reloaded into the routing MUX at boot.
- **Platform** — function-code-to-source mapping differs between standalone and central-i; see the table above.

## See also

- [DOutMode](DOutMode.md) — software function (when DOutSelect = 0)
- [DOutPort](DOutPort.md) — manual output state
- [UserPWM](UserPWM.md) — user PWM channels

## Central-i raw index outputs

On AGM800 and AGM800-EC, selectors 10/11 require the connected remote capability reported in `CIIdentity[27]` (FEATURES word 3), bit 13/14 respectively, with a valid coherent snapshot. Older FPGA/firmware without that advertisement must not be treated as supporting the route. Only fast differential or bidirectional differential outputs are eligible; set [BiDirConfig](../01-general-keywords/BiDirConfig.md) to output when using a bidirectional pin. Isolated outputs do not carry these routes.

The signal follows the physical incremental Z receiver, or the main SinCos/NQC Z receiver when that encoder mode is selected. AGFB incremental feedback uses its reference-mark receiver. Auxiliary routing supports its physical incremental Z receiver. Other encoder modes and absent build-time sources hold the route low. An unplugged cable follows the receiver's electrical state; this routing does not qualify encoder validity. No encoder filtering, A/B qualification, lock edge detection, PEG rearming or pulse stretching is added. Both edges pass, independently of travel direction. Selecting a different encoder mode or mux source can change the output immediately; reconfiguration is not a glitch-free switch. Output polarity uses the existing hardware convention; `DOutLog` does not invert this hardware source. Pulse-width and latency guarantees require the qualified board/image, receiver and output-driver limits; digital simulation is not a physical minimum-pulse-width specification.

Firmware rejects an unsupported source or isolated-pin assignment with range error 14 before storing a direct keyword write. Saved settings that contain index selectors wait for discovery before the output mux is restored. If discovery finishes without support, firmware logs range error 14, resets unsupported selectors to the default 0 in RAM, and rejects the restore batch without changing the hardware mux. Flash contents are unchanged until an explicit save. A subsequent explicit valid assignment applies the normalized map; valid assignments made while discovery is pending are retained and applied after discovery. Unsupported index values are never programmed as another index source. PCSuite hides unsupported choices while preserving selector numbers and validates Apply. Imports/direct clients are also checked by firmware.

Selectors 8/9 keep their pulse/direction behaviour. Encoder emulation is a separate delivery; these index selectors do not enable it.
