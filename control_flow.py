var_1 = 10
var_2 = 11
if var_1 > var_2:
    for i in range(10):
        print(i)
elif var_1 == var_2:
    print('they are the same')
else:
    for j in range(10):
        print(j)
        if j == 5:
            break
