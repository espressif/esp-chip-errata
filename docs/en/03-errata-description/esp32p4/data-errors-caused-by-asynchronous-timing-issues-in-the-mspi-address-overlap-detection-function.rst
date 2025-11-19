[MSPI-751] Data Errors Caused by Asynchronous Timing Issues in the MSPI Address Overlap Detection Function When Read/Write Operations Overlap at Specific Frequencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

When accessing PSRAM randomly through DMA or CACHE, if a write operation to a certain address range is followed by a read operation to the same range, data readout errors may occur under specific clock frequency configurations. The triggering conditions are:

- During random PSRAM accesses through DMA or CACHE, a “write followed by read” sequence occurs on the same address range.
- The frequency ratio between the AXI bus (freq_axi) and the MSPI core (freq_core) exceeds the safe range. The exact safe range depends on whether AXI concatenation is enabled and the actual timing characteristics of the chip.

Under these conditions, the read operation may fail to obtain the new data written by the prior write operation and instead return old data that existed in PSRAM before the write. This error breaks data consistency and may impact normal chip functionality.

Root cause: The MSPI IP's internal "address overlap detection" function has an asynchronous timing issue. When the clock-frequency ratio is near a critical boundary, this timing issue may cause the detection logic to fail, preventing it from correctly identifying overlapping addresses and eventually leading to incorrect data reads.

Workaround
^^^^^^^^^^

To ensure system stability, software configurations must satisfy the following frequency constraints, based on whether AXI concatenation is enabled and the timing conditions:

.. flat-table::
   :header-rows: 1
   :widths: 2 1 2

   * - Timing Condition
     - AXI Concatenation Status
     - Frequency Constraint
   * - :rspan:`1` Assuming poor timing
     - Enabled
     - 3 × freq_core ≥ freq_axi
   * - Disabled
     - freq_core ≥ freq_axi
   * - :rspan:`1` Assuming normal timing
     - Enabled
     - 4 × freq_core ≥ freq_axi
   * - Disabled
     - 2 × freq_core ≥ freq_axi

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
