#14) Вам дан произвольный двумерный список:
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]
res = []

for i in range(len(array)):
    temp = []
    for x in array:
        temp.append(x[i])
    res.append(temp)
print(res)

#15) Выведите на экран следующую пирамидку:
# XX
# XxxX
# XxxxxX
# XxxxxxxX
# XxxxxxxxxX

n=5
s = 'X'
for i in range(n):
    sl=s.lower()
    print(f'{s}{sl*i*2}{s}')