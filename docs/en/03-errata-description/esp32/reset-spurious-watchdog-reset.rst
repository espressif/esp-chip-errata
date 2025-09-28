[RES-3.1] A Spurious Watchdog Reset Occurs When ESP32 Is Powered up or Wakes up From Deep-sleep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

Description
^^^^^^^^^^^

A spurious watchdog reset occurs when ESP32 is powered up or wakes up from Deep-sleep.

Workarounds
^^^^^^^^^^^

To work around the watchdog reset when waking from Deep-sleep, the CPU can execute a program from RTC fast memory. This program must clear the illegal access flag in the cache MMU as follows:

    1. Set the PRO_CACHE_MMU_IA_CLR bit in DPORT_PRO_CACHE_CTRL1_REG to 1.
    2. Clear this bit.

During initial power-up the spurious watchdog reset cannot be worked around, but ESP32 will boot normally after this reset.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
