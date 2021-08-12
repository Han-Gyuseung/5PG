PoI mode
================

**P5Grand** can calculate the ensemble average of a system.

The basic command to calculate average property is ::

 $ python /dir/to/P5Grand/__main__.py CEL.log -calc a

or ::

 $ python /dir/to/P5Grand CEL.log -calc a 

If the name of input file is `CEL.log`, it is not essential to write `CEL.log`

We provide example files for testing a command `here <https://github.com/Han-Gyuseung/P5Grand/tree/main/example/bandgap-InGaAs>`_.
The log messages obtained from the example files is as follows:


::

 DataFile: CEL.log
 -strain : BM_constant.dat
 -unit   : eV
 -calc   : average_property
 -T      :   300.0 K
 -points :    32
 
 Read CEL.log
 Read BM_constant.dat
 
    x       energy   property1 
 0.00000   0.000000   1.292204 
 0.03125   0.005169   1.211994 
 0.06250   0.009607   1.140733 
 0.09375   0.013382   1.080268 
 0.12500   0.016504   1.029588 
 0.15625   0.018981   0.987125 
 0.18750   0.021256   0.952017 
 0.21875   0.023792   0.923276 
 0.25000   0.025879   0.898230 
 0.28125   0.027572   0.875879 
 0.31250   0.028973   0.856020 
 0.34375   0.029608   0.837696 
 0.37500   0.029766   0.817083 
 0.40625   0.030569   0.786566 
 0.43750   0.030986   0.755732 
 0.46875   0.030751   0.726637 
 0.50000   0.029708   0.699766 
 0.53125   0.028170   0.676245 
 0.56250   0.027533   0.651744 
 0.59375   0.027336   0.623788 
 0.62500   0.026197   0.596260 
 0.65625   0.024305   0.572390 
 0.68750   0.024103   0.560555 
 0.71875   0.023929   0.547659 
 0.75000   0.023124   0.533522 
 0.78125   0.022067   0.519020 
 0.81250   0.020669   0.503048 
 0.84375   0.018754   0.484639 
 0.87500   0.016341   0.463566 
 0.90625   0.013357   0.440446 
 0.93750   0.009720   0.415208 
 0.96875   0.005344   0.386767 
 1.00000   0.000000   0.353140

 
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
| To calculate average property, ``-calc`` must be `a`.

::

 $ python /dir/to/P5Grand CEL.log -calc a


``-strain``
***********

| -strain `[fileName]`
| default : BM_constant.dat

| 	The option to select the fitting equation for strain energy.

::

 $ python /dir/to/P5Grand CEL.log -calc a -strain BM_constant.dat

``-unit``
*********

| -unit `eV` | `J`
| default : `eV`

| The option to select energy unit of input file and strain energy.

::

 $ python /dir/to/P5Grand CEL.log -calc a -unit eV


``-T``
********

| -T `[real >0]`
| default : 300
| unit : Kelvin

| Target temperature to be calculated.

::

 $ python /dir/to/P5Grand CEL.log -calc a -T 500


``-x``
******

| -x `[real 0~1]`
| default : None

Target composition. must be within 0~1.

::

 $ python /dir/to/P5Grand CEL.log -calc a -x 0.5



``-points``
***********

| -points `[integer > 1]`
| default : 32

| The number of calculated compositions -1. composition interval=1/[int]
| ``-points`` is activated only when ``-x`` is not set.

::

 $ python /dir/to/P5Grand CEL.log -calc a -points 50
