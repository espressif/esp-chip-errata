[TWAI-3.13.5] Receiving an Erroneous Data Frame Can Cause the Data Bytes of the Next Received Data Frame to Be Invalid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller is receiving a data frame and a bit or stuff error occurs in the data or CRC fields, some data bytes of the next received data frame may be shifted or lost. Therefore, the next received data frame (including those filtered out by the acceptance filter) should be considered invalid.

Workarounds
^^^^^^^^^^^

Users can detect the errata triggering condition (i.e., bit or stuff error in the data or CRC field) by setting the INTERRUPT_BUS_ERR_INT_ENA and checking the ERROR_CODE_CAPTURE_REG when a bus error interrupt occurs. If the errata condition is met, the following workarounds are possible:

- The TWAI controller can transmit a dummy frame with 0 data bytes to reset the controller's internal signals. It is advisable to select an ID for the dummy frame that can be filtered out by all nodes on the TWAI bus.
- Hardware reset the TWAI controller (will require saving and restoring the current register values).

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
