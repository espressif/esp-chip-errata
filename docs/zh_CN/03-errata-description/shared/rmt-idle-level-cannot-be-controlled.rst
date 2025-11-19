[RMT-176] RMT 启用持续发送模式时，空闲信号电平可能出错
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0, v0.1, v0.2

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3

描述
^^^^

在 {IDF_TARGET_NAME} 的 RMT 模块中，如果启用了持续发送模式，那么预期发送通道在发送 RMT_TX_LOOP_NUM_CHn 次数据后会停止数据传输，之后空闲状态的信号电平应由结束标志中的 level 段决定。

但在实际数据传输中，停止数据传输后，通道空闲状态的信号电平并不由结束标志中的 level 段决定，而是由回卷数据携带的电平决定，最终的电平不能确定。

变通方法
^^^^^^^^

{IDF_TARGET_SUPPORT_VERSION:default="",esp32s3="v5.0",esp32c6="v5.1",esp32h2="v5.1",esp32p4="v5.2"}

建议用户置位 RMT_IDLE_OUT_EN_CHn，从而仅使用寄存器来控制空闲状态的信号电平。

从首个支持持续发送模式的 ESP-IDF 版本 ({IDF_TARGET_SUPPORT_VERSION}) 开始已自动绕过该问题。在这些版本的 ESP-IDF 中，空闲状态的信号电平只能由寄存器控制。

解决方案
^^^^^^^^

.. only:: not esp32h2 and not esp32p4

   :bdg-warning:`暂无` 修复计划。

.. only:: esp32h2

   已在芯片版本 :bdg-success:`v1.2` 中修复。

.. only:: esp32p4

   已在芯片版本 :bdg-success:`v3.0` 中修复。
