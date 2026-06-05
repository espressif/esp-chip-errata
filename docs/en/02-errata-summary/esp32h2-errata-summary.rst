.. flat-table:: Errata summary
   :header-rows: 2
   :widths: 3 2 4 1 1 1

   * - :rspan:`1` Category
     - :rspan:`1` Errata No.
     - :rspan:`1` Descriptions
     - :cspan:`2` Affected Revisions
   * - v0.0
     - v0.1
     - v1.2
   * - RISC-V CPU
     - CPU-206
     - :doc:`../03-errata-description/shared/cpu-load-store`
     - Y
     - Y
     -
   * - Clock
     - CLK-6996
     - :doc:`../03-errata-description/shared/clock-rc-fast-clk-inaccurate`
     - Y
     - Y
     -
   * - :rspan:`1` SAR ADC
     - ADC-7227
     - :doc:`../03-errata-description/esp32h2/adc1-unavailable-channel-4`
     - Y
     - Y
     -
   * - ADC-1477
     - :doc:`../03-errata-description/esp32h2/sar-adc-missing-lower-four-bits`
     - Y
     - Y
     -
   * - I2C
     - I2C-308
     - :doc:`../03-errata-description/shared/i2c-fail-in-multiple-reads-operation`
     - Y
     - Y
     -
   * - SPI
     - SPI-304
     - :doc:`../03-errata-description/esp32h2/spi-auto-suspend`
     - Y
     - Y
     -
   * - LEDC
     - LEDC-253
     - :doc:`../03-errata-description/esp32h2/ledc-unable-to-rearch-100%-duty-cycle`
     - Y
     - Y
     -
   * - RMT
     - RMT-176
     - :doc:`../03-errata-description/shared/rmt-idle-level-cannot-be-controlled`
     - Y
     - Y
     -
   * - Chip Boot
     - BOOT-9537
     - :doc:`../03-errata-description/esp32h2/accidentally-enter-usb-boot-mode`
     - Y
     - Y
     -
   * - AES|XTS-AES
     - AES-11401
     - :doc:`../03-errata-description/esp32h2/aes-cpa-attack`
     - Y
     - Y
     -
   * - :rspan:`2` ECC|ECDSA_DS\ :sup:`1`
     - ECC-11400
     - :doc:`../03-errata-description/esp32h2/ecc-timing-attack`
     - Y
     - Y
     -
   * - ECDSA_DS-836
     - :doc:`../03-errata-description/shared/ecdsa-invalid-r-and-s-signature-accepted`
     -
     -
     - Y
   * - ECDSA_DS-837
     - :doc:`../03-errata-description/shared/ecdsa-invalid-s-signature-accepted`
     - Y
     - Y
     -
   * - 802.15.4
     - 802.15.4-9538
     - :doc:`../03-errata-description/esp32h2/tx-power-lower-than-expected`
     - Y
     - Y
     -
   * - PCNT
     - PCNT-249
     - :doc:`../03-errata-description/esp32h2/pcnt-fail-to-trigger-step-interrupt`
     - Y
     - Y
     - Y

\ :sup:`1` ECDSA_DS: ECDSA Digital Signature Peripheral.
