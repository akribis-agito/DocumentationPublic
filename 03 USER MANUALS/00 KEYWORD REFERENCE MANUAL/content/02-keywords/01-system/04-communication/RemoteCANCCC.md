---
keyword: RemoteCANCCC
summary: CAN command code (parameter identifier) for a remote write issued by RemoteCANSend.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 441
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
  - -2147483648
  - 2147483647
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# RemoteCANCCC

CAN command code (parameter identifier) for a remote write issued by RemoteCANSend.

## Overview

`RemoteCANCCC` holds the **Complex CAN Code** (CCC) that identifies *which* parameter on the remote controller a [RemoteCANSend](RemoteCANSend.md) transaction acts on. It is more than a bare CAN code: it encodes the target keyword's CAN code together with the axis it applies to and, for array keywords, the array index. Together with [RemoteCANAdd](RemoteCANAdd.md) (the node) and [RemoteCANVal](RemoteCANVal.md) (the value) it forms a complete remote access. It is saved to flash.

## How it works

When `RemoteCANSend` runs, the controller decomposes `RemoteCANCCC` into its parts — the parameter's CAN code, the addressed axis, and the array index — and packs them into the outgoing CAN frame. This is why a single integer can address any parameter on the remote node, including a specific element of an array keyword and a specific axis.

The 32-bit value is split into three fields (bit 15 is unused):

| Bits | Field | Range | Meaning |
|---|---|---|---|
| 0–9 | CAN code | 0–1023 | The CAN code of the remote keyword |
| 10–14 | Axis | 0–31 | Axis number, 0-based (axis A = 0, axis B = 1, …) |
| 16–31 | Array index | 0–65535 | 1-based element for an array keyword; 0 for a scalar keyword |

The value is therefore:

$$\texttt{RemoteCANCCC} = (\text{index} \times 65536) + (\text{axis} \times 1024) + \text{CAN code}$$

The array-index field follows the controller's own validation: an array keyword must be addressed with an index of 1 or greater (index 0 is rejected), and a scalar keyword must use index 0 (any index greater than 0 is rejected). The default is 2.

For example, to address element 3 of an array keyword on axis A (axis = 0) whose CAN code is 100:

$$(3 \times 65536) + (0 \times 1024) + 100 = 196708$$

## Examples

```text
ARemoteCANCCC=100    ; encoded identifier of the remote parameter to access
```

## See also

- [RemoteCANAdd](RemoteCANAdd.md) — target node address
- [RemoteCANVal](RemoteCANVal.md) — value written, or value returned on a read
- [RemoteCANSend](RemoteCANSend.md) — execute the remote access
