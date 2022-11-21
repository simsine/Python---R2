def trappessum(a:int, b:int, N:int, f):
    """
    Funksjon som returnerer et estimat av det totale arealet under en graf ved trappessum metoden
    sum(N, i=1, ...)
    """
    areal = 0 # Deklarere areal
    delta_x = (b - a) / N # Finne delta x
    for i in range(1,N+1): # Sum
        areal += f((a+(i-1)* delta_x)) * delta_x # Legg til sum med itterasjon
    return(areal) # Returnere det totale arealet

def main():
    import numpy as np
    
    print(trappessum(1, 4, 100, lambda x: np.sqrt(x))) # Test
    print(trappessum(1, 4, 100, lambda x: 1/x)) # Test
    
if __name__ == '__main__':  # This code won't run if this file is imported.
     main()
