produkty = {"pomarancze":"Kg", "makaron":"paczka", "ciastka":"szt","pączek":"szt"}

print(produkty)

sztuki = [i for i in produkty.keys() if produkty[i] =="szt"]

print(sztuki)