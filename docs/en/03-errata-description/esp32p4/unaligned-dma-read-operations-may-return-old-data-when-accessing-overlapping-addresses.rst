[MSPI-750] PSRAM Unaligned DMA Read Operations May Return Old Data When Accessing Overlapping Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

When accessing PSRAM randomly through DMA or CACHE, if a write operation to a certain address range is followed by a read operation to the same range, data readout errors may occur. The triggering conditions are:

- Any write request is executed.
- The read operation is a DMA-initiated read request with a burst size of 1 byte or 2 bytes, and the access address is not 4-byte aligned.
- The address range accessed by the read operation overlaps with the address range previously written.

Under these conditions, the read operation may fail to obtain the new data written by the prior write operation and instead return old data that existed in PSRAM before the write.

Root cause: The MSPI IP's internal "address overlap detection" mechanism has an anomaly when processing the above unaligned read requests. The computed address range used for overlap detection may be 1 to 3 bytes shorter at the end than the actual address range the read request should access. This defect may cause the overlap detection to fail, resulting in incorrect data reads.

Workarounds
^^^^^^^^^^^

It is recommended that software applications enforce 4-byte alignment for all masters that may issue unaligned accesses (for example, burst sizes of 1 or 2 bytes), such as USB or SDMMC. This prevents the issue from occurring.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
