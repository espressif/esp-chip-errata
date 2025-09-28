[TWAI-3.13.10] A Negative Phase Error Where \|e\| > SJW (N) Will Cause the Remaining Transmitted Bits to Be Left Shifted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller encounters a recessive to dominant edge with a negative phase error (i.e., the edge is early), it will correct for the phase error using resynchronization as required by the CAN2.0B protocol. However, if the TWAI controller is acting as transmitter and encounters a negative phase error where e < 0 and \|e\| > SJW, the bits transmitted following the phase error will be left shifted by one bit. Thus, the transmitted frame's contents (i.e., DLC, data bytes, CRC sequence) will be corrupted.

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
