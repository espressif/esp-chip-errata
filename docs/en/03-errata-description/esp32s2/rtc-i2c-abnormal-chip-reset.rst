[RTC I2C] The falling edge of RTC_I2C_RESET triggers reset at low temperature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

At –40 °C, the chip will be restarted during wake-up.

Workarounds
^^^^^^^^^^^

None.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
