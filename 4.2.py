d = int(input('введите размер массива '))
e = int(input('введите размер массива '))
one, two, res = [], [], []
for i in range(0, d):
    op = int(input('введите число '))
    one.append(op)
for i in range(0, e):
    op = int(input('введите число '))
    two.append(op)
for i in one:
    if i in two and i not in res:
        res.append(i)
print('общие числа',res )
