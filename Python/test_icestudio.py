#!/usr/bin/env python3

import unittest
import json
from Icestudio import Size, DataInfo, Position, Block, Blocks, Graph
from Icestudio import Design, Ice


class TestSize(unittest.TestCase):

    def test_Size(self):
        """Test Size constructor"""

        size = Size(0,0)
        self.assertEqual(size.height, 0)
        self.assertEqual(size.width, 0)

        size = Size(248, 48)
        self.assertEqual(size.width, 248)
        self.assertEqual(size.height, 48)

        #-- Create a Size object with invalid arguments
        with self.assertRaises(AttributeError) as exc:
            Size("Hi",0)
        self.assertEqual(str(exc.exception), "Width is not an Integer value")

        #-- Check and invalid height argument
        with self.assertRaises(AttributeError) as exc:
            Size(0, "Go!")
        self.assertEqual(str(exc.exception), "Height is not an Integer value")
        


    def test_eq(self):
        """Test == operator"""

        self.assertTrue(Size(100, 200) == Size(100, 200))
        self.assertFalse(Size(1,2) == Size(3,4))


    def test_Size_str(self):
        """Test Size str method"""

        size = Size(0,0)
        self.assertEqual(str(size), "Size(0, 0)")

        size = Size(248, 48)
        self.assertEqual(str(size), "Size(248, 48)")


    def test_Size_file(self):
        """Test Size from json files"""

        #-- Open a json test file
        with open("../Test-files/size.ice") as f:
            size = Size(**json.load(f))

        self.assertEqual(size.width, 248)
        self.assertEqual(size.height, 48)


    def test_Size_json(self):
        """Test Size json method"""

        #-- Perform the test
        self.assertEqual(
            Size(248, 48).json(), 
            {"width": 248, "height": 48}
        )
        

class TestPosition(unittest.TestCase):

    def test_Position(self):
        """Test the constructor"""

        pos = Position(0,0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        pos = Position(360, 184)
        self.assertEqual(pos.x, 360)
        self.assertEqual(pos.y, 184)

        #-- Create a Position with invalid type of x
        with self.assertRaises(AttributeError) as exc:
            Position("Hi!", 200)
        
        self.assertEqual(str(exc.exception), "x is not an Integer value")

        #-- Invalid type for y
        with self.assertRaises(AttributeError) as exc:
            Position(0, "You!")

        self.assertEqual(str(exc.exception), "y is not an Integer value")


    def test_Position_str(self):
        """Test the str method"""

        pos = Position(0,0)
        self.assertEqual(str(pos), "Pos(0, 0)")

        pos = Position(360, 184)
        self.assertEqual(str(pos), "Pos(360, 184)")


    def test_Position_file(self):
        """Test Position from json files"""

        #-- Open a json test file
        with open("../Test-files/position.ice") as f:
             pos = Position(**json.load(f))

        self.assertEqual(pos.x, 360)
        self.assertEqual(pos.y, 184)


    def test_Position_json(self):
        """Test json method"""

        pos = Position(500, 400)

        #-- Perform the test
        self.assertEqual(
            pos.json(), 
            {"x": 500, "y": 400}
        )    


class TestDataInfo(unittest.TestCase):

    def test_DataInfo(self):
        """Test the constructor"""

        data = DataInfo("Hello",True)
        self.assertEqual(data.info, "Hello")
        self.assertEqual(data.readonly, True)

        data = DataInfo("", False)
        self.assertEqual(data.info, "")
        self.assertEqual(data.readonly, False)

        #-- Create a DataInfo with invalid type of info
        with self.assertRaises(AttributeError) as exc:
            DataInfo(3, True)
        
        self.assertEqual(str(exc.exception), "info is not a String")

        #-- Create a DataInfo with invalid type of readonly
        with self.assertRaises(ArithmeticError) as exc:
            DataInfo("Comment", 3)

        self.assertEqual(str(exc.exception), "readonly is not Boolean")


    def test_DataInfo_str(self):
        """Test the str method"""

        data = DataInfo("This is a comment", True)
        self.assertEqual(str(data), 
                         "Info: This is a comment\n"
                         "Readonly: True\n")
                         

        data = DataInfo("", False)
        self.assertEqual(str(data),
                         "Info: \n"
                         "Readonly: False\n")
        

    def test_DataInfo_file(self):
        """Test DataInfo from json files"""

        #-- Open a json test file
        with open("../Test-files/dataInfo.ice") as f:
            data = DataInfo(**json.load(f))

        self.assertEqual(data.info, "This is a comment")
        self.assertEqual(data.readonly, True)


    def test_DataInfo_json(self):
        """Test json method"""

        data = DataInfo("Testing...", True)

        #-- Perform the test
        self.assertEqual(
            data.json(), 
            {"info": "Testing...", "readonly": True})


class TestBlock(unittest.TestCase):

    def test_Block(self):
        """Test the constructor"""

        block = Block("id01", 
                      "basic.info",
                      DataInfo(),
                      Position(0,0),
                      Size(0,0))
        
        self.assertEqual(block.id, "id01")
        self.assertEqual(block.type, "basic.info")
        self.assertEqual(block.data, DataInfo())
        self.assertEqual(block.position, Position(0,0))
        self.assertEqual(block.size, Size(0,0))

        block = Block("9838541d-8656-43e3-8d83-69d14ebd9622",
                      "basic.info",
                      DataInfo("This is a comment",False).json(),
                      Position(360, 184).json(),
                      Size(248, 48))
        
        self.assertEqual(block.id, "9838541d-8656-43e3-8d83-69d14ebd9622")
        self.assertEqual(block.type, "basic.info")
        self.assertEqual(block.data, DataInfo("This is a comment", False))
        self.assertEqual(block.position, Position(360, 184))
        self.assertEqual(block.size, Size(248, 48))

        #-- Check for invalid data
        with self.assertRaises(AttributeError) as exc:
            #-- Invalid id: Should be a string
            Block(3)

        self.assertEqual(str(exc.exception), "id is not a String")

        with self.assertRaises(AttributeError) as exc:
            #-- Invalid block type: Should be a string
            Block("id1", 3)

        self.assertEqual(str(exc.exception), "type is not a String")

        with self.assertRaises(AttributeError) as exc:
            #-- Invalid type name
            Block("id1", "Hi")

        self.assertEqual(str(exc.exception), "Unknow block type name")

        #-- Invalid data type
        with self.assertRaises(AttributeError) as exc:
            Block("id1", "basic.info", 5)

        self.assertEqual(str(exc.exception), "Unknow type for data")

        #-- Invalid position type
        with self.assertRaises(AttributeError) as exc:
            Block("id1", "basic.info", DataInfo(), 3)

        self.assertEqual(str(exc.exception), "Unknow type for position")



    def test_Block_str(self):
        """Test the str method"""

        block = Block("9838541d-8656-43e3-8d83-69d14ebd9622",
                      "basic.info",
                      DataInfo("This is a comment",False),
                      Position(360, 184).json(),
                      Size(248, 48))

        self.assertEqual(str(block), 
                        "id: 9838541d-8656-43e3-8d83-69d14ebd9622\n"
                        "Type: basic.info\n"
                        "Data: Info: This is a comment\n"
                          "Readonly: False\n\n"
                        "Pos: Pos(360, 184)\n"
                        "Size: Size(248, 48)\n")
        
        block = Block("id01", 
                      "basic.info",
                      DataInfo(),
                      Position(0,0),
                      Size(0,0))
        
        self.assertEqual(str(block),
                         "id: id01\n"
                         "Type: basic.info\n"
                         "Data: Info: \nReadonly: True\n\n"
                         "Pos: Pos(0, 0)\n"
                         "Size: Size(0, 0)\n")
        
    
    def test_Block_file(self):
        """Test Block from json files"""

        #-- Open a json test file
        with open("../Test-files/block.ice") as f:
            block = Block(**json.load(f))

        self.assertEqual(block.id, "9838541d-8656-43e3-8d83-69d14ebd9622")
        self.assertEqual(block.type, "basic.info")

        self.assertEqual(block.data, DataInfo("This is a comment", True))
        self.assertEqual(block.position, Position(360, 184))

        self.assertIsInstance(block.size, Size)
        self.assertEqual(block.size, Size(248, 48))
        

    def test_Block_json(self):
        """Test json method"""

        block = Block("id01", 
                      "basic.info",
                      DataInfo(),
                      Position(0,0),
                      Size(0,0))
        
        self.assertEqual(block.json(), 
            {   "id": "id01",
                "type": "basic.info",
                "data": {'info': '', 'readonly': True},
                "position": {'x': 0, 'y': 0},
                "size": {'width': 0, 'height': 0}
            })
                         

class TestBlocks(unittest.TestCase):

    def test_Blocks(self):
        """Test the constructor"""

        block1 = Block(id="id1")
        block2 = Block(id="id2")
        blocks = Blocks(block1, block2)
        self.assertListEqual(blocks.list, [block1, block2])

        blocks = Blocks()
        self.assertListEqual(blocks.list, [])


    def test_Blocks_str(self):
        """Test the str method"""

        block1 = Block(id="id1")
        block2 = Block(id="id2")
        blocks = Blocks(block1, block2)
        self.assertEqual(str(blocks),
                        "id: id1\n"
                        "Type: basic.info\n"
                        "Data: Info: \nReadonly: True\n\n"
                        "Pos: Pos(0, 0)\n"
                        "Size: Size(0, 0)\n\n"
                        "id: id2\n"
                        "Type: basic.info\n"
                        "Data: Info: \nReadonly: True\n\n"
                        "Pos: Pos(0, 0)\n"
                        "Size: Size(0, 0)\n")

    def test_Blocks_file(self):
        """Test Blocks from json files"""

        #-- Open a json test file
        with open("../Test-files/blocks.ice") as f:
            blocks_json = json.load(f)
            blocks = Blocks(*blocks_json)

        self.assertEqual(blocks.list, blocks_json)

    def test_Blocks_json(self):
        """Test json method"""

        block1 = Block(id="id1")
        block2 = Block(id="id2")
        blocks = Blocks(block1, block2)
        
        self.assertEqual(blocks.json(), 
                         [{'id': 'id1', 'type': 'basic.info', 
                           'data': {'info': '', 'readonly': True}, 
                           'position': {'x': 0, 'y': 0},
                           'size': {'width': 0, 'height': 0}}, 
                         {'id': 'id2', 'type': 'basic.info', 
                          'data': {'info': '', 'readonly': True}, 
                          'position': {'x':0, 'y':0}, 
                          'size': {'width': 0, 'height': 0}}])



class TestGraph(unittest.TestCase):


    def test_Graph(self):
        """Test the constructor"""

        graph = Graph()
        self.assertEqual(graph.blocks, [])
        self.assertEqual(graph.wires, [])

        blocks = Blocks(Block())
        graph = Graph(blocks)
        self.assertEqual(graph.blocks, blocks)
        self.assertEqual(graph.wires, [])


    def test_Graph_str(self):
        """Test str method"""

        graph = Graph()
        self.assertEqual(str(graph), 
                        "* Blocks: []\n"
                        "* Wires: []\n")


    def test_Graph_file(self):
        """Test Graph from json files"""

        #-- Open a json test file
        with open("../Test-files/graph.ice") as f:
            graph_json = json.load(f)
            graph = Graph(**graph_json)

        self.assertEqual(graph.blocks, graph_json['blocks'])
        self.assertEqual(graph.wires, graph_json['wires'])


    def test_Graph_json(self):
        """Test json method"""

        graph = Graph()
        self.assertEqual(graph.json(), 
                         {'blocks': [], 'wires': []})


class TestDesign(unittest.TestCase):

    def test_Design(self):
        """Test the constructor"""

        design = Design()
        self.assertEqual(design.board, "")
        self.assertEqual(design.graph, {})


    def test_Design_str(self):
        """Test the str method"""

        design = Design()
        self.assertEqual(str(design),
                         "* Design:\n"
                         "Board: \n"
                         "Graph: {}\n")
        
    def test_Design_file(self):
        """Test Design from json files"""

        #-- Open a json test file
        with open("../Test-files/design.ice") as f:
            design_json = json.load(f)
            design = Design(**design_json)

        self.assertEqual(design.board, design_json['board'])
        self.assertEqual(design.graph, design_json['graph'])

    def test_Design_json(self):
        """Test json method"""

        design = Design()
        self.assertEqual(design.json(), 
                         {'board': "", 'graph': {}})


class TestIce(unittest.TestCase):

    def test_Ice(self):
        """Test the constructor"""

        ice = Ice()
        self.assertEqual(ice.version, "")
        self.assertEqual(ice.package, {})
        self.assertIsInstance(ice.design, Design)
        #--TODO: Compare if object ice.design is equal to the empty one
        self.assertEqual(ice.dependencies, {})


    def test_Ice_str(self):
        """Test the str method"""

        ice = Ice()
        self.assertEqual(str(ice),
                         "Version: \n"
                         "Package: {}\n"
                         "Design: * Design:\n"
                         "Board: \n"
                         "Graph: {}\n\n"
                         "Dependencies: {}\n")


    def test_Ice_file(self):
        """Test Ice from json files"""

        #-- Open a json test file
        with open("../Test-files/test-01-info.ice") as f:
            ice_json = json.load(f)
            ice = Ice(**ice_json)

        self.assertEqual(ice.version, ice_json['version'])
        self.assertEqual(ice.package, ice_json['package'])

        
        self.assertIsInstance(ice.design, Design)
        #-- TODO: Comparison: ice.design == ice_json['design']
        #self.assertEqual(ice.design, ice_json['design'])

        self.assertEqual(ice.dependencies, ice_json["dependencies"])

    def test_Ice_json(self):
        """Test json method"""

        ice = Ice()
        self.assertEqual(ice.json(), 
                          {'version': "",
                           'package': {},
                           'design' : {
                               'board': '',
                               'graph': {}
                           },
                           'dependencies': {}
                          })


if __name__ == '__main__':
    unittest.main()

