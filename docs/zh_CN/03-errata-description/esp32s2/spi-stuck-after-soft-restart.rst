[SPI] SPI 自动暂停后软件重启卡住
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

描述
^^^^

在开启 auto suspend 功能后，在 Memory SPI 擦写 flash 的过程中，如果发生 Cache 请求，Memory SPI 会自 动向 flash 发送 SUSPEND (0×75) 命令，如果在发送 RESUME 命令 (0×7A) 前发生系统复位并重启，则 Memory SPI 的状态机无法恢复，导致系统无法继续运行。

变通方法
^^^^^^^^

禁用 auto suspend 功能。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.0` 中修复。
