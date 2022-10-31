import math
from lib.part.digital import DigitalPart

class Memory (DigitalPart):
    def __init__ (self, *args, **kwargs):
        """ 
        Builds a new Memory part (Read Only Memory (ROM)), Programmable Memmory (PROM),
        Flash, Static RAM (SRAM) or Dynamic RAM (DRAM).
        kind: ["MOS", "Bipolar"] for modelization
        technology: ["ROM", "(EE)PROM", "DRAM (MOS & BIMOS)", "",] for modelization
        size: memory size (bytes)
        """
        super().__init__(*args, **kwargs)
        self.set_size(int(kwargs.get("size", "16K")))
        self.set_kind(kwargs.get("kind", "bipolar"))
        self.set_technology(kwargs.get("technology", "digital"))
    
    def set_kind (self, kind):
        """ 
        Sets internal kind of gate 
        """
        categories = Memory.Categories()
        if not kind in categories:
            raise ValueError("`{}` is not a valid Memory object".format(kind))
        self.kind = kind

    def set_technology (self, technology):
        """ 
        Sets internal technology 
        """
        technologies = Memory.Categories()[self.kind]
        if not technology in technologies: 
            raise ValueError("`{}` is not a valid {} Memory technology".format(technology, self.kind))
        self.technology = technology

    def set_size (self, n):
        """ 
        Assigns internal memory size 
        """
        if type(n) == str:
        elif type(n) == int:
            self.size = n

    def Sizes():
        """
        Returns memory size description
        """
        for i in range (40):
            bits = math.pow(2,i)
            if bits

    def failure_rate (self, duration):
        """ 
        Returns Gate failure rate for given duration 
        """
        (C1, C2) = self.C1C2()
        pi = self.pi
        (C1 * pi["T"] + C2 * pi["E"] + Memory.LambdaCycle()) * pi["Q"] * pi["L"] /pow(10,6) /duration.hours()

    def LambdaCycleA (cycle):
        """
        Returns (A1, A2) factors for Lambda_cyc equation, for given amount of 
        Write (programming) cycles
        """
        return (Memory.LambdaCycleA1(), Memory.LambdaCycleA2())

    def LambdaCycleA1 (cycle):
        """
        Returns A1 factor for Lambda_cyc equation, for given amount of 
        Write (programming) cycles
        """
        return (6.817 * cycle /pow(10,6), 

    def LambdaCycleA2 (cycle):
        """
        Returns A2 factor for lambda_cyc equation, for given amount of programming (Write) cycles
        """
        if cycle <= 300000:
            return 0.0
        elif cycle <= 400000:
            return 1.1
        elif cycle <= 500000:
            return 2.3

    def LambdaCycle (cycle, Q=1.0, ECC=None):
        Memory.LambdaCycleA1(cycle) 
            * Memory.LambdaCycleB1(cycle) + 
                (Memory.LambdaCycleA2(cycle) + Memory.LambdaCycleB2(cycle)) / Q

    def C1C2 (self):
        """ 
        Returns equations coefficient for given number of gates.
        "C1" is die complexity failure coefficient.
        "C2" is [...]
        """
        table = Memory.Table()
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
