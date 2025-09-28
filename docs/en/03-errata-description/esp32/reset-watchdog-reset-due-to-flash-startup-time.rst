[RES-3.8] Due to the Flash Start-up Time, a Spurious Watchdog Reset Occurs When ESP32 Is Powered up or Wakes up From Deepsleep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1

Description
^^^^^^^^^^^

If the ESP32 reads from the flash chip before it is ready, invalid data can cause booting to fail until a Watchdog Timer reset occurs. This can occur on power-on and on wake from Deep-sleep, if the ESP32 VDD_SDIO is used to power the flash chip.

Workarounds
^^^^^^^^^^^

1. Replace the flash chip with one with a fast start-up time (<800 μs from power-on to ready to read). This works around the issue for both power-on and wake from Deepsleep.
2. When waking from Deep-sleep, this issue is automatically worked around in ESP-IDF v2.0 and newer (the delay to wait can be configured if necessary). In this workaround, the CPU executes from RTC fast memory immediately after waking and a delay is added before continuing to read the program from flash.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v3.0`.
