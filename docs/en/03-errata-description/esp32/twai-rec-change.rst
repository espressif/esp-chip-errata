[TWAI-3.13.1] Receive Error Counter (REC) Is Allowed to Change Whilst in Reset Mode or Bus-off Recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller enters reset mode (e.g., by setting the RESET_MODE bit or due to a bus-off condition) or when the TWAI controller undergoes bus-off recovery, the REC is still permitted to change. This can lead to the following cases:

- Whilst in reset mode or bus-off recovery, a changing REC can lead to the error status bit changing which in turn could trigger the error warning limit interrupt.
- During bus-off recovery, an REC > 0 can prevent the bus-off recovery process from completing.

Workarounds
^^^^^^^^^^^

When entering reset mode, the TWAI controller should set the LISTEN_ONLY_MODE to freeze the REC. The desired mode of operation should be restored before exiting reset mode or when bus-off recovery completes.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
