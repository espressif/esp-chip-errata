[MSPI-749] 芯片在上电或唤醒过程中失败，并打印 "Load access fault" 错误信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

描述
^^^^

在 {IDF_TARGET_NAME} 进行上电或唤醒过程中，由于 MSPI IP 内部读数据请求通道处理异常，MSPI 不能正确处理 AXI 系统总线发起的首次及第二次访问请求，从而概率性返回不应出现的错误响应，导致启动流程失败。

变通方法
^^^^^^^^

上电流程：上电流程固定，若流程失败，系统仅能依靠看门狗超时复位芯片，实现“二次上电”。在“二次上电”后，flash MSPI 模块可恢复正常工作。

唤醒流程：在休眠唤醒过程中，LP memory 区域未掉电，其内容得以保持。可在休眠前预先在 LP memory 中部署一段可执行程序，该程序能够执行两次 dummy 读访问。唤醒时，CPU 将先执行该程序，再跳转至 ROM code 继续正常启动流程。代码如下：

.. code-block::

    REG32_WR(0x500ca000, 0x23);
    CLEAR_PERI_REG_MASK(0x5008c03c, 0x80000000);

    // 关闭 CPU 获取错误响应
    SET_PERI_REG_MASK(0x500e51a4, 0x00000007);

    // 使能 AXI
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c03c, 0x00000001);

    // 置 1 个 MSPI MMU 表项，用于将 AXI 地址映射到 flash 地址
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c380, 0x0);
    REG32_WR(0x500ca000, 0x23);
    SET_PERI_REG_MASK(0x5008c37c, 0x1000);

    // AXI 读取 flash MSPI 的第一次和第二次访问
    REG32_RD(0x80000000);
    REG32_WR(0x500ca000, 0x23);
    REG32_RD(0x80000040);
    REG32_WR(0x500ca000, 0x23);

    // 重新使能 CPU 获取错误响应
    CLEAR_PERI_REG_MASK(0x500e51a4, 0x00000007);

    SET_PERI_REG_MASK(0x50111014, 0x8000);
    SET_PERI_REG_MASK(0x50111014, 0x2000);

PSRAM MSPI：PSRAM MSPI 初始化时，在正式 AXI 读访问前插入两次 dummy 读，可有效规避初始访问异常。

解决方案
^^^^^^^^

.. only:: esp32p4

   已在芯片版本 :bdg-success:`v3.1` 中修复。
