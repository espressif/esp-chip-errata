.. list-table:: Revision History
   :header-rows: 1
   :widths: 2 1 7

   * - Date
     - Version
     - Release Notes
   * - 2025-10-11
     - v3.0
     - Update errata titles capitalization and errata numbering
   * - 2025-01-03
     - v2.9
     - - Updated Section :doc:`/03-errata-description/esp32/ulp-and-touch-sensors-cannot-be-used`
   * - 2024-07-29
     - v2.8
     - - Added Section :doc:`/03-errata-description/esp32/clock-rmii-clock-when-using-ethernet-and-wifi`
   * - 2023-09-19
     - v2.7
     - - Added Sections :doc:`/03-errata-description/shared/rtc-reg-read-error-from-light-sleep` and :doc:`/03-errata-description/esp32/cpu-subsequent-access-halted-when-get-interrupted`
       - Updated Sections :doc:`/03-errata-description/esp32/gpio-edge-interrupts` and :doc:`/03-errata-description/esp32/uart-fifo-cnt-indicates-data-length-incorrectly`
   * - 2023-02-02
     - v2.6
     - - Removed hall sensor from Section :doc:`/03-errata-description/esp32/gpio-inputs-pulled-down` according to `PCN <https://www.espressif.com/sites/default/files/pcn_downloads/PCN20221202%20Remove%20Hall%20Sensor%20from%20ESP32%20Series%20of%20Documentation.pdf>`_
   * - 2022-11-23
     - v2.5
     - - Added register GPIO_OUT_W1TS_REG in Section :doc:`/03-errata-description/esp32/cpu-writes-lost`
   * - 2022-10-13
     - v2.4
     - - Added chip revision v3.1 and v1.1
       - Added Sections :doc:`/03-errata-description/esp32/twai-rx-fifo-overruns` and :doc:`/03-errata-description/esp32/ulp-and-touch-sensors-cannot-be-used`
       - Renamed this document as “ESP32 Series SoC Errata”
   * - 2020-09-25
     - v2.3
     - - Updated Section :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces` and provided more information about UART FIFO read operation
   * - 2020-06-08
     - v2.2
     - - Added Sections :doc:`/03-errata-description/esp32/uart-fifo-cnt-indicates-data-length-incorrectly` and :doc:`/03-errata-description/esp32/cpu-limitations-when-accessing-peripherals`
   * - 2020-05-14
     - v2.1
     - - Added a note of fix in Section :doc:`/03-errata-description/esp32/reset-watchdog-reset-due-to-flash-startup-time`

.. list-table::
   :header-rows: 1
   :widths: 2 1 7

   * - Date
     - Version
     - Release Notes
   * - 2020-05-08
     - v2.0
     - - Added Sections :doc:`/03-errata-description/esp32/watchdog-issue-caused-by-live-lock` and :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces`
       - Added a note in Section :doc:`/03-errata-description/esp32/cpu-writes-lost`
       - Updated the address ranges of space A and B in Section :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu` and fixed a typo
   * - 2020-03-16
     - v1.9
     - - Added chip revision 3 in Table :doc:`Chip Revision Identification by Chip Marking </01-chip-identification/esp32/chip-marking-identification>`
       - Added note of fixes in sections :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-related-to-access-sequence` and :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`
       - Added Sections :doc:`/03-errata-description/esp32/twai-negative-phase-error` and :doc:`/03-errata-description/esp32/gpio-edge-interrupts`
       - Added documentation feedback link
   * - 2018-12
     - v1.8
     - - Added Section “ESP32 TWAI Errata”
   * - 2018-05
     - v1.7
     - - Added Section :doc:`/03-errata-description/esp32/ledc-duty-overflow-error`
   * - 2018-05
     - v1.6
     - - Overall update
   * - 2018-02
     - v1.5
     - - Added Section :doc:`/03-errata-description/esp32/gpio-inputs-pulled-down`
   * - 2018-02
     - v1.4
     - - Corrected typos in the register names in Section :doc:`/03-errata-description/esp32/cpu-writes-lost`

.. list-table::
   :header-rows: 1
   :widths: 2 1 7

   * - Date
     - Version
     - Release Notes
   * - 2017-06
     - v1.3
     - - Added Sections :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-related-to-access-sequence` and :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`
   * - 2017-04
     - v1.2
     - - Changed the description of Section :doc:`/03-errata-description/esp32/reset-spurious-watchdog-reset`
       - Added Section :doc:`/03-errata-description/esp32/reset-watchdog-reset-due-to-flash-startup-time`
   * - 2016-12
     - v1.1
     - - Modified the MEMW command in Section :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-using-cache`
   * - 2016-11
     - v1.0
     - - First release
