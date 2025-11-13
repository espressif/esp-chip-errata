[AES-11401] CPA Attack-Related Security Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

Description
^^^^^^^^^^^

The chip's Flash Encryption is based on XTS-AES. Flash Encryption as well as Secure Boot may be bypassed by using a Correlation Power Analysis (CPA) attack combined with Fault Injection (FI) and a buffer overflow exploitation.

Workarounds
^^^^^^^^^^^

Long lived encryption keys that are common between the devices or manufacturing batch should be avoided at all costs.

Enable Flash Encryption and Secure Boot at the same time, which can minimize the risk of attacker rewriting with the firmware.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`. Chip revision v1.2 has introduced anti-attack pseudo-round function, which can effectively resist CPA attacks.
