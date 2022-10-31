from part import Part
class System (Part):
    """
    System is the result of several `parts` hybridation
    """
    # <o
    #  if digital part is present:
    #     failure rate is dominant
    #  otherwise, if only analog/passive devices: 
    #     failure rate must be calculated accordingly

    #  total failure rate is the sum of all internal failure rates
    #  with the overall hybrid function xf
    #  the overall screening level pi_Q
    #  and overall maturity pi_L taken into account
    def __init__ (self, components=[]):
        self.components = components

    def add_component (self, component):
        """
        Adds given component to system assembly
        """
        self.components.append(component)

    def rm_component (self, component):
        """
        Removes given component from system assembly
        """
        for i in range (len(self)):
            if self.components[i] == component:
                del self.components[i]
                break 

    def rm_index (self, index):
        """
        Removes component by index
        """
        if len(self) > index:
            del self.components[i]

    def __len__ (self):
        """
        Returns total amount of subsystems contained in this assembly
        """
        return len(self.components)

    def __getitem__ (self, index):
        """
        Returns given part of this system
        """
        return self.components[index]
 
    def __setitem__ (self, index, item):
        """
        Assigns given part of this system
        """
        self.components[index] = item

    def has_active_components (self):
        """
        Returns true if self does have active components
        """
        for component in self.components:
            if component.is_active():
                return True
        return False
 
    def only_passive (self):
        """
        Returns true if self is only made of passive components
        """
        return not self.has_active_components
