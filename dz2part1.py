from random import randint as ri

n = 10
list = []

for i in range (n):
    list.append(ri(0,99))

print(list)

del list[-1]

print(list)

