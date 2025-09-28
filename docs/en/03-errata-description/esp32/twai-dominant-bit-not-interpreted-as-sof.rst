[TWAI-3.13.6] After Losing Arbitration, a Dominant Bit on the 3rd Bit of Intermission Is Not Interpreted as an SOF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

The CAN2.0B protocol stipulates that a dominant bit on the 3rd bit of intermission shall be interpreted as a Start of Frame (SOF). Therefore, nodes shall begin receiving or transmitting (i.e., competing for arbitration) the ID field on the next bit.

When the TWAI controller loses arbitration and the following intermission's 3rd bit is dominant, the TWAI controller will not interpret this as an SOF and will make no attempt to compete for arbitration (i.e., does not retransmit its frame).

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
