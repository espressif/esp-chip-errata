[LEDC-3.12] LEDC 递减渐变，duty 值溢出错误
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^^^^^^

在配置 LEDC 为递减渐变且 LEDC_DUTY_SCALE_HSCH\ *n* 为 1 的情况下，当 duty 值为 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES` 时，下一次 duty 变化应该为 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES` – 1，但是实际上 duty 值等于 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES+1`\ ，即出现 duty 值溢出的错误。（HSCH\ *n* 代表高速通道，\ *n* 为 0-7；HSTIMER\ *x* 代表高速定时器，\ *x* 为 0-3。）

对于低速通道，存在同样的问题。

变通方法
^^^^^^^^

使用 LEDC 的过程中，应避免以下三个条件同时成立：

#. LEDC 启动递减渐变功能；
#. LEDC 渐变过程中 scale 寄存器设置为 1；
#. LEDC 递减渐变开始时刻或者过程中的某一时刻，duty 值为 2\ :sup:`LEDC_HSTIMER\ x\ \_DUTY_RES` 或 2\ :sup:`LEDC_LSTIMER\ x\ \_DUTY_RES`\。

解决方案
^^^^^^^^^^^^

此问题在 ESP-IDF commit ID 为 `b2e264e <https://github.com/espressif/esp-idf/commit/b2e264ef52ae368b3b371bf6872fe29bd2b8b5df>`__ 及以后版本的 LEDC 驱动中已自动绕过，并于 ESP-IDF v3.1 中发布。
