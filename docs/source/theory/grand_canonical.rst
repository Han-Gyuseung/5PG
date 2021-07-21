Grand canonical ensemble
========================

The grand canonical ensemble treats the system as a collection of microstates.

Unlike the canonical ensemble, the grand canonical ensemble allows the local compositional fluctuation.

For a binary system
:math:`A_{x}B_{1-x}`
or a pseudobinary system
:math:`A_{x}B_{1-x}C`
, the grand canonical partition function, Z, is calculated as follows:

.. math::

 Z = \sum_{\sigma}\exp\left({ -\frac{\Delta E ^{total} _\sigma - \Delta \mu N_A }{k_B T} }\right)

, where :math:`N_A` and :math:`N_B` are the number of atom A and atom B in :math:`A_{x}B_{1-x}C`, and

.. math::
 \Delta \mu = \mu _A - \mu _B

:math:`\sigma` indicates a configuration (microstate). 
:math:`\mu` is a chemical potential of a species of atom. 
Total mixing energy :math:`\Delta E ^{total}`  is the sum of freely relaxed energy and the strain energy induced by compositional fluctuation.

.. math::

 \Delta E ^{total} _\sigma =\Delta E _\sigma + E^{strain}

The probability of a configuration is calculated as:

.. math::

 P _\sigma = \exp\left( -\frac{\Delta E ^{total} _\sigma - \Delta \mu N_A }{k_B T} \right) / Z

Then the entropy of this system is

.. math::
 
 S= \sum _\sigma P _\sigma \ln P _\sigma

The ensemble average of a property of interest, Y is given as:

.. math::

 \bar Y = \sum_{\sigma} Y _{\sigma} P _{\sigma}

When the Y is :math:`\Delta E`, the average energy is calculated.
With the entropy :math:`S`, the free energy :math:`F` at a finite temperature T can be calculated as:

.. math::
 
 S= -k_B \sum _\sigma P _\sigma \ln P _\sigma

 \Delta F= \Delta E - T \Delta S



:math:`\Delta \mu` is determined by following equation to satisfy the self-consistency for composition.

.. math::

 x = \sum_{\sigma} x _\sigma P _\sigma



A detailed explaination is in `this paper: J. Phys. D: Appl. Phys. 54, 045104 (2021) <https://doi.org/10.1088/1361-6463/abbf78>`_



