
class Size:
    """Class for representing the size of an Icestudio block"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __str__(self):
        """String representation"""
        cad = f"Size({self.width}, {self.height})"
        return cad
    
    def json(self):
        """Return the class as a Json object"""
    
        return {
            "width" : self.width,
            "height": self.height
        }



