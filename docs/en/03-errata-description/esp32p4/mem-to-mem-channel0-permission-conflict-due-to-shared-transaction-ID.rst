[DMA-767] DMA Channel 0 Transaction ID Overlap Causes Permission Management Issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

When performing a memory-to-memory transfer using AHB DMA channel 0, the transfer is assigned transaction ID "a", which is identical to the transaction ID used by the RMT peripheral DMA.

Because of this ID overlap, memory-to-memory transfers on channel 0 share the same permission settings as the RMT peripheral and cannot be controlled independently. This may lead to unintended or unauthorized accesses in systems requiring isolated permission management.

Workaround
^^^^^^^^^^

Avoid using memory-to-memory transfer channel 0. Perform all memory-to-memory transfers using channel 1 or channel 2.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
