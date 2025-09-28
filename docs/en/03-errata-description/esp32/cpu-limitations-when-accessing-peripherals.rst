[CPU-3.18] CPU Has Limitations When Accessing Peripherals in Chips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

As described in :doc:`/03-errata-description/esp32/cpu-writes-lost`, :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`, :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces`, CPU has limitations when accessing peripherals in chips of different revisions using 0x3FF0_0000 ~ 0x3FF1_EFFF, 0x3FF4_0000 ~ 0x3FF7_FFFF, and 0x6000_0000 ~ 0x6003_FFFF.

.. flat-table::
   :header-rows: 2
   :widths: 2 2 1 1 1 1 1 1

   * - :rspan:`1` Address space (Bus)
     - :rspan:`1` Register type
     - :rspan:`1` Operation
     - :cspan:`4` Chip Revision
   * - v0.0
     - v1.0
     - v1.1
     - v3.0
     - v3.1
   * - :rspan:`3` 0x3FF0_0000 ~ 0x3FF1_EFFF and 0x3FF4_0000 ~ 0x3FF7_FFFF (DPORT)
     - :rspan:`1` Non- FIFO
     - Write
     - :cspan:`2` Yes
     - :cspan:`1` Yes
   * - Read
     - :cspan:`2` No (refer to :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`)
     - :cspan:`1` Yes
   * - :rspan:`1` FIFO
     - Write
     - No (refer to :doc:`/03-errata-description/esp32/cpu-writes-lost`)
     - :cspan:`3` Yes
   * - Read
     - Yes
     - :cspan:`3` Yes
   * - :rspan:`3` 0x6000_0000 ~ 0x6003_FFFF (AHB)
     - :rspan:`1` Non- FIFO
     - Write
     - :cspan:`4` Yes
   * - Read
     - :cspan:`4` Yes
   * - :rspan:`1` FIFO
     - Write
     - :cspan:`4` Yes
   * - Read
     - :cspan:`4` No (No such feature, unpredictable results)

.. note::

    - Yes: operation is executed correctly
    - No: operation fails
