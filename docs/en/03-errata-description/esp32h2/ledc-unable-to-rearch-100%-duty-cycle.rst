[LEDC-253] Unable to Reach 100% Duty Cycle at Maximum Duty Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

When the timer selects the maximum duty resolution, in such case, 100% duty cycle is not achievable. Setting duty to (2\ :sup:`MAX_DUTY_RES`) will break the internal duty calculation.

Workarounds
^^^^^^^^^^^

No workaround.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.
