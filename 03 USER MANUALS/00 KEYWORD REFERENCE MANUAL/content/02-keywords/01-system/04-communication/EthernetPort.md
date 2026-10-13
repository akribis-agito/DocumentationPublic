---
keyword: EthernetPort
summary: TCP port for Ethernet communication.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 601
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 65535
  default: 50000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 65524
last_updated: '2026-10-13'
doc_revision: '2026.06'
---
# EthernetPort

TCP port for Ethernet communication.

## Overview

`EthernetPort` configures the main TCP command port. Its default is **50000**. It is saved to flash and read during start-up, so changes require [Save](../02-operation/Save.md) and [Reset](../02-operation/Reset.md).

How the value is used depends on the platform:

- **Standalone controllers and other products** retain their **0–65535** keyword range and existing listening behavior. The standalone "all-to-default" recovery DIP setting forces main port 50000 regardless of the stored value.
- **AGM800 and AGM800-EC development firmware containing [Firmware-Main #1213](https://github.com/akribis-agito/Firmware-Main/pull/1213)** accepts the keyword range **0–65524**. At start-up, a saved value in **1024–65524** selects the main command port; push/printf listens at main +10, and the optional PStat listener at main +11 when included in the firmware. Values below 1024, older saved values above 65524, or the "all-to-default" DIP setting select the effective defaults: main 50000, push 50010 and optional PStat 50011. The lower start-up bound is separate from the keyword's allowable range.
- **Earlier Central-i firmware** uses fixed main port 50000. The development behavior above does not describe the frozen 5.3.0 release or its rc3 candidate.

## Reserved port and saved-value recovery

In AGM800/AGM800-EC development firmware containing the port-policy prerequisite [Firmware-Main #1241](https://github.com/akribis-agito/Firmware-Main/issues/1241), a new assignment of **49990** is rejected because its push port would occupy reserved command port 50000. **49989** is rejected only when the optional PStat listener is included, because that listener would occupy 50000. A rejected assignment leaves the previous keyword value unchanged. Other products retain their existing policy.

If an older saved value has one of these conflicts, start-up uses effective main port **50000** and the derived default ports. It reports a port-conflict diagnostic and leaves the saved keyword and flash untouched. To replace that saved setting, assign a valid value and explicitly Save and Reset.

**Identity[52] reports the main command port actually in use.** It therefore reports 50000 after an effective-default start-up even when reading `EthernetPort` still returns the older saved value. For a valid saved port 51234, it reports 51234 and push listens at 51244.

The port-policy prerequisite creates only the main listener selected at start-up. It does not add a second command listener on reserved port 50000 when the main port is different.

In normal use this keyword is left at its default of 50000.

## Examples

```text
AEthernetPort       ; read the configured port
AEthernetPort=50000 ; set the TCP port (default), then Save and Reset
```

## See also

- [EthernetIP](EthernetIP.md) — IP address
- [EthernetMAC](EthernetMAC.md) — MAC address
