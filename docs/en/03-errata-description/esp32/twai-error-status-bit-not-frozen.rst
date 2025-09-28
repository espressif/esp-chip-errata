[TWAI-3.13.2] Error Status Bit Is Not Frozen During Bus-off Recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller undergoes the bus-off recovery process, the controller must monitor 128 occurrences of the bus free signal (11 consecutive recessive bits) before it can become error active again. The number of bus-free signals remaining is indicated by the transmit error counter (TEC). Because the error status bit is not frozen during bus-off recovery, its value will change when the transmit error counter drops below the user-defined transmit error warning limit (96 by default) thus trigger the error warning limit interrupt before bus-off recovery has completed.

Workarounds
^^^^^^^^^^^

When undergoing bus-off recovery, an error warning interrupt does not necessarily indicate the completion of recovery. Users should check the STATUS_NODE_BUS_OFF bit to verify whether bus-off recovery has completed.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
