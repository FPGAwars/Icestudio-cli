#!/usr/bin/env python3

import json
from Icestudio import Ice, Size, Blocks, Graph

ice = Ice()
ice.open_file("../Test-files/test-05-output-pin.ice")

#-- Print info about the circuit
print(f"* Version: {ice.version}")
print(f"* Board: {ice.design.board}")
print(f"* Blocks: {len(ice.design.graph.blocks.list)}")
print(f"* Wires: {len(ice.design.graph.wires)}")

print()

#-- Show all the blocks with its types and ids
blocks = ice.design.graph.blocks.list
for block in blocks:
    print(f"-{block.type} block")
    print(f"  id: {block.id}")

print()