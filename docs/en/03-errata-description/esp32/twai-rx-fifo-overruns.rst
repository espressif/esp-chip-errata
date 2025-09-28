[TWAI-3.13.11] When the RX Fifo Overruns With 64 or More Messages, the RX Fifo Becomes Unrecoverable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the RX FIFO overruns with multiple messages, and the RX message counter reaches 64, the RX FIFO will become unrecoverable. Any message read from the RX FIFO will be invalid. Attempting to release a message from the RX FIFO will have no effect.

Workarounds
^^^^^^^^^^^

The TWAI controller must be reset by software in order to recover the RX FIFO.

Solution
^^^^^^^^

This issue is automatically worked around in ESP-IDF v4.3 and newer.
