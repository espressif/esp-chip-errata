[802.15.4-9538] TX Power Variation in Certain RF Certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

In certain RF certification channels, the transmit power of chip revisions prior to v1.2 may be slightly lower than the design expectation. However, it still meets the certification requirements.

Workarounds
^^^^^^^^^^^

No workaround.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`. **The transmit spectrum band edge has been optimized in this revision.**
