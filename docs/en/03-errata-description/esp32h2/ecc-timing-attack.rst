[ECC-11400] Timing Attack-Related Security Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

ECC does not operate in a constant time when performing point multiplication, making it susceptible to timing attacks.

Workarounds
^^^^^^^^^^^

The ECC driver has randomized the power profile and made it appear constant time. This requires Secure Boot to be enabled for full effectiveness.

ESP-IDF has bypassed this issue in the following released versions.

.. flat-table:: ESP-IDF Released Versions
   :header-rows: 1
   :widths: 2 2

   * - ESP-IDF Release Branch
     - Released Version
   * - release/v5.4 and above
     - `v5.4 <https://github.com/espressif/esp-idf/releases/tag/v5.4>`_
   * - release/v5.3
     - `v5.3.2 <https://github.com/espressif/esp-idf/releases/tag/v5.3.2>`_
   * - release/v5.2
     - `v5.2.5 <https://github.com/espressif/esp-idf/releases/tag/v5.2.5>`_
   * - release/v5.1
     - `v5.1.5 <https://github.com/espressif/esp-idf/releases/tag/v5.1.5>`_

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`. Chip revision v1.2 has introduced constant time and consumption mode, in which each point multiplication calculation consumes the same amount of time and power, able to effectively resist timing attacks.
