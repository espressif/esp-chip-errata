[SPI] SPI is stuck after soft restart from auto suspension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

After auto suspend is enabled, if caching is requested while Memory SPI is erasing flash, Memory SPI will automatically send a SUSPEND command (0×75). If there is a system reset, and Memory SPI is restarted before sending a RESUME command (0×7A), the state machine of Memory SPI will not be restored. As a result, the system cannot continue operations.

Workarounds
^^^^^^^^^^^

Disable auto suspend function.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
