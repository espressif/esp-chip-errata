[ECDSA_DS-837] Signatures with Invalid ``s`` Values Are Incorrectly Accepted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3

Description
^^^^^^^^^^^

When the signature ``{r = (Qa + G).x, s = 0 or n}`` with an invalid ``s`` value is submitted to the ECDSA_DS peripheral against any message and public key, the peripheral incorrectly reports the signature as "valid".

Workarounds
^^^^^^^^^^^

Use RSA_DS Secure Boot instead of ECDSA_DS Secure Boot.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
