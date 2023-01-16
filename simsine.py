# Kapittel 1 - Følger og rekker
def lag_følge(ledd_1: int, antall_ledd: int, rekursiv: bool, formel: any, **kwargs):
    """
    Funksjon som returnerer resultatet av en rekursiv følge. \n
    'formel' argumentet må passeres med en lambda funksjon med f_n som et argument.
    """
    følge = []
    if rekursiv:
        følge.append(ledd_1)
        for n in range(0, antall_ledd-1):
            følge.append(formel(følge[n], **kwargs))
        return følge
    else:
        for n in range (1, antall_ledd+1):
            følge.append(formel(n))
        return følge

def sumasjon(nedre_grense, øvre_grense, funksjon):
    """
    Returnerer summen av verdiene for funksjonen mellom nedre og øvre grense
    """
    summert = 0
    for i in range(nedre_grense, øvre_grense):
        summert += funksjon(i)
    return summert

# Tror dette er en funksjon for n'te ledd av en aritmetisk følge
# Må skrives om og lage for andre formlr også
def ar_ledd(l_1:int, diff:int, nth:int):
    return(l_1 + (nth-1) * diff)

# Kapittel 2 - Integrasjon

def rektangelsum(a:int, b:int, N:int, f:any):
    """
    Funksjon som returnerer et estimat av det totale arealet under en graf ved rektangelsum metoden
    sum(N, i=1, ...)
    """
    areal = 0 # Deklarere areal
    delta_x = (b - a) / N # Finne delta x
    
    # TODO : Erstatt med sum funksjon
    for i in range(1,N+1): # Sum
        areal += f((a+(i-1)* delta_x)) * delta_x # Legg til sum med itterasjon
        
    return(areal) # Returnere det totale arealet

def trapessum(a:int, b:int, N:int, f:any):
    """
    Funksjon som returnerer et estimat av det totale arealet under en graf ved trapessum metoden
    sum(N, i=1, ...)
    """
    areal = 0 # Deklarere areal
    delta_x = (b - a) / N # Finne delta x
    
    # TODO : Erstatt med sum funksjon
    sumasjon = 0
    for i in range(1, N-1): # Sum
        sumasjon += f(a + i * delta_x) * delta_x
        
    areal = ((f(a) + f(b)) * delta_x/2) + sumasjon
    
    return(areal)

# Kapittel 3 - Trigonometri

def gradertilradianer(ngrader:float):
    """
    Konverterer grader til radianer\n
    (n°) / (180°) * (pi)
    """
    import numpy as np
    return((ngrader) / (180) * (np.pi))

def radianertilgrader(v:float):
    """
    Konverterer radianer til grader\n
    v / pi * 180°
    """
    import numpy as np
    return((v) / (np.pi) * (180))

# Eksempler med funksjoner
def main():
    # Kapittel 1 - Følger og rekker
    f_1, funksjon = 2, lambda f_n:(2 * f_n)
    print(lag_følge(ledd_1=f_1, antall_ledd=10, rekursiv=True, formel=funksjon ))
    
    # Kapittel 2 - Integrasjon
    import numpy as np
    print(rektangelsum(1, 4, 100, lambda x: (np.sqrt(x)) )) # Test
    print(trapessum(1, 4, 100, lambda x: (np.sin(x)) )) # Test
    
    # Kapittel 3 - Trigonometri
    grader = 90
    print(f"{grader} grader tilsvarer {gradertilradianer(grader)} radianer\n")

if __name__ == '__main__':  # This code won't run if this file is imported.
     main()