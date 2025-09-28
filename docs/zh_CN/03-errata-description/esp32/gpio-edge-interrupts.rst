[GPIO-3.14] 同一组 GPIO 管脚内，边沿中断不能和其他中断一起使用
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

在中断配置寄存器上，GPIO0~31 共用一组寄存器，GPIO32~39 共用一组寄存器，RTC GPIO0~17 共用另一组寄存器。在同一组内，如果某一管脚被配置为边沿中断，那么其他中断（包括边沿中断和电平中断）将不可用。

电平中断没有此限制，即一组内如果没有沿中断，则可以有多组电平中断。

原因
^^^^

GPIO 的以下三组 STATUS/W1TS/W1TC 寄存器操作的同时，可能造成同一组内边沿中断无法正常触发。具体为：

- 以下寄存器的操作可能造成 GPIO_STATUS_REG 的边沿中断无法正常触发：

   - GPIO_STATUS_W1TS_REG
   - GPIO_STATUS_W1TC_REG
   - GPIO_STATUS_REG

- 以下寄存器的操作可能造成 GPIO_STATUS1_REG 的边沿中断无法正常触发：

   - GPIO_STATUS1_W1TS_REG
   - GPIO_STATUS1_W1TC_REG
   - GPIO_STATUS1_REG

-  以下寄存器的操作可能造成 RTCIO_RTC_GPIO_STATUS_REG 的边沿中断无法正常触发：

   - RTCIO_RTC_GPIO_STATUS_W1TS_REG
   - RTCIO_RTC_GPIO_STATUS_W1TC_REG
   - RTCIO_RTC_GPIO_STATUS_REG

变通方法
^^^^^^^^

使用电平中断模拟边沿中断，具体如下：

要实现 GPIO 的上升沿中断，按照下面的步骤进行配置：

1. 配置 GPIO 的中断类型为高；
2. CPU 的中断服务响应后，把 GPIO 的中断类型改为低。此时会发生第二次中断，需要 CPU 忽略这次中断服务程序。

要实现 GPIO 的下降沿中断，按照下面的步骤进行配置：

1. 配置 GPIO 的中断类型为低；
2. CPU 的中断服务响应后，把 GPIO 的中断类型改为高。此时会发生第二次中断，需要 CPU 忽略这次中断服务程序。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
