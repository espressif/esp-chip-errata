[SPI-304] Enabling Flash Auto Suspend May Cause Abnormalities in Data Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

After the flash auto suspend feature is enabled, read operations on the SPI0 bus and erase/program operations on the SPI1 bus can be executed concurrently. When software performs erase or program operations on flash via SPI1, and the cache reads flash via SPI0 from time to time, if the erase or program operation is executed first, the expected request sequence is: **ERASE or PROGRAM > SUSPEND or WFI (wait for idle) > READ**.

In practice, when the erase or program operation is executed first, the request sequence is: **ERASE or PROGRAM > READ**, which may cause data read abnormalities and program execution issues.

Workarounds
^^^^^^^^^^^

Disable the auto suspend feature.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v0.2`.
