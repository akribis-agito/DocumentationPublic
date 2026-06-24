---
keyword: DownloadUPBin
summary: 将已编译的用户程序二进制镜像传输到控制器程序存储器的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 207
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# DownloadUPBin

将已编译的用户程序二进制镜像传输到控制器程序存储器的指令。

## 概述

`DownloadUPBin` 将已编译的用户程序二进制镜像传输到控制器的非易失性程序存储区，加载控制器后续将执行的程序。下载的程序在重新上电后仍保留。这是一个非轴指令。由于它会擦除并重新编程程序存储区，因此不能在轴运动中或电机使能时运行；请先停止运动并禁用电机。

典型工作流程是：先用 [ProgErase](ProgErase.md) 擦除现有程序，再用 `DownloadUPBin` 下载新镜像，然后在运行前用 [ProgReset](ProgReset.md) 重置程序状态。

## 工作原理

`DownloadUPBin` 首先停止所有运行中的用户程序线程，然后擦除程序存储区。若擦除失败，指令返回错误 27，且不开始传输。否则控制器以 `OK` 确认，上位机通过发出指令的通信通道（串口、CAN 或以太网）以一系列 8 字节数据块的形式流式传输已编译的二进制文件；每个块到达后即写入存储区。当上位机发送由八个回车字节组成的块作为文件结束标志时，传输结束。传输过程中收到长度异常的块将以错误 15 中止传输。

传输受 10 秒超时保护：若在收到文件结束标志之前数据块停止到达，下载将中止。超时时控制器不发送任何回复，因为链路被认为已失步，且存储区中不留有有效程序。正常收到文件结束标志后，控制器写入完成签名并验证程序校验和；若校验和不匹配，签名将被擦除（即无程序存在），指令返回错误 171。因此，失败或中断的下载会使控制器没有可用程序，镜像必须重新下载。

由于程序文件针对特定布局编译，二进制文件必须由 PC Suite 为目标控制器生成；[Jump](Jump.md) 等关键字所依赖的偏移量在文件构建时已固定。

## 示例

```text
; 在电机关闭且无运动进行时发出
ADownloadUPBin       ; 将已编译的用户程序二进制文件传输到程序存储器
```

## 参见

- [ProgErase](ProgErase.md) — 擦除当前用户程序
- [ProgReset](ProgReset.md) — 重置用户程序状态
- [ProgStatAll](ProgStatAll.md) — 所有用户程序线程的状态
