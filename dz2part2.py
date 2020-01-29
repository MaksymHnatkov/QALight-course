from random import randint as ri

A = ri(0,11)
B = ri(0,11)
C = ri (0,11)

if A > B:
    print ("Отлично!")
elif A < B:
    print ("Не хорошо(((")
elif A == B:
    print (C, "Теперь эта!")
    if (A + B) < C:
        print ("Супер!")
    elif (A + B) > C:
        print ("Печаль беда")
    elif (A + B) == C:
        print ("Срадания")
