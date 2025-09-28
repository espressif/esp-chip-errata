[CPU-3.21] When a CPU Is Interrupted While Accessing Five Specific Fifo Registers, Subsequent CPU Accesses Will Get Halted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the CPU attempts to read five FIFO registers 0x3FF40000 (UART0), 0x3FF50000 (UART1), 0x3FF6E000 (UART2), 0x3FF4F004 (I2S0), and 0x3FF6D004 (I2S1), and if an interrupt occurs, the read request will be interrupted. This will cause the bus bridge to be stuck in a state of waiting for the read request to end. Consequently, the subsequent access to the APB peripheral registers (0x3FF40000 ~ 0x3FF7FFFF or 0x60000000 ~ 0x6003FFFF) by any CPUs will be rejected and halted.

Writing to these five FIFO registers does not have such an issue.

Workarounds
^^^^^^^^^^^

Disable CPU interrupts before reading these five FIFO registers. Enable CPU interrupts after read access.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
