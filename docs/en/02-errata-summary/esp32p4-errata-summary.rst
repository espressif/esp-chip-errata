.. flat-table:: Errata summary
   :header-rows: 2
   :widths: 1 1 6 1 1 1 1 1 1

   * - :rspan:`1` Category
     - :rspan:`1` Errata No.
     - :rspan:`1` Descriptions
     - :cspan:`5` Affected Revisions
   * - v0.0
     - v1.0
     - v1.3
     - v3.0
     - v3.1
     - v3.2
   * - RMT
     - RMT-176
     - :doc:`/03-errata-description/shared/rmt-idle-level-cannot-be-controlled`
     - Y
     - Y
     - Y
     -
     -
     -
   * - I2C
     - I2C-308
     - :doc:`/03-errata-description/shared/i2c-fail-in-multiple-reads-operation`
     - Y
     - Y
     - Y
     -
     -
     -
   * - MSPI
     - MSPI-749
     - :doc:`/03-errata-description/esp32p4/load-access-fault-during-power-on-or-deepsleep-wakeup`
     -
     -
     -
     - Y
     -
     -
   * - MSPI
     - MSPI-750
     - :doc:`/03-errata-description/esp32p4/unaligned-dma-read-operations-may-return-old-data-when-accessing-overlapping-addresses`
     -
     -
     -
     - Y
     -
     -
   * - MSPI
     - MSPI-751
     - :doc:`/03-errata-description/esp32p4/data-errors-caused-by-asynchronous-timing-issues-in-the-mspi-address-overlap-detection-function`
     -
     -
     -
     - Y
     -
     -
   * - ROM
     - ROM-764
     - :doc:`/03-errata-description/esp32p4/secure-boot-buffer-address-error-in-rom`
     -
     -
     -
     - Y
     -
     -
   * - Analog
     - Analog-765
     - :doc:`/03-errata-description/esp32p4/output-regulators-cannot-generate-a-reliable-supply-when-peripheral-power-domain-is-off`
     -
     -
     -
     - Y
     -
     -
   * - DMA
     - DMA-767
     - :doc:`/03-errata-description/esp32p4/mem-to-mem-channel0-permission-conflict-due-to-shared-transaction-ID`
     -
     -
     -
     - Y
     -
     -
   * - APM
     - APM-560
     - :doc:`/03-errata-description/esp32p4/unauthorized-ahb-access-may-block-subsequent-psram-or-flash-transactions`
     - Y
     - Y
     - Y
     - Y
     -
     -
   * - ROM
     - ROM-770
     - :doc:`/03-errata-description/esp32p4/secure-download-mode-flash-power-on-failure`
     -
     -
     -
     -
     - Y
     -
   * - ROM
     - ROM-816
     - :doc:`/03-errata-description/esp32p4/device-hang-when-flash-power-on-sequence-runs-twice-with-rom-download-xpd-on-efuse`
     -
     -
     -
     -
     -
     - Y

..
  \ :sup:`1` Y* means some batches of a revision are affected.
