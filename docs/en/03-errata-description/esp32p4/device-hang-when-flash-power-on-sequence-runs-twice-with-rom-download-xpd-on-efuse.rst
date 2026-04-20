[ROM-816] Device Hang When Flash Power-On Sequence Runs Twice with ``rom_download_xpd_on eFuse``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.2

Description
^^^^^^^^^^^

To address the issue that, in Secure Download Mode on ESP32-P4 chip revision v3.1 and earlier versions, esptool cannot power on the flash, ESP32-P4 chip revision v3.2 introduces a new eFuse ``rom_download_xpd_on``. When this eFuse bit is programmed, the ROM automatically runs the flash power-on sequence during the download flow.

This power-on sequence must not run twice within the same power-on reset (POR) window; otherwise the ROM flow may fail to exit and the chip can hang.

Situations that can lead to the sequence running twice include:

- The ``rom_download_xpd_on`` eFuse is already programmed, but the host still sends a flash power-on sequence to the chip. A fixed esptool checks this eFuse bit when not in Secure Download Mode and only sends the automatic flash power-on sequence if the bit is not programmed, so this case is normally avoided.
- In Secure Download Mode, ``rom_download_xpd_on`` is programmed through the USB UART interface, followed by USB UART force download to flash firmware. Because a reset from USB UART is typically not a full POR, entering download again after reset can be equivalent to executing the flash power-on path twice within the same power-on context, which triggers the hang risk described above.

Workaround
^^^^^^^^^^

- Program the ``rom_download_xpd_on`` bit only when Secure Download Mode is actually required.
- If you use the USB UART interface for firmware download, perform a full POR before entering download after programming this eFuse bit.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
