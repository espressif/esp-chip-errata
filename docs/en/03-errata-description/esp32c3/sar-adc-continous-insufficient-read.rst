[ADC-270] SAR ADC Cannot Sample Sufficient Data in DMA Continuous Conversion Mode After Restart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c3

   .. tags::

      v0.0, v0.1, v0.2, v0.3, v0.4, v1.1

Description
^^^^^^^^^^^

In DMA continuous conversion mode, if the SAR ADC is stopped and then restarted, the internal hardware counter that counts ADC samples will not be automatically cleared, and there is no dedicated register to manually clear it.

Consequently, users might encounter scenarios such as:

- Garbled sampling results
- Samples fewer than the configured value

Workarounds
^^^^^^^^^^^

Before starting the ADC continuous conversion:

#. Reset the ADC by first setting and then clearing SYSTEM_APB_SARADC_RST
#. Sequentially configure the 16-bit APB_SARADC_APB_ADC_EOF_NUM field with all values ranging from the previously configured value down to 0, so as to clear the ADC sample counter

Note that this flow may take around 14 ms at most.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
