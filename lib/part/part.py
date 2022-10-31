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
