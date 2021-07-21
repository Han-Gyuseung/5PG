Introduction
============


Overview
---------

**5PG** (**P**\ ython **P**\ ackage for **P**\ roperty **P**\ rediction of **P**\ seudobinary systems using **G**\ rand canonical ensemble) predicts *thermodynamics properties* (such as average energy (*E*), free energy (*F*), and phase diagram) and ensemble-average properties (such as bandgap and dielectric constant) for pseudobinary systems using grand canonical ensemble.

The input data for **5PG** are the sufficient data of the energies and properties of interest (PoI) for various compositions and configurations in a pseudobinary system.
For better accuracy, the grand canonical ensemble is implemented which allows the compositional fluctuation to simulate more realistic situations. 
Therefore, parameters for calculating the local strain are required as input in order to be treated as a grand canonical ensemble. The input data can obtained from the density functional theory calculations, cluster expansion method or empirical data. 



Limitation & Current status
---------------------------

* **5PG** simulates only thermodynamic equilibrium state.
* Current version of **5PG** works only for binary systems and pseudobinary systems.
* Current version of **5PG** supports the parsers that extracts parameters for strain energy only from ``OUTCAR`` of `VASP <https://www.vasp.at/>`_.

