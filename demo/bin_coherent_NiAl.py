from openiec.calculate.calcsigma import SigmaCoherent
from pycalphad import Database


def test():
    """
    The calculation for the interfacial energy of the FCC_A1/GAMMA_PRIME interface in the Ni-Al system.
    """
    # Given temperature.
    T = 800.00
    # Given initial alloy composition. x0 is the mole fraction of Al.
    x0 = [0.2]  
    # Render thermodynamic database.
    db = Database("NiAlHuang1999.tdb")
    # Define components in the interface.
    comps = ["NI", "AL", "VA"]
    # Two phases separated by the interface.
    phasenames = ["FCC_A1", "GAMMA_PRIME"]

    # Molar volumes of pure components to construct corresponding molar volume database.
    # Molar volume of Ni.
    vni = "6.718*10.0**(-6.0) + (2.936*10.0**(-5)*10.0**(-6.0))*T**1.355" 
    # Molar volume of Al.
    val = "10.269*10.0**(-6.0) + (3.860*10.0**(-5)*10.0**(-6.0))*T**1.491"
    purevms = [[vni, val], ]*2

    # A composition range for searching initial interfacial equilirium composition.
    limit = [0.0001, 0.3]
    # The composition step for searching initial interfacial equilirium composition.
    dx = 0.1
    
    # Call the module for calculating coherent interfacial energies.
    sigma = SigmaCoherent(
        T=T,
        x0=x0,
        db=db,
        comps=comps,
        phasenames=phasenames,
        purevms=purevms,
        limit=limit,
        dx=dx,
    )
    
    # Print the calculated interfacial energy with xarray.Dataset type.
    print(sigma, "\n")
    # Print the calculated interfacial energy with xarray.DataArray type.
    print(sigma.Interfacial_Energy, "\n")
    # Print the calculated interfacial energy value.
    print(sigma.Interfacial_Energy.values, "\n")

    # Output
    """
    <xarray.Dataset>
    Dimensions:                     (Components: 2)
    Coordinates:
    * Components                  (Components) <U2 'NI' 'AL'
    Data variables:
        Temperature                 float64 800.0
        Initial_Alloy_Composition   (Components) float64 0.8 0.2
        Interfacial_Composition     (Components) float64 0.88 0.12
        Partial_Interfacial_Energy  (Components) float64 0.02662 0.02662
        Interfacial_Energy          float64 0.02662

    <xarray.DataArray 'Interfacial_Energy' ()>
    array(0.0266243)

    0.026624295289653314
    """


if __name__ == "__main__":
    test()
