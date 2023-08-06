#!/usr/bin/env python3
import argparse
import ase 
import numpy as np
from ase.build import bulk, make_supercell
def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("output", type=str)
    return vars(parser.parse_args())

def main(output:str, repeat: int):
    atoms=bulk("Ar", "fcc", a=5.36, cubic=True)
    atoms=make_supercell(atoms,np.diag([repeat,repeat,repeat]))
    ase.io.write(output,atoms,"xyz")    
    print(atoms.cell, atoms.get_volume())


if __name__=="__main__":
    main(**get_args())


