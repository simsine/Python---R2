from math import pi

def gradertilradianer(ngrader:float):
    """
    Konverterer grader til radianer\n
    (n°) / (180°) * (pi)
    """
    return((ngrader) / (180) * (pi))

def radianertilgrader(v:float):
    """
    Konverterer radianer til grader\n
    v / pi * 180°
    """
    return((v) / (pi) * (180))
    
    
def main():
    print(pi)
    # 1
    grader = 90
    print(f"{grader} grader tilsvarer {gradertilradianer(grader)} radianer\n")

if __name__ == '__main__':  # This code won't run if this file is imported.
    main()