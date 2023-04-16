#!/usr/bin/env python3

import json
from Icestudio import Ice, Size, Blocks, Graph

ice = Ice()
ice.open_file("../Test-files/test-12-bit1.ice")

#-- Print info about the circuit
print(f"* Blocks: {len(ice.design.graph.blocks.list)}")
print(f"* Wires: {len(ice.design.graph.wires)}")

print()

block = ice.design.graph.blocks.list[0]


#-- Show all the blocks with its types and ids
blocks = ice.design.graph.blocks.list
for block in blocks:
    ublock = ice.dependencies.dict[block.type]
    print(f"-{ublock.package.name} (v{ublock.package.version})")

print()
