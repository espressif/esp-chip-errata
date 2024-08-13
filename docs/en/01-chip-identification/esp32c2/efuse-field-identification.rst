- EFUSE_BLK2_DATA1_REG[21:20]
- EFUSE_BLK2_DATA1_REG[19:16]

.. flat-table:: Chip Revision Identification by eFuse Bits
   :header-rows: 2
   :widths: 2 5 1 1 1

   * - :rspan:`1`
     - :rspan:`1` eFuse Bit
     - :cspan:`2` Chip Revision
   * - v0.0
     - v1.0
     - v1.1
   * - :rspan:`1` Major Number
     - EFUSE_BLK2_DATA1_REG[21]
     - 0
     - 0
     - 0
   * - EFUSE_BLK2_DATA1_REG[20]
     - 0
     - 1
     - 1
   * - :rspan:`3` Minor Number
     - EFUSE_BLK2_DATA1_REG[19]
     - 0
     - 0
     - 0
   * - EFUSE_BLK2_DATA1_REG[18]
     - 0
     - 0
     - 0
   * - EFUSE_BLK2_DATA1_REG[17]
     - 0
     - 0
     - 0
   * - EFUSE_BLK2_DATA1_REG[16]
     - 0
     - 0
     - 1
