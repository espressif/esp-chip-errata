[LCD] LCD 模块在使用某些时钟分频器时行为不稳定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

描述
^^^^

1. 使用 RGB 格式时，如果时钟分频器设置为 1，即 LCD_CAM_LCD_CLK_EQU_SYSCLK = 1，则：

   -  LCD_PCLK 将无法设置为下降沿触发。
   -  在此模式下连续发送帧时（即 LCD_CAM_LCD_NEXT_FRAME_EN = 1），可能会出现第二帧在其首个帧插入上一帧最后一个数据的情况。

2. 使用 I8080 格式时，如果数据传输前 LCD_CLK 的时钟周期小于或等于 2，则可能导致第一个数据和后续数据量不准确。

  .. note::

    请参考下文获取 I8080 格式下数据传输前的时钟周期。

    数据传输前的时钟周期取决于以下因素：

    - VFK 周期长度（单位：LCD_PCLK）：VFK 阶段的时钟周期长度
    - CMD 周期长度（单位：LCD_PCLK）：CMD 阶段的时钟周期长度
    - DUMMY 周期长度（单位：LCD_PCLK）：DUMMY 阶段的时钟周期长度
    - LCD_CAM_LCD_CLK_EQU_SYSCLK：配置 LCD_PCLK 是否等于 LCD_CLK
    - LCD_CAM_LCD_CLKCNT_N：决定 LCD_PCLK 和 LCD_CLK 之间的分频关系

    基于上述信息，我们定义以下三个变量：

    - **total_pixels** = VFK 周期长度 + CMD 周期长度 + DUMMY 周期长度
    - **cycle_unit** =

      - 1（LCD_CAM_LCD_CLK_EQU_SYSCLK = 1 时）
      - LCD_CAM_LCD_CLKCNT_N + 1（LCD_CAM_LCD_CLK_EQU_SYSCLK = 0 时）

    - **ahead_cycle** = **total_pixels** * **cycle_unit**

    **ahead_cycle** 即为数据传输前的时钟周期，若该值小于或等于 2，则会产生错误。

变通方法
^^^^^^^^

建议用户：

- 使用 RGB 格式时，避免将 LCD_CAM_LCD_CLK_EQU_SYSCLK 配置为 1。
- 使用 I8080 格式时：

  - 尽量避免将 LCD_CAM_LCD_CLK_EQU_SYSCLK 配置为 1。
  - 如果必须将 LCD_CAM_LCD_CLK_EQU_SYSCLK 设置为 1，则需确保 **ahead_cycle** 大于 2。

在 ESP-IDF v4.4.5+、v5.0.3+、v5.1 及以上版本中已通过上述方法自动绕过该问题。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
