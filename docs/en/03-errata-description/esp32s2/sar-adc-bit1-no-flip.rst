[SAR ADC] Bit 1 of SAR ADC does not flip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s2

   .. tags::

      v0.0

Description
^^^^^^^^^^^

Bit 1 of SAR ADC is always 0, and does not change with measured voltage.

Workarounds
^^^^^^^^^^^

None.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`. The effective resolution of SAR ADC on chip revision v1.0 is changed from 13 bits to 12 bits. That is, bit 0 is not valid, and the valid bits are bit 1 ∼ bit 12 inclusive.
