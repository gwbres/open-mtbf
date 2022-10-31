import numpy as np

class Part:
    def __init__ (self, *args, **kwargs):
        """ builds a new \"Part\" with given base failure rate \"base-fr\"
        and possible environment biases \"pi-env\"
        """
        self.kind = "blackbox"
        self.pi = kwargs.get("pi", None)

    def lambda_p (self):
        """ returns lambda p failure prediction model """
        raise RuntimeError("prediction model not implemented for `{}`".format(self.kind))

    def failure_rate (self):
        """ returns failure rate for given part.
        Failure rate is expressed as the combination of a base model
        biased by environmental factors
        """
        raise RuntimeError("failure rate calculation not implemented for `{}`".format(self.kind))

    def Categories (self):
        return {"blackbox": None}

    def is_active (self):
        return False

    def weibull (self, t): 
        """
        Returns weibull factor for self given time point or axis
        """
        nu = 1.0 #TODO
        beta = self.failure_rate()
        A = beta / nu
        B = t / nu
        return A * np.power(B, beta-1) * np.exp(np.power(B, beta))

    def reliability (self, t):
        """
        Returns part reliability for given time point or axis
        """
        return np.exp(-self.failure_rate() * t)
