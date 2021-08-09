Free energy
===========

**P5Grand** can calculate the free energy of a system at a given temperature.

The basic command to calculate free energy is ::

 $ python /dir/to/P5Grand/__main__.py CEL.log -calc f

or ::

 $ python /dir/to/P5Grand CEL.log -calc f

If the name of input file is `CEL.log`, it is not essential to write `CEL.log`

We provide example files for testing a command `here <https://github.com/Han-Gyuseung/P5Grand/tree/main/example/thermodynamic>`_.
The log messages obtained from the example files is as follows:

::

 DataFile: CEL.log
 -strain : BM_constant.dat
 -unit   : eV
 -calc   : free_energy
 -T      :   300.0 K
 -points :    32
  
 Read CEL.log
 Read BM_constant.dat
 
 0.00000   0.000000
 0.03125   0.001674
 0.06250   0.004003
 0.09375   0.006320
 0.12500   0.008493
 0.15625   0.010476
 0.18750   0.012277
 0.21875   0.013920
 0.25000   0.015386
 0.28125   0.016765
 0.31250   0.018161
 0.34375   0.019448
 0.37500   0.020529
 0.40625   0.021405
 0.43750   0.022186
 0.46875   0.022806
 0.50000   0.023155
 0.53125   0.023316
 0.56250   0.023382
 0.59375   0.023344
 0.62500   0.023003
 0.65625   0.022341
 0.68750   0.021498
 0.71875   0.020451
 0.75000   0.019163
 0.78125   0.017695
 0.81250   0.016021
 0.84375   0.014063
 0.87500   0.011771
 0.90625   0.009123
 0.93750   0.006132
 0.96875   0.002883
 1.00000   0.000000
 
-------------------

.. contents::
   :depth: 2
   :local:

-------------------



options
-------

``-calc``
**********

| -calc `f` | `p` | `a`
| default : `p`

| The option to choose what to be calculated.
| `f` indicates free energy, `p` indicates phase diagram, and `a` indicates average property.
| To calculate free energy, ``-calc`` must be `f`.

::

 $ python /dir/to/P5Grand CEL.log -calc f



``-strain``
***********

| -strain `[fileName]`
| default : BM_constant.dat

| The option to select the input file for strain energy.

::

 $ python /dir/to/P5Grand CEL.log -calc f -strain BM_constant.dat


``-unit``
*********

| -unit `eV` | `J`
| default : `eV`

| The option to select energy unit of input file and strain energy.

::

 $ python /dir/to/P5Grand CEL.log -calc f -unit eV


``-T``
********

| -T `[real >0]`
| default : 300
| unit : Kelvin

| Target temperature to be calculated.

::

 $ python /dir/to/P5Grand CEL.log -calc f -T 500



``-points``
***********

| -points `[integer > 1]`
| default : 32

| The number of calculated compositions -1. The composition interval is set as 1/[int]

::

 $ python /dir/to/P5Grand CEL.log -calc f -points 50
