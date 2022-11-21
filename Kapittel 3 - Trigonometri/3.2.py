import math
from _radianer_og_grader import gradertilradianer, radianertilgrader

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