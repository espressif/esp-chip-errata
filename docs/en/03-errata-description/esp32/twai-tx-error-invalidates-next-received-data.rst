[TWAI-880] A Bus Error During Transmission Can Cause the Data Bytes of the Next Received Data Frame to Be Invalid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller is transmitting a data frame and a bus error occurs in the data or CRC field, some data bytes of the next received data frame may be shifted. The identifier and data length of that frame can remain correct, and the controller does not report an error for the received frame. Therefore, the next received data frame should be considered invalid.

The controller uses a shared byte counter to monitor bus activity during both transmission and reception. A bus error in the data field during transmission can leave this counter in an incorrect state if the frame ends before the CRC field, where the counter is normally cleared. The incorrect counter value then shifts the data bytes of the next received frame.

Workarounds
^^^^^^^^^^^

Set INTERRUPT_BUS_ERR_INT_ENA. When a bus error interrupt occurs, check ERROR_CODE_CAPTURE_REG to detect a bus error in the data or CRC field during transmission. If this condition is met, reset the TWAI controller. Save the current register values before the reset and restore them afterwards.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
