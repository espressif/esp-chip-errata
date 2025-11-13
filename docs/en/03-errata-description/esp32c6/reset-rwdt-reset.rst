[RES-7080] System Reset Triggered by RTC Watchdog Timer Cannot Be Correctly Reported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0

Description
^^^^^^^^^^^

When the RTC watchdog timer (RWDT) triggers a system reset, the reset source code can not be latched correctly. As a result, the reset cause reported is indeterminate and might be wrong.

Workarounds
^^^^^^^^^^^

No workaround.


Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v0.1`.
