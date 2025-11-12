[FLASH-938] Flash Manual Encryption May Fail When CPU Runs at 240 MHz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. only:: esp32c5

   .. tags::

      v1.0, v1.2

Description
^^^^^^^^^^^

On {IDF_TARGET_NAME} chips, flash manual encryption may fail when the CPU frequency is set to 240 MHz due to internal power consumption fluctuations.

Workaround
^^^^^^^^^^

When performing flash manual encryption, configure the CPU frequency to 160 MHz or lower.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
