from math import exp,log
from math import factorial as fact
from local_strain import local_strain
#from strain_function import strain_func
#kB=8.6173303*1E-5 #Boltzmann constant [eV/K]
#kB=1.3806488*1E-23 #Boltzmann constant [J/K]

# Calculate canonical average energy and entropy 
def canonical_ensemble(T,data,kB):
    """
    Function to calculate properties using canonical ensemble
    
    :param T: temperature [K]
    :type  T: float (>0)
    :param data: data obtained by read_data_file in read.py
    :type  data: dictionary (data[composition][energy][i_th_prop][property[i_th_prop]]=degeneracy)
    :param kB: Boltzmann constant in [eV/K] or [J/K]
    :type  kB: float

    :return: canonical ensemble result, the number of mixing atom in a cell
    :rtype:  dictionary {composition:[average energy, S/kB, average property]}, int
    """
    N_atom=len(data)-1
    #canonical_result={composition:[avgE,S_over_kB]} #[eV/mixingAtoms, eV/supercell]
    canonical_result={}
    for energy in data[0.0]:
        E0=energy #energy at x=0
    for energy in data[1.0]:
        E1=energy #energy at x=1
    num_prop=len(data[1.0][E1])

    for x in data:
        N_cal=0
        Z=0
        avgpropZ=[0]*num_prop
        S_over_k=0
        PlnP=0
        minE=min(data[x]) # To avoid error (OverflowError: math range error)

        for energy in data[x]:
            Exp=exp(-1.0*(energy-minE)*N_atom/(kB*T)) 
            Z+=data[x][energy][0][energy]*Exp
            for i in range(num_prop):
                for prop in data[x][energy][i]:
                    avgpropZ[i]+=prop*data[x][energy][i][prop]*Exp
            N_cal+=data[x][energy][0][energy]
        for energy in data[x]:
            Exp=exp(-1.0*(energy-minE)*N_atom/(kB*T))
            PlnP-=data[x][energy][0][energy]*Exp/Z*log(Exp/Z)

        avgprop=[_/Z for _ in avgpropZ]
        avgprop[0]=avgprop[0]-E0*(1-x)-E1*x
        S_over_k=PlnP-log(N_cal)+log(fact(N_atom)/fact(N_atom-N_atom*x)/fact(N_atom*x))
        avgprop.append(S_over_k)

        canonical_result[x]=avgprop

    return canonical_result,N_atom


class GrandCanonical(object):
    """
    Class to obtain average properties using grand canonical ensemble

    :param T: temperature [K]
    :type  T: float
    :param data: data obtained by read_data_file in read.py
    :type  data: dictionary (data[composition][energy][i_th_prop][property[i_th_prop]]=degeneracy)
    :param strain_list: parameters to fit local strain energy
    :type  strain_list: list
    :param kB: Boltzmann constant
    :type  kB: float
    """
    def __init__(self, T, data, strain_list, kB): #Kelvin
        self._canonical,self.N_atom=canonical_ensemble(T,data,kB)
        self._T=T
        self.kB=kB
        self._kT=kB*T
        self._g={}
        self._num_prop=len(self._canonical[0.0])-1
        self.average=[0.0]*self._num_prop
        for local_x in self._canonical:
            self._g[local_x]=exp(self._canonical[local_x][-1])
        self.strain_list=strain_list


    @property
    def T(self):
        """
        temperature
        """
        return self._T


    def E(self):
        return self.average[0]


    def __average_x(self,mu,total_E):
        avgXZ=0.0
        avgEZ=0.0
        avgprop=[0.0]*self._num_prop
        Z=0.0
        S_over_k=0.0
        dist={}

        # Purpose of b is preventing math range error which comes from exp(700) in python.
        b=max([-total_E[local_x]/self._kT+log(self._g[local_x])+self.N_atom*local_x*mu/self._kT+700 for local_x in self._canonical])
        b=max(b, -total_E[0.0]/self._kT+log(self._g[0])+700)

        for local_x in self._canonical:
            PZ=exp(-total_E[local_x]/self._kT+log(self._g[local_x])+self.N_atom*local_x*mu/self._kT-b)
            avgXZ+=local_x*PZ
            avgEZ+=total_E[local_x]*PZ
            for i in range(1,self._num_prop):
                avgprop[i]+=self._canonical[local_x][i]*PZ
            Z+=PZ

        for local_x in self._canonical:
            PZ=exp(-total_E[local_x]/self._kT+log(self._g[local_x])+self.N_atom*local_x*mu/self._kT-b)
            dist[local_x]=PZ/Z

            if dist[local_x]!=0:
                S_over_k+=dist[local_x]*(self._canonical[local_x][-1]-log(dist[local_x]))

        for i in range(1,self._num_prop):
            avgprop[i]/=Z
        avgprop[0]=avgEZ/Z/self.N_atom


        return avgXZ/Z, avgprop, dist, S_over_k/self.N_atom #unitless, eV/mixingAtoms, unitless, 1/atom


    def __find_mu(self, global_x,total_E):
        if global_x==1 or global_x==0:
            return 1400*(global_x-0.5)*self._kT  #Actually, infinite and -infinite is right, not 1400. But 1400 is enough high and the maximum value without math range error.

        guess1=700*self._kT
        result1=self.__average_x(guess1,total_E)[0]
        guess2=-700*self._kT
        result2=self.__average_x(guess2,total_E)[0]
        new_guess=(guess1+guess2)/2.0
        new_result=self.__average_x(new_guess,total_E)[0]
        if (result1<global_x):
            print ("global_x is too high")
            return guess1
            exit()
        elif (result2>global_x):
            print ("global_x is too low")
            return guess2

        while(abs(guess1-guess2)>1E-12):
            new_guess=(guess1+guess2)/2.0
            new_result=self.__average_x(new_guess,total_E)[0]
            if (new_result-global_x)*(result1-global_x)<0:
                guess2=new_guess
                result2=new_result
            elif (new_result-global_x)*(result2-global_x)<0:
                guess1=new_guess
                result1=new_result
            elif new_result==global_x:
                break
            else:
                print ("Something wrong during chemical potential calculation")
                print (guess1,result1)
                print (guess2,result2)
                print (new_guess,new_result)

        return new_guess


    def set_x(self, global_x):
        """
        Instance method to set average composition

        :param global_x: average composition
        :type  global_x: float (0~1)
        """
        if global_x<0.0 or global_x>1.0:
            print ("x must be within the range from 0 to 1")
            exit()
        # add strain energy
        total_E={}
        for local_x in self._canonical:
            total_E[local_x]=self._canonical[local_x][0]*self.N_atom+self.__strain_func(local_x,global_x,self.N_atom)  #energy per supercell

        dist={}

        mu=self.__find_mu(global_x,total_E)

        if global_x==1 or global_x==0:
            avgX=global_x
            avgE=total_E[global_x]
            for local_x in self._canonical: dist[local_x]=0.0
            dist[global_x]=1.0
            S_over_kB=0.0
        avgX,avgprop,dist,S_over_kB=self.__average_x(mu,total_E)

        self.mu=mu
        self.F=avgprop[0]-self._kT*S_over_kB
        #self.E=avgprop[0]
        self.average=avgprop
        self.S=S_over_kB*self.kB
        #self.s=S_over_kB
        self.distribution=dist


    def __strain_func(self,local_x,global_x,N_atom):

        #strain=[float(self.strain_list[0]),float(self.strain_list[1])]
        #volume=[float(self.strain_list[2]),float(self.strain_list[3])] # [V(x=0),V(x=1)]
        #lattice=[volume[0]**(1/3.), volume[1]**(1/3.)]

        #V0_over_V_2_3_1=((lattice[0]+(lattice[1]-lattice[0])*local_x)/(lattice[0]+(lattice[1]-lattice[0])*global_x))**2-1
        #E_strain=strain[0]*9/16.0*((strain[1]-4.0)*V0_over_V_2_3_1**3+2*V0_over_V_2_3_1**2)

        E_strain=local_strain(self.strain_list,local_x,global_x,N_atom)
        return E_strain*N_atom
