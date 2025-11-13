[BOOT-9537] Accidentally Enter USB Download Boot Mode If the Power-up Duration Is Too Long
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

During power-on, if the voltage rises from 0 V to 3.3 V in more than 12 ms, the chip may accidentally enter USB Download Boot mode.

Workarounds
^^^^^^^^^^^

Ensure that the power-up duration is less than 12 ms.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.
