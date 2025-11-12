[HUK-576] HUK Is Unavailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c5

   .. tags::

      v0.0, v0.1, v1.0

Description
^^^^^^^^^^^

On {IDF_TARGET_NAME} chips, inrush current during power-on can cause the first HUK recovery attempt to fail with a certain probability.

In the affected chip revisions, the ROM uses the HUK data immediately after power-on to derive flash encryption and decryption keys through the key manager (introduced in ESP-IDF v5.5.2). When HUK recovery fails, the ROM may fail to derive these keys.

Workaround
^^^^^^^^^^

No workaround.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.

The updated ROM re-powers the HUK and retries recovery if the initial attempt fails.
