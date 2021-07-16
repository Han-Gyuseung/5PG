import matplotlib.pyplot as plt
import numpy as np
from grand_canonical import GrandCanonical
import sys

# Last way to calculate binodal, spinodal points
def points(grand,num=100,tol=1E-10,plot=0): #num:x interval become 1/num
    """
    Function to calculate binodal and spinodal points

    :param grand: instance of class GrandCanonical
    :type  grand: instance of class GrandCanonical
    :param num: value from ``-points``
    :type  num: int
    :param tol: tolerance for determining whether straight line or not
    :type  tol: float
    """
    x=np.linspace(0,1,num+1)
    y=np.zeros(num+1)
    #Y=np.zeros(num+1)
    
    for i in range(num+1):
        grand.set_x(x[i])
        y[i]=grand.F
        #Y[i]=y[i]
    
    old_list=[]
    for i in range(1,num):
        old_list.append(i)

    flag=1
    COUNT=0
    speedup_list=[]
    
    while(flag==1):
        new_list=[]
        flag=0

        for i in old_list:
            if y[i]*2-tol>y[i-1]+y[i+1]:
                y[i]=(y[i-1]+y[i+1])/2.0
                flag=1
                new_list.append(i-1)
                new_list.append(i)
                new_list.append(i+1)
                speedup_list.append(i-1)   #is it ok?
                speedup_list.append(i)
                speedup_list.append(i+1)  #Is it ok?
    
        old_list=sorted(set(new_list))
        
        if 0 in old_list:
            old_list.remove(0)
        if num in old_list:
            old_list.remove(num)
        
        #speedup start
        speedup_list=sorted(set(speedup_list))
    
        range_list=[]
        for i in range(len(speedup_list)):
            if x[i]!=0 and i!=len(speedup_list)-1:
                if speedup_list[i]+1!=speedup_list[i+1]:
                    right_i=speedup_list[i]
                    range_list.append([left_i,right_i])
                    left_i=speedup_list[i+1]
            elif x[i]==0.0:
                left_i=speedup_list[i]
            elif i==len(speedup_list)-1:
                right_i=speedup_list[i]
                if not left_i==right_i:
                    range_list.append([left_i,right_i])
    
        for i,j in range_list:
            for k in range(i,j):
                y0=(y[i]-y[j])/(x[i]-x[j])*(x[k]-x[j])+y[j]
                if y0<y[k]:
                    y[k]=(y[i]-y[j])/(x[i]-x[j])*(x[k]-x[j])+y[j]
        #speedup end
        
        if COUNT==0: spinodal=range_list[:]
        COUNT+=1
    
    if plot!=0:
        plt.plot(x,y)
        #plt.plot(x,Y)
        plt.show()
    #print ("It is done in", COUNT,"iteration")

    binodal_set=[]
    spinodal_set=[]
    for left,right in spinodal:
        spinodal_set.extend([[x[left],grand.T],[x[right],grand.T]])
    for left,right in range_list:
        binodal_set.extend([[x[left],grand.T],[x[right],grand.T]])
    return spinodal_set,binodal_set
    



def convert_list_to_dict(data_list): # [[x,T], ...] => {T:[x, ...], ...}
    data_dict={}
    for x,T in data_list:
        try: data_dict[T].append(x)
        except KeyError: data_dict[T]=[x]
    return data_dict

def find_nearest_set(x_target,x_list_at_T):
    min_diff=2
    for i in range(len(x_list_at_T)):
        diff=abs(x_list_at_T[i]-x_target)
        if diff<min_diff:
            j=i
            min_diff=diff
    return min_diff,j

def connect_nearest_points(data_dict):
    x_result=[]
    t_result=[]
    while (len(data_dict)!=0):
        T_list=sorted(data_dict)

        i=0

        T=T_list[i]
        T_init=T

        x=data_dict[T].pop(0)

        x_result.append(x)
        t_result.append(T)

        flag=1
        Flag=1
        while(flag==1):
            flag=0
            candidate=[]
            if i!=0:
                if not len(data_dict[T_list[i-1]])==0:
                    min_diff,j=find_nearest_set(x,data_dict[T_list[i-1]])
                    candidate.append([min_diff,j,i-1])
                    flag=1

            if i<len(T_list)-1:
                if not len(data_dict[T_list[i+1]])==0:
                    min_diff,j=find_nearest_set(x,data_dict[T_list[i+1]])
                    candidate.append([min_diff,j,i+1])
                    flag=1

            if Flag!=0:
                if not len(data_dict[T_list[i]])==0:
                    min_diff,j=find_nearest_set(x,data_dict[T_list[i]])
                    candidate.append([min_diff,j,i])
                    flag=1

            if flag==0: break

            if len(candidate)>1:
                if sorted(candidate)[0][0]==sorted(candidate)[1][0]:
                    tmp,j,i=sorted(candidate)[1]
                else:
                    tmp,j,i=sorted(candidate)[0]
            else:
                tmp,j,i=sorted(candidate)[0]

            #tmp,j,i=sorted(candidate)[0]
            T=T_list[i]
            x=data_dict[T].pop(j)
            x_result.append(x)
            t_result.append(T)
            Flag=1
            if len(data_dict[T_list[i]])==0:
                del data_dict[T_list[i]]
                T_list=sorted(data_dict)
                Flag=0

            if T==T_init: break

    return x_result,t_result

def split_line(x_one_line,T_one_line):
    x_multi_line=[]
    T_multi_line=[]
    i_prev=0
    for i in range(len(x_one_line)-1):
     if(x_one_line[i]>x_one_line[i+1]):
      x_multi_line.append(x_one_line[i_prev:i+1])
      T_multi_line.append(T_one_line[i_prev:i+1])
      i_prev=i+1
    x_multi_line.append(x_one_line[i_prev:])
    T_multi_line.append(T_one_line[i_prev:])
    return x_multi_line, T_multi_line
    

def plot_line(bx,bt,sx,st,Tmin,Tmax):
    plt.xlim(0,1)
    plt.ylim(Tmin,Tmax)

    for i in range(len(sx)):
     plt.plot(sx[i],st[i],'r--')
    for i in range(len(bx)):
     plt.plot(bx[i],bt[i],'r-')

    plt.show()


def align_data_to_plot_line(binodal,spinodal,Tmin,Tmax):

    Binodal=convert_list_to_dict(binodal)
    Spinodal=convert_list_to_dict(spinodal)

    Bx,Bt=connect_nearest_points(Binodal)
    Sx,St=connect_nearest_points(Spinodal)

    split_Bx,split_Bt=split_line(Bx,Bt)
    split_Sx,split_St=split_line(Sx,St)
    
    plot_line(split_Bx,split_Bt,split_Sx,split_St,Tmin,Tmax)
    #return Bx,Bt,Sx,St


def align_data_to_plot_point(binodal,spinodal,Tmin,Tmax):
    bx=[point[0] for point in binodal]
    bT=[point[1] for point in binodal]
    sx=[point[0] for point in spinodal]
    sT=[point[1] for point in spinodal]

    plt.xlim(0,1)
    plt.ylim(Tmin,Tmax)

    for i in range(len(sx)):
     plt.plot(sx[i],sT[i],'bx')
    for i in range(len(bx)):
     plt.plot(bx[i],bT[i],'ro')

    plt.show()

    



def draw_phase_diagram(data,strain_list,num,dT,T0,dT_tol,maximum_T,kB):
    """
    Function to calculate and draw phase diagram
    
    :param data: data obtained by read_data_file in read.py
    :type  data: dictionary (data[composition][energy][i_th_prop][property[i_th_prop]]=degeneracy)
    :param strain_list: parameters to fit local strain energy
    :type  strain_list: list
    :param num: value from ``-points``
    :type  num: int
    :param dT: value from ``-dT``
    :type  dT: float
    :param T0: value from ``-Tmin``
    :type  T0: float
    :param dT0: value from ``-dTmin``
    :type  dT0: float
    :param maximum_T: value from ``-Tmax``
    :type  maximum_T: float
    :param kB: Boltzmann constant
    :type  kB: float
    """

    if dT_tol==None or dT_tol>dT:
        dT_tol=dT/10.0
    
    spinodal=[]
    binodal=[]
    
    sys.stdout.write('\r on calculating at {:10.3f} K'.format(T0))
    sys.stdout.flush()

    T_final=None
    a=GrandCanonical(T0,data,strain_list,kB)
    s0,b0=points(a,num)
    spinodal.extend(s0)
    binodal.extend(b0)
    Num_spinodal_point=len(s0)
    Num_binodal_point=len(b0)

    Tmin=T0
    dT0=dT
    T1=T0+dT
    flag=0
    while (Num_binodal_point>0 and T1<maximum_T):
        sys.stdout.write('\r on calculating at {:10.3f} K'.format(T1))
        sys.stdout.flush()

        a=GrandCanonical(T1,data,strain_list,kB)
        
        s1,b1=points(a,num)
        spinodal.extend(s1)
        binodal.extend(b1)

        if Num_spinodal_point!=len(s1) or Num_binodal_point!=len(b1): #Search at more lower temperature
            if flag==0:
                Tmax=T1
                Num_spinodal_point_at_Tmax=len(s1)
                Num_binodal_point_at_Tmax=len(b1)
            dT=dT/2.0
            T1=T0+dT
            flag=1
        else: # Num_spinodal_point==len(s1) and Num_binodal_point==len(b1)
            if flag==1:
                dT=dT/2.0
            T0=T1
            T1=T0+dT
   
        if dT<dT_tol:
            dT=dT0
            #T1=T0+dT
            T_final=T0
            T1=Tmax+dT
            T0=Tmax
            Num_spinodal_point=Num_spinodal_point_at_Tmax
            Num_binodal_point=Num_binodal_point_at_Tmax
            flag=0

    sys.stdout.write('\rFinal temperature : {:10.3f} K\n'.format(T_final))
    sys.stdout.flush()

    #print ("\nBinodal points and spinodal points are calculated.")
    #print ("The code draws a plausible diagram with data points.")
    #print ("But there is no guarantee that line is correct.")
    #print ("If a diagram seems to be wrong, redaw a diagram with the data points")

    #plot phase diagram
    #align_data_to_plot_line(binodal,spinodal,Tmin,Tmax)
    align_data_to_plot_point(binodal,spinodal,Tmin,Tmax)

    #a=GrandCanonical(500,data,strain_list,kB)
    #tmp_x=np.linspace(0,1,num+1)
    #tmp_y=np.zeros(num+1)
    #for i in range(num+1):
    #    a.set_x(tmp_x[i])
    #    tmp_y[i]=a.F
    #    plt.xlim(0,1)
    #
    #plt.xlim(0,1)
    #plt.plot(tmp_x,tmp_y,'b.')
    #
    #plt.show()
