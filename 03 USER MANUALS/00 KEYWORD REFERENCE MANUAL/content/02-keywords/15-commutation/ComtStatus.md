---
keyword: ComtStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 143
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtStatus

**Definition:**

ComtStatus reports the actual commutation status.

| Index | Descriptions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Phasing status **Default:** 0 Value Commutation status 0 Required and not executed yet. 1 Commutation in progress. 100 Successfully finished. 200 Commutation is not required (e.g. DC, voice coil or stepper motors). 300 Rough commutation is done, waiting for index pulse for fine commutation adjustment. 400 Rough commutation is done. Waiting for Hall sequence change for fine commutation adjustment. 500 Learn process changed parameters (recommended to save to flash). 600 Burn-in mode is activated. -1 Unexpected motor off. Motor off occurred during commutation. -2 Illegal commutation method selected. -3 “Jump to zero” commutation failed. Please check motor, encoder and commutation parameters (such as voltage and accuracy). -4 Encoder error is detected. Commutation is required. -5 Parameter is modified. Commutation is required. -6 Amplifier power cycle is required. -7 Illegal halls sequence detected. -8 Central-I failure during commutation process. -9, -10, -11, -12 Illegal halls sequence is detected during learn process. | Value | Commutation status | 0 | Required and not executed yet. | 1 | Commutation in progress. | 100 | Successfully finished. | 200 | Commutation is not required (e.g. DC, voice coil or stepper motors). | 300 | Rough commutation is done, waiting for index pulse for fine commutation adjustment. | 400 | Rough commutation is done. Waiting for Hall sequence change for fine commutation adjustment. | 500 | Learn process changed parameters (recommended to save to flash). | 600 | Burn-in mode is activated. | -1 | Unexpected motor off. Motor off occurred during commutation. | -2 | Illegal commutation method selected. | -3 | “Jump to zero” commutation failed. Please check motor, encoder and commutation parameters (such as voltage and accuracy). | -4 | Encoder error is detected. Commutation is required. | -5 | Parameter is modified. Commutation is required. | -6 | Amplifier power cycle is required. | -7 | Illegal halls sequence detected. | -8 | Central-I failure during commutation process. | -9, -10, -11, -12 | Illegal halls sequence is detected during learn process. |
| Value | Commutation status |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Required and not executed yet. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Commutation in progress. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | Successfully finished. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 200 | Commutation is not required (e.g. DC, voice coil or stepper motors). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 300 | Rough commutation is done, waiting for index pulse for fine commutation adjustment. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 400 | Rough commutation is done. Waiting for Hall sequence change for fine commutation adjustment. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 500 | Learn process changed parameters (recommended to save to flash). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 600 | Burn-in mode is activated. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | Unexpected motor off. Motor off occurred during commutation. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -2 | Illegal commutation method selected. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -3 | “Jump to zero” commutation failed. Please check motor, encoder and commutation parameters (such as voltage and accuracy). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -4 | Encoder error is detected. Commutation is required. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -5 | Parameter is modified. Commutation is required. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -6 | Amplifier power cycle is required. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -7 | Illegal halls sequence detected. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -8 | Central-I failure during commutation process. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -9, -10, -11, -12 | Illegal halls sequence is detected during learn process. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
</td>
</tr>
<tr>
<td>2</td>
<td><p>Number of successful consecutive steps</p>
<p><strong>Default:</strong> 0</p>
<p><strong>Condition:</strong> Only for when ComtMode[1]=1 (“jump to zero” commutation mode)</p></td>
</tr>
<tr>
<td>3</td>
<td></td>
</tr>
</tbody>
</table>
