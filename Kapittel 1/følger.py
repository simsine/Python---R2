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

def main():
    #EKSEMPEL:
    # Følgen: f_1 = 2 og f_n+1 = 2*f_n
    print(lag_følge(ledd_1=2, antall_ledd=10, rekursiv=True, formel=lambda f_n:(2 * f_n) ))

if __name__ == '__main__':  # This code won't run if this file is imported.
    main()