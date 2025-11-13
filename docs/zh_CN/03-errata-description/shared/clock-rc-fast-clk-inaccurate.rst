[CLK-6996] RC_FAST_CLK 时钟无法校准
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{IDF_TARGET_XTAL_FREQ:default="",esp32c6="40 MHz",esp32h2="32 MHz"}

.. only:: esp32c6

   .. tags::

      v0.0

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

描述
^^^^

{IDF_TARGET_NAME} 芯片 RC_FAST_CLK 时钟源的频率过于接近参考时钟 ({IDF_TARGET_XTAL_FREQ} XTAL_CLK)，导致无法校准，用户无法获取 RC_FAST_CLK 的准确时钟频率，进而对使用 RC_FAST_CLK 且对其准确时钟频率要求较高的外设产生影响。

使用 RC_FAST_CLK 的外设，详见 *《{IDF_TARGET_NAME} 技术参考手册》 > 章节 复位和时钟* [`PDF <{IDF_TARGET_TRM_CN_URL}#resclk>`__]。

变通方法
^^^^^^^^

使用 RC_FAST_CLK 之外的其他时钟源。

解决方案
^^^^^^^^

.. only:: esp32c6

   已在芯片版本 :bdg-success:`v0.1` 中修复。

.. only:: esp32h2

   已在芯片版本 :bdg-success:`v1.2` 中修复。
