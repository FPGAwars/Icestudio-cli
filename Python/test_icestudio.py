#!/usr/bin/env python3

import unittest
import json
from Icestudio import Size, DataInfo


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

        size = Size(248, 48)

        #-- Get the json string
        json_str = json.dumps(size.json())

        #-- Perform the test
        self.assertEqual(
            json_str, 
            '{"width": 248, "height": 48}')
        
    


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

        #-- Get the json string
        json_str = json.dumps(data.json())

        #-- Perform the test
        self.assertEqual(
            json_str, 
            '{"info": "Testing...", "readonly": true}')



if __name__ == '__main__':
    unittest.main()

