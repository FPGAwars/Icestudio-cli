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

            #-- Check if the string represent a valid type
            match(type):
                case "basic.info":
                    self.type = type
                case _:
                    raise AttributeError("Unknow block type name")

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

            case _:
        
                #-- Unknown type for the design attribute
                raise AttributeError("Unsupported block type")


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
