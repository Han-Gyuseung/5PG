Local strain energy
===================

When the lattice constant depends on the local composition, lattice of microstates varies according to its composition.
By local compositional fluctucation, microstates with various local composition coexist.
In this document, the strain induced by local compositional fluctuation is referred to as **local strain**.

In 5PG, the local strain energy is fitted to Birch-Murnaghan equation of state.
[Ref]_

Brich-Murnahan equation of state is 

.. math::

 E^{strain} = \frac{9V_0B_0}{16} \left\{ \left[ \left( \frac{V_0}{V} \right)^{\frac{2}{3}}-1 \right]^3 B'_0 + \left[ \left( \frac{V_0}{V} \right)^{\frac{2}{3}}-1 \right]^2 \left[ 6-4\left( \frac{V_0}{V} \right)^{\frac{2}{3}} \right]  \right\}

, where :math:`V_0` and :math:`V` are free relaxed volume and strained volume, :math:`B_0` and :math:`B'_0` are bulk modulus and its derivative.

The governing equation for local strain energy can be changed by editing strain_energy.py.

.. note:: The result of strain_energy.py must be energy per mixing atom.

.. [Ref]
  `F. D. Murnaghan, "The compressibility of media under extreme pressures" *Proc. Natl Acad. Sci. U.S.A.* 30 (1944) 244 <https://doi.org/10.1073/pnas.30.9.244>`__


