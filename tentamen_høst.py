def main():
    from simsine import sumasjon
    import numpy as np

    print(f"pi: {np.pi}") # Printe pi eksakt
    
    f = lambda x: ((-1)**x) / (2 * x + 1) * 4
    
    for i in range(1, 6):
        print(f"100 ledd: {sumasjon(0,100, f)}")

if __name__ == '__main__':  # This code won't run if this file is imported.
     main()

# S = 0
# for i in range(0,1000):
#     S += (-1)**i / (2*i + 1)
# print(4*S)
