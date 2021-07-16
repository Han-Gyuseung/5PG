Average property
================

5PG can calculate the ensemble average of a system.

The basic command for calculate average property ::

 $ python /dir/to/5PG/__main__.py CEL.log -calc a

or ::

 $ python /dir/to/5PG CEL.log -calc a 

If the name of data file is `CEL.log`, it is not essential to write `CEL.log`

We provide example files for testing a command at `here <https://github.com/Han-Gyuseung/5PG/tree/main/example/property>`_.

 
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

 $ python /dir/to/5PG CEL.log -calc a


``-strain``
***********

| -strain `[fileName]`
| default : BM_constant.dat

| The option to select the data file for strain energy.

::

 $ python /dir/to/5PG CEL.log -calc a -strain BM_constant.dat

``-unit``
*********

| -unit `eV` | `J`
| default : `eV`

| The option to select energy unit of data file and strain energy.

::

 $ python /dir/to/5PG CEL.log -calc a -unit eV


``-T``
********

| -T `[real >0]`
| default : 300
| unit : Kelvin

| Target temperature to be calculated.

::

 $ python /dir/to/5PG CEL.log -calc a -T 500


``-x``
******

| -x `[real 0~1]`
| default : None

Target composition. must be within 0~1.

::

 $ python /dir/to/5PG CEL.log -calc a -x 0.5



``-points``
***********

| -points `[integer > 1]`
| default : 32

| The number of calculated compositions -1. composition interval=1/[int]
| ``-points`` is activated only when ``-x`` is not set.

::

 $ python /dir/to/5PG CEL.log -calc a -points 50
