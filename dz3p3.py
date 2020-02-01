from random import randint as ri

userString = (str(input("Введіть будь-яку фразу та натисніть Enter: ")))

def func (x,y,z):
    result = {x:ri(y,z+1)}
    return result

print (func(userString,0,999))

