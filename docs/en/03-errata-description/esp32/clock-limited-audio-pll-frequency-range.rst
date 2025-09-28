[CLK-3.7] Audio Pll Frequency Range Is Limited
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

Description
^^^^^^^^^^^

When configuring the Audio PLL, configuration registers sdm0 & sdm1 are not used. This limits the range and precision of PLL frequencies which can be configured.

For chip revision v0.0, the Audio PLL frequency is calculated in hardware as follows:

.. math::

    f_{out} = \frac{f_{xtal} \times (sdm2 + 4)}{2 \times (odiv + 2)}

For chip revision v1.0 onwards this bug is fixed and the Audio PLL frequency is calculated in hardware as follows:

.. math::

    f_{out} = \frac{f_{xtal} \left(sdm2 + \frac{sdm1}{2^8} + \frac{sdm0}{2^{16}} + 4 \right)}{2 \times (odiv + 2)}

Workarounds
^^^^^^^^^^^

The particular hardware frequency calculation is automatically accounted for when setting Audio PLL frequency via the I2S driver in ESP-IDF v3.0 and newer. However, the range and precision of available Audio PLL frequencies is still limited when using chip revision v0.0.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.0`.
