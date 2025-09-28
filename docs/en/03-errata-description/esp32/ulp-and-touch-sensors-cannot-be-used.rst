[ULP-3.19] ULP Coprocessor And Touch Sensors Can Not Be Used In Deep-sleep Mode If RTC_PERIPH Power Domain Is Powered Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

The main operating clock for the ULP coprocessor and touch sensor is **FAST_CLK**. In **Deep-sleep** mode, if the **RTC_PERIH** power domain (RTC Peripherals) remains powered up, the ULP coprocessor and touch sensor will receive the wake-up signal earlier than the clock management module. This causes them to operate under **SLOW_CLK** for a period before switching to **FAST_CLK**, leading to inaccuracies in the operating clock. Therefore, in Deep-sleep mode, if RTC_PERIH is powered up, the ULP co-processor and touch sensor cannot be used.

Workarounds
^^^^^^^^^^^

If the user wants to utilize the ULP coprocessor and touch sensor functionalities, the RTC_PERIPH must remain powered down in Deep-sleep mode. Note that during this time, the **EXT0** wake-up is not available, as it only operates when RTC_PERIPH is powered up.

Users need to make a trade-off between using the EXT0 wake-up function and the ULP coprocessor and touch sensor functionalities:

- **If the EXT0 wake-up function is needed**: The RTC_PERIPH power domain must remain powered up, and the ULP coprocessor and touch sensor functionalities will not be available.
- **If the ULP coprocessor and touch sensor functionalities are needed**: The RTC_PERIPH must remain powered down, and the EXT0 wake-up function will not be available.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
