tool/extract_strain
~~~~~~~~~~~~~~~~~~~

**5PG** provides ``tool/extract_strain.py``, which is a code for extracting parameters for local strain from the ``OUTCAR`` of **VASP**.

The basic command to extract the parameters for local strain from the OUTCAR of **VASP**.

::

 $ python /dir/to/5PG/tool/extract_strain.py atomA atomB

We provide an example for testing a command at `example/strain <https://github.com/Han-Gyuseung/5PG/tree/main/example/strain>`_.
The materials for example is GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ . For the test with example, the command become:

::

 $ python /dir/to/5PG/tool/extract_strain.py As Sb
