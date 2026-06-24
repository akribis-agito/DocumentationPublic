# 龙门控制

用于配置和整定龙门（双电机）轴的关键字，其中两台并联驱动电机在协调 MIMO 控制下驱动单一机构运动。

本类别组织如下：

- [通用变量](01-general-variables/00-overview.md) — 启用龙门模式及映射/偏摆校正变量
- [龙门运动学反馈](02-gantry-kinematic-feedback/00-overview.md) — 反馈、偏置及辅助编码器读数
- [龙门整定](03-gantry-tuning/00-overview.md) — 偏摆位置/速度增益及前馈项
- [双环龙门控制](04-dual-loop-gantry-control/00-overview.md) — 双环及伪双环模式的反馈来源

## 龙门控制工作原理

龙门机构由两台并联驱动电机分别驱动同一横梁的两端。控制器不对每台电机独立控制，而是将两台电机的测量值变换为两个虚拟轴——**共模（线性）模式**为两端的平均值（即工作台实际平移量，由主轴指令），**差模（偏摆）模式**为两端之差（即横梁的垂直度，通常保持为零或 [GantryYawRef](01-general-variables/GantryYawRef.md) 设定的偏置值）。每个虚拟轴运行各自的位置环和速度环，两个环输出重新合并为各电机的电流指令：一台电机接收线性 + 偏摆，另一台接收线性 − 偏摆。这种解耦意味着平移指令不会引发偏摆，偏摆校正也不会引发平移。

共模/差模变换及重合并过程在 [通用变量 / GantryOn](01-general-variables/GantryOn.md) 下的示意图中有所说明。

## 操作流程：接入龙门控制

在设置 `GantryOn` 之前，两台电机必须已上电、完成换相，且偏摆轴不得被独立指令。以主轴 `A` / 偏摆轴 `B` 组合为例，完整接入顺序如下：

1. **启动两台电机。** 先将 `A` 和 `B` 电机均使能。[GantryOn](01-general-variables/GantryOn.md) 在任一电机关闭时自动清零为 `0`，因此只在两台电机均使能后再接入。两台电机还必须完成换相（`AComtStatus[1]` 和 `BComtStatus[1]` 均为 `100`），龙门才能正确驱动电流，但换相状态并非维持 `GantryOn` 置位的条件：

   ```text
   AMotorOn=1           ; enable the master motor
   BMotorOn=1           ; enable the yaw motor (same pair)
   ```

2. **在主轴上接入龙门模式。** 在 `0` → `1` 跳变时，控制器将两端当前差值捕获至 [GantryOffset](02-gantry-kinematic-feedback/GantryOffset.md) 并折入反馈中，使差模（偏摆）读数从干净的零值开始，而无需强制横梁垂直。控制方案切换至龙门 MIMO 拓扑：

   ```text
   AGantryOn=1          ; engage MIMO gantry control on the master axis
   AGantryOffset        ; read back the captured A/B offset (set at the 0->1 transition)
   ```

3. **验证反馈。** [GantryFdbk](02-gantry-kinematic-feedback/GantryFdbk.md) 的主轴值为线性环跟随的共模（平均）龙门位置；偏摆轴值为偏摆环驱动至 [GantryYawRef](01-general-variables/GantryYawRef.md) 的差模读数。反馈仅在**龙门使能时**每周期重新计算；首次接入前读取为 `0`，退出后保持最后值直至下次接入。

   ```text
   AGantryFdbk          ; mean (common) gantry position
   BGantryFdbk          ; differential (yaw) reading
   AGantryYawRef        ; commanded yaw target (default 0)
   ```

4. **仅通过主轴指令运动**（龙门运动通过 `A` 的普通运动关键字指令）。偏摆环安静地保持横梁垂直。若运动中某台电机因故障关闭，控制器将主动关闭另一台，并在被强制关闭的一侧记录 [ConFlt](../07-status-and-faults/ConFlt.md) 码 `1061`；随后 `AGantryOn` 清回 `0`，故障排除后须重新接入。

5. **退出：** 写入 `AGantryOn=0`。两轴恢复独立控制。循环切换龙门模式会重新捕获 `GantryOffset`，因此在横梁有负载时请勿随意切换。

若线性环需闭环于独立测量值（例如工件下方的标尺），请参阅[双环龙门控制](04-dual-loop-gantry-control/00-overview.md)中的 [GantryDLoopOn](01-general-variables/GantryDLoopOn.md) 和 [GantryFdbkSrc](02-gantry-kinematic-feedback/GantryFdbkSrc.md)。若需沿横梁进行位置相关的 50/50 分配，请参阅 [GantryMapType](01-general-variables/GantryMapType.md)（central-i v5）。
