Input files
===========

Suports calculations
for a binary system
:math:`A_{x}B_{1-x}`
or a pseudobinary system
:math:`A_{x}B_{1-x}C`
, x=0~1. 

input file I
----------------------

The grand canonical takes into account the local compositional fluctuation and enables to predict the average value of the “property of interest” (PoI) for any composition and temperature. 
However, it requires the energy and PoI for all possible compositions and configurations, which is not practically feasible.

Therefore, **P5Grand** requires the PoI of feasibly large number of (not all) configurations, which are randomly generated at each possible composition.

The energy and property of each configuration can be obtained by diverse ways such as:

1. all by DFT calculations
2. by machine learning based on some DFT data
3. by empirical-based data

For the free energy mode and the phase diagram mode, it consists of two columns and many rows. Each column presents the composition (x) and the energy (E\ :sub:`σ`\ ) of a certain configuration (σ) while each row corresponds to each configuration.

::

 0 -8.675196
 0.03125 -8.700504
 0.0625 -8.725803
 0.0625 -8.726524
 0.0625 -8.726524
 ...

For the PoI mode, it consists of three columns and many rows. Each column presents x, E\ :sub:`σ`\  and PoI of a certain configuration.

::

 0.0 -9.189511 0.713310
 0.03125 -9.211485 0.676563
 0.0625 -9.234508 0.691304
 0.0625 -9.233217 0.660815
 0.0625 -9.234138 0.672744
 ...

Each row indicates a configuration.
The first and the second column is the composition and energy of a configuration.
The third column is PoI like bandgap of a configuration.

The composition of a configuration (the first column) should be within 0~1.

The unit of the energy of a configuration (the second column) can be either eV/[mixing atoms] or J/[mixing atoms].

In this document, the name of input file is referred to as ``CEL.log``, which is the default name of input file to be read in **P5Grand**.


input file II
-------------

The grand canonical requires the strain energy induced by local compositional fluctuation.
In this document, the strain induced by local compositional fluctuation is referred to as `local strain <../strain.html>`__.

**P5Grand** approximates the local strain energy to Birch-Murnaghan equation of state using several parameters. 
As a default, **P5Grand** requires a file which contains four parameters.

:math:`B_0V_0 \ \ \ B'_0 \ \ \ 1 \ \ \ \frac{V_0(x=1)}{V_0(x=0)}`

, where V\ :sub:`0`\  and V are free relaxed volume and strained volume, B\ :sub:`0`\  and B'\ :sub:`0`\  are bulk modulus and its derivative.

The first and second values are V\ :sub:`0`\  B\ :sub:`0`\  and B'\ :sub:`0`\ , respectively. Fourth value over third value should be the V\ :sub:`0`\ (x=1) divided by V\ :sub:`0`\ (x=0), which limits V/V\ :sub:`0`\  to be calculated.

The fitting equations can be manually modified by editing the ``local_strain.py`` module.

.. note::

 The unit of strain energy should be same to the unit of energy in ``CEL.log``, either eV/[mixing atoms] or J/[mixing atoms].
 
 [mixing atoms] indicates the number of atoms in microstates. 
 For an pseudobinary system of GaAs\ :sub:`x`\ Sb\ :sub:`1-x`\ as an example, a 2x2x2 zincblende supercell is composed of 32 cations and 32 anions.
 In this case, the number of mixing atoms is 32.

.. include:: tool.rst

