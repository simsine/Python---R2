def main():
    import numpy as np

    def sumasjon(nedre_grense, øvre_grense, funksjon):
        summert = 0
        for i in range(nedre_grense, øvre_grense):
            summert += funksjon(i)
        return summert

    print(f"pi: {np.pi}") # Printe pi eksakt
    
    print(f"100 ledd: {sumasjon(0,100, lambda x: ((-1)**x) / (2 * x + 1) * 4)}")
    print(f"1000 ledd: {sumasjon(0,1000, lambda x: ((-1)**x) / (2 * x + 1) * 4)}")
    print(f"10000 ledd: {sumasjon(0,10000, lambda x: ((-1)**x) / (2 * x + 1) * 4)}")
    print(f"100000 ledd: {sumasjon(0,100000, lambda x: ((-1)**x) / (2 * x + 1) * 4)}")
    print(f"10000000 ledd: {sumasjon(0,10000000, lambda x: ((-1)**x) / (2 * x + 1) * 4)}")


if __name__ == '__main__':  # This code won't run if this file is imported.
     main()


# S = 0
# for i in range(0,1000):
#     S += (-1)**i / (2*i + 1)
# print(4*S)
