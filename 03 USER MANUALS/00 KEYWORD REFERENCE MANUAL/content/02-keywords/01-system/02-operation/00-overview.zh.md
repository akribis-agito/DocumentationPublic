# 操作

**概述：**

作用于控制器整体状态的命令：将参数保存到闪存以及从闪存加载、执行软件复位、进入固件或 FPGA 下载模式，以及自动启动用户程序。这些命令中的大多数在电机使能或运动中时无法发出。

![Save copies the working parameters in RAM to non-volatile flash; Load copies them back from flash (also automatically at power-up); Reset reboots the controller and reloads from flash](save-load-reset.svg)
