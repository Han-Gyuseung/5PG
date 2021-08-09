def local_strain(strain_parameter,local_x,global_x,N_atom):
    '''
    A function to calculate local strain energy
    
    :param strain_parameter: fitting parameters
    :type  strain_parameter: list
    :param local_x: local composition
    :type  local_x: float 0~1
    :param global_x: average composition
    :type  global_x: float 0~1
    :param N_atom: the number of mixing atoms
    :type  N_atom: int
    :return: local strain energy [eV/mixing atom] or [J/mixing atom]
    :rypte: float
    '''

    return Birch_Murnaghan(strain_parameter,local_x,global_x,N_atom)


def Birch_Murnaghan(strain_parameter,local_x,global_x,N_atom):
    '''
    A function to calculate local strain energy according to Birch-Murnaghan equation of state. 
    Assumption: B0V0 and B0' is constant regardless of local composition
    
    :param strain_parameter: fitting parameters
    :type  strain_parameter: [B0V0, B0', 1, V0(x=1)/V0(x=0)] or [B0V0, B0', V0(x=0), V0(x=1)]
    :param local_x: local composition
    :type  local_x: float 0~1
    :param global_x: average composition
    :type  global_x: float 0~1
    :param N_atom: the number of mixing atoms
    :type  N_atom: int
    :return: local strain energy calculated from Birch-Murnaghan equation of state [eV/mixing atom] or [J/mixing atom]
    :rypte: float
    '''
    
    #strain_parameter=[B0V0, B0', 1, V0(x=1)/V0(x=0)] or  [B0V0, B0', V0(x=0), V0(x=1)]
    strain=[float(strain_parameter[0]),float(strain_parameter[1])]
    volume=[float(strain_parameter[2]),float(strain_parameter[3])] # [V(x=0),V(x=1)]
    lattice=[volume[0]**(1/3.), volume[1]**(1/3.)]

    V0_over_V_2_3_1=((lattice[0]+(lattice[1]-lattice[0])*local_x)/(lattice[0]+(lattice[1]-lattice[0])*global_x))**2-1

    return strain[0]*9/16.0*((strain[1]-4.0)*V0_over_V_2_3_1**3+2*V0_over_V_2_3_1**2)


def Murnaghan(strain_parameter,local_x,global_x,N_atom):
    '''
    A function to calculate local strain energy according to Murnaghan equation of state. 
    Assumption: K0V0 and K0' is constant regardless of local composition
    
    :param strain_parameter: fitting parameters
    :type  strain_parameter: [K, K', 1, V0(x=1)/V0(x=0)] or [K, K', V0(x=0), V0(x=1)]
    :param local_x: local composition
    :type  local_x: float 0~1
    :param global_x: average composition
    :type  global_x: float 0~1
    :param N_atom: the number of mixing atoms
    :type  N_atom: int
    :return: local strain energy calculated from Birch-Murnaghan equation of state [eV/mixing atom] or [J/mixing atom]
    :rypte: float
    '''

    strain=[float(strain_parameter[0]),float(strain_parameter[1])]
    volume=[float(strain_parameter[2]),float(strain_parameter[3])] # [V(x=0),V(x=1)]
    lattice=[volume[0]**(1/3.), volume[1]**(1/3.)]
    V=(lattice[0]+(lattice[1]-lattice[0])*global_x)**3
    V0=(lattice[0]+(lattice[1]-lattice[0])*local_x)**3
    #V_over_V0=((lattice[0]+(lattice[1]-lattice[0])*global_x)/(lattice[0]+(lattice[1]-lattice[0])*local_x))**3

    return strain[0]*V0*(1/(strain[1]*(strain[1]-1))*(V/V0)**(1-strain[1])+V/(strain[1]*V0)-1/(strain[1]-1))
