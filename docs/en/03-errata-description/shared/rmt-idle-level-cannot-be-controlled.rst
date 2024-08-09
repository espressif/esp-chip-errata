[RMT] The Idle State Signal Level Might Run into Error in RMT Continuous TX Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c6

   .. tags::
      
      v0.0, v0.1, v0.2

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

Description
^^^^^^^^^^^

In {IDF_TARGET_NAME}'s RMT module, if the continuous TX mode is enabled, it is expected that the data transmission stops after the data is sent for RMT_TX_LOOP_NUM_CHn rounds, and after that, the signal level in idle state should be controlled by the "level" field of the end-marker.

However, in real situation, after the data transmission stops, the channel's idle state signal level is not controlled by the "level" field of the end-marker, but by the level in the data wrapped back, which is indeterminate.

Workarounds
^^^^^^^^^^^

{IDF_TARGET_SUPPORT_VERSION:default="",esp32s3="v5.0",esp32c6="v5.1"}

Users are suggested to set RMT_IDLE_OUT_EN_CHn to 1 to only use registers to control the idle level.

This issue has been bypassed since the first ESP-IDF version that supports continuous TX mode ({IDF_TARGET_SUPPORT_VERSION}). In these versions of ESP-IDF, it is configured that the idle level can only be controlled by registers.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
