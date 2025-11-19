All Errata Descriptions
=======================

:link_to_translation:`zh_CN:[中文]`

.. only:: esp32c3

    .. only:: html

        .. include:: shared/sar-adc-adc2-not-work.rst
        .. include:: {IDF_TARGET_PATH_NAME}/sar-adc-continous-insufficient-read.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/sar-adc-adc2-not-work
            {IDF_TARGET_PATH_NAME}/sar-adc-continous-insufficient-read

.. only:: esp32c6

    .. only:: html

        .. include:: shared/cpu-load-store.rst
        .. include:: shared/clock-rc-fast-clk-inaccurate.rst
        .. include:: {IDF_TARGET_PATH_NAME}/clock-rc32k-not-oscillate.rst
        .. include:: {IDF_TARGET_PATH_NAME}/reset-rwdt-reset.rst
        .. include:: {IDF_TARGET_PATH_NAME}/spi-auto-suspend.rst
        .. include:: shared/rmt-idle-level-cannot-be-controlled.rst
        .. include:: {IDF_TARGET_PATH_NAME}/sar-adc-access-dma.rst
        .. include:: {IDF_TARGET_PATH_NAME}/sar-adc-missing-lower-four-bits.rst
        .. include:: {IDF_TARGET_PATH_NAME}/wifi-ftm.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/cpu-load-store
            shared/clock-rc-fast-clk-inaccurate
            {IDF_TARGET_PATH_NAME}/clock-rc32k-not-oscillate
            {IDF_TARGET_PATH_NAME}/reset-rwdt-reset
            {IDF_TARGET_PATH_NAME}/spi-auto-suspend
            shared/rmt-idle-level-cannot-be-controlled
            {IDF_TARGET_PATH_NAME}/sar-adc-access-dma
            {IDF_TARGET_PATH_NAME}/sar-adc-missing-lower-four-bits
            {IDF_TARGET_PATH_NAME}/wifi-ftm

.. only:: esp32s3

    .. only:: html

        .. include:: {IDF_TARGET_PATH_NAME}/cache-hit-error-during-writeback.rst
        .. include:: shared/rtc-reg-read-error-from-light-sleep.rst
        .. include:: {IDF_TARGET_PATH_NAME}/analog-power-config-might-damage-chip.rst
        .. include:: {IDF_TARGET_PATH_NAME}/lcd-equ-sysclk-issue.rst
        .. include:: {IDF_TARGET_PATH_NAME}/usb-otg-download-func-bug.rst
        .. include:: shared/rmt-idle-level-cannot-be-controlled.rst
        .. include:: shared/tchsen-scan-done-int-raw-data-undefined.rst
        .. include:: shared/sar-adc-adc2-not-work.rst

    .. only:: latex

        .. toctree::
            :hidden:

            {IDF_TARGET_PATH_NAME}/cache-hit-error-during-writeback
            shared/rtc-reg-read-error-from-light-sleep
            {IDF_TARGET_PATH_NAME}/analog-power-config-might-damage-chip
            {IDF_TARGET_PATH_NAME}/lcd-equ-sysclk-issue
            {IDF_TARGET_PATH_NAME}/usb-otg-download-func-bug
            shared/rmt-idle-level-cannot-be-controlled
            shared/tchsen-scan-done-int-raw-data-undefined
            shared/sar-adc-adc2-not-work

.. only:: esp32h2

    .. only:: html

        .. include:: ./shared/cpu-load-store.rst
        .. include:: ./shared/clock-rc-fast-clk-inaccurate.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/adc1-unavailable-channel-4.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/sar-adc-missing-lower-four-bits.rst
        .. include:: ./shared/i2c-fail-in-multiple-reads-operation.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/spi-auto-suspend.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/ledc-unable-to-rearch-100%-duty-cycle.rst
        .. include:: ./shared/rmt-idle-level-cannot-be-controlled.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/accidentally-enter-usb-boot-mode.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/aes-cpa-attack.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/ecc-timing-attack.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/tx-power-lower-than-expected.rst
        .. include:: ./{IDF_TARGET_PATH_NAME}/pcnt-fail-to-trigger-step-interrupt.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/cpu-load-store
            shared/clock-rc-fast-clk-inaccurate
            {IDF_TARGET_PATH_NAME}/adc1-unavailable-channel-4
            {IDF_TARGET_PATH_NAME}/sar-adc-missing-lower-four-bits
            ./shared/i2c-fail-in-multiple-reads-operation.rst
            ./{IDF_TARGET_PATH_NAME}/spi-auto-suspend.rst
            ./{IDF_TARGET_PATH_NAME}/ledc-unable-to-rearch-100%-duty-cycle.rst
            ./shared/rmt-idle-level-cannot-be-controlled.rst
            ./{IDF_TARGET_PATH_NAME}/accidentally-enter-usb-boot-mode.rst
            ./{IDF_TARGET_PATH_NAME}/aes-cpa-attack.rst
            ./{IDF_TARGET_PATH_NAME}/ecc-timing-attack.rst
            ./{IDF_TARGET_PATH_NAME}/tx-power-lower-than-expected
            ./{IDF_TARGET_PATH_NAME}/pcnt-fail-to-trigger-step-interrupt.rst

.. only:: esp32c2

    .. only:: html

        .. include:: {IDF_TARGET_PATH_NAME}/crystal-40mhz-not-work.rst

    .. only:: latex

        .. toctree::
            :hidden:

            {IDF_TARGET_PATH_NAME}/crystal-40mhz-not-work


.. only:: esp32s2

    .. only:: html

        .. include:: {IDF_TARGET_PATH_NAME}/system-current-leakage-at-pins.rst
        .. include:: {IDF_TARGET_PATH_NAME}/system-random-flash-download-failure.rst
        .. include:: {IDF_TARGET_PATH_NAME}/rtc-i2c-abnormal-chip-reset.rst
        .. include:: {IDF_TARGET_PATH_NAME}/spi-stuck-after-soft-restart.rst
        .. include:: {IDF_TARGET_PATH_NAME}/usb-otg-abnormal-data-ahb-arbitration.rst
        .. include:: {IDF_TARGET_PATH_NAME}/sar-adc-bit1-no-flip.rst
        .. include:: shared/rtc-reg-read-error-from-light-sleep.rst
        .. include:: shared/tchsen-scan-done-int-raw-data-undefined.rst
        .. include:: {IDF_TARGET_PATH_NAME}/tchsen-scan-done-int-occurs-twice.rst

    .. only:: latex

        .. toctree::
            :hidden:

            {IDF_TARGET_PATH_NAME}/system-current-leakage-at-pins
            {IDF_TARGET_PATH_NAME}/system-random-flash-download-failure
            {IDF_TARGET_PATH_NAME}/rtc-i2c-abnormal-chip-reset
            {IDF_TARGET_PATH_NAME}/spi-stuck-after-soft-restart
            {IDF_TARGET_PATH_NAME}/usb-otg-abnormal-data-ahb-arbitration
            {IDF_TARGET_PATH_NAME}/sar-adc-bit1-no-flip
            shared/rtc-reg-read-error-from-light-sleep
            shared/tchsen-scan-done-int-raw-data-undefined
            {IDF_TARGET_PATH_NAME}/tchsen-scan-done-int-occurs-twice

.. only:: esp32

    .. only:: html

        .. include:: {IDF_TARGET_PATH_NAME}/cpu-crash-of-cpu-when-clock-frequency-switches.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-limitations-when-accessing-peripherals.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-limited-access-to-address-spaces.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-read-and-write-errors-related-to-access-sequence.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-read-and-write-errors-using-cache.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-read-error-of-dual-core-cpu.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-subsequent-access-halted-when-get-interrupted.rst
        .. include:: {IDF_TARGET_PATH_NAME}/cpu-writes-lost.rst
        .. include:: {IDF_TARGET_PATH_NAME}/ulp-and-touch-sensors-cannot-be-used.rst
        .. include:: {IDF_TARGET_PATH_NAME}/gpio-control-of-gpio-resistors-via-registers.rst
        .. include:: {IDF_TARGET_PATH_NAME}/gpio-edge-interrupts.rst
        .. include:: {IDF_TARGET_PATH_NAME}/gpio-inputs-pulled-down.rst
        .. include:: {IDF_TARGET_PATH_NAME}/reset-bor-function-fails.rst
        .. include:: {IDF_TARGET_PATH_NAME}/reset-spurious-watchdog-reset.rst
        .. include:: {IDF_TARGET_PATH_NAME}/reset-watchdog-reset-due-to-flash-startup-time.rst
        .. include:: {IDF_TARGET_PATH_NAME}/clock-limited-audio-pll-frequency-range.rst
        .. include:: {IDF_TARGET_PATH_NAME}/clock-rmii-clock-when-using-ethernet-and-wifi.rst
        .. include:: shared/rtc-reg-read-error-from-light-sleep.rst
        .. include:: {IDF_TARGET_PATH_NAME}/watchdog-issue-caused-by-live-lock.rst
        .. include:: {IDF_TARGET_PATH_NAME}/uart-fifo-cnt-indicates-data-length-incorrectly.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-dominant-bit-not-interpreted-as-sof.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-erroneous-message-transmits.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-error-passive-state-not-entered.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-error-status-bit-not-frozen.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-invalid-received-data-frame.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-negative-phase-error.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-rec-change.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-rx-fifo-overruns.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-suspend-transmission.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-tec-value-not-increased.rst
        .. include:: {IDF_TARGET_PATH_NAME}/twai-transmit-interrupt-lost.rst
        .. include:: {IDF_TARGET_PATH_NAME}/ledc-duty-overflow-error.rst

    .. only:: latex

        .. toctree::
            :hidden:

            {IDF_TARGET_PATH_NAME}/cpu-crash-of-cpu-when-clock-frequency-switches
            {IDF_TARGET_PATH_NAME}/cpu-limitations-when-accessing-peripherals
            {IDF_TARGET_PATH_NAME}/cpu-limited-access-to-address-spaces
            {IDF_TARGET_PATH_NAME}/cpu-read-and-write-errors-related-to-access-sequence
            {IDF_TARGET_PATH_NAME}/cpu-read-and-write-errors-using-cache
            {IDF_TARGET_PATH_NAME}/cpu-read-error-of-dual-core-cpu
            {IDF_TARGET_PATH_NAME}/cpu-subsequent-access-halted-when-get-interrupted
            {IDF_TARGET_PATH_NAME}/cpu-writes-lost
            {IDF_TARGET_PATH_NAME}/ulp-and-touch-sensors-cannot-be-used
            {IDF_TARGET_PATH_NAME}/gpio-control-of-gpio-resistors-via-registers
            {IDF_TARGET_PATH_NAME}/gpio-edge-interrupts
            {IDF_TARGET_PATH_NAME}/gpio-inputs-pulled-down
            {IDF_TARGET_PATH_NAME}/reset-bor-function-fails
            {IDF_TARGET_PATH_NAME}/reset-spurious-watchdog-reset
            {IDF_TARGET_PATH_NAME}/reset-watchdog-reset-due-to-flash-startup-time
            {IDF_TARGET_PATH_NAME}/clock-limited-audio-pll-frequency-range
            {IDF_TARGET_PATH_NAME}/clock-rmii-clock-when-using-ethernet-and-wifi
            shared/rtc-reg-read-error-from-light-sleep
            {IDF_TARGET_PATH_NAME}/watchdog-issue-caused-by-live-lock
            {IDF_TARGET_PATH_NAME}/uart-fifo-cnt-indicates-data-length-incorrectly
            {IDF_TARGET_PATH_NAME}/twai-dominant-bit-not-interpreted-as-sof
            {IDF_TARGET_PATH_NAME}/twai-erroneous-message-transmits
            {IDF_TARGET_PATH_NAME}/twai-error-passive-state-not-entered
            {IDF_TARGET_PATH_NAME}/twai-error-status-bit-not-frozen
            {IDF_TARGET_PATH_NAME}/twai-invalid-received-data-frame
            {IDF_TARGET_PATH_NAME}/twai-negative-phase-error
            {IDF_TARGET_PATH_NAME}/twai-rec-change
            {IDF_TARGET_PATH_NAME}/twai-rx-fifo-overruns
            {IDF_TARGET_PATH_NAME}/twai-suspend-transmission
            {IDF_TARGET_PATH_NAME}/twai-tec-value-not-increased
            {IDF_TARGET_PATH_NAME}/twai-transmit-interrupt-lost
            {IDF_TARGET_PATH_NAME}/ledc-duty-overflow-error

.. only:: esp32p4

    .. only:: html

        .. include:: shared/rmt-idle-level-cannot-be-controlled.rst
        .. include:: shared/i2c-fail-in-multiple-reads-operation.rst
        .. include:: esp32p4/load-access-fault-during-power-on-or-deepsleep-wakeup.rst
        .. include:: esp32p4/unaligned-dma-read-operations-may-return-old-data-when-accessing-overlapping-addresses.rst
        .. include:: esp32p4/data-errors-caused-by-asynchronous-timing-issues-in-the-mspi-address-overlap-detection-function.rst
        .. include:: esp32p4/secure-boot-buffer-address-error-in-rom.rst
        .. include:: esp32p4/output-regulators-cannot-generate-a-reliable-supply-when-peripheral-power-domain-is-off.rst
        .. include:: esp32p4/mem-to-mem-channel0 -permission-conflict-due-to-shared-transaction-ID.rst
        .. include:: esp32p4/unauthorized-ahb-access-may-block-subsequent-psram-or-flash-transactions.rst
        .. include:: esp32p4/secure-download-mode-flash-power-on-failure.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/rmt-idle-level-cannot-be-controlled
            shared/i2c-fail-in-multiple-reads-operation
            esp32p4/load-access-fault-during-power-on-or-deepsleep-wakeup
            esp32p4/unaligned-dma-read-operations-may-return-old-data-when-accessing-overlapping-addresses
            esp32p4/data-errors-caused-by-asynchronous-timing-issues-in-the-mspi-address-overlap-detection-function
            esp32p4/secure-boot-buffer-address-error-in-rom
            esp32p4/output-regulators-cannot-generate-a-reliable-supply-when-peripheral-power-domain-is-off
            esp32p4/mem-to-mem-channel0 -permission-conflict-due-to-shared-transaction-ID
            esp32p4/unauthorized-ahb-access-may-block-subsequent-psram-or-flash-transactions
            esp32p4/secure-download-mode-flash-power-on-failure

.. only:: esp32c5

    .. only:: html

        .. include:: shared/psram-read-after-write-consistency.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/psram-read-after-write-consistency

.. only:: esp32c61

    .. only:: html

        .. include:: shared/psram-read-after-write-consistency.rst

    .. only:: latex

        .. toctree::
            :hidden:

            shared/psram-read-after-write-consistency
