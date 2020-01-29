from random import randint as ri

list = []

for i in range (10):
    list.append(ri(0,99))

print(list)

del list[-1]

print(list)


