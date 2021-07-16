Introduction
============


Overview
---------

**5PG** allows the efficient property calculation using the grand canonical ensemble.

The requirements for the program are the sufficient data for the properties of configurations and the parameters to calculate local strain. 
It doesn't matter wheter the data was obtained by density functional theory, cluster expansion, or something else.

The aim here is to calculate a *thermodynamics properties* such as average energy, free energy, and phase diagram and an *ensemble average* of a property such as bandgap for a binary (pseudobinary) system.

For better accuracy, the grand canonical ensemble is implemented which allows compositional fluctuation, allowing for more realistic simulations. 


Limitation
----------

* The program simulates only thermodynamic equilibrium state
* Current version only works for binary systems and pseudobinary systems

