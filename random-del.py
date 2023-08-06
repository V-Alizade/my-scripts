#!/usr/bin/env python3
import argparse   #command line argument
import qcelemental as qcel
import numpy as np
def delete_atoms(mol: qcel.models.Molecule,delete: int)-> qcel.models.Molecule:
    natoms=len(mol.symbols) #len is gives the lenghts of the instance back; here natom is a variable which holds the integer number
    included_atoms=sorted(np.random.choice(natoms,(natoms-delete,),False)) 
    #print(natoms)
    #print(included_atoms)
    symbols=[mol.symbols[atom]for atom in included_atoms]
    geometry=[mol.geometry[atom]for atom in included_atoms]
    return qcel.models.Molecule(symbols=symbols, geometry=geometry)
def get_args():
    parser=argparse.ArgumentParser()  #it is a specifier for arg parsering. and we want to have instance for the parser. parser has not doing any thing
    parser.add_argument("input",type=str) #now we add argumnet for parser .this step is specification
    parser.add_argument("--delete",type=int,default=0)
    return vars(parser.parse_args()) #now we are using parser, 
def main(input,delete):
    mol=qcel.models.Molecule.from_file(input)
    mol=delete_atoms(mol,delete)
    print(mol.to_string(dtype="xyz"))

if __name__ == "__main__":
    main(**get_args())
     