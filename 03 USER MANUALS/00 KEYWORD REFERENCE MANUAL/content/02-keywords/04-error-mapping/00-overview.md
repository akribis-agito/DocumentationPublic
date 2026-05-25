# Error mapping

Agito supports 1D, 2D and 3D error mapping. The error mapping works by correcting the feedback (Pos), and not the command (PosRef).

PosBeforeMap is the position value from the encoder **before** error mapping correction, while Pos is the position value **after** error mapping correction.

![error-mapping-sum.drawio.svg](../../02-keywords/04-error-mapping/error-mapping-sum.drawio.svg)

MapType selects the error mapping dimension 1D, 2D, or 3D.

MapEncoder\[\] selects which axis’s encoder is used for the mapping.

MapStartPos\[\], MapPosGap\[\], MapLength\[\] define the coordinates of the error mapping points.

MapTable\[\] stores the error values. MapTableB\[\], MapTableC\[\] MapTableD\[\], MapTableE\[\] extends the array size. I.e. MapTableB\[1\] comes after MapTable\[65536\].

| MapTable Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|----|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| X Enc |  |  |  |  |  | a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Y Enc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Z Enc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Template

The complex CAN code bits are divided into the following bit fields:

| Complex code bit fields | Descriptions                                    |
|-------------------------|-------------------------------------------------|
| Bits \#0 – 9 (LSB)      | CAN code of the keyword                         |
| Bits \#10 – 14          | Axis number (0 represents first axis/axis “A”)  |
| Bits \#16 – 31          | Index of the array (if the keyword is an array) |

For example, if keyword DInPort\[4\] is to be represented (CAN code = 35, axis number = 3 (axis D), array index = 4) , then complex CAN code = 35 + (3\<\<10) + (4\<\<16) = 35 + 3 \* 2<sup>10</sup> + 4 \* 2<sup>16</sup> = 265251.

The following table illustrates the complex CAN code of DInPort\[4\].
