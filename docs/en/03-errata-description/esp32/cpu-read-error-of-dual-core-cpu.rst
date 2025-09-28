[CPU-3.10] When Each CPU Reads Certain Different Address Spaces Simultaneously, a Read Error May Occur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1

Description
^^^^^^^^^^^

Running in dual-core CPU mode, when one CPU bus reads address space A (0x3FF0_0000 ~ 0x3FF1_EFFF), while the other CPU bus reads address space B (0x3FF4_0000 ~ 0x3FF7_FFFF), an incorrect read may be generated on the CPU reading address space B.

Workarounds
^^^^^^^^^^^

Either of the following workarounds can be used:

- When either CPU reads address space A, prevent the other CPU bus from reading address space B via locks and interrupts.
- Before reading address space A, disable interrupts and insert a read from address space B on the same CPU (read a non-FIFO register, e.g., 0x3FF40078).

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v3.0`.
