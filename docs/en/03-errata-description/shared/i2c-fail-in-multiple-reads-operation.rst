[I2C-308] I2C Slave Fails in Multiple-read Under Non-FIFO Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::

      v0.0, v0.1

.. only:: esp32p4

   .. tags::

      v0.0, v1.0, v1.3

Description
^^^^^^^^^^^

If the I2C slave non-FIFO mode is enabled and the master performs multiple-read operation on the slave, the master can not correctly read the data from the slave.

Workarounds
^^^^^^^^^^^

Set I2C_FIFO_ADDR_CFG_EN and I2C_SLV_TX_AUTO_START_EN to 1 and I2C_FIFO_PRT_EN to 0 for the slave.

After configuration, the master must access the slave using the following command sequence: RSTART -> WRITE (slave addr, fifo addr) -> RSTART -> WRITE (slave addr) -> READ (NACK) -> STOP, with only one byte allowed to be read each time.

Solution
^^^^^^^^

.. only:: esp32h2

   Fixed in chip revision :bdg-success:`v1.2`.

.. only:: esp32p4

   To be fixed in the :bdg-warning:`next chip revision`.
