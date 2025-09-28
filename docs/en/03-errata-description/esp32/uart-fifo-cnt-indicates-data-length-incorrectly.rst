[UART-3.17] UART fifo_cnt Does Not Indicate the Data Length In Fifo Correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When software uses DPORT to read UART fifo_cnt, and such operation is interrupted, then fifo_cnt will decrement by 1 erroneously.

Workarounds
^^^^^^^^^^^

When using DPort to read fifo, calculate the real count based on the FIFO read and write offset address. For example:

.. code-block::

    if (wr_addr > rd_addr) {
        len = wr_addr - rd_addr;
    } else if (wr_addr < rd_addr){
        len = (wr_addr + 128) - rd_addr;
    } else {
        len = fifo_cnt > 0 ? 128 : 0;
    }

In the above code snippet, ``wr_addr`` represents the FIFO write offset address, ``rd_addr`` represents the FIFO read offset address, ``fifo_cnt`` represents the number of valid bytes in the FIFO, ``len`` represents the correct number of valid bytes after calculation.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
