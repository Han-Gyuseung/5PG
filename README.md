5PG
=====

***Python Package for Property Prediction of Pseudobinary systems using Grand canonical ensemble***

[[manual]](https://5pg.readthedocs.io/en/latest/index.html)

**A python tool to calculate the average property using the grand canonical ensemble.** <br>
If you have used ***5PG*** to obtain **phase diagram**, please cite the following article (https://doi.org/10.1088/1361-6463/abbf78): <br>
> Gyuseung Han, In Won Yeu, Jaehong Park, Kun Hee Ye, Seung-Cheol Lee, Cheol Seong Hwang, and Jung-Hae Choi, "Effect of local strain energy to predict accurate phase diagram of III-V pseudobinary systems: case of Ga(As,Sb) and (In,Ga)As," J. Phys. D: Appl. Phys. 54, 045104 (2021)

If you have used ***5PG*** to obtain **average property**, please cite the following article (--): <br>
> Gyuseung Han, In Won Yeu, Kun Hee Ye, Cheol Seong Hwang, and Jung-Hae Choi, "Atomistic prediction on the composition- and configuration- dependent bandgap of Ga(As,Sb) using cluster expansion and ab initio thermodynamics," submitted.


<br>
You can see manual at https://5pg.readthedocs.io/en/latest/index.html

<br>

## Usage
### Pre-process
- **data file** <br>
The default name is CEL.log <br>
Each row indicates a configuration. <br>
The first column is composition, and the second column is energy. <br>
The third column is property. But the third column is optional. <br>

- **strain energy** <br>
```$ python <5PGDirectory>/util/extract_strain.py <species of atom A> <species of atom B>``` <br>
For example, for GaAs_x Sb_1-x, species of atom A is `As` and species of atom B is ``Sb``


### Process
- **phase diagram**
```
$ python <5PGDirectory> -calc p
```
- **free energy**
```
$ python <5PGDirectory> -calc f
```
- **average property**
```
$ python <5PGDirectory> -calc a
```

In order to see all of the available options and their default values: <br>
```
$ python <5PGDirectory> -calc a
```

<br>

## Requirements
python2 or python3 <br>
numpy <br>
matplotlib <br>
scipy : option

## etc
contact
Dr. Gyuseung Han (hgs911121@gmail.com)
* ORCID: https://orcid.org/0000-0002-5553-0741

Dr. Jung-Hae Choi (choijh@kist.re.kr) 
* homepage: https://sites.google.com/view/junghaechoi/publication/code
