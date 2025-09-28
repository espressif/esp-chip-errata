[CPU-3.3] CPU 访问外设时，如果连续不间断地写同一个地址，会出现数据丢失的现象
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

描述
^^^^^^^^

一些 ESP32 外设映射到两条内部存储器总线（AHB 和 DPORT）。当通过 DPORT 写入时，对相同地址的连续写入可能会出现数据丢失的现象。

变通方法
^^^^^^^^

当连续写同一个地址（即类似 FIFO 的地址）时，使用 AHB 地址而不是 DPORT 地址。（对于其他类型的寄存器写入，使用 DPORT 地址可能写性能更好。）

.. list-table::
    :widths: 40 30 30
    :header-rows: 1
    :align: center

    * - 寄存器名称
      - DPORT 地址
      - AHB（安全）地址
    * - UART_FIFO_REG
      - 0x3FF40000
      - 0x60000000
    * - UART1_FIFO_REG
      - 0x3FF50000
      - 0x60010000
    * - UART2_FIFO_REG
      - 0x3FF6E000
      - 0x6002E000
    * - I2S0_FIFO_RD_REG
      - 0x3FF4F004
      - 0x6000F004
    * - I2S1_FIFO_RD_REG
      - 0x3FF6D004
      - 0x6002D004
    * - GPIO_OUT_REG
      - 0x3FF44004
      - 0x60004004
    * - GPIO_OUT_W1TS_REG
      - 0x3FF44008
      - 0x60004008
    * - GPIO_OUT_W1TC_REG
      - 0x3FF4400C
      - 0x6000400C
    * - GPIO_OUT1_REG
      - 0x3FF44010
      - 0x60004010
    * - GPIO_OUT1_W1TS_REG
      - 0x3FF44014
      - 0x60004014
    * - GPIO_OUT1_W1TC_REG
      - 0x3FF44018
      - 0x60004018
    * - GPIO_ENABLE_REG
      - 0x3FF44020
      - 0x60004020
    * - GPIO_ENABLE_W1TS_REG
      - 0x3FF44024
      - 0x60004024
    * - GPIO_ENABLE_W1TC_REG
      - 0x3FF44028
      - 0x60004028
    * - GPIO_ENABLE1_REG
      - 0x3FF4402C
      - 0x6000402C
    * - GPIO_ENABLE1_W1TS_REG
      - 0x3FF44030
      - 0x60004030
    * - GPIO_ENABLE1_W1TC_REG
      - 0x3FF44034
      - 0x60004034

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.0` 中修复。

.. note::

    软件不可以使用 AHB 地址读 FIFO。
