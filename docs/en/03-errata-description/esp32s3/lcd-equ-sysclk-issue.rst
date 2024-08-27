[LCD] The LCD Module Exhibits Unreliable Behavior When Certain Clock Dividers Are Used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

1. When the RGB format is used, if the clock divider is set to 1, i.e., LCD_CAM_LCD_CLK_EQU_SYSCLK = 1:

  - The pixel clock output (LCD_PCLK) will not be able to be set to falling edge trigger.
  - When frames are continuously sent in this mode (i.e., LCD_CAM_LCD_NEXT_FRAME_EN = 1), it might occur that the second frame inserts the last data of the previous frame in the first frame.

2. When the I8080 format is used, if the clock cycle of the LCD core clock (LCD_CLK) before data transmission is less than or equal to 2, it can result in incorrect value of the first data and the subsequent data quantity.

  .. note::

    Please refer to the following steps to obtain the clock cycle before data transmission with the I8080 format.

    The clock cycle before data transmission depends on the following factors:

    - VFK cycle length (unit: LCD_PCLK): The clock cycle length during the VFK phase
    - CMD cycle length (unit: LCD_PCLK): The clock cycle length during the CMD phase
    - DUMMY cycle length (unit: LCD_PCLK): The clock cycle length during the DUMMY phase
    - LCD_CAM_LCD_CLK_EQU_SYSCLK: Decides if LCD_PCLK equals LCD_CLK
    - LCD_CAM_LCD_CLKCNT_N: Decides the division relationship between LCD_PCLK and LCD_CLK

    Based on the information above, three variables are defined below:

    - **total_pixels** = VFK cycle length + CMD cycle length + DUMMY cycle length
    - **cycle_unit** =

      - 1, if LCD_CAM_LCD_CLK_EQU_SYSCLK = 1
      - LCD_CAM_LCD_CLKCNT_N + 1, if LCD_CAM_LCD_CLK_EQU_SYSCLK = 0

    - **ahead_cycle** = **total_pixels** * **cycle_unit**

    **ahead_cycle** indicates the clock cycle before data transmission, which, if less than or equal to 2, will cause an error.

Workarounds
^^^^^^^^^^^

Users are suggested to do the followings:

- When using the RGB format, avoid configuring LCD_CAM_LCD_CLK_EQU_SYSCLK as 1.
- When using the I8080 format:

  - try to avoid configuring LCD_CAM_LCD_CLK_EQU_SYSCLK as 1.
  - ensure that **ahead_cycle** is larger than 2 if LCD_CAM_LCD_CLK_EQU_SYSCLK has to be set as 1.

This issue has been bypassed through the methods described above in ESP-IDF v4.4.5+, v5.0.3+, v5.1 and above.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
