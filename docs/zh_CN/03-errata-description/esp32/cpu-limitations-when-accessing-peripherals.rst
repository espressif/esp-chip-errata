[CPU-3.18] CPU 访问不同版本芯片的外设寄存器存在限制
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

由于 :doc:`/03-errata-description/esp32/cpu-writes-lost`、:doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu` 和 :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces` 章节描述的原因，在不同芯片版本中，CPU 使用 0x3FF0_0000 ~ 0x3FF1_EFFF、0x3FF4_0000 ~ 0x3FF7_FFFF 和 0x6000_0000 ~ 0x6003_FFFF 地址访问外设寄存器时需注意：

.. flat-table::
   :header-rows: 2
   :widths: 2 2 1 1 1 1 1 1

   * - :rspan:`1` 地址空间（总线）
     - :rspan:`1` 寄存器类型
     - :rspan:`1` 操作
     - :cspan:`4` 芯片版本
   * - v0.0
     - v1.0
     - v1.1
     - v3.0
     - v3.1
   * - :rspan:`3` 0x3FF0_0000 ~ 0x3FF1_EFFF 和 0x3FF4_0000 ~ 0x3FF7_FFFF (DPORT)
     - :rspan:`1` Non- FIFO
     - 写
     - :cspan:`2` Yes
     - :cspan:`1` Yes
   * - 读
     - :cspan:`2` No （详见 :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`）
     - :cspan:`1` Yes
   * - :rspan:`1` FIFO
     - 写
     - No （详见 :doc:`/03-errata-description/esp32/cpu-writes-lost`）
     - :cspan:`3` Yes
   * - 读
     - Yes
     - :cspan:`3` Yes
   * - :rspan:`3` 0x6000_0000 ~ 0x6003_FFFF (AHB)
     - :rspan:`1` Non- FIFO
     - 写
     - :cspan:`4` Yes
   * - 读
     - :cspan:`4` Yes
   * - :rspan:`1` FIFO
     - 写
     - :cspan:`4` Yes
   * - 读
     - :cspan:`4` No （无此功能，无法预知结果）

.. note::

    - Yes: 操作正确执行
    - No: 操作失败
