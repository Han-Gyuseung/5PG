tool/extract_strain
~~~~~~~~~~~~~~~~~~~

**P5Grand** provides ``tool/extract_strain.py`` script to generate a file containing fitting parameters.
``tool/extract_strain.py`` script extracts parameters for local strain from the ``OUTCAR`` of **VASP**, and automatically write them in a file named ``BM_constant.dat``.

The basic command to extract the parameters for local strain from the OUTCAR of **VASP**.

::

 $ python /dir/to/P5Grand/tool/extract_strain.py atomA atomB

We provide an example for testing a command at `example/strain <https://github.com/Han-Gyuseung/P5Grand/tree/main/example/strain>`_.
The materials for example is GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ . For the test with example, the command become:

::

 $ python /dir/to/P5Grand/tool/extract_strain.py As Sb

The fitting equations can be manually modified by editing the ``tool/extract_strain.py`` module.
