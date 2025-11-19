[ROM-770] Secure Download Mode Flash Power-On Failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.1

Description
^^^^^^^^^^^

To support both 1.8 V and 3.3 V flash, {IDF_TARGET_NAME} introduces a power-control mechanism in which, in Joint Download Boot Mode, the PMU does not power on the flash by default. In the normal download flow, software determines the flash operating voltage, updates eFuse PXA0_TIEH_SEL_0, and configures the related registers (this sequence is integrated into the esptool download command) to power on the flash before programming.

However, the ROM includes a Secure Download feature. When this feature is enabled via the eFuse ENABLE_SECURITY_DOWNLOAD, the ROM rejects register read/write commands and only allows flash programming operations. As a result, software has no opportunity to configure the flash power-control registers, preventing the flash from being powered on and causing the download process to fail.

Workaround
^^^^^^^^^^

- Do not enable Secure Download Mode.

- Alternatively, provide a board-level mechanism to switch between internal and external flash power to ensure the flash is powered during download. Note that continuous external flash power may affect some IDF features, for example, the flash may not be able to power down in sleep mode. Therefore, it is recommended to switch back to internal flash power before entering sleep mode.

Solution
^^^^^^^^

.. only:: esp32p4

   To be fixed in the :bdg-warning:`next chip revision`.
