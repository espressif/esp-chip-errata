[System] Random flash download failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

In download mode, the first stage bootloader in ROM receives serial data from two different input pins. Among the two intput pins, pin 24 DAC_2 (GPIO18) is not pulled up by default. If this pin is not pulled up in PCB design and is left floating, in download mode the first stage bootloader will not function properly (including download applications) due to interference.

Workarounds
^^^^^^^^^^^

This problem can be bypassed in PCB design by pulling up pin 24 DAC_2. The typical value of the pull-up resistor is 10 kΩ. All official development boards by Espressif pull this pin up, while official modules are not.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0` by pulling pin 24 up by default.
