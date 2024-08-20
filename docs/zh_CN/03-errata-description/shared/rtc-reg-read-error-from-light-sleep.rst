[RTC] 从 Light-sleep 模式唤醒后 RTC 电源域寄存器读取错误
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

.. only:: esp32s2

   .. tags::

      v0.0, v1.0


描述
^^^^

如果在 Light-sleep 模式下关闭 RTC 外设的电源，从 Light-sleep 模式唤醒后，{IDF_TARGET_NAME} 的 CPU 读取 RTC 电源域的寄存器时会有一定概率出错。

变通方法
^^^^^^^^

建议用户避免在 Light-sleep 模式下关闭 RTC 外设的电源，此时不会影响功耗。

.. only:: esp32s3

   在 ESP-IDF v4.4 及以上版本中已自动绕过该问题。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
