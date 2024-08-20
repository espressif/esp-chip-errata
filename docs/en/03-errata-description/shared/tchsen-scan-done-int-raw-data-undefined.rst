[Touch Sensor] The TOUCH_SCAN_DONE_INT Interrupt Raw Data Value Is Undefined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

.. only:: esp32s2

   .. tags::

      v0.0, v1.0

Description
^^^^^^^^^^^

For {IDF_TARGET_NAME}'s touch sensor, the raw data value is undefined for the first two TOUCH_SCAN_DONE_INT interrupts.

Workarounds
^^^^^^^^^^^

Users are suggested to skip the first two TOUCH_SCAN_DONE_INT interrupts, then turn them off and stop using them.

.. only:: esp32s2

   This issue has been bypassed in all versions of ESP-IDF through this method.

   This issue has been bypassed in the Touch Element component (touch_element) in ESP-IDF (introduced in ESP-IDF release version v4.3). If you are directly developing on the lower-level touch sensor driver, please follow the implementation provided within the Touch Element component and the recommendations mentioned above to bypass the issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
