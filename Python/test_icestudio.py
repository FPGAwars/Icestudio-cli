#!/usr/bin/env python3

import unittest
import json
from Icestudio import \
    Size, DataInfo, Position, Block, Blocks, Graph, Design, Ice, Pin, \
    Pins, DataPin, Port, Range, Ports, InOutPorts, DataCode, EndPoint, \
    Wire, Wires, Package

class TestPackage(unittest.TestCase):

    def test_Package(self):
        """Test constructor"""

        pack = Package("b1","1.0","hi!", "me", "svg")
        self.assertEqual(pack.name, "b1")
        self.assertEqual(pack.version, "1.0")
        self.assertEqual(pack.description, "hi!")
        self.assertEqual(pack.author, "me")
        self.assertEqual(pack.image, "svg")

        #-- Check for invalid arguments
        with self.assertRaises(AttributeError) as exc:
            Package(3)

        self.assertEqual(str(exc.exception),"name is not an String")

        with self.assertRaises(AttributeError) as exc:
            Package("b1", 3)

        self.assertEqual(str(exc.exception),"version is not an String")

        with self.assertRaises(AttributeError) as exc:
            Package("b1", "1.0", 3)

        self.assertEqual(str(exc.exception),"description is not an String")

        with self.assertRaises(AttributeError) as exc:
            Package("b1", "1.0", "hi!", 3)

        self.assertEqual(str(exc.exception),"author is not an String")

        with self.assertRaises(AttributeError) as exc:
            Package("b1", "1.0", "hi!", "me", 3)

        self.assertEqual(str(exc.exception),"image is not an String")


    def test_Package_str(self):
        """Test str method"""

        pack = Package("b1","1.0","hi!", "me", "svg")
        self.assertEqual(str(pack), "Package(b1,1.0,hi!,me,svg)")


    def test_Package_json(self):
        """Test json method"""

        #-- Perform the test
        pack = Package("b1","1.0","hi!", "me", "svg")
        self.assertEqual(
            pack.json(), 
            {"name": "b1", "version": "1.0", "description": "hi!",
             "author": "me", "image": "svg"
            }
        )

    def test_eq(self):
        """Test == operator"""

        pack1 = Package("b1","1.0","hi!", "me", "svg")
        pack2 = Package()
        self.assertTrue(pack1 == pack1)
        self.assertFalse(pack1 == pack2)


    def test_Package_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/package.ice") as f:
            pack = Package(**json.load(f))

        self.assertEqual(pack.name, "bit1")
        self.assertEqual(pack.version, "1.0")
        self.assertEqual(pack.description, "cool")
        self.assertEqual(pack.author, "obi")
        self.assertEqual(pack.image, "svg") 
        

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


class TestRange(unittest.TestCase):

    def test_Range(self):
        """Test the constructor"""

        r = Range(2)
        self.assertEqual(r.max, 1)
        self.assertEqual(r.size, 2)

        r = Range("[1:0]")
        self.assertEqual(r.max, 1)
        self.assertEqual(r.size, 2)

        #-- Check for invalid types
        with self.assertRaises(AttributeError) as exc:
            Range([2,0])

        self.assertEqual(str(exc.exception), "Unknown type for max")

        with self.assertRaises(AttributeError) as exc:
            Range("hi")

        self.assertEqual(str(exc.exception), "Invalid range format")


    def test_Range_str(self):
        """Test the str() method"""

        r = Range(2)
        self.assertEqual(str(r), "[1:0]")

    def test_Range_eq(self):
        """Test the == operator"""

        r1 = Range(2)
        r2 = Range(2)
        self.assertEqual(r1, r2)

        r3 = Range(3)
        self.assertNotEqual(r1, r3)
        

class TestPorts(unittest.TestCase):
    
    def test_Ports(self):
        """Test the constructor"""

        ports = Ports(Port("a"), Port("b"))
        self.assertEqual(ports.list, [Port("a"), Port("b")])

        ports = Pins()
        self.assertListEqual(ports.list, [])

        #-- Check invalid arguments
        #-- Invalid type
        with self.assertRaises(AttributeError) as exc:
            Ports(3)

        self.assertEqual(str(exc.exception), 
                        "Argument is not of port type")


    def test_Ports_str(self):
        """Test the str method"""

        ports = Ports(Port("a"), Port("b"))
        self.assertEqual(str(ports),
                        "Ports(a,b)")
        
    def test_Ports_json(self):
        """Test json method"""

        ports = Ports(Port("a", 2), Port("b"))
        self.assertEqual(ports.json(), 
                         [{'name': 'a', 'range': '[1:0]', 'size': 2},
                          {'name': 'b'}
                         ])
        
    def test_Port_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/ports.ice") as f:
            ports_json = json.load(f)
            ports = Ports(*ports_json)
        #-- TODO ports.list == Ports(*pins_json)


    def test_Ports_eq(self):
        """Test === operator"""

        ports1 = Ports(Port("a"), Port("b"))
        ports2 = Ports(Port("a"), Port("b"))
        self.assertEqual(ports1, ports2)

        ports3 = Ports(Port("c"), Port("d"))
        self.assertNotEqual(ports1, ports3)


class TestInOutPorts(unittest.TestCase):
    
    def test_InOutPorts(self):
        """Test the constructor"""

        ports1 = Ports(Port("a",2), Port("b"))
        ports2 = Ports(Port("c"))
        ioports = InOutPorts(ports1, ports2)
        self.assertEqual(ioports.inp, ports1)
        self.assertEqual(ioports.out, ports2)

        #-- Check invalid types
        with self.assertRaises(AttributeError) as exc:
            InOutPorts(3)

        self.assertEqual(str(exc.exception), "Unknown type for inports")

        with self.assertRaises(AttributeError) as exc:
            InOutPorts(ports1, 3)

        self.assertEqual(str(exc.exception), "Unknown type for outports")


    def test_InOutPorts_str(self):
        """Test the str() method"""

        ports1 = Ports(Port("a",2), Port("b"))
        ports2 = Ports(Port("c"))
        ioports = InOutPorts(ports1, ports2)
        self.assertEqual(str(ioports), 
                         "InPorts(a[1:0],b), OutPorts(c)")
        
        
    def test_InOutPorts_json(self):
        """Test the Json method"""

        ports1 = Ports(Port("a",2), Port("b"))
        ports2 = Ports(Port("c"))
        ioports = InOutPorts(ports1, ports2)
        self.assertEqual(
            ioports.json(),
            {
                "in": [
                    {
                      "name": "a",
                      "range": "[1:0]",
                      "size": 2
                    }, 
                    {
                      "name": "b"
                    }
                ],
                "out": [
                    { "name": "c"}
                ]
            })


    def test_InOutPort_eq(self):
        """Test the eq method"""

        ports1 = Ports(Port("a",2), Port("b"))
        ports2 = Ports(Port("c"))
        ioports1 = InOutPorts(ports1, ports2)
        ioports2 = InOutPorts(ports1, ports2)
        self.assertEqual(ioports1, ioports2)

        ports3 = Ports(Port("c"), Port("d"))
        ioports3 = InOutPorts(ports1, ports3)
        self.assertNotEqual(ioports1, ioports3)


    def test_Port_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/inoutports.ice") as f:
            ioports_json = json.load(f)

            #-- Cambiar la propiedad "in" por "inp"
            ioports_json["inp"] = ioports_json.pop("in")
            ioports = InOutPorts(**ioports_json)

        inports = Ports(*ioports_json["inp"])
        outports = Ports(*ioports_json["out"])

        self.assertEqual(ioports.inp, inports)
        self.assertEqual(ioports.out, outports)



class TestPort(unittest.TestCase):

    def test_Port(self):
        """Test the constructor"""

        port = Port("out")
        self.assertEqual(port.name, "out")
        self.assertEqual(port.range, None)
        self.assertEqual(port.size, None)

        port = Port("Hi", 2)
        self.assertEqual(port.name, "Hi")
        self.assertEqual(port.range, Range(2))
        self.assertEqual(port.size, 2)

        port = Port("Dude!", "[2:0]")
        self.assertEqual(port.name, "Dude!")
        self.assertEqual(port.range, Range(3))
        self.assertEqual(port.size, 3)

        port = Port("Bye", "[3:0]")
        self.assertEqual(port.name, "Bye")
        self.assertEqual(port.range, Range(4))
        self.assertEqual(port.size, 4)


        #-- Check, for invalid arguments
        with self.assertRaises(AttributeError) as exc:
            Port(3)

        self.assertEqual(str(exc.exception), "name is not an String")

        with self.assertRaises(AttributeError) as exc:
            Port("Hi", [])

        self.assertEqual(str(exc.exception), "Unknown type for max")


    def test_Port_str(self):
        """Test the str() method"""

        port = Port("out")
        self.assertEqual(str(port), "out")


    def test_Port_json(self):
        """Test the Json method"""

        port = Port("Hi")
        self.assertEqual(port.json(),
                         {
                           "name": "Hi"
                         })
        
        port = Port("Bye", 2)
        self.assertEqual(port.json(), 
                         {
                           "name": "Bye",
                           "range": "[1:0]",
                           "size": 2 
                         })

    def test_Port_eq(self):
        """Test the eq method"""

        p1 = Port("Hi")
        p2 = Port("Hi")
        self.assertEqual(p1, p2)

        p3 = Port("Dude!")
        self.assertNotEqual(p1, p3)


    def test_Port_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/port1.ice") as f:
             port = Port(**json.load(f))

        self.assertEqual(port.name, "Hi!")


class TestPin(unittest.TestCase):

    def test_Pin(self):
        """Test the constructor"""

        pin = Pin()
        self.assertEqual(pin.index, "0")
        self.assertEqual(pin.name, "NULL")
        self.assertEqual(pin.value, "NULL")

        #-- check for invalid arguments
        with self.assertRaises(AttributeError) as exc:
            Pin(3)

        self.assertEqual(str(exc.exception), "Invalid type for index")

        with self.assertRaises(AttributeError) as exc:
            Pin("0", 3)

        self.assertEqual(str(exc.exception), "Invalid type for name")

        with self.assertRaises(AttributeError) as exc:
            Pin("0", "NULL", 3)

        self.assertEqual(str(exc.exception), "Invalid type for value")


    def test_Pin_str(self):
        """Test the str method"""

        pin = Pin("0", "Hi", "Dude!")
        self.assertEqual(str(pin), "Pin(0, Hi, Dude!)")


    def test_eq(self):
        """Test == operator"""

        self.assertTrue(Pin() == Pin())
        self.assertTrue(Pin("0","hola","1") == Pin("0", "hola", "1"))
        self.assertFalse(Pin("1") == Pin("0"))

    def test_Pin_file(self):
        """Test Pin from json files"""

        #-- Open a json test file
        with open("../Test-files/pin.ice") as f:
             pin = Pin(**json.load(f))

        self.assertEqual(pin.index, "2")
        self.assertEqual(pin.name, "Hi")
        self.assertEqual(pin.value, "Dude!")


class TestPins(unittest.TestCase):

    def test_Pins(self):
        """Test the constructor"""

        pin1 = Pin("0", "P0")
        pin2 = Pin("1", "P1")
        pins = Pins(pin1, pin2)
        self.assertListEqual(pins.list, [pin1, pin2])

        pins = Pins()
        self.assertListEqual(pins.list, [])

        #-- Check invalid arguments
        #-- Invalid block type
        with self.assertRaises(AttributeError) as exc:
            Pins(3)

        self.assertEqual(str(exc.exception), 
                        "Argument is not of pin type")


    def test_Pin_str(self):
        """Test the str method"""

        pin1 = Pin("0", "P0", "V0")
        pin2 = Pin("1", "P1", "V1")
        pins = Pins(pin1, pin2)
        self.assertEqual(str(pins),
                        "Pins:\n"
                        "Pin(0, P0, V0)\n"
                        "Pin(1, P1, V1)")


    def test_Pin_json(self):
        """Test json method"""

        pin1 = Pin("0", "P0", "V0")
        pin2 = Pin("1", "P1", "V1")
        pins = Pins(pin1, pin2)
        self.assertEqual(pins.json(), 
                         [{'index': '0', 'name': 'P0', 'value': 'V0'},
                          {'index': '1', 'name': 'P1', 'value': 'V1'}
                         ])
        
    def test_Pins_file(self):
        """Test Pins from json files"""

        #-- Open a json test file
        with open("../Test-files/pins.ice") as f:
            pins_json = json.load(f)
            pins = Pins(*pins_json)
        #-- TODO pins.list == Pins(*pins_json)

    def test_Pins_eq(self):
        """Test === operator"""

        pins1 = Pins(Pin("0"), Pin("2"))
        pins2 = Pins(Pin("0"), Pin("2"))
        self.assertEqual(pins1, pins2)

        pins3 = Pins(Pin("0"), Pin("3"))
        self.assertNotEqual(pins1, pins3)


class TestEndPoint(unittest.TestCase):

    def test_EndPoint(self):
        """Test the constructor"""

        endp = EndPoint()
        self.assertEqual(endp.block, "")
        self.assertEqual(endp.port, "")

        endp = EndPoint("block1", "a")
        self.assertEqual(endp.block, "block1")
        self.assertEqual(endp.port, "a")

        #--- Check for invalid parameter
        with self.assertRaises(AttributeError) as exc:
            EndPoint(3)

        self.assertEqual(str(exc.exception), "block is not a String")

        with self.assertRaises(AttributeError) as exc:
            EndPoint("block1", 3)

        self.assertEqual(str(exc.exception), "port is not a String")


    def test_EndPoint_str(self):
        """Test the str method"""

        endp1 = EndPoint("block1", "a")
        self.assertEqual(str(endp1), 
                         "EndPoint(block1, a)")
        
    def test_EndPoint_eq(self):
        """Test the eq method"""

        endp1 = EndPoint("block1", "a")
        endp2 = EndPoint("block1", "a")
        self.assertEqual(endp1, endp2)

        endp3 = EndPoint("block3", "c")
        self.assertNotEqual(endp1, endp3)


    def test_EndPoint_json(self):
        """Test json method"""

        endp = EndPoint("block1", "a")

        #-- Perform the test
        self.assertEqual(
            endp.json(), 
            {"block": "block1",
             "port": "a"
            })
        

    def test_EndPoint_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/endpoint.ice") as f:
            endp = EndPoint(**json.load(f))

        self.assertEqual(endp, EndPoint("0766f96f", "out"))

        
class TestWire(unittest.TestCase):

    def test_Wire(self):
        """Test the constructor"""

        wire = Wire()
        self.assertEqual(wire.source, EndPoint())
        self.assertEqual(wire.target, EndPoint())
        self.assertEqual(wire.size, None)
        

        wire = Wire(EndPoint("b1","o1"), EndPoint("b2","i1"))
        self.assertEqual(wire.source, EndPoint("b1","o1"))
        self.assertEqual(wire.target, EndPoint("b2","i1"))
        self.assertEqual(wire.size, None)

        wire = Wire(EndPoint("b2","o1"), EndPoint("b3","i1"), 2)
        self.assertEqual(wire.source, EndPoint("b2","o1"))
        self.assertEqual(wire.target, EndPoint("b3","i1"))
        self.assertEqual(wire.size, 2)

        #-- Check for invalid arguments
        with self.assertRaises(AttributeError) as exc:
            Wire(3)

        self.assertEqual(str(exc.exception), 
                         "Unknown type for source EndPoint")
        
        with self.assertRaises(AttributeError) as exc:
            Wire(EndPoint(), 3)

        self.assertEqual(str(exc.exception), 
                         "Unknown type for target EndPoint")
        

    def test_Wire_str(self):
        """Test the str method"""

        wire = Wire(EndPoint("b1","o1"), EndPoint("b2","i1"))
        self.assertEqual(str(wire), 
                         "Wire(EndPoint(b1, o1),"
                              "EndPoint(b2, i1),1)")
        
    def test_Wire_eq(self):
        """Test the == method"""

        wire1 = Wire(EndPoint("b1","o1"), EndPoint("b2","i1"))
        wire2 = Wire(EndPoint("b1","o1"), EndPoint("b2","i1"))
        self.assertEqual(wire1, wire2)

        wire3 = Wire()
        self.assertNotEqual(wire1, wire3)


    def test_Wire_json(self):
        """Test json method"""

        wire = Wire(EndPoint("b1","o1"), EndPoint("b2","i1"))

        #-- Perform the test
        self.assertEqual(wire.json(),
            {
              'source': {
                'block': 'b1', 
                'port': 'o1'
              },
              'target': {
                'block': 'b2', 
                'port': 'i1'
              }
            })
        
    def test_Wire_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/wire.ice") as f:
            wire = Wire(**json.load(f))

        self.assertEqual(wire.source, 
                         EndPoint("0766f96f-9f07-49b1-8c78-f24dce15cb5e",
                                  "out"))
        self.assertEqual(wire.target, 
                         EndPoint("f2c3641d-ddfd-4a4b-a092-33b6f4bf838a",
                                  "in"))
        self.assertEqual(wire.size, 2)
        
        
class TestWires(unittest.TestCase):

    def test_Wires(self):
        """Test the constructor"""

        wire1 = Wire(EndPoint("b1","o"), EndPoint("b2","i"))
        wire2 = Wire(EndPoint("a1","o"), EndPoint("a2", "o"))
        wires = Wires(wire1, wire2)
        self.assertListEqual(wires.list, [wire1, wire2])

        wires = Wires()
        self.assertListEqual(wires.list, [])

        #-- Check invalid arguments
        #-- Invalid wire type
        with self.assertRaises(AttributeError) as exc:
            Wires(3)

        self.assertEqual(str(exc.exception), 
                               "Argument is not of wire type")
        

    def test_Wiress_str(self):
        """Test the str method"""

        wire1 = Wire(EndPoint("b1","o"), EndPoint("b2","i"))
        wire2 = Wire(EndPoint("a1","o"), EndPoint("a2", "o"))
        wires = Wires(wire1, wire2)
        self.assertEqual(str(wires),
                         "Wire(EndPoint(b1, o),EndPoint(b2, i),1)\n"
                         "Wire(EndPoint(a1, o),EndPoint(a2, o),1)")
        

    def test_Wiress_json(self):
        """Test json method"""

        wire1 = Wire(EndPoint("b1","o"), EndPoint("b2","i"))
        wire2 = Wire(EndPoint("a1","o"), EndPoint("a2", "o"))
        wires = Wires(wire1, wire2)
        self.assertEqual(wires.json(), 
          [
            {'source': {'block': 'b1', 'port': 'o'}, 
             'target': {'block': 'b2', 'port': 'i'}
            }, 
            {'source': {'block': 'a1', 'port': 'o'},
             'target': {'block': 'a2', 'port': 'o'}}
          ])
        
    def test_wires_file(self):
        """Test Wires from json files"""

        #-- Open a json test file
        with open("../Test-files/wires.ice") as f:
            wires_json = json.load(f)
            wiress = Wires(*wires_json)
        #-- TODO wires.list == Wires(*wires_json)


class TestDataCode(unittest.TestCase):

    def test_DataCode(self):
        """Test the constructor"""

        data = DataCode(InOutPorts())
        self.assertEqual(data.ports, InOutPorts())
        self.assertEqual(data.params, [])
        self.assertEqual(data.code, "")

        #-- Check for invalid parameter
        with self.assertRaises(AttributeError) as exc:
            DataCode(3)

        self.assertEqual(str(exc.exception), "Unknown type for ports (ioports)")

        with self.assertRaises(AttributeError) as exc:
            DataCode(InOutPorts(), [], 3)

        self.assertEqual(str(exc.exception), "code is not a String")


    def test_DataCode_str(self):
        """Test the str method"""

        data = DataCode(InOutPorts(),[],"//-- Hi")
        self.assertEqual(str(data), 
                         "DataCode:\n"
                         "* InPorts(), OutPorts()\n"
                         "* Params: []\n"
                         "* Code: //-- Hi")


    def test_DataCode_json(self):
        """Test json method"""

        data = DataCode(InOutPorts(),[],"//-- Hi")

        #-- Perform the test
        self.assertEqual(
            data.json(), 
            {"ports": {'in': [], 'out': []},
             "params": [],
             "code": "//-- Hi"
             })


    def test_DataInfo_file(self):
        """Test from json files"""

        #-- Open a json test file
        with open("../Test-files/dataCode.ice") as f:
            data = DataCode(**json.load(f))

        self.assertEqual(data.ports, 
                         InOutPorts(Ports(), 
                                    Ports(Port("o", 2))))
        self.assertEqual(data.params, [])
        self.assertEqual(data.code, "//-- Hi!")


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


class TestDataPin(unittest.TestCase):

    def test_DataPin(self):
        """Test the constructor"""

        data = DataPin("LED", False, Pins(Pin(), Pin()))
        self.assertEqual(data.name, "LED")
        self.assertEqual(data.virtual, False)
        #-- TODO
        #self.assertEqual(data.pins, Pins(Pin(), Pin()))

        #-- Creat DataPin with invalid type of name
        with self.assertRaises(AttributeError) as exc:
            DataPin(3)

        self.assertEqual(str(exc.exception), "name is not a String")

        #-- Invalid virtual property
        with self.assertRaises(AttributeError) as exc:
            DataPin("Hi", 3)

        self.assertEqual(str(exc.exception), "virtual is not Boolean")

        #-- Invalid pins property
        with self.assertRaises(AttributeError) as exc:
            DataPin("Hi", False, None, 3)

        self.assertEqual(str(exc.exception), "Invalid type for pins")


    def test_DataPin_str(self):
        """Test the str method"""

        data = DataPin("LED", False)
        self.assertEqual(str(data), 
                         "Name: LED\n"
                         "Virtual: False\n"
                         "Pins:")
        
    def test_DataPin_json(self):
        """Test the json method"""

        data = DataPin("LED", False, None, Pins(Pin(), Pin()))
        self.assertEqual(
            data.json(), 
            {
            "name": "LED",
            "virtual": False,
            "pins": [
                {'index': '0', 'name': 'NULL', 'value': 'NULL'},
                {'index': '0', 'name': 'NULL', 'value': 'NULL'}
            ]
            }
        )

        data = DataPin("LED", False, None, Pins(Pin(), Pin()), False)
        self.assertEqual(
            data.json(), 
            {
            "name": "LED",
            "virtual": False,
            "pins": [
                {'index': '0', 'name': 'NULL', 'value': 'NULL'},
                {'index': '0', 'name': 'NULL', 'value': 'NULL'}
            ],
            "clock": False
            }
        )


    def test_DataPin_file(self):
        """Test DataPin from json files"""

        #-- Open a json test file
        with open("../Test-files/dataPin.ice") as f:
            data = DataPin(**json.load(f))

        self.assertEqual(data.name, "Led")
        self.assertEqual(data.virtual, False)
        self.assertEqual(data.pins, Pins(Pin("1", "N1", "V1")))

        with open("../Test-files/dataPin2.ice") as f:
            data = DataPin(**json.load(f))

        self.assertEqual(data.name, "Boton")
        self.assertEqual(data.virtual, False)
        self.assertEqual(data.pins, Pins(Pin("0", "SW1", "34")))
        self.assertEqual(data.clock, False)


    def test_DataPin_eq(self):
        """Test operator =="""

        datapin1 = DataPin("Led", True, Pins(Pin("1")))
        datapin2 = DataPin("Led", True, Pins(Pin("1")))
        self.assertEqual(datapin1, datapin2)

        datapin3 = DataPin("Led2", False, Pins())
        self.assertNotEqual(datapin1, datapin3)
    


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

        #-- Invalid data type
        with self.assertRaises(AttributeError) as exc:
            Block("id1", "basic.info", 5)

        self.assertEqual(str(exc.exception), "Unknow type for data")

        #-- Invalid position type
        with self.assertRaises(AttributeError) as exc:
            Block("id1", "basic.info", DataInfo(), 3)

        self.assertEqual(str(exc.exception), "Unknow type for position")

        #-- Invalid Size type
        with self.assertRaises(AttributeError) as exc:
            Block("id1", "basic.info", DataInfo(), Position(), 3)

        self.assertEqual(str(exc.exception), "Unknow type for size")



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

        #-- Check invalid arguments
        #-- Invalid block type
        with self.assertRaises(AttributeError) as exc:
            Blocks(3)

        self.assertEqual(str(exc.exception), 
                               "Argument is not of block type")


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
        #-- TODO blocks.list == Blocks(*blocks_json)

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

        self.assertTrue(isinstance(graph.blocks, Blocks))
        self.assertTrue(isinstance(graph.wires, list))
        
        #-- TODO
        #self.assertEqual(graph.blocks, [])
        #self.assertEqual(graph.wires, [])

        #-- TODO
        # blocks = Blocks(Block())
        # graph = Graph(blocks)
        # self.assertEqual(graph.blocks, blocks)
        # self.assertEqual(graph.wires, [])


    def test_Graph_str(self):
        """Test str method"""

        graph = Graph()
        self.assertEqual(str(graph), 
                        "* Blocks: \n"
                        "* Wires: []\n")


    def test_Graph_file(self):
        """Test Graph from json files"""

        #-- Open a json test file
        with open("../Test-files/graph.ice") as f:
            graph_json = json.load(f)
            graph = Graph(**graph_json)

        #-- TODO
        #self.assertEqual(graph.blocks, graph_json['blocks'])
        #self.assertEqual(graph.wires, graph_json['wires'])


    def test_Graph_json(self):
        """Test json method"""

        graph = Graph()
        self.assertEqual(graph.json(), 
                         {'blocks': [], 'wires': []})


class TestDesign(unittest.TestCase):

    def test_Design(self):
        """Test the constructor"""

        design = Design("")
        self.assertEqual(design.board, "")
        #-- TODO
        #self.assertEqual(design.graph, {})

        #-- Check for invalid board type
        with self.assertRaises(AttributeError) as exc:
            Design(3)

        self.assertEqual(str(exc.exception), "board is not a string")

        #-- Check for invalid graph type
        with self.assertRaises(AttributeError) as exc:
            Design("hi", 3)

        self.assertEqual(str(exc.exception), "Unknown type for Graph")


    def test_Design_str(self):
        """Test the str method"""

        design = Design("")
        self.assertEqual(str(design),
                         "* Design:\n"
                         "Board: \n"
                         "Graph: * Blocks: \n"
                         "* Wires: []\n\n")
        
    def test_Design_file(self):
        """Test Design from json files"""

        #-- Open a json test file
        with open("../Test-files/design.ice") as f:
            design_json = json.load(f)
            design = Design(**design_json)

        self.assertEqual(design.board, design_json['board'])
        #-- TODO
        #self.assertEqual(design.graph, design_json['graph'])


    def test_Design_json(self):
        """Test json method"""

        design = Design("")
        self.assertEqual(design.json(), 
                         {'board': "", 
                          'graph': {'blocks': [], 'wires': []}
                          })


class TestIce(unittest.TestCase):

    def test_Ice(self):
        """Test the constructor"""

        ice = Ice()
        self.assertEqual(ice.version, "")
        self.assertEqual(ice.package, {})
        self.assertIsInstance(ice.design, Design)
        #--TODO: Compare if object ice.design is equal to the empty one
        self.assertEqual(ice.dependencies, {})

        #-- Check for invalid version
        with self.assertRaises(AttributeError) as exc:
            Ice(2)

        self.assertEqual(str(exc.exception), 
                         "Invalid version type (should be a string)")


    def test_Ice_str(self):
        """Test the str method"""

        ice = Ice()
        self.assertEqual(str(ice),
                         "Version: \n"
                         "Package: {}\n"
                         "Design: * Design:\n"
                         "Graph: * Blocks: \n"
                         "* Wires: []\n\n\n"
                         "Dependencies: {}\n")
        
        ice = Ice(design=Design("alhambra-II"))
        self.assertEqual(str(ice),
                         "Version: \n"
                         "Package: {}\n"
                         "Design: * Design:\n"
                         "Board: alhambra-II\n"
                         "Graph: * Blocks: \n"
                         "* Wires: []\n\n\n"
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
                               'graph': {
                                    'blocks': [],
                                    'wires': []
                               }
                           },
                           'dependencies': {}
                          })
        
        ice = Ice(design=Design("alhambra-ii"))
        self.assertEqual(ice.json(), 
                          {'version': "",
                           'package': {},
                           'design' : {
                               'board': "alhambra-ii",
                               'graph': {
                                    'blocks': [],
                                    'wires': []
                               }
                           },
                           'dependencies': {}
                          })


if __name__ == '__main__':
    unittest.main()

