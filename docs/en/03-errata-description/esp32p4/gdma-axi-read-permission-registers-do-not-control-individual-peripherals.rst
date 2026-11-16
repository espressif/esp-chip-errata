[APM-885] GDMA-AXI Read Permission Registers Do Not Control Individual Peripherals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3, v3.0, v3.1, v3.2

Description
^^^^^^^^^^^

The General-Purpose DMA for AXI Bus (GDMA-AXI) connects LCD_CAM, General Purpose SPI2 (GP-SPI2), General Purpose SPI3 (GP-SPI3), PARLIO, AES, and SHA. GDMA-AXI read requests from these peripherals are controlled only by the DUMMY Master's read permission register, ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG``. Denying read access in a peripheral's own read permission register (e.g., ``PMS_DMA_AXI_PDMA_LCDCAM_R_PMS_REG``) has no effect.

Reason: The Read Address ID (ARID) decode logic in the APM does not match the ARID encoding on the GDMA-AXI side. The APM therefore identifies all of these peripherals as the DUMMY Master and checks their read requests against ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG``.

As a result, the DUMMY Master's read permission applies to LCD_CAM, GP-SPI2, GP-SPI3, PARLIO, AES, and SHA at the same time. Read access for AES or SHA cannot be restricted separately from the other peripherals.

Workaround
^^^^^^^^^^

GDMA-AXI read access cannot be restricted on a per-peripheral basis through software. To block read access to an address region, set that region's bit to 0 in the DUMMY Master's read permission register, ``PMS_DMA_AXI_PDMA_DUMMY_R_PMS_REG``. The same bit applies to LCD_CAM, GP-SPI2, GP-SPI3, PARLIO, AES, and SHA at the same time.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
