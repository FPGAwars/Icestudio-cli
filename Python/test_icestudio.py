#!/usr/bin/env python3

import unittest
import json
from Icestudio import Size, DataInfo, Position, Block


class TestSize(unittest.TestCase):

    def test_Size(self):
        """Test Size constructor"""

        size = Size(0,0)
        self.assertEqual(size.height, 0)
        self.assertEqual(size.width, 0)

        size = Size(248, 48)
        self.assertEqual(size.width, 248)
        self.assertEqual(size.height, 48)


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


    def test_DataInfo_str(self):
        """Test the str method"""

        data = DataInfo("This is a comment", True)
        self.assertEqual(str(data), 
                         "DataInfo: True\n"
                         "  Info: This is a comment")

        data = DataInfo("", False)
        self.assertEqual(str(data),
                         "DataInfo: False\n"
                         "  Info: ")
        

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
                      DataInfo().json(),
                      Position(0,0).json(),
                      Size(0,0).json())
        
        self.assertEqual(block.id, "id01")
        self.assertEqual(block.type, "basic.info")
        self.assertEqual(block.data, {'info': '', 'readonly': True})
        self.assertEqual(block.position, {'x': 0, 'y': 0})
        self.assertEqual(block.size, {'width': 0, 'height': 0})

        block = Block("9838541d-8656-43e3-8d83-69d14ebd9622",
                      "basic.info",
                      DataInfo("This is a comment",False).json(),
                      Position(360, 184).json(),
                      Size(248, 48).json())
        
        self.assertEqual(block.id, "9838541d-8656-43e3-8d83-69d14ebd9622")
        self.assertEqual(block.type, "basic.info")
        self.assertEqual(block.data, {'info': 'This is a comment',
                                      'readonly': False})
        self.assertEqual(block.position, {'x': 360, 'y': 184})
        self.assertEqual(block.size, {'width': 248, 'height': 48})
        

    def test_Block_str(self):
        """Test the str method"""

        block = Block("9838541d-8656-43e3-8d83-69d14ebd9622",
                      "basic.info",
                      DataInfo("This is a comment",False).json(),
                      Position(360, 184).json(),
                      Size(248, 48).json())

        self.assertEqual(str(block), 
                        "id: 9838541d-8656-43e3-8d83-69d14ebd9622\n"
                        "Type: basic.info\n"
                        "Data: {'info': 'This is a comment', "
                          "'readonly': False}\n"
                        "Pos: {'x': 360, 'y': 184}\n"
                        "Size: {'width': 248, 'height': 48}\n")
        
        block = Block("id01", 
                      "basic.info",
                      DataInfo().json(),
                      Position(0,0).json(),
                      Size(0,0).json())
        
        self.assertEqual(str(block),
                         "id: id01\n"
                         "Type: basic.info\n"
                         "Data: {'info': '', 'readonly': True}\n"
                         "Pos: {'x': 0, 'y': 0}\n"
                         "Size: {'width': 0, 'height': 0}\n")
        
    
    def test_Block_file(self):
        """Test Block from json files"""

        #-- Open a json test file
        with open("../Test-files/block.ice") as f:
            block = Block(**json.load(f))

        self.assertEqual(block.id, "9838541d-8656-43e3-8d83-69d14ebd9622")
        self.assertEqual(block.type, "basic.info")
        self.assertEqual(block.data, {"info": "This is a comment",
                                      "readonly": True})
        self.assertEqual(block.position, {"x": 360, "y": 184})
        self.assertEqual(block.size, {"width": 248, "height": 48})
        

    def test_Block_json(self):
        """Test json method"""

        block = Block("id01", 
                      "basic.info",
                      DataInfo().json(),
                      Position(0,0).json(),
                      Size(0,0).json())
        
        self.assertEqual(block.json(), 
            {   "id": "id01",
                "type": "basic.info",
                "data": {'info': '', 'readonly': True},
                "position": {'x': 0, 'y': 0},
                "size": {'width': 0, 'height': 0}
            })
                         
    

if __name__ == '__main__':
    unittest.main()

