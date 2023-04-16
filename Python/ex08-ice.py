#!/usr/bin/env python3
import sys
from Icestudio import Ice

def is_basic_block(type):
    return type in ['basic.output', 'basic.info', 'basic.code', 'basic.input']


#-- The first argument is the .ice circuit to analyze
if ( len(sys.argv) < 2 ):
    print("No icestudio file")
    print("Usage: ex08-ice.py icestudio-file")
    print()
    sys.exit()

file = sys.argv[1]
#file = "../Test-files/temp.ice"

#-- Read the file
ice = Ice()
ice.open_file(file)

#-- Top level blocks
blocks = ice.design.graph.blocks.list

#-- List with basic blocks
basic_lst = []  #-- Basic blocks
block_lst = []  #-- User blocks

#-- Fill the lists with the type of block
for block in blocks:

    if is_basic_block(block.type):
        basic_lst.append(f"  -{block.type}")

    else:
        ublock = ice.dependencies.dict[block.type]
        block_lst.append(f"  -{ublock.package.name}" 
                         f" (v{ublock.package.version})")

#-- Number of blocks
nbasic = len(basic_lst)
nblock = len(block_lst)

#-- Print the blocks
print(f"File: {file}")
print()

print(f"Number of blocks: {nbasic + nblock}\n")

if nblock > 0:
    print(f"* Blocks: {nblock}")
    print("\n".join(block_lst))
    print()

if nbasic > 0:
    print(f"* Basic blocks: {nbasic}")
    print("\n".join(basic_lst))

print()
