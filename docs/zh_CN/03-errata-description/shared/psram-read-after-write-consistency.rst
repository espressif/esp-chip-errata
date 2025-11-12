[CPU-718] PSRAM 先写后读一致性问题
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c5

   .. tags::

      v0.0, v0.1, v1.0

.. only:: esp32c61

   .. tags::

      v0.0, v0.1, v0.2, v1.0

描述
^^^^^^^^^^^

当 CPU 通过 CACHE 或 DMA 对 PSRAM 进行随机读写时，如果满足以下任一条件，可能会出现 CPU 访问 PSRAM 的数据一致性问题：

- PSRAM 加密或解密已启用，或
- 通过 DMA 访问 PSRAM 时，AHB_DMA_OUT_DATA_BURST_MODE_SEL_CHn 配置为 0 或 1

原因
"""""

MSPI 硬件负责管理 CPU 对 PSRAM 的读写请求，并且内部存在缓存。因此，MSPI 接收到的 CPU 读写请求并不一定会立即作为 SPI 事务提交到 PSRAM。

如果 CPU 在很短时间内先对某一 PSRAM 物理地址执行写操作，又立即对相同地址执行读操作，先发出的写操作可能因 MSPI 内部缓存或加解密延迟而尚未完成；结果 MSPI 可能先执行后发出的读操作，导致读取到过期或不一致的数据。

示例
""""""""

- 当 CACHE 从启用加解密的 PSRAM 区间读取且发生 cache miss 时，回写的数据可能不一致。
- 在 DMA 写入 PSRAM 完成后，随即进行的 DMA 读或 CACHE 读同一 PSRAM 区域可能返回不一致的数据。

变通方法
^^^^^^^^^^^

- 针对因加解密导致的 cache miss 引起的数据一致性问题：在存在随机读写访问的场景下，不建议启用 PSRAM 加密功能。
- 针对 CPU 通过 DMA 访问时出现的数据一致性问题：在 DMA 写入完成后，或在 CPU 读取相同物理地址之前，增加延时，以确保 MSPI 已实际完成对 PSRAM 的写入操作。

解决方案
^^^^^^^^

.. only:: esp32c5 or esp32c61

   预计将在 :bdg-warning:`下个芯片版本` 中修复。
