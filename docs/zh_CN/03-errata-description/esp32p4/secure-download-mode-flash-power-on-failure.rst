[ROM-770] 安全下载模式下 flash 上电失败
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.1

描述
^^^^

为同时支持 1.8 V 和 3.3 V flash，{IDF_TARGET_NAME} 引入了一种电源控制机制：在 Joint Download 模式，PMU 默认不会为 flash 上电。在正常下载流程中，软件会先确定 flash 工作电压、更新 eFuse PXA0_TIEH_SEL_0 并配置相关寄存器（此序列已集成到 esptool 下载命令中），从而在烧录前为 flash 上电。

然而，ROM 包含一项安全下载功能。当通过 eFuse ENABLE_SECURITY_DOWNLOAD 启用此功能时，ROM 会拒绝寄存器读写命令，仅允许 flash 烧录。因此，软件无法配置 flash 电源控制寄存器，导致 flash 无法上电，进而使下载过程失败。

变通方法
^^^^^^^^

- 不启用 Secure Download 模式。

- 或在板级电路设计中，提供 flash 内部/外部供电切换方案，使 flash 在下载阶段可正常上电。如使用外部电源为 flash 供电，进入 sleep mode 前需切换回 flash 内部供电，否则会影响休眠功能。

解决方案
^^^^^^^^

预计将在 :bdg-warning:`下个芯片版本` 中修复。
