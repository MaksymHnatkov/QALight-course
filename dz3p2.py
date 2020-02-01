from random import randint as ri

a = (int(input("Введіть бажану довжину першого списку та натисніть Enter: ")))
b = (int(input("Введіть бажане максимальне значення елементів першого списку та натисніть Enter: ")))
c = (int(input("Введіть бажану довжину другого списку та натисніть Enter: ")))
d = (int(input("Введіть бажане максимальне значення елементів другого списку та натисніть Enter: ")))

def listFunc2 (x,y,w,z):
    list1 = []
    for i in range(x):
        list1.append(ri(0, y))

    list2 = []
    for e in range(w):
        list2.append(ri(0, z))

    list3 =[]
    for s in list1:
        if s in list2:
            list3.append(s)

    if len(list3) == 0:
        print ("Співпадінь не виявлено")
        return list3
    else:
        return list3

print (listFunc2(a,b,c,d))


