#!/usr/bin/env python3

import json
from Icestudio import Ice, Size, Blocks, Graph

#-- Open a json test file
# with open("../Test-files/graph.ice") as f:
#     graph_json = json.load(f)
#     graph = Graph(**graph_json)

# print(graph)

# with open("../Test-files/blocks.ice") as f:
#     blocks_json = json.load(f)
#     blocks = Blocks(*blocks_json)
# print(blocks)

ice = Ice()
ice.open_file("../Test-files/test-01-info.ice")
print(ice)