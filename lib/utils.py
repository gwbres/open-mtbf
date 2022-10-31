import numpy as np

def kelvin2celcius (kv):
    """
    Converts Kelvin degrees [K] to celcius degrees [C]
    """
    return k - 273

def celcius2kelvin (c):
    """
    Converts celcius degrees [C] to Kelvin degrees [K]
    """
    return c + 273

def arrhenius(tj_ref, tj)
    """
    Arrhenius equations gives the acceleration factor `Af`
    for given tj_ref: Reference junction temperature [K]
    and tj: junction temperature [K] during tests
    """
    K = 8.617 * 10E-5 # Boltzmann's constant [eV/Tk]
    Ea = 1.0 # Activation Energy [eV]
    B = 1/tj_ref - 1/tj 
    A = Ea / k
    return np.exp(A * B)

def arrhenius_celcius(tj_ref, tj)
    """
    Macro to compute Arrhenius equation from given tj and tj_ref
    expressed in Celcius degrees [C]
    """
    return arrhenius(celcius2kelvin(tj_ref), celcius2kelvin(tj))
