[SPI-855] Flash Boot Fails at 1.8 V VDD_SPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s31

   .. tags::

      v0.0

Description
^^^^^^^^^^^

The voltage corresponding to the default value of EXT_LDO_DREF is not 1.8 V, and the chip cannot boot from flash under 1.8 V VDD_SPI conditions.

Workaround
^^^^^^^^^^

Boot from flash using 3.3 V VDD_SPI.

Solution
^^^^^^^^

To be fixed in the :bdg-warning:`next chip revision`.
