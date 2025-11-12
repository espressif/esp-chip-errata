[SRAM-436] Internal SRAM Contents May Be Corrupted After Digital Peripheral Power Domain Power-Down
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c5

   .. tags::

      v1.0

Description
^^^^^^^^^^^^^^

On some {IDF_TARGET_NAME} v1.0 chips, when the power-down feature of the digital peripheral power domain is enabled, part of the internal SRAM contents may be corrupted. This may trigger a CPU_LOCKUP reset or cause the system to hang.

Workaround
^^^^^^^^^^^^^^

Starting from ESP-IDF v5.5, the power-down feature of the digital peripheral power domain is disabled for {IDF_TARGET_NAME} v1.0 chips.

Solution
^^^^^^^^^^^

Fixed in hardware starting from chip revision :bdg-success:`v1.2`.
