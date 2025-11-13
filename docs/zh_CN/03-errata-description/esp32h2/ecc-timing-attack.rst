[ECC-11400] 涉及时间分析攻击的安全漏洞
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

描述
^^^^

ECC 执行点乘运算时，不同乘数的计算时间存在差异，因此 ECC 外设未能以恒定时间运行，导致其易受时间分析攻击。

变通方法
^^^^^^^^

在 ECC 驱动中随机化功耗特征，使其成为恒定时间。注意，使用这一方法时，必须启用安全启动模式。

ESP-IDF 已在以下版本中自动绕过该问题：

.. flat-table:: ESP-IDF 发布版本
   :header-rows: 1
   :widths: 2 2

   * - ESP-IDF Release 分支
     - 已发布版本
   * - release/v5.4 及以上
     - `v5.4 <https://github.com/espressif/esp-idf/releases/tag/v5.4>`_
   * - release/v5.3
     - `v5.3.2 <https://github.com/espressif/esp-idf/releases/tag/v5.3.2>`_
   * - release/v5.2
     - `v5.2.5 <https://github.com/espressif/esp-idf/releases/tag/v5.2.5>`_
   * - release/v5.1
     - `v5.1.5 <https://github.com/espressif/esp-idf/releases/tag/v5.1.5>`_

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.2` 中修复。芯片版本 v1.2 中引入恒时恒功耗模式。ECC 加速器在每次进行点乘计算时均会消耗相同的时间，消耗相同的功耗。
