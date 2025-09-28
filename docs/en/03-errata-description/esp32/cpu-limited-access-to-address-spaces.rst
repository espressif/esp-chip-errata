[CPU-3.16] There Are Limitations to the CPU Access to 0x3ff0_0000 ~ 0x3ff1_efff and 0x3ff4_0000 ~ 0x3ff7_ffff Address Spaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

1. The CPU read operations that fall in these two address spaces are speculative. Speculative read operations can cause the behavior described by the program to be inconsistent with the actual behavior of the hardware.
2. If the two CPUs continuously access address space 0x3FF0_0000 ~ 0x3FF1_EFFF at the same time, some of the access may be lost.
3. When the CPU reads FIFO through the address space 0x3FF4_0000 ~ 0x3FF7_0000, the FIFO read pointer is updated with delays. As the CPU frequency increases, the interval between two consecutive FIFO reads initiated by the CPU is shortened. When a new FIFO read request arrives, the FIFO read pointer has not been updated, causing the CPU to read the value of the previous FIFO read operation.

Workarounds
^^^^^^^^^^^

1. Insert "MEMW" instruction before the CPU access operation that falls in these two address spaces. That is, in C/C++, software needs to always use the "volatile" attribute when accessing registers in these two address spaces.

2. When the CPU frequency is 160 MHz, add six "nop" between two consecutive FIFO reads. When the CPU frequency is 240 MHz, add seven "nop" between two consecutive FIFO reads.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
