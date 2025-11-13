[ADC-305] Data Duplication May Occur When SAR ADC Accessing GDMA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

When the SAR ADC accesses the DMA, if the clock frequency of AHB_CLK and APB_CLK are different, multiple DMA access will be triggered. The number of repeated access is directly proportional to the frequency ratio, resulting in the same data being stored repeatedly and wasting storage space.

Workarounds
^^^^^^^^^^^

When using the SAR ADC, divide AHB_CLK by 1 to generate APB_CLK (configure the PCR_APB_DIV_NUM field to 0, which is the default value).

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v0.2`.
