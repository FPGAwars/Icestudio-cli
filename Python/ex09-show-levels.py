#!/usr/bin/env python3
import sys
from Icestudio import Ice, Blocks, Dependencies

#-- Manual file
#FILE = ""
FILE = "../Test-files/test-18-k-simple-two-levels.ice"


if FILE == "":

    #-- The first argument is the .ice circuit to analyze
    if ( len(sys.argv) < 2 ):
        print("No icestudio file")
        print("Usage: ex08-ice.py icestudio-file")
        print()
        sys.exit()

    file = sys.argv[1]
else:
    file = FILE

#-- Read the file
ice = Ice()
ice.open_file(file)

#-- Get all the blocks, by levels
levels = ice.get_level_blocks()

#-- Print depth of the circuit
print(f"Depth: {len(levels)}")

#-- Print all the blocks, by levels
for index, level in enumerate(levels):
    print(f"-Level {index}: Block(s): {len(level)}")

    #-- Print the block types in this level
    for block in level:
        if Ice.is_basic_block(block.type):
            print(f"  -{block.type}")
        else:
            comp = ice.dependencies.dict[block.type]
            print(f"  -{comp.package.name}")



        
