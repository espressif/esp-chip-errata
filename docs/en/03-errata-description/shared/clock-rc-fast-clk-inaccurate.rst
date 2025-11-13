[CLK-6996] Inaccurate Calibration of RC_FAST_CLK Clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{IDF_TARGET_XTAL_FREQ:default="",esp32c6="40 MHz",esp32h2="32 MHz"}

.. only:: esp32c6

   .. tags::

      v0.0

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

In the {IDF_TARGET_NAME} chip, the frequency of the RC_FAST_CLK clock source is too close to the reference clock ({IDF_TARGET_XTAL_FREQ} XTAL_CLK) frequency, making it impossible to calibrate accurately. This may affect peripherals that use RC_FAST_CLK and have stringent requirements for its accurate clock frequency.

For peripherals using RC_FAST_CLK, please refer to *{IDF_TARGET_NAME} Technical Reference Manual > Chapter Reset and Clock* [`PDF <{IDF_TARGET_TRM_EN_URL}#resclk>`__].

Workarounds
^^^^^^^^^^^

Use other clock sources instead of RC_FAST_CLK.

Solution
^^^^^^^^

.. only:: esp32c6

   Fixed in chip revision :bdg-success:`v0.1`.

.. only:: esp32h2

   Fixed in chip revision :bdg-success:`v1.2`.
