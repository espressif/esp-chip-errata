[CLK-8588] 32 kHz Internal Slow RC Oscillator May Fail to Oscillate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

The 32 kHz internal slow RC oscillator (RC32K_CLK) may fail to oscillate in low-temperature scenarios, leading to malfunction in modules that rely on this clock.

For modules using RC32K_CLK, please refer to the *{IDF_TARGET_NAME} Technical Reference Manual > Chapter Reset and Clock* [`PDF <{IDF_TARGET_TRM_EN_URL}#resclk>`__].

Workarounds
^^^^^^^^^^^

Use the 136 kHz internal slow RC oscillator (RC_SLOW_CLK). For more information, please refer to `AR2024-011 Usage Instructions for Internal 32kHz RC Oscillator Clock Source in ESP32-C6 and Precautions for Changing the System Slow Clock Source via OTA <https://www.espressif.com/sites/default/files/advisory_downloads/AR2024-011_Usage_Instructions_for_Internal_32kHz_RC_Oscillator_Clock_Source_in_ESP32-C6_and_Precautions_for_Changing_the_System_Slow_Clock_Source_via_OTA_en.pdf>`__.

Solution
^^^^^^^^^

:bdg-warning:`No fix` scheduled.
