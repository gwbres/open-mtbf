class Environment:
    def __init__ (self, *args, **kwargs):
        self.set_kind(kwargs.get("kind", "ground"))
        self.set_model(kwargs.get("model", "fixed"))
    
    def Categories(self):
        return {
            "ground": {
                "laboratory": {
                    "short": "GB",
                    "help": """Nonmobile  temperature and humidity
                    controlled environments readily accessitde to
                    maintenance; includes laboratory instruments
                    and test equipment, medical electronic
                    equipment, businass and scientifc computer
                    complexes, and missiles and support
                    equipment in ground sibs.""",
                },
                "fixed": {
                    "short": "GF",
                    "help": """Moderately amtrolied environments such as
                    installation in permanent racks with adequate
                    oooling air and possible installation m unheated
                    buildings; includes permanent tnstattatton of air
                    traffic control radar and communications
                    facilities.""",
                },
                "mobile": {
                    "short": "GM",
                    "help": """Equipment installed on wheeled or tradwd
                    vehicles and equipment manually transported;
                    includes ttiicai missile ground support
                    equipment, mobile communication equipment,
                    tactical fire direction systems, handheld
                    communications equipment, laser designations
                    and range finders."""
                },
            },
        }

    def short (self):
        return Environment.Categories()[self.kind][self.model]["short"]

    def case_temperature (self):
        
