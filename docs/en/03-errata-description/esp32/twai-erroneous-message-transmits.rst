[TWAI-3.13.3] Message Transmitted After Bus-off Recovery Is Erroneous
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

Upon completion of bus-off recovery, the next message that the TWAI controller transmits may be erroneous (i.e., does not adhere to TWAI frame format).

Workarounds
^^^^^^^^^^^

Upon detecting the completion of bus-off recovery (via the error warning interrupt), the TWAI controller should enter then exit reset mode so that the controller's internal signals are reset.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
