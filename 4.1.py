massive=[]
op=int(input("введите кол-во чисел в массиве "))
if op<=0:
    print("вы ввели 0 или отрицательное число ")
else:
    for x in range(op):
        massive.append(float(input("введите число с плавающей точкой ")))
    he=max(massive)
    massive=massive[:massive.index(he) + 1] + [0]*(len(massive)- len(massive[:massive.index(he) + 1]))
    print(massive)
