[ROM-764] Secure Boot Verification Failure Caused by Incorrect Buffer Address in ROM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

In the ROM, the start address of the secure-boot stage buffer is incorrectly configured. It points to the L2 cache data memory (0x4FF0_0000), which is part of the L2 cache and not writable by the CPU.

Because of this misconfiguration, data stored in the secure-boot buffer may be lost, potentially causing hash calculation failures or signature verification failures during the secure-boot process.

Workaround
^^^^^^^^^^

Do not enable secure boot.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
