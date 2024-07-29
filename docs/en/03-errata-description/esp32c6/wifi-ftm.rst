[Wi-Fi] {IDF_TARGET_NAME} Cannot Be 802.11mc FTM Initiator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::
      
      v0.0, v0.1

Description
^^^^^^^^^^^

The time of T3 (i.e., time of departure of ACK from Initiator) used in 802.11mc Fine Time Measurement (FTM) cannot be acquired correctly, and as a result {IDF_TARGET_NAME} cannot be the FTM Initiator.

Workarounds
^^^^^^^^^^^

No workaround.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v0.2`.
