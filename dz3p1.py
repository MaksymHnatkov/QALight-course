from random import randint as ri

a = (int(input( "Введіть бажану довжину списку та натисніть Enter: ")))
b = (int(input("Введіть бажане максимальне значення елементів списку та натисніть Enter: ")))

def listFunc (x,y):
    list = []
    for i in range(x):
        list.append(ri(0,y))
    return list

print(listFunc(a,b))
