芯片版本标识
============

:link_to_translation:`en:[English]`

乐鑫引入了新的 **vM.X** 编号方案来表示芯片的修订版本。本指南概述了该编号方案的含义，并介绍了芯片版本的其他各类标识。


芯片版本编号
------------

乐鑫使用 **vM.X** 编码方式表示芯片版本 (Chip Revision)。

**M** – 主版本号，表示芯片修订的主要版本。该号码变更表示在旧版芯片上使用的软件与新版芯片不兼容，需要升级软件方可使用。

**X** – 次版本号，表示芯片修订的次要版本。该号码变更表示在旧版芯片上使用的软件与新版芯片兼容，无需升级软件。

**vM.X** 编码方式将取代旧的编码方式，包括 ECO 编码、Vxxx 编码等。


主要标识方式
------------

eFuse 位
++++++++

.. only:: not esp32

    芯片版本使用两个 eFuse 字段编码：

.. only:: esp32

    芯片版本使用四个 eFuse 字段编码：

.. include:: ./{IDF_TARGET_PATH_NAME}/efuse-field-identification.rst

.. _sec-chip-marking:

芯片标识
++++++++

- 芯片丝印的 **Espressif Tracking Information（乐鑫追踪信息）** 行

.. only:: not esp32p4

    .. figure:: ../../_static/chip-marking.png
        :align: center
        :scale: 32%
        :alt: 芯片丝印示意图

        芯片丝印示意图

.. only:: esp32p4

    .. figure:: ../../_static/chip-marking-p4.png
        :align: center
        :scale: 55%
        :alt: 芯片丝印示意图

        芯片丝印示意图

.. include:: ./{IDF_TARGET_PATH_NAME}/chip-marking-identification.rst

.. only:: not esp32p4

    模组标识
    ++++++++

    - 模组丝印的 **规格标识码** 行

      .. figure:: ../../_static/module-marking__CN.png
        :align: center
        :scale: 55%
        :alt: 模组丝印示意图

        模组丝印示意图

    .. include:: ./{IDF_TARGET_PATH_NAME}/module-marking-identification.rst


其他标识方式
------------

日期代码
++++++++

有些芯片错误不需要在晶圆片上修复，即不需要引入新的芯片版本。

此时，芯片可通过丝印中的 **Date Code（日期代码）** 来识别，如图 :ref:`sec-chip-marking`。更多信息，请参考 `{IDF_TARGET_NAME} 芯片包装信息 > 芯片丝印 <https://docs.espressif.com/projects/esp-packaging/zh_CN/latest/{IDF_TARGET_PATH_NAME}/01-marking/index_chip.html#id1>`__。

.. only:: not esp32p4

    生产工单
    ++++++++

    内置芯片的模组可通过物料标签中的 **生产工单 (PW Number)** 来识别，如图 :ref:`fig-PW-number`。更多信息，请参考 `{IDF_TARGET_NAME} 模组包装信息 > 披萨盒 <https://docs.espressif.com/projects/esp-packaging/zh_CN/latest/{IDF_TARGET_PATH_NAME}/03-tape-and-reel/index_module.html#id4>`__。

    .. _fig-PW-number:

    .. figure:: ../../_static/PW-number.png
        :align: center
        :scale: 37%
        :alt: 模组物料标签

        模组物料标签

    .. note::

        注意，仅装在铝箔袋中的模组卷盘含有 **生产工单 (PW Number)** 信息。


ESP-IDF 支持版本
----------------

关于特定芯片版本的 ESP-IDF 支持版本，请参考 `ESP-IDF 版本与乐鑫芯片版本兼容性 <https://github.com/espressif/esp-idf/blob/master/COMPATIBILITY_CN.md>`__。


相关文档
--------

-  更多关于芯片版本升级及识别系列产品版本的信息，请参考 `{IDF_TARGET_NAME} 产品/工艺变更通知 (PCN) <https://www.espressif.com/zh-hans/support/documents/pcns?keys={IDF_TARGET_NAME}>`__。

-  芯片版本的编码策略，请参考 `关于芯片版本 (Chip Revision) 编码方式的兼容性公告 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2022-005%20%E5%85%B3%E4%BA%8E%E8%8A%AF%E7%89%87%E7%89%88%E6%9C%AC%E7%BC%96%E7%A0%81%E6%96%B9%E5%BC%8F%20%28Chip%20Revision%29%20%E7%9A%84%E5%85%BC%E5%AE%B9%E6%80%A7%E5%85%AC%E5%91%8A.pdf>`__。
