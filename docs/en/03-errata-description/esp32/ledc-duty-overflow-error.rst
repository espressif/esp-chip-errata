[LEDC-3.12] When the LEDC Is in Decremental Fade Mode, a Duty Overflow Error May Occur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

This issue may happen when the LEDC is in decremental fade mode and LEDC_DUTY_SCALE_HSCH\ *n* is 1. If the duty is 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES`, then the next one should be 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES` – 1, however, the next duty is actually 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES+1`, which indicates a duty overflow error. (HSCH\ *n* refers to high-speed channel with *n* being 0-7; HSTIMER\ *x* refers to high-speed timer with *x* being 0-3.)

For low-speed channels, the same issue may also happen.

Workarounds
^^^^^^^^^^^

When using LEDC, avoid the concurrence of following three cases:

#. The LEDC is in decremental fade mode;
#. The scale register is set to 1;
#. The duty is 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES` or 2\ :sup:`LEDC_LSTIMER\ x\ \_DUTY_RES`.

Solution
^^^^^^^^

This issue is automatically worked around in the LEDC driver since the ESP-IDF commit ID `b2e264e <https://github.com/espressif/esp-idf/commit/b2e264ef52ae368b3b371bf6872fe29bd2b8b5df>`__ and is released in ESP-IDF v3.1.
