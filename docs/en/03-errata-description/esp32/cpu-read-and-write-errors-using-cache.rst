[CPU-3.2] When the CPU Accesses External Sram Through Cache, Under Certain Conditions Read and Write Errors Occur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

Description
^^^^^^^^^^^

Access to external SRAM through cache will cause read and write errors if these operations are pipelined together by the CPU.

Workarounds
^^^^^^^^^^^

If accessing external SRAM from chip revision v0.0, users must ensure that access is always one-way—only a write or a read can be in progress at a single time in the CPU pipeline.

The MEMW instruction can be used: insert __asm__("MEMW") after any read from external PSRAM that may be followed by a write to PSRAM before the CPU pipeline is flushed.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
