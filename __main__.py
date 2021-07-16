import read
from phase_diagram import draw_phase_diagram
from average_property import averaging,free_energy
import sys

Tmin	= 300
Tmax    = 10000
dT	= 100
dTmin   = None
points	= 32
file_name = 'CEL.log'
strain_name = 'BM_constant.dat'
calc    = 'p' # 'p' for phase diagram   'a' for average property
T       = 300
x       = None
h       = False
unit    = 'e'
#kB      =8.6173303*1E-5 #Boltzmann constant [eV/K]
#kB=1.3806488*1E-23 #Boltzmann constant [J/K]


argv=iter(sys.argv)
next(argv) #skip sys.argv[0] (= name (__main__.py))

for element in argv:
 if   element=='-Tmin':     Tmin   = float(next(argv))
 elif element=='-Tmax':     Tmax   = float(next(argv))
 elif element=='-dT':       dT     = float(next(argv))
 elif element=='-dTmin':    dTmin  = float(next(argv))
 elif element=='-points':   points = int  (next(argv))
 elif element=='-strain':   strain_name =  next(argv) 
 elif element=='-calc':     calc   =       next(argv)[0].lower()
 elif element=='-T':        T      = float(next(argv))
 elif element=='-x':        x      = float(next(argv))
 elif element=='-unit':     unit   =       next(argv)[0].lower()
 elif element=='-h':        h      = True
 elif element=='--help':    h      = True
 else: file_name = element


if dTmin==None: dTmin=dT/10.0
if dTmin>dT:    dTmin=dT; print("dTmin should be equal or smaller than dT")

if   unit=='e':   unit='eV'; kB=8.6173303*1E-5 #Boltzmann constant [eV/K]
elif unit=='j':   unit='J';  kB=1.3806488*1E-23 #Boltzmann constant [J/K]


if h==True:
 print ("COMMAND")
 print ("python __main__.py NameOfDatafile [options]")
 print ("")
 print ("-strain [the name of file containing strain energy]")
 print ("")
 print ("-calc   a|p|f   : p : calculating phase diagram")
 print ("                : f : calculating free energy")
 print ("                : a : calculating average_properties")
 print ("")
 print ("-unit   eV|J    : eV : all unit for energy become [eV]")
 print ("                  J  : all energy unit become [J]")
 print ("")
 print ("For -calc p")
 print ("-Tmax   [float] : Upper limit of calculated temperature. Unit : Kelvin")
 print ("-Tmin   [float] : Lower limit of calculated temperature. Unit : Kelvin")
 print ("-dT     [float] : usual interval of calculated temperature. Unit : Kelvin")
 print ("-dTmin  [float] : minimum interval of calculated temperature. Unit : Kelvin")
 print ("-points [int]   : the number of calculated compositions -1. composition interval=1/[int]")
 print ("")
 print ("For -calc f")
 print ("-T      [float] : target temperature. Unit : Kelvin")
 print ("-points [int]   : the number of calculated compositions -1. composition interval=1/[int]")
 print ("")
 print ("For -calc a")
 print ("-T      [float] : target temperature. Unit : Kelvin")
 print ("-x      [float] : target composition. must be within 0~1")
 print ("-points [int]   : the number of calculated compositions -1. Activated only when -x is not set. composition interval=1/[int]")
 print ("")
 print ("-h --help       : show this message")
 sys.exit()

elif calc=='p':
 print ("DataFile: %s"      %file_name  )
 print ("-strain : %s"      %strain_name)
 print ("-unit   : %s"      %unit  )
 print ("-calc   : phase_diagram"  )
 print ("-Tmax   : %7.1f K" %Tmax  )
 print ("-Tmin   : %7.1f K" %Tmin  )
 print ("-dT     : %7.1f K" %dT    )
 print ("-dTmin  : %7.1f K" %dTmin )
 print ("-points : %5d"     %points)

elif calc=='a':
 print ("DataFile: %s"      %file_name  )
 print ("-strain : %s"      %strain_name)
 print ("-unit   : %s"      %unit  )
 print ("-calc   : average_property")
 print ("-T      : %7.1f K" %T      )
 if x==None:
  print("-points : %5d"     %points  )
 else:
  print("-x      : %0.5f"   %x       )

elif calc=='f':
 print ("DataFile: %s"      %file_name  )
 print ("-strain : %s"      %strain_name)
 print ("-unit   : %s"      %unit  )
 print ("-calc   : free_energy")
 print ("-T      : %7.1f K" %T      )
 print ("-points : %5d"     %points  )
 
else:
# print('First letter for -calc should be "p" or "a".')
 sys.exit('First letter for -calc should be "p" or "a".')

#assert read.is_file(file_name), 'No such file: '+file_name
print ("\nRead %s" %file_name)
data=read.read_data_file(file_name)

#assert read.is_file(strain_name), 'No such file: '+strain_name
print ("Read %s\n" %strain_name)

if calc=='p':
 draw_phase_diagram(data,read.read_strain_file(strain_name),points,dT,Tmin,dTmin,Tmax,kB)
elif calc=='a':
 averaging(data,read.read_strain_file(strain_name),T,points,x,kB)
elif calc=='f':
 free_energy(data,read.read_strain_file(strain_name),T,points,kB)

#draw_phase_diagram(data,num=100,T0=300,dT=100) 
