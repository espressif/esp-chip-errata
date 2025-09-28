[CLK-3.7] Audio PLL 使用频率有限制
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

描述
^^^^

当配置 Audio PLL 频率时，不会用到配置寄存器 sdm0 和 sdm1，这样就限制了 PLL 频率可以配置的范围和精度。

芯片版本 v0.0 的 Audio PLL 频率公式如下：

.. math::

    f_{out} = \frac{f_{xtal} \times (sdm2 + 4)}{2 \times (odiv + 2)}

芯片版本 v1.0 及之后的 ESP32 芯片已修复此问题，Audio PLL 频率公式如下：

.. math::

    f_{out} = \frac{f_{xtal} \left(sdm2 + \frac{sdm1}{2^8} + \frac{sdm0}{2^{16}} + 4 \right)}{2 \times (odiv + 2)}

变通方法
^^^^^^^^

在 ESP-IDF v3.0 及更高版本中通过 I2S 驱动程序设置 Audio PLL 频率时，会自动考虑相关的频率公式。但是对于芯片版本 v0.0，Audio PLL 的使用频率仍然有限制。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.0` 中修复。
