[APM-560] Unauthorized AHB Access May Block Subsequent PSRAM or Flash Transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3, v3.0

Description
^^^^^^^^^^^

When multiple AHB Masters (USB OTGFS, USB OTGHS, GMAC, SDMMC, Trace0/1, AHB PDMA, L2MEM Monitor, TCM Monitor, etc.) concurrently access PSRAM or flash, and one of the masters does not have access permission, the access permission check in the DMA APM correctly intercepts the unauthorized transaction.

During interception, the DMA APM does not properly mask downstream responses, so it leads to abnormal subsequent transfers. As a result, after an unauthorized access, even valid accesses initiated by an authorized AHB Master may be stalled.

Workaround
^^^^^^^^^^

Avoid triggering unauthorized accesses to PSRAM or flash. If unauthorized access cannot be avoided and the system enters the stuck state described above, the only available recovery method is to perform a system reset.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
