[TWAI-3.13.8] Suspend Transmission Is Included Even After Losing Arbitration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

The CAN2.0B protocol stipulates that an error passive node that was the transmitter of a message shall add a suspend transmission field within the subsequent interframe space. However, error passive receivers shall not add a suspend transmission field.

When the TWAI controller is error passive and loses arbitration (hence becomes a receiver), it will still add a suspend transmission field in the subsequent interframe space. This results in the TWAI controller being late to start retransmission. Therefore, if another node transmits immediately after the interframe space is over, the TWAI controller will fail to compete for arbitration due to the other nodes not including a suspend transmission field in their interframe space (as per CAN2.0B specification).

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
