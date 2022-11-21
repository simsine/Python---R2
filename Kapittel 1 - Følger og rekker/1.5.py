from følger import lag_følge

def main():
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


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
