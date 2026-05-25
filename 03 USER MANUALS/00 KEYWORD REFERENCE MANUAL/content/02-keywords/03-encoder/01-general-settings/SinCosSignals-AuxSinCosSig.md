# SinCosSignals/AuxSinCosSig

**Condition:**

SinCosSignals is only used when EncType=4 (SIN/COS encoder).

**Definition:**

SinCosSignals is a read-only parameter array that displays the status of the SIN/COS signals interpolation. Depending on the product, each array element represents different statuses.

The descriptions below are for all Agito products with SIN/COS encoder support, except for AGFB01. SinCosSignals is operational only when analog test mode state is entered (SinCosSetup\[20\] = 1).

| Index | Descriptions |
|----|----|
| 1 | Raw SIN+ signal reading, in millivolt (mV) |
| 2 | Raw SIN- signal reading, in millivolt (mV) |
| 3 | Difference between raw SIN+ and SIN- readings, in millivolt \[mV\]. This equals to SinCosSignals\[1\] – SinCosSignals\[2\] |
| 4 | Raw COS+ signal reading, in millivolt (mV) |
| 5 | Raw COS- signal reading, in millivolt (mV) |
| 6 | Difference between raw COS+ and COS- readings, in millivolt \[mV\]. This equals to SinCosSignals\[4\] – SinCosSignals\[5\] |

The descriptions below are for AGFB01.

| Index | Descriptions |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 1 | **Quadrant alignment status** **Default:** 0 The quadrant inferred from comparator is checked against the quadrant inferred from atan2 operation of raw SIN/COS signals. Value State 0 Ok -1 Fail (invalid quadrant difference) | Value | State | 0 | Ok | -1 | Fail (invalid quadrant difference) |
| Value | State |  |  |  |  |  |  |
| 0 | Ok |  |  |  |  |  |  |
| -1 | Fail (invalid quadrant difference) |  |  |  |  |  |  |
</td>
</tr>
<tr>
<td>2</td>
<td><p><strong>Raw quadrant counter from digital path of SIN/COS signals</strong></p>
<p><strong>Default:</strong> 0</p>
<p>SIN/COS signals are passed through comparators to form digital A/B signals. An internal counter will count the number of quadrants passed, while respecting the direction.</p>
<p>For example, if quadrant passes from 2 to 3, counter will increment. If quadrant passes from 2 to 1, counter will decrement.</p></td>
</tr>
<tr>
<td>3</td>
<td><p><strong>Raw sine signal reading</strong></p>
<p><strong>Default:</strong> 0</p>
<p>This value is raw sine reading in terms of microvolt (µV), after amplitude and phase offsets as defined by SinCosSignals.</p></td>
</tr>
<tr>
<td>4</td>
<td><p><strong>Quadrant code determined from the comparators (digital path)</strong></p>
<p><strong>Default:</strong> 0</p>
<p>The quadrant is determined from the digital path of the SIN/COS encoder where SIN/COS signals are passed through comparators (compared to 0) to form digital A/B signals.</p>
<p>SinCosSignals[4] represents the quadrant in code value (not quadrant number), as follows.</p>
| Quadrant code | Quadrant | Comparator A value (for SIN) | Comparator B value (for COS) | Angle [degrees] |
|---|---|---|---|---|
| 3 | First | 1 (SIN > 0) | 1 (COS > 0) | [0, 90) |
| 2 | Second | 1 (SIN > 0) | 0 (COS ≤ 0) | [90, 180) |
| 1 | Third | 0 (SIN ≤ 0) | 0 (COS ≤ 0) | [180, 270) |
| 0 | Fourth | 0 (SIN ≤ 0) | 1 (COS > 0) | [270, 360) |
</td>
</tr>
<tr>
<td>5</td>
<td><p><strong>Quadrant code determined from the SIN/COS values (analog path)</strong></p>
<p><strong>Default:</strong> 0</p>
<p>The quadrant is determined from the analog path of the SIN/COS encoder where the angle is determined by the atan2 formula.</p>
<p>SinCosSignals[5] represents the quadrant in code value (not quadrant number), as follows.</p>
| Quadrant code | Quadrant | SIN sign | COS sign | Angle [degrees] |
|---|---|---|---|---|
| 3 | First | + | + | [0, 90) |
| 2 | Second | + | - | [90, 180) |
| 1 | Third | - | - | [180, 270) |
| 0 | Fourth | - | + | [270, 360) |
</td>
</tr>
<tr>
<td>6</td>
<td><p><strong>Raw cosine signal reading</strong></p>
<p><strong>Default:</strong> 0</p>
<p>This value is raw cosine reading in terms of microvolt (µV), after amplitude and phase offsets as defined by SinCosSignals.</p></td>
</tr>
</tbody>
</table>
