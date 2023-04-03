#!/usr/bin/env python3

import unittest
import json
from Icestudio import Size


class TestIcestudio(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()

