def local_strain(strain_parameter,local_x,global_x,N_atom):
    '''
    strain_parameter=[B0V0, B0', 1, V0(x=1)/V0(x=0)]
    or
    strain_parameter=[B0V0, B0', V0(x=0), V0(x=1)]

    return local strain energy fitted to Birch-Murnaghan equation of state in [eV/mixing atom] or [J/mixing atom]
    The unit is determined by strain_parameter.
    '''
    strain=[float(strain_parameter[0]),float(strain_parameter[1])]
    volume=[float(strain_parameter[2]),float(strain_parameter[3])] # [V(x=0),V(x=1)]
    lattice=[volume[0]**(1/3.), volume[1]**(1/3.)]

    V0_over_V_2_3_1=((lattice[0]+(lattice[1]-lattice[0])*local_x)/(lattice[0]+(lattice[1]-lattice[0])*global_x))**2-1

    return strain[0]*9/16.0*((strain[1]-4.0)*V0_over_V_2_3_1**3+2*V0_over_V_2_3_1**2)
