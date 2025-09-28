[CPU-3.9] When the CPU Accesses External Sram in a Certain Sequence, Read and Write Errors May Occur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v1.0, v1.1

Description
^^^^^^^^^^^

This error may occur when the CPU executes the following instructions to access external SRAM:

.. code-block::

    store.x at0, as0, n
    load.y at1, as1, m

In the pseudo-assembly instructions above, ``store.x`` represents an x-bit write operation, while ``load.y`` represents a y-bit read operation. ``as0+n`` and ``as1+m`` represent the same address in external SRAM.

- The instructions can be sequential or contained within the same pipeline (less than four intermediate instructions, and no pipeline flushes.)
- When x >= y, the data write may be lost. (NOTE: when both the ``load`` and the ``store`` refer to 32-bit values, the write is only lost if an interrupt occurs between the first and second instructions.)
- When x < y, data writes may be lost and invalid data may be read.

Workarounds
^^^^^^^^^^^

This bug is automatically worked around when external SRAM use is enabled in ESP-IDF v3.0 and newer.

- When x >= y, insert four nop instructions between ``store.x`` and ``load.y``.
- When x < y, insert a memw instruction between ``store.x`` and ``load.y``.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v3.0`.
