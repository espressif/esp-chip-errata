[TWAI-3.13.7] When the 8th Bit of the Error Delimiter Is Dominant, the Error Passive State Is Not Entered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When the TWAI controller is the transmitter and has a TEC value between 120 and 127, transmitting an error frame will increment its TEC by 8 thus make the controller error passive (due to TEC becoming >= 128). However, if the 8th bit of the error delimiter is dominant, the TEC will still increment by 8 but the controller will not become error passive. Instead, the controller will become error passive when another error frame is transmitted. Note that the controller will still generate the required overload frame due to the dominant 8th bit.

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
