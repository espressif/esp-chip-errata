[ECDSA_DS-836] Signatures with Invalid ``r`` and ``s`` Values Are Incorrectly Accepted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v1.2

.. only:: esp32p4

   .. tags::

      v3.0, v3.1, v3.2

.. only:: esp32s31

   .. tags::

      v0.0

Description
^^^^^^^^^^^

When the signature ``{r = 0 or n, s = 0 or n}`` with invalid ``r`` and ``s`` values is submitted to the ECDSA_DS peripheral against any message and public key, the peripheral incorrectly reports the signature as "valid".

Workarounds
^^^^^^^^^^^

Use RSA_DS Secure Boot instead of ECDSA_DS Secure Boot.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
