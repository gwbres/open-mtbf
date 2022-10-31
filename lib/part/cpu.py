from part import Gate
class Cpu (Gate):
    def __init__ (self, *args, **kwargs):
        """ builds a new CPU part (digital microprocessor).
        technology: ["bipolar", "mos",] for modellization
        bits: architecture nb of bits [8, 16, 32, 64]
        """
        super().__init__(*args, **kwargs)
        self.technology = kwargs.get("technology", "digital")
        self.bits = int(kwargs.get("bits", 8))

    def failure_rate (self, duration):
        """ returns Gate failure rate for given duration """
        (self.C("C1") * self.pi_T() + self.C("C2") * self.pi_E()) * self.pi_Q()*self.pi_L() /pow(10,6)/duration.hours()

    def C (self, c):
        """ returns weight coefficient.
        "C1" is die complexity failure coefficient.
        "C2" is [...]
        """
        fr = 0.0
        table = self.table(t)
        for (pop, r) in table:
            if pop < self.nb_gates:
                fr = r
            else:
                break
        return fr
               
    def table (self, c):
        if self.technology == "bipolar":
            self.bipolar_table(c)
        elif self.technoloyg == "mos":
            self.cmos_table(c)
        else:
            raise RuntimeError(format("`{:0}` is not a supported kind of gate", self.kind))
