[GPIO-3.14] Within the Same Group of GPIO Pins, Edge Interrupts Cannot Be Used Together With Other Interrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

GPIO0 ~ GPIO31 share a set of interrupt configuration registers and belong to one group, GPIO32 ~ GPIO39 share another set of registers and belong to another group, and RTC GPIO0 ~ GPIO17 share yet another set of registers and belong to yet another group. If one GPIO pad within a group is configured with edge-triggered interrupt, then other interrupts (including both edge-triggered and level-triggered interrupts within that group cannot be configured.

There is no such limitation for level-triggered interrupts, which means, if there are no edgetriggered interrupts configured within a group, then there can be any number of leveltriggered interrupts in that group.

Reason
^^^^^^^^^^^

When the following three sets of STATUS/W1TS/W1TC registers for GPIOs are being operated, edge-triggered interrupts may not be properly triggered within the same group.

- When the following registers are being operated, edge-triggered interrupts for GPIO_STATUS_REG may not be properly triggered:

    - GPIO_STATUS_W1TS_REG
    - GPIO_STATUS_W1TC_REG
    - GPIO_STATUS_REG

- When the following registers are being operated, edge-triggered interrupts for GPIO_STATUS1_REG may not be properly triggered:

    - GPIO_STATUS1_W1TS_REG
    - GPIO_STATUS1_W1TC_REG
    - GPIO_STATUS1_REG

- When the following registers are being operated, edge-triggered interrupts for RTCIO_RTC_GPIO_STATUS_REG may not be properly triggered:

    - RTCIO_RTC_GPIO_STATUS_W1TS_REG
    - RTCIO_RTC_GPIO_STATUS_W1TC_REG
    - RTCIO_RTC_GPIO_STATUS_REG

Workarounds
^^^^^^^^^^^

Simulate edge-triggered interrupts using level-triggered interrupts, as outlined below.

To trigger a GPIO interrupt on a rising edge, follow the steps:

1. Set the GPIO interrupt type to high.
2. After the CPU services the interrupt, change the GPIO interrupt type to low. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine.

To trigger a GPIO interrupt on a falling edge, follow the steps:

1. Set the GPIO interrupt type to low.
2. After the CPU services the interrupt, change the GPIO interrupt type to high. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
