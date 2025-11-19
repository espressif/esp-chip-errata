[APM-560] 未授权的 AHB 访问可能会阻塞后续对 PSRAM 或 flash 的访问
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3, v3.0

描述
^^^^

当多个 AHB Master（USB OTGFS、USB OTGHS、GMAC、SDMMC、Trace0/1、AHB PDMA、L2MEM Monitor、TCM Monitor 等）并发访问 PSRAM 或 flash 时，如果其中某个 Master 不具备访问权限，DMA APM 的访问权限检查会正确拦截该越权访问。

在拦截过程中，DMA APM 并未正确屏蔽下游响应，导致后续传输异常。因此，一旦发生越权访问，此后即便是由具备权限的 AHB Master 发起的正常访问，也可能被阻塞。

变通方法
^^^^^^^^

避免触发对 PSRAM 或 flash 的越权访问。如果无法避免越权访问且系统已经进入上述卡死状态，唯一可用的恢复方式是执行系统复位。

解决方案
^^^^^^^^

.. only:: esp32p4

   已在芯片版本 :bdg-success:`v3.1` 中修复。
