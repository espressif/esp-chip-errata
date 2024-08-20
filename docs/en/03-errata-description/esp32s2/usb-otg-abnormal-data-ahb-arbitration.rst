[USB OTG]  Abnormal data during AHB bus arbitration by USB OTG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

When the USB OTG peripheral and some other competing peripherals (listed below) simultaneously execute a request on the Advanced High-performance Bus (AHB), the AHB may generate incorrect arbitration signals, which results in the USB OTG peripheral reading or writing erroneous data. The competing peripherals include:

* I2S
* SPI

Workarounds
^^^^^^^^^^^

1. Avoid AHB bus competition between USB OTG and above peripherals by not using DMA mode of USB OTG, or disabling DMA mode of above peripherals.
2. Avoid competing with the USB OTG’s AHB bus access. Specifically, set USB OTG’s AHB burst transfer mode to INCR to prevent competition from the other peripherals. In this mode, USB OTG will occupy the AHB bus exclusively until the burst transfer is completed.

.. note::
    Use the INCR burst mode with care, as it requires adjustment to maximum packet size (MPS) for USB OTG endpoints, so that burst time is smaller than the timeout period of the competing peripherals.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`. With this fix, the AHB bus will correctly arbitrate competing access.
ESP-IDF adds USB OTG support starting from v4.4. When the specific conditions listed below are met, ESP-IDF enables the INCR mode workaround, i.e., using the INCR mode to guarantee that the USB OTG’s exclusive access to the AHB. The conditions for ESP-IDF to enable this workaround are as follows:

1. For chip revision v0.0, ESP-IDF always enables the workaround.
2. ESP-IDF added support for chip revision v1.0 in ESP-IDF v4.4.6, v5.0.4, v5.1.2, and v5.2. In these and above version, the software automatically detects the chip revision. When chip revision v1.0 or later revisions are detected, ESP-IDF no longer enables the workaround.
3. In ESP-IDF versions that do not support chip revision v1.0, i.e., v4.4-v4.4.5, v5.0-v5.0.3, v5.1-v5.1.1, ESP-IDF always enables the workaround.
