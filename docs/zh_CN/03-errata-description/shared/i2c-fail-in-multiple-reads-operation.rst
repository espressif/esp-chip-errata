[I2C-308] 在分多次读操作中，主机无法正确读取从机数据
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3

描述
^^^^^^^^^^^

如果启用了 I2C 从机 non-FIFO 模式且主机多次对从机进行读操作时，主机无法正确从从机中读取正确的数据。

变通方法
^^^^^^^^^^^

配置从机的 I2C_FIFO_ADDR_CFG_EN 和 I2C_SLV_TX_AUTO_START_EN 为 1，并配置 I2C_FIFO_PRT_EN 为 0。

配置完成后，主机必须使用 RSTART -> WRITE (slave addr, fifo addr) -> RSTART -> WRITE (slave addr) -> READ (NACK) -> STOP 的命令序列对从机进行访问，每次读取仅限一个字节。

解决方案
^^^^^^^^

.. only:: esp32h2

   已在芯片版本 :bdg-success:`v1.2` 中修复。

.. only:: esp32p4

   已在芯片版本 :bdg-success:`v3.0` 中修复。
