
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

