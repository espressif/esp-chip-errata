[ADC-183] The Digital Controller (DMA) of SAR ADC2 Cannot Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c3

   .. tags::

      v0.0, v0.1, v0.2, v0.3, v0.4, v1.1

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

The Digital Controller of SAR ADC2, i.e., DIG ADC2 controller, may receive a false sampling enable signal. In such a case, the controller will enter an inoperative state.

Workarounds
^^^^^^^^^^^

.. only:: esp32c3

    It is suggested to use SAR ADC1.

.. only:: esp32s3

    It is suggested to use RTC controller to control SAR ADC2.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
