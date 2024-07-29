[CPU] Possible Deadlock Due to Out-of-Order Execution of Instructions When Writing to LP SRAM Is Involved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::
      
      v0.0, v0.1

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

When HP CPU executes instructions (instruction A and instruction B successively) in LP SRAM, and instruction A and instruction B happen to follow the following patterns:

- Instruction A involves writing to memory. Examples: **sw**/**sh**/**sb**
- Instruction B involves only accessing the instruction bus. Examples: **nop**/**jal**/**jalr**/**lui**/**auipc**
- The address of instruction B is not 4-byte aligned

The data written by instruction A to memory is only committed after instruction B has completed execution. This introduces a risk where, after instruction A writing to memory, if an infinite loop is executed in instruction B, the writing of instruction A will never complete.

Workarounds
^^^^^^^^^^^

When you experience this problem, or when you check the assembly code
and see the above mentioned pattern,

- Add a **fence** instruction between instruction A and the infinite loop. This can be achieved by using the *rv_utils_memory_barrier* interface in ESP-IDF.
- Replace the infinite loop with instruction **wfi**. This can be achieved by using the *rv_utils_wait_for_intr* interface in ESP-IDF.
- Disable the RV32C (compressed) extension when compiling code that to be executed in LP SRAM to avoid instructions with not 4-byte aligned addresses.

Solution
^^^^^^^^

.. only:: esp32c6

   Fixed in chip revision :bdg-success:`v0.2`.

.. only:: esp32h2

   To be fixed in the :bdg-warning:`future chip revisions`.
