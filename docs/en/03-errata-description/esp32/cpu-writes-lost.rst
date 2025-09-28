[CPU-3.3] When the CPU Accesses Peripherals and Writes a Single Address Repeatedly, Some Writes May Be Lost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

Description
^^^^^^^^^^^

Some ESP32 peripherals are mapped to two internal memory buses (AHB & DPORT). When written via DPORT, consecutive writes to the same address may be lost.

Workarounds
^^^^^^^^^^^

When writing the same register address (i.e., FIFO-like addresses) in sequential instructions, use the equivalent AHB address not the DPORT address. (For other kinds of register writes, using DPORT registers will give better write performance.)

.. list-table::
    :widths: 40 30 30
    :header-rows: 1
    :align: center

    * - Registers
      - DPORT Addresses
      - AHB (Safe) Addresses
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

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.

.. note::

    Software cannot use AHB addresses to read FIFO.
