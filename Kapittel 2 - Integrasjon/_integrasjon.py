def rektangelsum(a:int, b:int, N:int, f:any):
    """
    Funksjon som returnerer et estimat av det totale arealet under en graf ved rektangelsum metoden
    sum(N, i=1, ...)
    """
    areal = 0 # Deklarere areal
    delta_x = (b - a) / N # Finne delta x
    for i in range(1,N+1): # Sum
        areal += f((a+(i-1)* delta_x)) * delta_x # Legg til sum med itterasjon
    return(areal) # Returnere det totale arealet

def trapessum(a:int, b:int, N:int, f:any):    
    areal = 0 # Deklarere areal
    delta_x = (b - a) / N # Finne delta x
    
    sumasjon = 0
    for i in range(1, N-1): # Sum
        sumasjon += f(a + i * delta_x) * delta_x
        
    areal = ((f(a) + f(b)) * delta_x/2) + sumasjon
    
    return(areal)

def main():
    import numpy as np
    
    print(rektangelsum(1, 4, 100, lambda x: (np.sqrt(x)) )) # Test
    print(rektangelsum(1, 4, 100, lambda x: (1/x) )) # Test
    print(rektangelsum(1, 4, 100, lambda x: (np.sin(x)) )) # Test
    
    print(trapessum(1, 4, 100, lambda x: (np.sin(x)) )) # Test
    
if __name__ == '__main__':  # This code won't run if this file is imported.
     main()
