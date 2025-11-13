[ADC-7227] Unavailable Channel 4 in SRA ADC1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

Channel 4 (ADC1_CH4) of ADC1 is not operational in the {IDF_TARGET_NAME} chip.

Workarounds
^^^^^^^^^^^

Use other channels instead of ADC1_CH4.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.
