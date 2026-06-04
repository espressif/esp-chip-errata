[ECC-833] Forcing ECC Memory Power-Down Bypasses ECDSA_DS Signature Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c5

   .. tags::

      v1.0, v1.2

Description
^^^^^^^^^^^

On {IDF_TARGET_NAME} chips, if ECC memory is force-powered down via the system register, ECDSA_DS reports any submitted signature as valid.

Workaround
^^^^^^^^^^

Use RSA_DS instead of ECDSA_DS for signature verification.

Solution
^^^^^^^^

To be fixed in the :bdg-warning:`next chip revision`.
