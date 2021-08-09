Introduction
============


Overview
---------

**P5Grand** (**P**\ ython **P**\ ackage for **P**\ roperty **P**\ rediction of **P**\ seudobinary systems using **Grand** canonical ensemble) predicts *thermodynamics properties* (such as average energy (*E*), free energy (*F*), and phase diagram) and ensemble-average properties (such as bandgap and dielectric constant) for pseudobinary systems using grand canonical ensemble.

The input data for **P5Grand** are the sufficient data of the energies and properties of interest (PoI) for various compositions and configurations in a pseudobinary system.
For better accuracy, the grand canonical ensemble is implemented which allows the compositional fluctuation to simulate more realistic situations. 
Therefore, parameters for calculating the local strain are required as input in order to be treated as a grand canonical ensemble. The input data can obtained from the density functional theory calculations, cluster expansion method or empirical data. 



Limitation & Current status
---------------------------

* **P5Grand** simulates only thermodynamic equilibrium state.
* **P5Grand** assumes that local strain energy is configuration-independent property.
* Current version of **P5Grand** works only for binary systems and pseudobinary systems.
* Current version of **P5Grand** supports the parsers (``tool``) that extracts parameters for strain energy only from ``OUTCAR`` of `VASP <https://www.vasp.at/>`_.


