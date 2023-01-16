SELECT = float(input("Hvilken oppgave vil du velge? : "))
match SELECT:
    case 1.5:
        from simsine import lag_følge
        
        # a)
        # Følgen: a_1 = 2 og f_n+1 = 2*a_n
        print(lag_følge(ledd_1=2, antall_ledd=10, rekursiv=True, formel=lambda f_n:(2 * f_n) ))

        # b)
        # Følgen: b_1 = 5 og f_n = (b_n - 1) + 3
        print(lag_følge(5, 10, True, lambda f_n: ((f_n -1) + 3) ))

        # c)
        # Følgen: c_1 = 1 og c_n+1 = 2c_n - 3
        print(lag_følge(1, 10, True, lambda f_n: (2 * f_n - 3) ))

        # d)
        # Følgen: d_1 = 1 og d_n+1 = d_n + n
        # print(lag_følge(1, 10, True, lambda f_n, n: (f_n + n) ))
        
        # eksplisitt
        print(lag_følge(1, 10, False, lambda n: (n * 2) ))
        
    case 3.2:
        from simsine import gradertilradianer, radianertilgrader
        import math
        
        # 1
        grader = 90
        print(f"{grader} grader tilsvarer {gradertilradianer(grader)} radianer\n")
        # 2
        grader = 36.9
        print(f"{grader} grader tilsvarer {gradertilradianer(grader)} radianer\n")
        # 3
        radianer = math.floor(1/4 * math.pi)
        print(f"{radianer} radianer tilsvarer {math.floor(radianertilgrader(radianer))} grader\n")
        # 4
        radianer = 0.963
        print(f"{radianer} radianer tilsvarer {math.floor(radianertilgrader(radianer))} grader\n")

    case 2.56:
        # c)     
        import numpy as np
        data = np.loadtxt("rakett.txt")
        tid = data[:,0]
        hastighet = data[:,1]
        deltax = tid[1] - tid[0]
        
         
            
    case _:
        print("Ugyldig seleksjon, prøv igjen\n")