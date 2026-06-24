# 换相

换相是找到直流无刷电机（至少 3 相）电角度偏移的过程。它确保控制器在运动过程中交替切换相电流时，所施加的电流矢量始终与磁场保持 90 电气度，从而高效产生力/力矩。

![Establishing the electrical angle: ComtMode selects the method (search, Hall, absolute encoder or minimal-jumps search); StatReg bit 0 is set and normal motion allowed once a usable angle exists (the rough Hall angle at ComtStatus 300/400 for methods 3/4, or 100 / not-required 200 otherwise); ComtAng reports the angle in effect](commutation-overview.svg)

控制器必须知道电机电角度才能正确换相。该角度可直接来自霍尔传感器、之前存储的绝对式编码器参考值，或通过施加小幅指令并观察响应的搜索法获得。在没有霍尔传感器的情况下，角度必须从编码器推导，而编码器通常与电机电气相位不对齐，因此需要进行初始化（定相）过程来对齐二者。

换相运行的时机由 [ComtMode](ComtMode.md) 配置（上电后、电机使能时、两者均触发，或仅手动触发）；该过程也可按需重新触发。[StatReg](../07-status-and-faults/StatReg.md) 的换相完成位（位 0）控制正常运动的门控：对于大多数方法，换相完成（[ComtStatus](ComtStatus.md) `100`）或不需要换相（`200`）时置位；但对于霍尔启动切换方法（`ComtMode[1]=3` 或 `4`），在粗略阶段（`ComtStatus` `300`/`400`）即已置位，轴可立即运动。仅在尚无可用角度（状态 `0`/`1`）或换相失败（负状态）时，该位保持清零，阻止正常运动。

本类别包含：

| 编号 | 关键字 | 说明 |
|-----|---------|---------|
| 1 | [ComtAng](ComtAng.md) | 瞬时换相（电气）角度 |
| 2 | [ComtMode](ComtMode.md) | 换相设置数组（方法与模式） |
| 3 | [ComtStatus](ComtStatus.md) | 换相过程状态 |
| 4 | [HallsValue](HallsValue.md) | 霍尔传感器原始状态 |
| 5 | [HallsAngle](HallsAngle.md) | 各霍尔状态对应的电角度 |
| 6 | [HallsAngleSw](HallsAngleSw.md) | HallsAngle 条目的解释方式（Central-i v5） |
| 7 | [HallOnlyFilt](HallOnlyFilt.md) | 纯霍尔换相角的滤波器 |

## 操作指南：使用霍尔传感器与编码器索引初始化换相

带霍尔传感器和编码器索引的无刷电机的典型设置为"粗略后精细"：先从霍尔状态对应的角度出发，使轴立即运动，然后在下一个编码器索引脉冲处精细到确切的电角度零点。这是换相方法 `3`（霍尔 + 特殊编码器切换）。

1. **选择方法及运行时机。** `[ComtMode](ComtMode.md)[19] = 0`（默认）时，控制器在上电后自动运行换相。方法在 `[1]` 中设置：

   ```text
   AComtMode[1]=3       ; method 3: Hall + special-encoder switching (wait for index)
   AComtMode[19]=0      ; run automatically after power-on (default)
   ```

2. **确认霍尔映射正常。** 方法 `3` 依赖 [HallsValue](HallsValue.md)（原始霍尔状态，预期读取 `1..6`；`0` 和 `7` 为非法值）以及将每个合法霍尔状态映射到其电角度的 [HallsAngle](HallsAngle.md) 表。电机静止时，应看到 `AHallsValue` 在 `1..6` 范围内，且 `AHallsAngle` 已按电机配置。

3. **使能电机，让定相运行。** 换相开始时，[ComtStatus](ComtStatus.md)`[1]` 依次经过：

   | 值 | 含义 |
   |---|---|
   | `1` | 进行中 |
   | `300` | 粗略换相完成（来自霍尔传感器）；等待索引脉冲 |
   | `100` | 成功完成——精细角度已锁定在索引处 |

   ```text
   AMotorOn=1               ; enable the motor; phasing begins
   AComtStatus[1]           ; 1, then 300 (rough done), then 100 (fine done)
   ```

   对于此方法，控制器在粗略阶段（`AComtStatus[1]` = `300`）即已设置 [StatReg](../07-status-and-faults/StatReg.md) 位 0（换相完成），因此轴可立即产生力矩并运动——如果编码器索引尚未被读头经过，可命令小幅运动使其到位。当索引脉冲到来时，控制器将换相角固定到索引参考值，`AComtStatus[1]` 读取 `100`；这会细化角度，但不会改变位 0（已经置位）。

4. **验证并继续。** 对于此方法，`StatReg` 位 0 已在粗略阶段（状态 `300`）置位，因此在索引细化角度之前，正常运动即已使能：

   ```text
   AComtAng                 ; the resulting electrical angle in use
   AStatReg                 ; bit 0 set = commutation complete
   ```

   如果 `AComtStatus[1]` 报告负值，请参阅 [ComtStatus](ComtStatus.md) 中的值表（例如，`-7` 表示检测到非法霍尔序列——通常为接线问题）。

5. **按需重新触发。** 若要在不更改方法的情况下按需重新运行换相，将特殊值 `1282` 写入 `[5]` 槽（控制器仅在电机关闭且轴处于正常运行状态时执行，并将该槽清零回 `0`）：

   ```text
   AMotorOn=0
   AComtMode[5]=1282        ; re-run commutation now
   AMotorOn=1
   ```

对于没有索引脉冲或霍尔跳变信号可信度高的电机，使用方法 `4`（等待下一次霍尔跳变而非索引）——粗略完成值为 `400`。对于没有霍尔传感器的电机，基于搜索的方法（`0`、`5`）施加小幅指令并观察响应；对于绝对式编码器，使用方法 `2`（无需运动，从 `ComtMode[4]` 读取之前存储的零点）。纯霍尔连续换相为方法 `6`，可选择由 [HallOnlyFilt](HallOnlyFilt.md) 滤波。
