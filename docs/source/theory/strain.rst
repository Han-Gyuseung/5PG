Local strain energy
===================

By the local compositional fluctuation in a grand canonical ensemble, microstates with various local compositions coexist in a system.
If the lattice constant depends on compoisition, the lattice constant of each microstate also varies according to its local composition.
In this document, the strain indcued by this local compositional fluctuation is referred to as **local strain**.

..
 .. include:: strain_code.rst

In **P5Grand**, the local strain energy is fitted to Birch-Murnaghan equation of state.
[Ref]_

Brich-Murnahan equation of state is 

.. math::

 E^{strain} = \frac{9V_0B_0}{16} \left\{ \left[ \left( \frac{V_0}{V} \right)^{\frac{2}{3}}-1 \right]^3 B'_0 + \left[ \left( \frac{V_0}{V} \right)^{\frac{2}{3}}-1 \right]^2 \left[ 6-4\left( \frac{V_0}{V} \right)^{\frac{2}{3}} \right]  \right\}

, where :math:`V_0` and :math:`V` are free relaxed volume and the strained volume of a configuration, :math:`B_0` and :math:`B'_0` are bulk modulus and its derivative.

The governing equation for local strain energy can be changed by editing strain_energy.py.

.. note:: The result of strain_energy.py must be eV/[mixing atoms] or J/[mixing atoms].

.. [Ref]
  `F. D. Murnaghan, "The compressibility of media under extreme pressures" *Proc. Natl Acad. Sci. U.S.A.* 30 (1944) 244 <https://doi.org/10.1073/pnas.30.9.244>`__


