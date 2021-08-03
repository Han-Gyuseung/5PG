import os, sys
from scipy.optimize import curve_fit

#For A(x) B(1-x), each elements are
A=sys.argv[1]
B=sys.argv[2]

def get_info(outcar,subdirname):
 """
 A function to read OUTCAR
 
 :param outcar: path to OUTCAR
 :type  outcar: string
 :param subdirname: name of directory
 :type  subdirname: string
 
 :return: data in OUTCAR
 :rtype: dictionary
 """
 with open(outcar,'r') as File:
  lines=File.readlines()
  element_kind=[]
  element_num=[]
  elements={A:0, B:0}
  element_total_num=0

  for line in lines:
   if 'VRHFIN' in line:
    element_kind.append(line.replace('=',' ').replace(':',' ').split()[1])
   if 'ions per type' in line:
    element_num=line.split()[4:]
    break;
  
  for i in range(len(element_kind)):
   elements[element_kind[i]]=int(element_num[i])
   element_total_num+=int(element_num[i])

  for line in reversed(lines):
   if 'TOTEN' in line:
    energy=float(line.split()[4])
   if 'volume of cell' in line:
    volume=float(line.split()[4])
    break;

 return {'energy':energy/(elements[A]+elements[B]), \
         'volume':volume, \
         'isStrained':isStrained(subdirname), \
         'elements':elements, \
         'r_volume':None, \
         'dE':None, \
         'N_atom': element_total_num, \
         'AandB':elements[A]+elements[B]
        }


def isStrained(subdirname):
 if subdirname=='unstrained':
  return False
 else:
  return True




configDirList=[]
N_atom=0

for path_of_dir, dirs_in_dir, files_in_dir in os.walk('.'):
 if 'unstrained' in dirs_in_dir:
  tmp=[]
  for subdirname in dirs_in_dir:
   if os.path.isfile(os.path.join(path_of_dir,subdirname,'OUTCAR')):
    tmp.append(get_info(os.path.join(path_of_dir,subdirname,'OUTCAR'),subdirname))
    N_atom=tmp[-1]['N_atom']
  if len(tmp)>1:
   configDirList.append(tmp)
   if(tmp[-1]['N_atom'] != N_atom):
    print ("Number of atom is different in %s" %(path_of_dir))



for configDir in configDirList:
 for info in configDir:
  if info['isStrained']==False:
   unstrained=info
#   unstrained['AandB']=unstrained['elements'][A]+unstrained['elements'][B]

 for info in configDir:
#  info['AandB']=info['elements'][A]+info['elements'][B]
  info['composition']=info['elements'][A]/(info['AandB']*1.0)
  info['r_volume']=info['volume']/unstrained['volume'] * unstrained['AandB']/info['AandB']
  info['dE']=info['energy'] - unstrained['energy']# * unstrained['AandB']/info['AandB']  #dE : per mixing elements
  if info['composition']==0.0 and info['isStrained']==False: V0=info['volume']
  elif info['composition']==1.0 and info['isStrained']==False: V1=info['volume']



data={} # data[x]={'r_volume': [...], 'dE': [...]}
Data={'r_volume':[], 'dE':[]} # Data={'r_volume': [...], 'dE': [...]}
for configDir in configDirList:
 for info in configDir:
  if not info['composition'] in data:
   data[info['composition']]={'r_volume':[], 'dE':[]}

  data[info['composition']]['r_volume'].append(info['r_volume'])
  data[info['composition']]['dE'].append(info['dE'])
  Data['r_volume'].append(info['r_volume'])
  Data['dE'].append(info['dE'])


# fitting
def BM_EOS(rV,a,b):
 """
 Birch-Murnaghan equation of state
 
 :param rV: V/V0
 :type  rV: float
 :param a: B0V0
 :type  a: float
 :param b: B'0
 :type  b: float
 
 :return: strain energy per mixing atom
 :rtype: float
 """
 rV23_1 = rV**(-2/3.)-1
 return a*9/16.0 * ((b-4)*rV23_1**3 + 2*rV23_1**2) # per mixing atom

popt,pcov = curve_fit(BM_EOS, Data['r_volume'],Data['dE']) #popt : a = B0V * N_atom / (N(A)+N(B))  where V is volume per atom.   b=B0'

volume_range=V1/V0 # 1 ~ volume_range (can be either >1, <1)
#lattice=[1,volume_range**(1/3.)]

File=open('BM_constant.dat','w')
File.write(' '.join(str(i) for i in popt))
File.write(' 1 '+str(volume_range)+'\n')
File.close()
