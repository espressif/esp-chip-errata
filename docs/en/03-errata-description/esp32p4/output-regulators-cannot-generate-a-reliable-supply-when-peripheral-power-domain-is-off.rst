[Analog-765] Output Regulators Cannot Generate a Reliable Supply When Peripheral Power Domain Is Off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32p4

   .. tags::

      v3.0

Description
^^^^^^^^^^^

The output regulators can not generate a reliable supply when the peripheral power domain is turned off.

Workaround
^^^^^^^^^^

If you intend to use output regulators as the supply source for external PCB components, do not turn off the peripheral power domain in Light-sleep mode.

Solution
^^^^^^^^

.. only:: esp32p4

   Fixed in chip revision :bdg-success:`v3.1`.
