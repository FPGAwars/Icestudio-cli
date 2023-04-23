#!/usr/bin/env python3
import sys
import json
from Icestudio import Ice, Blocks, Dependencies

FILE_SRC = "../Test-files/Icestudio/08-basic-output-label-2.ice"
FILE_TARGET = "../Test-files/temp.ice"

#-- Read original file created with icestudio
ice = Ice()
ice.open_file(FILE_SRC)

#-- Save as an .ice file
with open(FILE_TARGET, "w") as outfile:
    json.dump(ice.json(), outfile, indent=2)
    #test = ice.design.graph.blocks.list[0].data
    #print(test.json())


#-- Compare the two files
import filecmp

if filecmp.cmp(FILE_SRC, FILE_TARGET):
    print("Los archivos son iguales")
else:
    print("Los archivos son diferentes")

