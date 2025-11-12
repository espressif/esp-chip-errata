[CPU-718] PSRAM Read-After-Write Consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c5

   .. tags::

      v0.0, v0.1, v1.0

.. only:: esp32c61

   .. tags::

      v0.0, v0.1, v0.2, v1.0

Description
^^^^^^^^^^^

When the CPU performs random read or write accesses to PSRAM through CACHE or DMA, and one of the following conditions is true:

- PSRAM encryption or decryption is enabled, or
- When accessing PSRAM via DMA, AHB_DMA_OUT_DATA_BURST_MODE_SEL_CHn is set to 0 or 1.

Data-consistency issues may occur for CPU accesses to PSRAM.

Cause
"""""

The MSPI hardware handles CPU read or write requests to PSRAM and uses an internal buffer or cache. Because of this buffering (and encryption or decryption latency), CPU read or write requests received by MSPI are not always executed on the SPI bus immediately.

If the CPU performs a write to a PSRAM address and then quickly issues a read to the same physical address, the write may still be delayed inside MSPI. In that case, MSPI can execute the read before the earlier write has actually completed on the PSRAM, leading to stale or inconsistent data being returned.

Examples
""""""""

- If CACHE reads from an encrypted or decrypted PSRAM region and a cache miss occurs, the data written back can be inconsistent.
- After a DMA write to PSRAM completes, a subsequent DMA read or CACHE read of the same PSRAM region may return inconsistent data.

Workarounds
^^^^^^^^^^^

- For consistency problems caused by cache misses during encryption or decryption: Avoid enabling PSRAM encryption in workloads that perform random read or write access.
- For consistency problems when the CPU accesses PSRAM via DMA: Insert a short delay after the DMA write finishes, or before the CPU reads the same physical address, to ensure MSPI has completed the actual PSRAM write.

Solution
^^^^^^^^

.. only:: esp32c5 or esp32c61

   To be fixed in the :bdg-warning:`next chip revision`.
