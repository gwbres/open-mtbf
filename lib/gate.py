from lib.part import Part
class Gate (Part):
    def __init__ (self, *args, **kwargs):
        """ 
        Builds a new Gate part (transistor, digital microcircuit).
        kind: ["bipolar", "mos"] for modelization
        technology: ["digital", "linear", "pla", "pal"] for modelization
        gates: number of logical gates or transistors in the circuit
        """
        super().__init__(*args, **kwargs)
        self.set_gates(int(kwargs.get("gates", 1)))
        self.set_kind(kwargs.get("kind", "bipolar"))
        self.set_technology(kwargs.get("technology", "digital"))
    
    def set_kind (self, kind):
        """ 
        Sets internal kind of gate 
        """
        categories = Gate.Categories()
        if not kind in categories:
            raise ValueError("`{}` is not a valid Gate object".format(kind))
        self.kind = kind

    def set_technology (self, technology):
        """ 
        Sets internal technology 
        """
        technologies = Gate.Categories()[self.kind]
        print(technologies)
        if not technology in technologies: 
            raise ValueError("`{}` is not a valid {} Gate technology".format(technology, self.kind))
        self.technology = technology

    def set_gates (self, n):
        """ 
        Assigns internal number of gates 
        """
        self.nb_gates = n

    def failure_rate (self, duration):
        """ 
        Returns Gate failure rate for given duration 
        """
        (C1, C2) = self.C1C2()
        pi = self.pi
        (C1 * pi["T"] + C2 * pi["E"]) * pi["Q"] * pi["L"] /pow(10,6) /duration.hours()

    def C1C2 (self):
        """ 
        Returns equations coefficient for given number of gates.
        "C1" is die complexity failure coefficient.
        "C2" is [...]
        """
        table = Gate.Table()
        if not self.kind in table:
            raise RuntimeError("`{}` is not a supported kind of gate".format(self.kind))
        table = table[self.kind]
        if not self.technology in table:
            raise RuntimeError("non supported `{}` technology for `{}` gate".format(self.technology, self.kind))

        table = table[self.technology]
        c = {
            "C1": 0.0,
            "C2": 0.0,
        }
        
        for k in ["C1", "C2"]:
            t = table[k]
            keys = list(t.keys())
            c[k] = t[keys[0]]
            for i in range (1, len(keys)):
                n_n1 = keys[i-1]
                n = keys[i]
                if self.nb_gates <= n:
                    if self.nb_gates > n_n1: # within
                        c[k] = t[n] # current interval
                elif i == len(keys)-1: # largest pop was reached
                    c[k] = t[n]
        return c

    def Categories():
        return {
            "Bipolar": ["Digital", "Linear", "PAL", "PLA"],
            "MOS": ["Digital", "Linear", "PAL", "PLA"],
        }

    def Table():
        table = {
            "Bipolar": {
                "Digital": {
                    "C1": {
                         100: 0.0025,
                        1000: 0.005,
                        3000: 0.010,
                       10000: 0.020,
                       30000: 0.040,
                       60000: 0.080
                    },
                    "C2": {
                         100: 0.0025,
                        1000: 0.0050,
                        3000: 0.010,
                       10000: 0.020,
                       30000: 0.040,
                       60000: 0.080
                    }
                },
                "Linear": {
                    "C1": { 
                        100: 0.01,
                        300: 0.02,
                        1000: 0.04,
                        10000: 0.06
                    },
                    "C2": {
                        100: 0.01,
                        300: 0.02,
                        1000: 0.04,
                        10000: 0.06
                    },
                },
                "PAL": {
                    "C1": {
                        200: 0.01,
                        1000: 0.021,
                        5000: 0.042
                    },
                    "C2": {
                        200: 0.01,
                        1000: 0.021,
                        5000: 0.042
                    },
                },
            },
            "MOS": {
                "Digital": {
                    "C1": {
                        100: 0.01,
                        1000: 0.02,
                        3000: 0.04,
                        10000: 0.08,
                        30000: 0.16,
                        60000: 0.29,
                    },
                    "C2": {
                        100: 0.01,
                        1000: 0.02,
                        3000: 0.04,
                        10000: 0.08,
                        30000: 0.16,
                        60000: 0.29,
                    },
                },
                "Linear": {
                    "C1": {
                        100: 0.01,
                        300: 0.02,
                        1000: 0.04,
                        10000: 0.06,
                    },
                    "C2": {
                        100: 0.01,
                        300: 0.02,
                        1000: 0.04,
                        10000: 0.06,
                    },
                },
                "PAL": {
                    "C1": {
                        500: 0.00085,
                        1000: 0.0017,
                        5000: 0.0034,
                        20000: 0.0068,
                    },
                    "C2": {
                        500: 0.00085,
                        1000: 0.0017,
                        5000: 0.0034,
                        20000: 0.0068,
                    },
                },
            },
        }
        table["MOS"]["PLA"] = table["MOS"]["PAL"].copy()
        table["Bipolar"]["PLA"] = table["Bipolar"]["PAL"].copy()
        return table
