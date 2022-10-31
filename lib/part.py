import numpy as np
class Part:
    def __init__ (self, *args, **kwargs):
        """ builds a new \"Part\" with given base failure rate \"base-fr\"
        and possible environment biases \"pi-env\"
        """
        self.pi = kwargs.get("pi", None)

    def lambda_p (self):
        """ returns lambda p failure prediction model """
        raise RuntimeError("prediction model not implemented for this part")

    def failure_rate (self):
        """ returns failure rate for given part.
        Failure rate is expressed as the combination of a base model
        biased by environmental factors
        """
        raise RuntimeError("failure rate calculation not implemented for this part")

    def failure_curve (self, t_axis):
        """ returns Gate failure rate for given duration range """
        y = []
        for t in t_axis:
            y.append(self.failure_rate(t))
        return y

    def Categories (self):
        return {"blackbox": None}
    
