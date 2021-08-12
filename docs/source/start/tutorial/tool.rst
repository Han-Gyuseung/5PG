tool/extract_strain
~~~~~~~~~~~~~~~~~~~

**P5Grand** provides ``tool/extract_strain.py`` script to generate a file containing fitting parameters.
``tool/extract_strain.py`` script extracts parameters for local strain from the ``OUTCAR`` of **VASP**, and automatically write them in a file named ``BM_constant.dat``.

For a binary system
:math:`A_{x}B_{1-x}`
or a pseudobinary system
:math:`A_{x}B_{1-x}C`
, directories for x=0, x=1, various configurations(0<x<1) are necessary. Also, they must include unstrained & several strained calculation directories. All lowest subdirectories must involve ``OUTCAR``.

You can prepare a directory like following structure.

::

 strain
 ├── x_equal_0_and_1_must_be_included
 │   ├── 0
 │   │   ├── 0_strain
 │   │   │   └── OUTCAR
 │   │   ├──     .
 │   │   │       .
 │   │   ├──     .
 │   │   │       .
 │   │   ├── n_strain
 │   │   │   └── OUTCAR
 │   │   └── unstrained 
 │   │       └── OUTCAR
 │   └── 1
 │       ├── 0_strain
 │       │   └── OUTCAR
 │       ├──     .
 │       │       .
 │       ├──     .
 │       │       .
 │       ├── n_strain
 │       │   └── OUTCAR
 │       └── unstrained
 │           └── OUTCAR 
 ├── configuration_1
 │   ├── 0_strain
 │   │   └── OUTCAR
 │   ├── 	.
 │   │   	.
 │   ├── 	.
 │   │   	.
 │   ├── n_strain
 │   │   └── OUTCAR
 │   └── unstrained
 │       └── OUTCAR
 ├── configuration_2
 │   ├── 0_strain
 │   │   └── OUTCAR
 │   ├── 	.
 │   │   	.
 │   ├── 	.
 │   │   	.
 │   ├── n_strain
 │   │   └── OUTCAR
 │   └── unstrained
 │       └── OUTCAR
 ├──         .
 │           .
 ├──         .
 │           .
 └── configuration_n
     ├── 0_strain
     │   └── OUTCAR
     ├── 	.
     │   	.
     ├── 	.
     │   	.
     ├── n_strain
     │   └── OUTCAR
     └── unstrained
         └── OUTCAR



The basic command to extract the parameters for local strain from the OUTCAR of **VASP**. 
Enter this command in ``strain`` directory above.

::

 $ python /dir/to/P5Grand/tool/extract_strain.py atomA atomB

We provide an example for testing a command at `example/strain <https://github.com/Han-Gyuseung/P5Grand/tree/main/example/strain>`_.
The materials for example is GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ . For the test with example, the command become:

::

 $ python /dir/to/P5Grand/tool/extract_strain.py As Sb
 
You can get ``BM_constant.dat`` file and fitting graph as follows

.. image:: ../../_static/BM_fitting.png

The fitting equations can be manually modified by editing the ``tool/extract_strain.py`` script.
