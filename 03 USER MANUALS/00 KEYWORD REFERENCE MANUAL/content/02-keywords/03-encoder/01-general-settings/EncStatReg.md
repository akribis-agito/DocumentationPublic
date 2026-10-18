---
keyword: EncStatReg
summary: Read-only status register reporting absolute-encoder health bits (disconnect, error, warning, CRC).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 422
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-18'
doc_revision: '2026.10'
---
# EncStatReg

Read-only, per-axis encoder status. Read it in PCSuite with `AEncStatReg` (axis A). The layout and available information depend on the controller, FPGA image and feedback type. It is not a universal feedback-validity register.

## Central-i main feedback

For main BiSS-C, EnDat and Tamagawa feedback, the CI_MASTER firmware synthesizes status from the received remote inputs. Firmware containing the [status-reporting repair](https://github.com/akribis-agito/Firmware-Main/issues/1273) refreshes these existing mapped bits whenever the main absolute-encoder handler runs, after its initialization window. Firmware containing the [Tamagawa startup repair](https://github.com/akribis-agito/Firmware-Main/issues/1452) also publishes these same mapped bits during active standard AMP main-Tamagawa settling:

| Bit | Mask | Received input |
|---|---|---|
| 0 | `0x01` | Remote main-encoder protection indication. Its physical meaning depends on protocol and hardware. |
| 1 | `0x02` | Either existing error or warning input in the remote status word; the inputs are combined. |
| 4 | `0x10` | Existing CRC input in the remote status word. |

Each mapped bit reflects its own current input, including simultaneous conditions. Recovered conditions clear, including CRC; other register bits are preserved. Reporting is independent of [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md). The repair changes reporting only: it retains the existing counter, motor-off, commutation and extrapolation policy.

These names describe the firmware mapping, not equivalent physical evidence across protocols. In the CIG1 completed-main Tamagawa path, the shared field carries CRC, protocol error and unavailable. Unavailable combines several causes, including no new completion since the most recent gather; it is not a cable-disconnect verdict. BiSS-C and EnDat do not use this same completed-main publication, and that shared field can instead carry inverse-period status. The main-encoder protection signal is also protocol-dependent: for example, the CIG1 EnDat path combines CRC and encoder error into it. Do not interpret every bit-0 indication as a physically disconnected cable or every clear register as healthy, fresh feedback.

## Standalone controllers

The local main BiSS-C, EnDat and Tamagawa branch reads the FPGA status register at offset `0x005c`, retaining its low five bits. Protocol-specific packing matters. In the consolidated FPGA packages, BiSS-C packs disconnected/amplitude/frequency/system/CRC at bits 0/1/2/3/4; EnDat packs encoder-error/unsupported-mode/Error1/Error2/CRC at bits 0/1/2/3/4. Check the image's contract before interpreting another protocol or variant.

The standalone handler uses the status itself for its fault policy and can clear bits 0/1 in the bypass/no-error branch. The CI_MASTER reporting repair does not change that behavior. Do not assume identical clearing semantics across standalone and Central-i controllers. SIN/COS has separate amplitude-status handling using this register; its bits are not serial-reply status. This register does not establish equivalent auxiliary-encoder monitoring or SSI/Nikon support.

## Reporting versus fault response

Firmware containing the [accepted-quality repair](https://github.com/akribis-agito/Firmware-Main/issues/1408) preserves this current-input diagnostic mapping. For active standard AMP main BiSS-C, EnDat and Tamagawa feedback on AGM800/EC, encoder-error policy instead uses quality accepted with the main position under CRC1. After a rejected or skipped decode, diagnostics can differ from that retained policy evidence: a rejected bad frame can set diagnostic bits without spoiling accepted good quality, and a rejected clean frame can clear diagnostic bits without clearing accepted bad quality. This does not change lock/event status ownership or qualify startup, physical freshness or full encoder alarms.

`EncAbsErrTime=-1` bypasses the existing CRC/error counting, extrapolation and timeout fault response. Independent main-encoder protection handling remains active. With handling enabled, CRC and generic-error conditions use separate counters and can produce [ConFlt](../../07-status-and-faults/ConFlt.md) 1069 and 1068; the existing protection path uses 1070. A reported condition and a recorded fault are different observations. Consult the fault log for recorded fault history.

This status does not provide a physical acquisition timestamp, a common freshness guarantee, measured/held/predicted position selection, or detailed Tamagawa SF/ALMC alarms. A clear register does not itself qualify a position sample. The Tamagawa startup repair uses separate new-acceptance/quality eligibility and reports diagnostics during settling without advancing the existing fault schedule; other feedback paths retain their initialization window. Capture at control-cycle resolution to investigate short transients: host polling can miss a condition that has recovered.

## See also

- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — existing error-handling timeout and bypass
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — absolute-position initialization offset
- [EncType](EncType-AuxEncType.md) — feedback selection
- [StatReg](../../07-status-and-faults/StatReg.md) — general axis status
- [ConFlt](../../07-status-and-faults/ConFlt.md) — reported fault code
