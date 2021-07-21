Free energy
===========

5PG can calculate the free energy of a system at a given temperature.

The basic command to calculate free energy is ::

 $ python /dir/to/5PG/__main__.py CEL.log -calc f

or ::

 $ python /dir/to/5PG CEL.log -calc f

If the name of input file is `CEL.log`, it is not essential to write `CEL.log`

We provide example files for testing a command `here <https://github.com/Han-Gyuseung/5PG/tree/main/example/thermodynamic>`_.
 
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

 $ python /dir/to/5PG CEL.log -calc f



``-strain``
***********

| -strain `[fileName]`
| default : BM_constant.dat

| The option to select the input file for strain energy.

::

 $ python /dir/to/5PG CEL.log -calc f -strain BM_constant.dat


``-unit``
*********

| -unit `eV` | `J`
| default : `eV`

| The option to select energy unit of input file and strain energy.

::

 $ python /dir/to/5PG CEL.log -calc f -unit eV


``-T``
********

| -T `[real >0]`
| default : 300
| unit : Kelvin

| Target temperature to be calculated.

::

 $ python /dir/to/5PG CEL.log -calc f -T 500



``-points``
***********

| -points `[integer > 1]`
| default : 32

| The number of calculated compositions -1. The composition interval is set as 1/[int]

::

 $ python /dir/to/5PG CEL.log -calc f -points 50
