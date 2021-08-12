tool/extract_strain
~~~~~~~~~~~~~~~~~~~

**P5Grand** provides ``tool/extract_strain.py`` script to generate a file containing fitting parameters.
``tool/extract_strain.py`` script extracts parameters for local strain from the ``OUTCAR`` of **VASP**, and automatically write them in a file named ``BM_constant.dat``.

For each configuration, directories should be treed as below. 

::

 configuration
 ├── unstrained
 │   └── OUTCAR
 ├── 0_strained
 │   └── OUTCAR
 ├── 	.
 │   	.
 ├── 	.
 │   	.
 └── n_strained
     └── OUTCAR

.. Note::

 Directory named ``unstrained`` which calculates freely relaxed state is essential.
 
 Other directories involves the calculation results for strained state.
 
 Every lowest subdirectory should involve ``OUTCAR``.

Overall directory tree is follows.

::

 strain
 ├── x_equal_0_and_1_must_be_included
 │   ├── 0
 │   │   ├── unstrained
 │   │   │   └── OUTCAR
 │   │   ├── 0_strained
 │   │   │   └── OUTCAR
 │   │   ├──     .
 │   │   │       .
 │   │   ├──     .
 │   │   │       .
 │   │   └── n_strained
 │   │       └── OUTCAR
 │   └── 1
 │       ├── unstrained
 │       │   └── OUTCAR
 │       ├── 0_strained
 │       │   └── OUTCAR
 │       ├──     .
 │       │       .
 │       ├──     .
 │       │       .
 │       └── n_strained
 │           └── OUTCAR
 ├── configuration_1
 │   ├── unstrained
 │   │   └── OUTCAR
 │   ├── 0_strained
 │   │   └── OUTCAR
 │   ├── 	.
 │   │   	.
 │   ├──    .
 │   │      .
 │   └── n_strained
 │       └── OUTCAR
 ├── configuration_2
 │   ├── unstrained
 │   │   └── OUTCAR
 │   ├── 0_strained
 │   │   └── OUTCAR
 │   ├── 	.
 │   │   	.
 │   ├──    .
 │   │      .
 │   └── n_strained
 │       └── OUTCAR
 ├──         .
 │           .
 ├──         .
 │           .
 └── configuration_n
     ├── unstrained
     │   └── OUTCAR
     ├── 0_strained
     │   └── OUTCAR
     ├── 	.
     │   	.
     ├──    .
     │      .
     └── n_strained
         └── OUTCAR

.. Note:: Directories for x=0 and x=1 should be included.

Enter the below command in ``strain`` directory to extract the parameters for local strain from the OUTCAR of **VASP**.

::

 $ python /dir/to/P5Grand/tool/extract_strain.py atomA atomB

An example of this command is provided at `example/strain <https://github.com/Han-Gyuseung/P5Grand/tree/main/example/strain>`_ for the case of GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ . For this example, the command is:

::

 $ python /dir/to/P5Grand/tool/extract_strain.py As Sb
 
Then, you can get ``BM_constant.dat`` file and fitting graph as follows.

.. image:: ../../_static/BM_fitting.png

The fitting equation can be manually modified by editing the ``tool/extract_strain.py`` script, and will be updated to account for the composition-dependent cases.
