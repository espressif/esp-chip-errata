[MSPI-749] Load Access Fault During Chip Power-on or Deep-Sleep Wake-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

During the power-on or wake-up process of {IDF_TARGET_NAME}, due to abnormal handling inside the MSPI IP read-request channel, the MSPI may fail to correctly process the first and second access requests initiated by the AXI system bus. This can occasionally result in unexpected error responses, causing the boot process to fail.

Workarounds
^^^^^^^^^^^

Power-on sequence: The power-on sequence is fixed. If the sequence fails, the system can only rely on the watchdog timeout to reset the chip and perform a “second power-on”. After this second power-on, the flash MSPI module can resume normal operation.

Wake-up sequence: During the Deep-sleep wake-up, the LP memory region remains powered and retains its contents. A small executable program can be pre-loaded into LP memory before entering sleep. This program should perform two dummy read accesses. Upon wake-up, the CPU will execute this program first and then jump to the ROM code to continue the normal boot process. The code is as follows:

.. code-block::

    REG32_WR(0x500ca000, 0x23);
    CLEAR_PERI_REG_MASK(0x5008c03c, 0x80000000);

    // Disable CPU error response handling
    SET_PERI_REG_MASK(0x500e51a4, 0x00000007);

    // Enable AXI interface
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c03c, 0x00000001);

    // Configure one MSPI MMU entry to map the AXI address to the flash address
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c380, 0x0);
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c37c, 0x1000);

    //Perform the first and second AXI read accesses from flash MSPI
    REG32_RD(0x80000000);
    REG32_WR(0x500ca000, 0x23);
    REG32_RD(0x80000040);
    REG32_WR(0x500ca000, 0x23);

    //Re-enable CPU error response handling
    CLEAR_PERI_REG_MASK(0x500e51a4, 0x00000007);

    SET_PERI_REG_MASK(0x50111014, 0x8000);
    SET_PERI_REG_MASK(0x50111014, 0x2000);

PSRAM MSPI: During PSRAM MSPI initialization, inserting two dummy reads before the first actual AXI read access can effectively avoid the initial access anomaly.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
