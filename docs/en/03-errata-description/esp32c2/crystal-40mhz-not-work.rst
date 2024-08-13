[Crystal] 40 MHz Crystal Cannot Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. only:: esp32c2

   .. tags::

      v0.0, v1.0

Description
^^^^^^^^^^^

{IDF_TARGET_NAME} was designed to support 26 MHz and 40 MHz crystals. However, for revision v1.0 and previous versions, some chips cannot work properly when equipped with 40 MHz crystal. Specific symptoms of the problem include clock issues, or printing garbled characters when powering on, etc.

Workarounds
^^^^^^^^^^^

Use 26 MHz crystal instead of 40 MHz for revision v1.0 and previous chips.


Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.1`, which supports both 26 MHz and 40 MHz crystals.
