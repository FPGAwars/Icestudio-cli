import re
import json

class Package:
    """Description of the design on the current level"""

    def __init__(self, 
                 name:str="", 
                 version:str="",
                 description:str="",
                 author:str="",
                 image:str="") -> None:
        
        #-- Set the name attribute
        if isinstance(name, str):
            self.name = name
        else:
            raise AttributeError("name is not an String")
        
        #-- Set the version attribute
        if isinstance(version, str):
            self.version = version
        else:
            raise AttributeError("version is not an String")
        
        #-- Set the description attribute
        if isinstance(description, str):
            self.description = description
        else:
            raise AttributeError("description is not an String")
        
        #-- Set the author attribute
        if isinstance(author, str):
            self.author = author
        else:
            raise AttributeError("author is not an String")
        
        #-- Set the image attribute
        if isinstance(image, str):
            self.image = image
        else:
            raise AttributeError("image is not an String")
        

    def __str__(self) -> str:
        """String representation"""

        cad = f"Package({self.name},{self.version},{self.description}," \
              f"{self.author},{self.image})"
        return cad
    
    def __repr__(self) -> str:
        return str(self)
    
    def json(self):
        """Return the class as a Json object"""
    
        return {
            "name" : self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "image": self.image
        }
    
    def __eq__(self, __value: object) -> bool:
        """Compare two Size objects"""

        if isinstance(__value, Package):
            return (self.name == __value.name) and \
                   (self.version == __value.version) and \
                   (self.description == __value.description) and \
                   (self.author == __value.author) and \
                   (self.image == __value.image)
    
    


class Size:
    """Class for representing the size of an Icestudio block"""

    def __init__(self, width:int=0, height:int=0):
        """Create a Size Object"""

        #-- Set the width attribute
        if isinstance(width, int):
            self.width = width

            #-- Width is an invalid argument (invalid type)
        else:
            raise AttributeError("Width is not an Integer value")
        
        #-- Set the height attribute
        if isinstance(height, int):
            self.height = height
        else:
            #-- Height is an invalid argument (invalid type)
            raise AttributeError("Height is not an Integer value")

    
    def __str__(self) -> str:
        """String representation"""

        cad = f"Size({self.width}, {self.height})"
        return cad
    
    def __repr__(self) -> str:
        return str(self)
    
    def json(self):
        """Return the class as a Json object"""
    
        return {
            "width" : self.width,
            "height": self.height
        }
    
    def __eq__(self, __value: object) -> bool:
        """Compare two Size objects"""

        if isinstance(__value, Size):
            return (self.width == __value.width) and \
                   (self.height == __value.height)


class Position:
    """Class for representing the position of an Icestudio block"""

    def __init__(self, x=0, y=0) -> None:
        """Create a position object"""

        #-- Set the x attribute
        if isinstance(x, int):
            self.x = x

            #-- Invalid type for x
        else:
            raise AttributeError("x is not an Integer value")
        
        #-- Set the y attribute
        if isinstance(y, int):
            self.y = y

            #-- Invalid type for y
        else:
            raise AttributeError("y is not an Integer value")


    def __str__(self) -> str:
        """String representation"""

        cad = f"Pos({self.x}, {self.y})"
        return cad
    
    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, Position):
            return (self.x == __value.x) and \
                   (self.y == __value.y)
    

    def json(self):
        """Return the class as a Json object"""

        return {
            "x": self.x,
            "y": self.y
        }


class Range:
    """Class for representing a verilog range (Ej. [3:0])"""

    @staticmethod
    def get_max(string: str) -> int:
        """Get the max number from the string [max:0]"""

        #-- Define the pattern
        pattern = r"\[(\d+):0\]"
        
        #-- Check the string format
        match = re.search(pattern, string)
        
        #-- Return the result
        if match:

            #-- Match ok
            return int(match.group(1))
        else:
            #-- No match found
            return None


    def __init__(self, max=2) -> None:

        #-- Property max --> [max:0]

        #-- when it is defined by an int, its meaning is the
        #-- total size of the range (max + 1)
        if isinstance(max, int):
            self.max = max - 1

        #-- It can also be defined with a string "[max:0]"
        elif isinstance(max, str):

            #-- check the string format is [max:0]
            #-- and get the max number
            self.max = Range.get_max(max)

            #-- If no max, the given string was not valid
            if self.max == None:
                raise AttributeError("Invalid range format")

        else:
            raise AttributeError("Unknown type for max")
        
    def __str__(self) -> str:
        cad = f"[{self.max}:0]"
        return cad
    
    @property
    def size(self):
        return self.max + 1

    def __eq__(self, __value: object) -> bool:
        return self.max == __value.max


class Port:
    """Class for representing a verilog port"""

    def __init__(self, name="o", range=None, size=None) -> None:

        #----- name attribute
        if isinstance(name, str):
            self.name = name

        else:
            raise AttributeError("name is not an String")
        
        #---- Range attribue
        #-- None by default
        self.range = None

        #-- If given, check range types
        if range != None:
            if isinstance(range, Range):
                self.range = range

            else: 
                self.range = Range(range)


    @property
    def size(self):
        if not self.range:
            return None
        
        return self.range.size
        

    def __str__(self) -> str:
        cad = f"{self.name}"
        if self.range:
            cad += f"{self.range}"
        return cad
    

    def __repr__(self) -> str:
        return (str(self))
    

    def json(self) -> dict:
        obj = {
            "name": self.name
        }

        if self.range:
            obj["range"] = str(self.range)
            obj["size"] = self.range.size
    
        return obj
    
    
    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, Port):
            return self.name == __value.name


class Ports:
    """Class for representing a list of ports"""

    def __init__(self, *ports) -> None:
        self.list = list(ports)

        #-- Empty list initially
        self.list = []

        for port in ports:
            if isinstance(port, Port):
                self.list.append(port)

            #-- The port is given as a dicctionary (json)
            elif isinstance(port, dict):
                self.list.append(Port(**port))

            else:
                raise AttributeError("Argument is not of port type")
            

    def __str__(self) -> str:

        #-- Create a list with the names of the ports
        l = [str(port) for port in self.list]
        l = ",".join(l)

        cad = f"Ports({l})"
        return cad
    

    def __repr__(self) -> str:
        return str(self)
    
    def json(self):
        """Return the class as a Json object"""

        list_json = [port.json() for port in self.list]

        return list_json
    
    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, Ports):

            #-- Diferent number of ports
            if len(self.list) != len(__value.list):
                return False
            
            res = False
            #-- Compare the ports, one by one
            for i, j in zip(self.list, __value.list):
                if i != j:
                    return False
            else:
                return True


class InOutPorts:
    """All input and output ports of a verilog entity"""

    def __init__(self, inp=Ports(), out=Ports()) -> None:

        #-- Inp property
        if isinstance(inp, Ports):
            self.inp = inp

        elif isinstance(inp, list):
            self.inp = Ports(*inp) 

        else:
            raise AttributeError("Unknown type for inports")
        
        #-- Out property
        if isinstance(out, Ports):
            self.out = out

        elif isinstance(out, list):
            self.out = Ports(*out)

        else:
            raise AttributeError("Unknown type for outports")


    def __str__(self) -> str:
        cad = f"In{self.inp}, "
        cad += f"Out{self.out}"
        return cad
    
    def __repr__(self) -> str:
        return str(self)
    
    def json(self) -> dict:
        return {
            "in": self.inp.json(),
            "out": self.out.json(),
        }
    
    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, InOutPorts):
            return (self.inp == __value.inp) and \
                   (self.out == __value.out)


class Pin:
    """Class for representing one pin"""

    def __init__(self, 
                 index: str = "0", #-- Pin position in icestudio
                 name: str = "NULL",  #-- Pin name
                 value: str = "NULL", #--- FPGA pin number
                 ) -> None:
        """Pin constructor"""

        #----- index property
        if isinstance(index, str):
            self.index = index

        #-- Invalid type for index
        else:
            raise AttributeError("Invalid type for index")
        
        #----- Name property
        if isinstance(name, str):
            self.name = name

        #-- Invalid type for name
        else:
            raise AttributeError("Invalid type for name")
        
        #----- Value property
        if isinstance(value, str):
            self.value = value

        #-- Invalid type for value
        else:
            raise AttributeError("Invalid type for value")
        
    def __str__(self) -> str:
        cad = (f"Pin({self.index}, {self.name}, {self.value})")
        return cad
    
    def __repr__(self) -> str:
        return str(self)
    
    def json(self) -> dict:
        return {
            "index": self.index,
            "name": self.name,
            "value": self.value
        }
    
    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, Pin):
            return (self.index == __value.index) and \
                   (self.name == __value.name) and \
                   (self.value == __value.value)


class Pins:
    """Class for representing a list of pins"""

    def __init__(self, *pins) -> None:
        self.list = list(pins)

        #-- Empty list initially
        self.list = []

        for pin in pins:
            if isinstance(pin, Pin):
                self.list.append(pin)

            #-- The pin is given as a dicctionary (json)
            elif isinstance(pin, dict):
                self.list.append(Pin(**pin))

            else:
                raise AttributeError("Argument is not of pin type")
            
    def __str__(self) -> str:
        cad = "Pins:"
        for pin in self.list:
            cad += '\n' + str(pin)
        return cad
    
    def __repr__(self) -> str:
         
        #-- Create a list with the names of the pins
        l = [pin.name for pin in self.list]
        l = ",".join(l)

        cad = f"Pins[{l}]"
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        list_json = [pin.json() for pin in self.list]

        return list_json
    
    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, Pins):

            #-- Diferent number of pins
            if len(self.list) != len(__value.list):
                return False
            
            res = False
            #-- Compare the pins, one by one
            for i, j in zip(self.list, __value.list):
                if i != j:
                    return False
            else:
                return True


class EndPoint:
    """Connection Point"""

    def __init__(self, block:str="", port:str="") -> None:
        
        #--- Block attribute: Block identifier
        if isinstance(block, str):
            self.block = block
        else:
            raise AttributeError("block is not a String")

        #--- Port attribute: Port that is connected
        if isinstance(port, str):
            self.port = port
        else:
            raise AttributeError("port is not a String")


    def __str__(self) -> str:
        """String representation"""

        cad = f"EndPoint({self.block}, {self.port})"
        return cad
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, EndPoint):
            return (self.block == __value.block) and \
                   (self.port == __value.port)
        
    def json(self):
        """Return the class as a Json object"""

        return {
            "block": self.block,
            "port": self.port
        }


class Wire:
    """Icestudio wire"""

    def __init__(self, 
                 source=EndPoint(), 
                 target=EndPoint(), 
                 size=None) -> None:

        #-- A wire connects 2 Endpoints: from source to target
        #-- The size property is the bus size. When the wire
        #-- is only 1-bit, this property is NOT present

        #-- Source property
        if isinstance(source, EndPoint):
            self.source = source
        elif isinstance(source, dict):
            self.source = EndPoint(**source)
        else:
            raise AttributeError("Unknown type for source EndPoint")
        
        #-- Target property
        if isinstance(target, EndPoint):
            self.target = target
        elif isinstance(target, dict):
            self.target = EndPoint(**target)
        else:
            raise AttributeError("Unknown type for target EndPoint")
        
        if isinstance(size,int) or size==None:
            self.size = size
        else:
            raise AttributeError("Invalid size")


    def __str__(self) -> str:
        cad = f"Wire({self.source},{self.target}"
        if self.size == None:
            cad += ",1"
        else:
            cad += f",{self.size}"
        cad += ")"
        return cad
    
    def __repr__(self) -> str:
        cad = "Wire(...)"
        return cad
    
    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, Wire):
            return (self.source == __value.source) and \
                   (self.target == __value.target) and \
                   (self.size == __value.size)
        
    def json(self):
        """Return a json object"""

        obj = {
            "source": self.source.json(),
            "target": self.target.json()
        }

        if self.size != None:
            if self.size > 1:
                obj["size"]= self.size

        return obj


class Wires:
    """List of Icestudio wires"""

    def __init__(self, *wires) -> None:

        #-- Empty list initially
        self.list = []

        #-- Check that all the arguments are of type Wire
        for wire in wires:
            if isinstance(wire, Wire):
                self.list.append(wire)

            #-- The wire is given as a dicctionary (json)
            elif isinstance(wire, dict):
                self.list.append(Wire(**wire))

            else:
                raise AttributeError("Argument is not of wire type")

    def __str__(self) -> str:
        cad = "\n".join([str(wire) for wire in self.list])
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        list_json = [wire.json() for wire in self.list]

        return list_json

     
class DataCode:
    """Class for representing the data part of the Code blocks"""

    def __init__(self, 
                 ports=InOutPorts(),
                 params=[],
                 code:str=""
                 ) -> None:
        
        #--- ports Attribute (ioports)
        if isinstance(ports, InOutPorts):
            self.ports = ports

        elif isinstance(ports, dict):

            #-- Cambiar la propiedad "in" por "inp"
            ports["inp"] = ports.pop("in")
            self.ports = InOutPorts(**ports)

        else:
            raise AttributeError("Unknown type for ports (ioports)")

        #--- params Attribute
        self.params = params

        #--- code attribute
        if isinstance(code, str):
            self.code = code

        else:
            raise AttributeError("code is not a String")
    

    def __str__(self) -> str:
        """String representation"""

        cad = "DataCode:\n"
        cad += f"* {self.ports}\n"
        cad += f"* Params: {self.params}\n"
        cad += f"* Code: {self.code}"
        return cad
    
    def __repr__(self) -> str:
        return "DataCode(...)"
    
    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, DataCode):
            return (self.ports == __value.ports) and \
                   (self.params == __value.params) and \
                   (self.code == __value.code)

    
    def json(self):
        """Return the class as a Json object"""

        return {
            "ports": self.ports.json(),
            "params": self.params,
            "code": self.code
        }



class DataInfo:
    """Class for representing the data part of the Info blocks"""

    def __init__(self, info:str="", readonly:bool=True) -> None:

        #-- Set the info attribute
        if isinstance(info, str):
            self.info = info

        else:
            raise AttributeError("info is not a String")
        
        #-- Set the readonly attribute
        if isinstance(readonly, bool):
            self.readonly = readonly

        else:
            raise ArithmeticError("readonly is not Boolean")



    def __str__(self) -> str:
        """String representation"""

        cad = f"Info: {self.info}\n"
        cad += f"Readonly: {self.readonly}\n"
        return cad

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, DataInfo):
            return (self.info == __value.info) and \
                   (self.readonly == __value.readonly)


    def json(self):
        """Return the class as a Json object"""

        return {
            "info": self.info,
            "readonly": self.readonly
        }
    

class DataPin:
    """Class for representing the data part of the Pin blocks"""

    def __init__(self, 
                 name="", 
                 virtual=False, 
                 range=None,
                 pins=Pins(),
                 clock=None) -> None:

        #-- Set the name attribute
        if isinstance(name, str):
            self.name = name

        else:
            raise AttributeError("name is not a String")

        #-- Set the virtual attribute
        if isinstance(virtual, bool):
            self.virtual = virtual

        else:
            raise AttributeError("virtual is not Boolean")
        
        #-- Set the range attribute
        if range != None:
            if isinstance(range, str):
                self.range = range

        #-- Set the pins attribute
        if isinstance(pins, Pins):
            self.pins = pins

        elif isinstance(pins, list):
            self.pins = Pins(*pins)

        else:
            raise AttributeError("Invalid type for pins")

        #-- Set the clock attribute (only input pins)
        if clock != None:
            if isinstance(clock, bool):
                self.clock = clock

            else:
                raise AttributeError("Invalid type for clock")


    def __str__(self) -> str:
        """String representation"""

        cad = f"Name: {self.name}\n"
        cad += f"Virtual: {self.virtual}\n"
        cad += f"{self.pins}"
        if hasattr(self, "clock"):
            cad += f"\nClock: {self.clock}"
        return cad
    
    def json(self) -> dict:
        obj = {
            "name": self.name,
            "virtual": self.virtual,
            "pins": self.pins.json()
        }

        #-- Add the clock attribute (if it exists)
        if hasattr(self, "clock"):
            obj["clock"] = self.clock

        return obj
    

    def __eq__(self, __value: object) -> bool:
        """Compare two objects"""

        if isinstance(__value, DataPin):
            return (self.name == __value.name) and \
                   (self.virtual == __value.virtual) and \
                   (self.pins == __value.pins)



class Block:
    """Class for representing an Icestudio block"""
    def __init__(self, 
                 id="", 
                 type="basic.info",
                 data=DataInfo(),
                 position=Position(),
                 size=Size()) -> None:
        
        #------------ Id Attribute
        #-- Check if it is an String
        if isinstance(id, str):
            self.id = id

        #-- Unknown type for the id attribute
        else:
            raise AttributeError("id is not a String")

        #--------- Type Attribute
        #-- Check if it is a valid string
        if isinstance(type, str):
                self.type = type
        else:
            raise AttributeError("type is not a String")

        #-------- Data attribute
        match(type):

            case "basic.info":
                #-- Check if it is a DataInfo object
                if isinstance(data, DataInfo):
                    self.data = data

                #-- Check if it has been defined as an Json object (dictionary)
                elif isinstance(data, dict):
                    self.data = DataInfo(**data)

                else:
                    raise AttributeError("Unknow type for data")
                
            case "basic.output" | "basic.input":
                #-- Check if it is a DataPin object
                if isinstance(data, DataPin):
                    self.data = data
                
                #-- check if it has been defined as a Json object (dictionary)
                elif isinstance(data, dict):
                    self.data = DataPin(**data)

                else:
                    raise AttributeError("Unknow type for data")
                
            case "basic.code":
                #-- Check if it is a DataCode object
                if isinstance(data, DataCode):
                    self.data = data
                
                #-- check if it has been defined as a Json object (dictionary)
                elif isinstance(data, dict):
                    self.data = DataCode(**data)

                else:
                    raise AttributeError("Unknow type for data")

            #-- User block
            case _:
        
                #-- Unknown type for the design attribute
                #raise AttributeError("Unsupported block type")
                ...


        #------- Position property
        #-- Check if it is a Position object
        if isinstance(position, Position):
            self.position = position

        #-- Check if it has been defined as an Json object (dictionary)
        elif isinstance(position, dict):
            self.position = Position(**position)

        #-- Unknown type for the design attribute
        else:
            raise AttributeError("Unknow type for position")

        #------- Size property
        #-- Check if it is a Size object
        if isinstance(size, Size):
            self.size = size

        #-- Check if it has been defined as an Json object (dictionary)
        elif isinstance(size, dict):
            self.size = Size(**size)

        #-- Unknown type for the design attribute
        else:
            raise AttributeError("Unknow type for size")


    def __str__(self) -> str:
        """String representation"""

        cad = f"id: {self.id}\n"
        cad += f"Type: {self.type}\n"
        cad += f"Data: {self.data}\n"
        cad += f"Pos: {self.position}\n"
        cad += f"Size: {self.size}\n"
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        return {
            "id": self.id,
            "type": self.type,
            "data": self.data.json(),
            "position": self.position.json(),
            "size": self.size.json()
        }
    
class Blocks:
    """Class for representing a list of icestudio blocks"""
    def __init__(self, *blocks) -> None:

        #-- Empty list initially
        self.list = []

        #-- Check that all the arguments are of type Block
        for block in blocks:
            if isinstance(block, Block):
                self.list.append(block)

            #-- The block is given as a dicctionary (json)
            elif isinstance(block, dict):
                self.list.append(Block(**block))

            else:
                raise AttributeError("Argument is not of block type")


    def __str__(self) -> str:
        cad = "\n".join([str(block) for block in self.list])
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        list_json = [block.json() for block in self.list]

        return list_json
    

class Graph:
    """Class for representing an Icestudio circuit"""

    def __init__(self, blocks=Blocks(), wires=[]) -> None:

        #-- Set the blocks attribute
        if isinstance(blocks, Blocks):
            self.blocks = blocks

        #-- Given as a list (json object)
        elif isinstance(blocks, list):
            self.blocks = Blocks(*blocks)

            #-- Invalid type for blocks
        else:
            raise AttributeError("blocks is not of type Blocks")


        self.wires = wires
        
    def __str__(self) -> str:
        cad = f"* Blocks: {self.blocks}\n"
        cad += f"* Wires: {self.wires}\n"
        return cad

    def json(self) -> dict:
        """Return the class as a Json object"""

        return {
            "blocks": self.blocks.json(),
            "wires": self.wires
        }
    
class Design:
    """Class for representing an Icestudio design"""

    def __init__(self, board=None, graph=Graph()) -> None:

        #--- Check board attribute
        if board != None:
            if (isinstance(board, str)):
                self.board = board

            else:
                raise AttributeError("board is not a string")

        #-- Check Graph attribute
        if isinstance(graph, Graph):
            self.graph = graph

        #-- Check if it is a dict (json object)    
        elif isinstance(graph, dict):
            self.graph = Graph(**graph)
        
        else:
            raise AttributeError("Unknown type for Graph")


    def __str__(self) -> str:
        cad = f"* Design:\n"
        if hasattr(self, "board"):
            cad += f"Board: {self.board}\n"
        cad += f"Graph: {self.graph}\n"
        return cad
    
    def json(self) -> dict:
        obj = {
            "graph": self.graph.json()
        }
        if hasattr(self, "board"):
            obj['board'] = self.board

        return obj


class Ice:
    """Class for representing a full Icestudio circuit"""

    def __init__(self, 
                 version: str="", 
                 package={}, 
                 design=Design(), 
                 dependencies={}) -> None:
        
        #---- Version attribute
        #-- Check version
        if isinstance(version, str):
            self.version = version

        #-- Invalid version type (should be a string)
        else:
            raise AttributeError("Invalid version type (should be a string)")

        self.package = package

        #-- Design property
        #-- Check if it is a Design object
        if isinstance(design, Design):
            self.design = design

        #-- Check if have been defined as an Json object (dictionary)
        elif isinstance(design, dict):
            self.design = Design(**design)

        #-- Unknown type for the design attribute
        else:
            raise(AttributeError)
        

        self.dependencies = dependencies

    def __str__(self) -> str:
        cad = f"Version: {self.version}\n"
        cad += f"Package: {self.package}\n"
        cad += f"Design: {self.design}\n"
        cad += f"Dependencies: {self.dependencies}\n"
        return cad
    
    def json(self) -> dict:
        return {
            "version": self.version,
            "package": self.package,
            "design": self.design.json(),
            "dependencies": self.dependencies
        }
    
    def open_file(self, file) -> None:
        """Read an Icestudio circuito (.ice)"""

        #-- Read the json file and create the object
        with open(file) as f:
            ice_json = json.load(f)
            
        #-- Initialize the class from the json object
        self.version = ice_json['version']
        self.package = ice_json['package']
        self.design = Design(**ice_json['design'])
        self.dependencies = ice_json['dependencies']
