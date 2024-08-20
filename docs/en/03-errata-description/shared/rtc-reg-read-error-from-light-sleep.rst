[RTC] RTC Register Read Error After Wake-up from Light-sleep Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

.. only:: esp32s2

   .. tags::

      v0.0, v1.0

Description
^^^^^^^^^^^

If an RTC peripheral is turned off in Light-sleep mode, there is a certain probability that after waking up from Light-sleep, the CPU of {IDF_TARGET_NAME} will read the registers in the RTC power domain incorrectly.

Workarounds
^^^^^^^^^^^

Users are suggested not to power down RTC peripherals in Light-sleep mode. There will be no impact on power consumption.

.. only:: esp32s3

   This issue has been bypassed in ESP-IDF v4.4 and above.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
