[RES-3.1] 芯片上电或 Deep-sleep 醒来后，会随机发生一次看门狗复位
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

描述
^^^^

芯片上电或 Deep-sleep 醒来后，会随机发生一次看门狗复位。

变通方法
^^^^^^^^

Deep-sleep 醒来后，CPU 可以立即执行 RTC fast memory 中的一段程序。RTC fast memory 中的这段程序通过清除 cache MMU 的非法访问标志从而绕过 Deep-sleep 醒来后的看门狗复位，具体为：

    1. 将 DPORT_PRO_CACHE_CTRL1_REG 寄存器的 PRO_CACHE_MMU_IA_CLR 比特置 1。
    2. 将该比特清零。

芯片上电的看门狗复位无法使用软件绕过，但复位后 ESP32 正常启动。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.0` 中修复。
