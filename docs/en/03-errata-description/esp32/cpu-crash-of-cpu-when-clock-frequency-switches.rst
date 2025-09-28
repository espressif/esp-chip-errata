[CPU-3.5] The CPU Crashes When the Clock Frequency Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

Description
^^^^^^^^^^^

The CPU crashes when the clock frequency switches directly from 240 MHz to 80/160 MHz

Workarounds
^^^^^^^^^^^

When switching frequencies, use intermediate frequencies as follows:

    1. 2 MHz <-> 40 MHz <-> 80 MHz <-> 160 MHz
    2. 2 MHz <-> 40 MHz <-> 240 MHz

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
