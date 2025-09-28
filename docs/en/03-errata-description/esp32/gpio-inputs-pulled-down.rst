[GPIO-3.11] When Certain Rtc Peripherals Are Powered on, the Inputs of GPIO36 and GPIO39 Will Be Pulled Down for Approximately 80 ns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

Powering on the following RTC peripherals will trigger this issue:

- SAR ADC1
- SAR ADC2
- AMP

Workarounds
^^^^^^^^^^^

When enabling power for any of these peripherals, ignore input from GPIO36 and GPIO39.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
