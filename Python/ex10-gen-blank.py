#!/usr/bin/env python3
import sys
import json
from Icestudio import Ice, Blocks, Dependencies

FILE_SRC = "../Test-files/Icestudio/temp-wire.ice"
FILE_TARGET = "../Test-files/temp.ice"

#-- Read original file created with icestudio
ice = Ice()
ice.open_file(FILE_SRC)

obj = ice.design.graph.wires
print(type(obj))

#-- Save as an .ice file
with open(FILE_TARGET, "w") as outfile:
    json.dump(ice.json(), outfile, indent=2, ensure_ascii=False)


#-- Compare the two files
import filecmp

if filecmp.cmp(FILE_SRC, FILE_TARGET):
    print("Los archivos son iguales")
else:
    print("Los archivos son diferentes")

