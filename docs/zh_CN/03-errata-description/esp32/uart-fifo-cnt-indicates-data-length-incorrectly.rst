[UART-3.17] UART fifo_cnt 不能正确表示 FIFO 中有效数据长度
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

使用 DPORT 读 UART FIFO 时，如果软件的读 FIFO 操作被中断打断，那么 fifo_cnt 会被错误地减 1。

变通方法
^^^^^^^^

使用 DPORT 读取 FIFO 时，需结合读/写 FIFO 偏移地址计算 FIFO 中有效数据长度。例如：

.. code-block::

    if (wr_addr > rd_addr) {
        len = wr_addr - rd_addr;
    } else if (wr_addr < rd_addr){
        len = (wr_addr + 128) - rd_addr;
    } else {
        len = fifo_cnt > 0 ? 128 : 0;
    }

其中 ``wr_addr`` 表示写 FIFO 偏移地址，``rd_addr`` 表示读 FIFO 偏移地址，``fifo_cnt`` 表示芯片记录的 FIFO 中有效字节数，``len`` 表示重新计算后正确的有效字节数。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
