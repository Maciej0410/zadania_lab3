def trapez(a,b,h):
    if (str(a).isdigit()==False)|(str(b).isdigit()==False|str(h).isdigit()==False):
        return "Podaj poprawne wartości"
    else:
        a=float(a)
        b=float(b)
        h=float(h)

        if (a<0)|(b<0)|(h<0):
            return "Błąd"
        else:
            wynik = ((a + b) * h) * 0.5

            return print("Oto pole trapezu: %f" % (wynik))




a=input("Podaj długość pierwszej podstawy: ")
b=input("Podaj długość drugiej podstawy: ")
h=input("Podaj wysokość: ")

print(trapez(a,b,h))

