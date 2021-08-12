options
===========


.. contents::
   :depth: 1
   :local:

-------------------

``-h`` ``--help``
*****************

With ``-h`` or ``--help`` option, you can check options before running P5Grand.

:: 

 $ python /dir/to/P5Grand -h

or

::

 $ python /dir/to/P5Grand --help



::

 python __main__.py NameOfDatafile [options]
 
 -strain [the name of file containing strain energy]

 -calc   a|p|f   : p : calculating phase diagram
                 : f : calculating free energy
                 : a : calculating average_properties

 -unit   eV|J    : eV : all unit for energy become [eV]
                   J  : all energy unit become [J]

 For -calc p
 -Tmax   [float] : Upper limit of calculated temperature. Unit : Kelvin
 -Tmin   [float] : Lower limit of calculated temperature. Unit : Kelvin
 -dT     [float] : usual interval of calculated temperature. Unit : Kelvin
 -dTmin  [float] : minimum interval of calculated temperature. Unit : Kelvin
 -points [int]   : the number of calculated compositions -1. composition interval=1/[int]

 For -calc f
 -T      [float] : target temperature. Unit : Kelvin
 -points [int]   : the number of calculated compositions -1. composition interval=1/[int]

 For -calc a
 -T      [float] : target temperature. Unit : Kelvin
 -x      [float] : target composition. must be within 0~1
 -points [int]   : the number of calculated compositions -1. Activated only when -x is not set. composition interval=1/[int]

 -h --help       : show this message




``-calc``
**********

| -calc `f` | `p` | `a`
| default : `p`

| The option to choose the calculations modes: 
| f indicates the free energy mode, p indicates the phase diagram mode, and a indicates the PoI mode, respectively.

::

 $ python /dir/to/P5Grand CEL.log -calc f
 $ python /dir/to/P5Grand CEL.log -calc p
 $ python /dir/to/P5Grand CEL.log -calc a




``-strain``
***********

| -strain `[fileName]`
| default : BM_constant.dat

| The option to select the fitting equation for strain energy

::

 $ python /dir/to/P5Grand CEL.log -calc f -strain BM_constant.dat
 $ python /dir/to/P5Grand CEL.log -calc p -strain BM_constant.dat
 $ python /dir/to/P5Grand CEL.log -calc a -strain BM_constant.dat


``-unit``
*********

| -unit `eV` | `J`
| default : `eV`

| The option to select energy unit of data file and strain energy.

::

 $ python /dir/to/P5Grand CEL.log -calc f -unit eV
 $ python /dir/to/P5Grand CEL.log -calc p -unit eV
 $ python /dir/to/P5Grand CEL.log -calc a -unit eV


``-T``
********

| -T `[real >0]`
| default : 300
| unit : Kelvin

| Target temperature to be calculated.
| When ``-calc`` is `a`, ``-points`` is activated only when ``-x`` is not set.

::

 $ python /dir/to/P5Grand CEL.log -calc f -T 500
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

| The number of calculated compositions -1. The composition interval is set as 1/[int]

::

 $ python /dir/to/P5Grand CEL.log -calc f -points 50
 $ python /dir/to/P5Grand CEL.log -calc a -points 50



``-Tmax``
*********

| -Tmax `[real >Tmax]`
| default : 10000
| unit : Kelvin

| The highest temperature to be calculated.
| If phase separation is not found below ``-Tmax``, **P5Grand** stop calculating before reaching ``-Tmax``

::

 $ python /dir/to/P5Grand CEL.log -calc p -Tmax 1000




``-Tmin``
*********

| -Tmax `[real >Tmax]`
| default : 300
| unit : Kelvin

| The starting temperature of the calculation.
| The lowest temperature to be calculated.

::

 $ python /dir/to/P5Grand CEL.log -calc p -Tmin 200




``-dT``
*********

| -Tmax `[real]`
| default : 100
| unit : Kelvin

| The basic temperature step to be calculated.

::

 $ python /dir/to/P5Grand CEL.log -calc p -dT 10



``-dTmin``
**********

| -Tmax `[real <dT]`
| default : dT/10
| unit : Kelvin

| The minimum temperature step.
| The temperature step can be reduced down to the ``-dTmin`` value to obtain more precise phase diagram.


::

 $ python /dir/to/P5Grand CEL.log -calc p -dTmin 100

