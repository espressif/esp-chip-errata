[APM-885] GDMA-AXI 读权限寄存器无法单独控制各外设
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3, v3.0, v3.1, v3.2

描述
^^^^

GDMA-AXI（General-Purpose DMA for AXI Bus，AXI 总线通用 DMA）连接 LCD_CAM、通用 SPI2 (GP-SPI2)、通用 SPI3 (GP-SPI3)、PARLIO、AES 和 SHA。这些外设的 GDMA-AXI 读请求只受 DUMMY Master 的读权限寄存器 ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG`` 控制。在某个外设自己的读权限寄存器（如 ``PMS_DMA_AXI_PDMA_LCDCAM_R_PMS_REG``）中禁止读访问不会生效。

原因：APM 中的读地址 ID (Read Address ID, ARID) 译码逻辑与 GDMA-AXI 侧的 ARID 编码不匹配。因此，APM 会将上述外设全部识别为 DUMMY Master，并按其读权限寄存器 ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG`` 检查读请求。

因此，DUMMY Master 的读权限会同时作用于 LCD_CAM、GP-SPI2、GP-SPI3、PARLIO、AES 和 SHA。AES 或 SHA 的读访问无法与其他外设分开限制。

变通方法
^^^^^^^^

GDMA-AXI 的读访问无法通过软件针对单个外设进行限制。如需禁止某个地址区间的读访问，将 DUMMY Master 的读权限寄存器 ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG`` 中该区间对应的位设置为 0。该位会同时作用于 LCD_CAM、GP-SPI2、GP-SPI3、PARLIO、AES 和 SHA。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
