import matplotlib.pyplot as plt
import numpy as np
from grand_canonical import GrandCanonical
import sys

def print_it(x,float_list):
    string="%0.5f " % x
    for _ in float_list:
        string+= "%10.6f " % _
    print(string)
#    return string

def averaging(data,strain_list,T,num,x,kB):
    """
    Function to calculate and print average property using grand canonical ensemble

    :param data: obtained by read_data_file in read.py
    :type  data: dictionary
    :param strain_list
    :param strain_list: parameters to fit local strain energy
    :type  strain_list: list
    :param T: temperature [K]
    :type  T: float
    :param num: value from ``-points``
    :type  num: int
    :param x: value from ``-x``
    :type  x: float
    :param kB: Boltzmann constant
    :type  kB: float
    """
#    xs=[]
#    asdf=[[]]

    a=GrandCanonical(T,data,strain_list,kB)
    num_prop=len(a.average)
    label="   x       energy "
    for i in range(1,num_prop):
        label+="%10s" %"property"+str(i)+" "
#        asdf.append([])
    print (label)

    if x==None:
        for i in range(num+1):
            x=i/(num+0.0)
            a.set_x(x)
            print_it(x,a.average)
#            xs.append(x)
#            for j in range(num_prop):
#                asdf[j].append(a.average[j])
#        for i in range(len(asdf)):
#            plt.plot(xs,asdf[i])
#        plt.show()

    else:
        a.set_x(x)
        print_it(x,a.average)

def free_energy(data,strain_list,T,num,kB):
    """
    Function to calculate and print free energy using grand canonical ensemble

    :param data: obtained by read_data_file in read.py
    :type  data: dictionary
    :param strain_list
    :param strain_list: parameters to fit local strain energy
    :type  strain_list: list
    :param T: temperature [K]
    :type  T: float
    :param num: value from ``-points``
    :type  num: int
    :param kB: Boltzmann constant
    :type  kB: float
    """
    a=GrandCanonical(T,data,strain_list,kB)
    for i in range(num+1):
        x=i/(num+0.0)
        a.set_x(x)
        print("%0.5f %10.6f" %(x, a.F))
