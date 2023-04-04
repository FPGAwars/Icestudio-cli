
class Size:
    """Class for representing the size of an Icestudio block"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
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


class Position:
    """Class for representing the position of an Icestudio block"""

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

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
                 size={}) -> None:
        
        self.id = id
        self.type = type
        self.data = data
        self.position = position
        self.size = size

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
            "size": self.size
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

    def json(self) -> str:
        """Return the class as a Json object"""

        return {
            "blocks": self.blocks,
            "wires": self.wires
        }