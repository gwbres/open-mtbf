from lib.part import Part

class AnalogPart (Part): 
    def __init__ (self, *args, **kwargs):
        """ 
        Builds a new Analog part (transistor, diode..) 
        """
        super().__init__(*args, **kwargs)
