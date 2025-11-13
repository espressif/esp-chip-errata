[CLK-8588] 32 kHz 内部慢速 RC 振荡器可能无法正常振动
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::

      v0.0, v0.1, v0.2

描述
^^^^

32 kHz 内部慢速 RC 振荡器 RC32K_CLK 在低温场景下可能无法正常振动，导致依赖该时钟的模块无法正常工作。

使用 RC32K_CLK 的模块，详见 *《{IDF_TARGET_NAME} 技术参考手册》 > 章节 复位和时钟* [`PDF <{IDF_TARGET_TRM_CN_URL}#resclk>`__]。

变通方法
^^^^^^^^

使用 136 kHz 内部慢速 RC 振荡器 RC_SLOW_CLK。更多信息，请参考 `AR2024-011 关于 ESP32-C6 内部 32kHz RC 振荡器时钟源使用说明及通过 OTA 更改系统慢速时钟源的注意事项 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2024-011_Usage_Instructions_for_Internal_32kHz_RC_Oscillator_Clock_Source_in_ESP32-C6_and_Precautions_for_Changing_the_System_Slow_Clock_Source_via_OTA_cn.pdf>`__。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
