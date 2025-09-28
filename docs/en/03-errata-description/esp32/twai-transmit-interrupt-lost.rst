[TWAI-3.13.4] Reading the Interrupt Register May Lead to a Transmit Interrupt Being Lost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

The TWAI controller's interrupt signals are cleared by reading the INTERRUPT_REG. However, if a transmit interrupt occurs whilst the INTERRUPT_REG is being read (i.e., in the same APB clock cycle), the transmit interrupt is lost.

Workarounds
^^^^^^^^^^^

When a message is awaiting completion of transmission (i.e., transmission has been requested), users should also check the STATUS_TRANSMIT_BUFFER bit each time the INTERRUPT_REG is read. A set STATUS_TRANSMIT_BUFFER bit whilst the TWAI_TRANSMIT_INT_ST is not indicates a lost transmit interrupt.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
