[System] Leakage current at the VDDA and VDD3P3_RTC pin during shutdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

When a chip is connected to the power supply, but the CHIP_PU pin is held low (meaning that the chip powers off), there will be a leakage current in the µA range at power pins such as VDDA and VDD3P3_RTC.

Workarounds
^^^^^^^^^^^

None.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
