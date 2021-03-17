def trojkat(x,y,z):
    if (str(x).isdigit() == False) | (str(y).isdigit()==False) | (str(z).isdigit()==False):
        return "Podano zle wartosci"
    else:
        x = float(x)
        y = float(y)
        z = float(z)
        if (x<=0)|(y<=0)|(z<=0):
            return "Podano wartosci ujemne"
        elif (x>y)|(x>z):
            spr = (y**2) + (z**2)
            if spr==(x**2):
                return "Trójkąt jest prostokątny"
            else:
                return "Trójkąt nie jest prostokątny"
        elif (y>x)|(y>z):
            spr = (x**2) + (z**2)
            if spr==(y**2):
                return "Trójkąt jest prostokątny"
            else:
                return "Trójkąt nie jest prostokątny"
        else:
            spr = (x**2) + (y**2)
            if spr==(z**2):
                return "Trójkąt jest prostokątny"
            else:
                return "Trójkąt nie jest prostokątny"


a=input(u"Podaj długość a: ")
b=input(u"Podaj długość b: ")
c=input(u"Podaj długość c: ")

print(trojkat(a,b,c))