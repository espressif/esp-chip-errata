[CPU-863] Misaligned Memory Access May Lead to Exception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c3

   .. tags::

      v0.0, v0.1, v0.2, v0.3, v0.4, v1.1

.. only:: esp32c6

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

A misaligned **load** instruction immediately followed by a **store** instruction may raise a load access fault exception (exception code 5) when the load address and the store address lie in regions with different access permissions configured via Physical Memory Protection (PMP) or Physical Memory Attributes (PMA).

For example, the following sequence commonly triggers this issue when copying an unaligned word from flash or ROM into RAM:

.. code-block:: asm

   lw  a0, 0(a1)   # unaligned 32-bit address load from a read-only PMP region (e.g., ROM)
   sw  a0, 0(a2)   # store to a read-write PMP region (e.g., RAM)

**Root cause:**

A misaligned **load** that crosses a word boundary is split internally into two transactions. Due to a timing alignment issue in the design, the second transaction of the misaligned **load** can incorrectly be checked against the store's access permissions instead of its own, triggering an exception.

Workarounds
^^^^^^^^^^^

The RISC-V specification does not guarantee that hardware supports misaligned accesses. General-purpose RISC-V code should not rely on that support. If misaligned accesses cannot be avoided, such as when porting third-party libraries, use the following workarounds:

- Insert one or more **nop** instructions between the misaligned **load** and the following **store**. This prevents the incorrect permission check described above.

  .. note::

     Linkers that support the ``--fix-esp-pmp-misalign`` option can insert **nop** instructions between consecutive **load** and **store** instructions automatically. This option is conservative, as it may also insert extra **nop** instructions for pairs that would not trigger this exception, for example, when the accesses are aligned or when both access the same PMP region.

- When copying memory, use misaligned **load**/**store** only for the first and last misaligned words of a data block, and use aligned **load**/**store** for the words in between. This approach requires fewer **nop** instructions and has better performance than inserting **nop** instructions throughout.
- Configure the same PMP/PMA permissions for the memory regions accessed by the misaligned **load** and the following **store**. This may require saving and restoring the permission settings around the affected code.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
