.. flat-table:: 勘误表
   :header-rows: 2
   :widths: 1 1 6 1 1 1

   * - :rspan:`1` 类别
     - :rspan:`1` 勘误编号
     - :rspan:`1` 描述
     - :cspan:`2` 影响版本
   * - v0.0
     - v0.1
     - v0.2
   * - RISC-V CPU
     - CPU-206
     - :doc:`/03-errata-description/shared/cpu-load-store`
     - Y
     - Y
     -
   * - :rspan:`1` 时钟
     - CLK-6996
     - :doc:`/03-errata-description/shared/clock-rc-fast-clk-inaccurate`
     - Y
     -
     -
   * - CLK-8588
     - :doc:`/03-errata-description/esp32c6/clock-rc32k-not-oscillate`
     - Y
     - Y
     - Y
   * - 复位
     - RES-7080
     - :doc:`/03-errata-description/esp32c6/reset-rwdt-reset`
     - Y
     -
     -
   * - SPI
     - SPI-304
     - :doc:`/03-errata-description/esp32c6/spi-auto-suspend`
     - Y
     - Y
     -
   * - RMT
     - RMT-176
     - :doc:`/03-errata-description/shared/rmt-idle-level-cannot-be-controlled`
     - Y
     - Y
     - Y
   * - :rspan:`1` SAR ADC
     - ADC-305
     - :doc:`/03-errata-description/esp32c6/sar-adc-access-dma`
     - Y
     - Y
     -
   * - ADC-1477
     - :doc:`/03-errata-description/esp32c6/sar-adc-missing-lower-four-bits`
     - Y
     - Y
     -
   * - Wi-Fi
     - WIFI-9686
     - :doc:`/03-errata-description/esp32c6/wifi-ftm`
     - Y
     - Y
     -

..
  \ :sup:`1` Y* 表示版本的部分批次受到影响。
