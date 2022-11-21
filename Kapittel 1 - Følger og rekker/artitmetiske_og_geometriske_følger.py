def ar_ledd(l_1:int, diff:int, nth:int):
    return(l_1 + (nth-1) * diff)


følge = []
for i in range(1,15):
    følge.append(ar_ledd(3,3,i))
print(følge)

# def ar_sum(l_1:int, )