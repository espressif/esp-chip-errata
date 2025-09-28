[TWAI-3.13.4] CPU 读取中断寄存器信息时可能导致发送中断信号丢失
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

CPU 通过读取 INTERRUPT_REG 寄存器来复位 TWAI 控制器的中断信号。如果在同一个 APB 时钟周期内 TWAI 控制器刚好产生发送中断信号，则发送中断信号丢失。

变通方法
^^^^^^^^

数据等待发送完成期间（即发送请求已发起），每一次读取 INTERRUPT_REG 后，用户都应检查 STATUS_TRANSMIT_BUFFER 位。如果 STATUS_TRANSMIT_BUFFER 置位而 TWAI_TRANSMIT_INT_ST 没有置位，则说明发送中断信号丢失。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
