[CACHE-126] Cache Hit Error During Cache Write-Backs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

When a cache write-back is in progress, if the CPU accesses other addresses within the same cache line, the access request will be treated as a cache miss. This triggers the miss handling module to reload the cache line from external memory, resulting in two identical cache data entries in the same cache line.

Due to hardware logic issues, the cache hit logic may select incorrect cache data, causing the CPU to return incorrect results. If the CPU also writes to the cache line, it may cause the data being written back to be lost.

For example, the following scenarios may lead to cache hit errors in {IDF_TARGET_NAME}:

- Accessing data in a cache line that is being written back to the cache during an interrupt:

  During the cache write-back process, when the CPU is waiting for the write-back completion signal, an interrupt request occurs and the interrupt handler is entered, accessing the memory in the same buffer. If the data accessed by the handler and the write-back address are in the same cache line, cache hit errors may occur.

- Conflicts in a multi-core system:

  In a multi-core system, if CPU0 is waiting for a cache write-back to complete while CPU1 accesses the same cache line address, cache hit errors may occur.

Workarounds
^^^^^^^^^^^

During a cache write-back, it is recommended that users take the following precautions at the same time:

- Disable interrupts on the current CPU, and re-enable them only after the cache write-back has completed.
- Enable the cache freeze feature to stop another CPU from accessing the cache.

This issue has been automatically bypassed using the above methods in ESP-IDF v4.4.6+, v5.0.4+, v5.1.1+, v5.2, and above versions.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
