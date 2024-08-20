[Touch Sensor] The scan done interrupt RTC_CNTL_TOUCH_SCAN_DONE_INT_ENA occurs twice during a single scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0, v1.0

Description
^^^^^^^^^^^

The touch sensor of {IDF_TARGET_NAME} triggered the scan done interrupt RTC_CNTL_TOUCH_SCAN_DONE_INT_ENA twice during a single scan, occurring when scanning the last two channels.

Workarounds
^^^^^^^^^^^

Users are suggested to register one more interrupt in the RTC driver to filter, checking if the current measuring channel is the last channel. If it is not the last channel, then clear the RTC_CNTL_TOUCH_SCAN_DONE_INT_ENA interrupt directly. If it is, then the current RTC_CNTL_TOUCH_SCAN_DONE_INT_ENA interrupt can be regarded as a valid interrupt.
This issue has been bypassed in all versions of ESP-IDF through this method.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
