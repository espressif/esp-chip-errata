.. list-table:: 修订历史
   :header-rows: 1
   :widths: 2 1 7

   * - 日期
     - 版本
     - 发布说明
   * - 2025-10-11
     - v3.0
     - 更新勘误标题的大小写格式和勘误编号
   * - 2025-01-03
     - v2.9
     - - 更新章节 :doc:`/03-errata-description/esp32/ulp-and-touch-sensors-cannot-be-used`
   * - 2024-07-29
     - v2.8
     - - 新增章节 :doc:`/03-errata-description/esp32/clock-rmii-clock-when-using-ethernet-and-wifi`
   * - 2023-09-19
     - v2.7
     - - 新增章节 :doc:`/03-errata-description/shared/rtc-reg-read-error-from-light-sleep` 和 :doc:`/03-errata-description/esp32/cpu-subsequent-access-halted-when-get-interrupted`
       - 更新章节 :doc:`/03-errata-description/esp32/gpio-edge-interrupts` 和 :doc:`/03-errata-description/esp32/uart-fifo-cnt-indicates-data-length-incorrectly`
   * - 2023-02-02
     - v2.6
     - - 根据 `PCN <https://www.espressif.com/sites/default/files/pcn_downloads/PCN20221202%20Remove%20Hall%20Sensor%20from%20ESP32%20Series%20of%20Documentation.pdf>`_，删除章节 :doc:`/03-errata-description/esp32/gpio-inputs-pulled-down` 中的霍尔传感器
   * - 2022-11-23
     - v2.5
     - - 章节 :doc:`/03-errata-description/esp32/cpu-writes-lost` 增加寄存器 GPIO_OUT_W1TS_REG
   * - 2022-10-13
     - v2.4
     - - 新增芯⽚版本 v3.1 和 v1.1
       - 新增章节 :doc:`/03-errata-description/esp32/twai-rx-fifo-overruns` 和 :doc:`/03-errata-description/esp32/ulp-and-touch-sensors-cannot-be-used`
       - 重命名⽂档为“ESP32 系列芯⽚勘误表”
   * - 2020-09-25
     - v2.3
     - - 更新章节 :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces`， 添加对 UART FIFO 读操作的说明
   * - 2020-06-08
     - v2.2
     - - 增加章节 :doc:`/03-errata-description/esp32/uart-fifo-cnt-indicates-data-length-incorrectly` 和 :doc:`/03-errata-description/esp32/cpu-limitations-when-accessing-peripherals`
   * - 2020-05-14
     - v2.1
     - - 增加对章节 :doc:`/03-errata-description/esp32/reset-watchdog-reset-due-to-flash-startup-time` 的修复说明

.. list-table::
   :header-rows: 1
   :widths: 2 1 7

   * - 日期
     - 版本
     - 发布说明
   * - 2020-05-08
     - v2.0
     - - 增加章节 :doc:`/03-errata-description/esp32/watchdog-issue-caused-by-live-lock` 和 :doc:`/03-errata-description/esp32/cpu-limited-access-to-address-spaces`
       - 章节 :doc:`/03-errata-description/esp32/cpu-writes-lost` 增加一条说明
       - 更新章节 :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu` 中 A、B 地址空间范围，修正⼀处错误
   * - 2020-03-16
     - v1.9
     - - 更新表 :doc:`芯片丝印芯片版本标识 </01-chip-identification/esp32/chip-marking-identification>`，增加芯⽚版本 ECO V3
       - 增加对章节 :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-related-to-access-sequence` 和 :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu` 的修复说明
       - 增加章节 :doc:`/03-errata-description/esp32/twai-negative-phase-error` 和 :doc:`/03-errata-description/esp32/gpio-edge-interrupts`
       - 增加⽂档反馈链接
   * - 2018-12
     - v1.8
     - - 增加	“ESP32 TWAI 相关问题” 小节
   * - 2018-05
     - v1.7
     - - 增加章节 :doc:`/03-errata-description/esp32/ledc-duty-overflow-error`
   * - 2018-05
     - v1.6
     - - 整体更新
   * - 2018-02
     - v1.5
     - - 增加章节 :doc:`/03-errata-description/esp32/gpio-inputs-pulled-down`
   * - 2018-02
     - v1.4
     - - 修正章节 :doc:`/03-errata-description/esp32/cpu-writes-lost` 中前五个寄存器的名称⾥的笔误
   * - 2017-06
     - v1.3
     - - 增加章节 :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-related-to-access-sequence` 和 :doc:`/03-errata-description/esp32/cpu-read-error-of-dual-core-cpu`

.. list-table::
   :header-rows: 1
   :widths: 2 1 7

   * - 日期
     - 版本
     - 发布说明
   * - 2017-04
     - v1.2
     - - 修改章节 :doc:`/03-errata-description/esp32/reset-spurious-watchdog-reset` 中的描述
       - 增加章节 :doc:`/03-errata-description/esp32/reset-watchdog-reset-due-to-flash-startup-time`
   * - 2016-12
     - v1.1
     - - 修订章节 :doc:`/03-errata-description/esp32/cpu-read-and-write-errors-using-cache` 中的 MEMW 指令
   * - 2016-11
     - v1.0
     - - 首次发布
