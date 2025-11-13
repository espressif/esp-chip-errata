[PCNT-249] Unable to Trigger Step Interrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1, v1.2

Description
^^^^^^^^^^^

When the step counter is enabled and the step counter reaches the low limit or high limit, step interrupts are not generated properly.

Workarounds
^^^^^^^^^^^

Configure the system to notify the application every time the counter increases or decreases by a specified value (x). When this condition is met, the program enters the interrupt, reads the current counter value, and calls the user's callback, passing the counter value to the caller.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
