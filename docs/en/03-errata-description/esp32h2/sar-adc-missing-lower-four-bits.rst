[ADC-1477] Loss of Precision in Lower Four Bits of SAR ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

The lower four bits of the SAR ADC data bits are missing, causing a loss of precision in the corresponding bits.

Workarounds
^^^^^^^^^^^

No workaround.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.
