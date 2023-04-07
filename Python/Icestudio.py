import json

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
    
    def json(self):
        """Return the class as a Json object"""

        return {
            "x": self.x,
            "y": self.y
        }


class DataInfo:
    """Class for representing the data part of the Info blocks"""

    def __init__(self, info="", readonly=True) -> None:
        self.info = info
        self.readonly = readonly

    def __str__(self) -> str:
        """String representation"""

        cad = f"DataInfo: {self.readonly}\n"
        cad += f"  Info: {self.info}"
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        return {
            "info": self.info,
            "readonly": self.readonly
        }


class Block:
    """Class for representing an Icestudio block"""
    def __init__(self, 
                 id="", 
                 type="",
                 data={},
                 position={},
                 size=Size()) -> None:
        
        self.id = id
        self.type = type
        self.data = data
        self.position = position

        #-- Size property
        #-- Check if it is a Size object
        if isinstance(size, Size):
            self.size = size

        #-- Check if it has been defined as an Json object (dictionary)
        elif isinstance(size, dict):
            self.size = Size(**size)

        #-- Unknown type for the design attribute
        else:
            raise(AttributeError)


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
            "data": self.data,
            "position": self.position,
            "size": self.size.json()
        }
    
class Blocks:
    """Class for representing a list of icestudio blocks"""
    def __init__(self, *blocks) -> None:
        self.list = list(blocks)

    def __str__(self) -> str:
        cad = "\n".join([str(block) for block in self.list])
        return cad
    
    def json(self):
        """Return the class as a Json object"""

        list_json = [block.json() for block in self.list]

        return list_json
    

class Graph:
    """Class for representing an Icestudio circuit"""

    def __init__(self, blocks=[], wires=[]) -> None:
        self.blocks = blocks
        self.wires = wires
        
    def __str__(self) -> str:
        cad = f"* Blocks: {self.blocks}\n"
        cad += f"* Wires: {self.wires}\n"
        return cad

    def json(self) -> dict:
        """Return the class as a Json object"""

        return {
            "blocks": self.blocks,
            "wires": self.wires
        }
    
class Design:
    """Class for representing an Icestudio design"""

    def __init__(self, board="", graph={}) -> None:
        self.board = board
        self.graph = graph

    def __str__(self) -> str:
        cad = f"* Design:\n"
        cad += f"Board: {self.board}\n"
        cad += f"Graph: {self.graph}\n"
        return cad
    
    def json(self) -> dict:
        return {
            "board": self.board,
            "graph": self.graph
        }

class Ice:
    """Class for representing a full Icestudio circuit"""

    def __init__(self, 
                 version: str="", 
                 package={}, 
                 design=Design(), 
                 dependencies={}) -> None:
        
        self.version = version
        self.package = package

        #-- Design property
        #-- Check if it is a Design object
        if isinstance(design, Design):
            self.design = design

        #-- Check if have been defined as an Json object (dictionary)
        elif isinstance(design, dict):
            self.design = Design(design)

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
        self.design = Design(ice_json['design'])
        self.dependencies = ice_json['dependencies']
