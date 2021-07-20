util/extract_strain
~~~~~~~~~~~~~~~~~~~

**5PG** can calculate the ensemble average of a pseudobinary system.

The basic command for extract parameters for local strain ::

 $ python /dir/to/5PG/util/extract_strain.py atomA atomB

We provide an example for testing a command at `example/strain <https://github.com/Han-Gyuseung/5PG/tree/main/example/strain>`_.
The materials for example is GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ . For the test with example, the command become:

::

 $ python /dir/to/5PG/util/extract_strain.py As Sb
